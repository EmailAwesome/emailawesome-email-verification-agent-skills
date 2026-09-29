import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


preflight = load("ea4_preflight", "skills/emailawesome-list-cleaner/scripts/preflight_csv.py")
segmenter = load("ea4_segment", "skills/emailawesome-list-cleaner/scripts/segment_results.py")
reconcile = load("ea4_reconcile", "skills/emailawesome-api-validation/scripts/reconcile_jobs.py")


class CsvTests(unittest.TestCase):
    def test_preflight_preserves_multiline_rows_and_formula_safety(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.csv"
            output = Path(temp) / "working.csv"
            source.write_text('Email,Notes\na@example.com,"line one\nline two"\nb@example.com,=SUM(1)\n', encoding="utf-8")
            result = preflight.preflight(source, output)
            self.assertEqual(result["selected_email_column"], "Email")
            with output.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["Notes"], "line one\nline two")
            self.assertEqual(rows[1]["Notes"], "'=SUM(1)")

    def test_preflight_requires_choice_when_columns_tie(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.csv"
            output = Path(temp) / "working.csv"
            source.write_text("primary,secondary\na@example.com,b@example.com\n", encoding="utf-8")
            result = preflight.preflight(source, output)
            self.assertTrue(result["requires_email_column_selection"])

    def test_preflight_txt_preserves_lines_and_never_overwrites_source(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.txt"
            output = Path(temp) / "working.csv"
            source.write_text("a@example.com\n =1+1\n", encoding="utf-8")
            result = preflight.preflight(source, output)
            self.assertEqual(result["source_format"], "txt")
            self.assertEqual(result["rows"], 2)
            with output.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[0]["_ea_source_row_id"], "1")
            self.assertEqual(rows[1]["_ea_preflight_issue"], "formula_like_email_requires_review")
            self.assertTrue(rows[1]["email"].startswith("'"))
            with self.assertRaisesRegex(ValueError, "must not overwrite"):
                preflight.preflight(source, source)

    def test_preflight_single_column_csv_keeps_header_and_rows(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "input.csv"
            source.write_text("email\na@example.com\nb@example.com\n", encoding="utf-8")
            result = preflight.preflight(source, Path(temp) / "working.csv")
            self.assertEqual(result["rows"], 2)
            self.assertEqual(result["selected_email_column"], "email")

    def test_segmenter_preserves_every_row(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "results.csv"
            working = Path(temp) / "working.csv"
            output = Path(temp) / "segments"
            source.write_text(
                "_ea_source_row_id,email_address_status\n1,VALID\n2,INVALID\n3,CATCH_ALL\n4,UNKNOWN\n5,FAILED\n",
                encoding="utf-8",
            )
            working.write_text(
                "_ea_source_row_id,email\n1,a@example.com\n2,b@example.com\n3,c@example.com\n4,d@example.com\n5,e@example.com\n",
                encoding="utf-8",
            )
            summary = segmenter.segment(source, output, "email_address_status", working)
            self.assertTrue(summary["mapping_complete"])
            self.assertFalse(summary["terminal_results_complete"])
            self.assertFalse(summary["reconciled"])
            self.assertEqual(summary["segments"]["unresolved"], 1)

    def test_segmenter_detects_duplicate_and_missing_source_ids(self):
        with tempfile.TemporaryDirectory() as temp:
            results = Path(temp) / "results.csv"
            working = Path(temp) / "working.csv"
            results.write_text(
                "_ea_source_row_id,email_address_status\n1,VALID\n1,VALID\n",
                encoding="utf-8",
            )
            working.write_text("_ea_source_row_id,email\n1,a@example.com\n2,b@example.com\n", encoding="utf-8")
            summary = segmenter.segment(results, Path(temp) / "segments", "email_address_status", working)
            self.assertEqual(summary["duplicate_result_ids"], ["1"])
            self.assertEqual(summary["missing_source_ids"], ["2"])
            self.assertFalse(summary["reconciled"])

    def test_segmenter_counts_explicit_exclusion_and_protects_input(self):
        with tempfile.TemporaryDirectory() as temp:
            results = Path(temp) / "valid.csv"
            working = Path(temp) / "working.csv"
            results.write_text("_ea_source_row_id,email_address_status\n1,VALID\n", encoding="utf-8")
            working.write_text("_ea_source_row_id,email\n1,a@example.com\n2,b@example.com\n", encoding="utf-8")
            summary = segmenter.segment(
                results, Path(temp) / "segments", "email_address_status", working, ["2"]
            )
            self.assertTrue(summary["reconciled"])
            self.assertEqual(summary["segments"]["excluded"], 1)
            with self.assertRaisesRegex(ValueError, "would overwrite"):
                segmenter.segment(results, Path(temp), "email_address_status", working)


class AsyncTests(unittest.TestCase):
    def test_reconciliation_reports_missing_duplicates_and_unmapped(self):
        result = reconcile.reconcile(
            ["1", "2"],
            [
                {"source_id": "1", "status": "COMPLETE"},
                {"source_id": "1", "status": "COMPLETE"},
                {"status": "FAILED"},
            ],
        )
        self.assertEqual(result["missing"], ["2"])
        self.assertEqual(result["duplicates"], ["1"])
        self.assertEqual(result["records_without_source_id"], 1)
        self.assertFalse(result["reconciled"])

    def test_pending_job_is_mapped_but_not_complete(self):
        result = reconcile.reconcile(["1"], [{"source_id": "1", "status": "PENDING"}])
        self.assertTrue(result["mapping_complete"])
        self.assertFalse(result["terminal_results_complete"])
        self.assertFalse(result["reconciled"])

    def test_terminal_job_needs_explicit_email_result(self):
        mapped_only = reconcile.reconcile(["1"], [{"source_id": "1", "status": "COMPLETE"}])
        self.assertFalse(mapped_only["terminal_results_complete"])
        final = reconcile.reconcile(
            ["1"],
            [{"source_id": "1", "status": "COMPLETE", "email_address_status": "VALID"}],
        )
        self.assertTrue(final["terminal_results_complete"])
        self.assertTrue(final["reconciled"])


if __name__ == "__main__":
    unittest.main()
