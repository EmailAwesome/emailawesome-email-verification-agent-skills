#!/usr/bin/env python3
"""Split Email Awesome CSV results and check source-to-result reconciliation."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

STATUSES = {
    "VALID": "valid",
    "INVALID": "invalid",
    "CATCH_ALL": "catch_all",
    "UNKNOWN": "unknown",
}


SOURCE_ID = "_ea_source_row_id"


def read_csv(path: Path) -> tuple[list[dict], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows, headers = list(reader), list(reader.fieldnames or [])
        if not headers or any(not name for name in headers) or len(headers) != len(set(headers)):
            raise ValueError("CSV headers must be present and unique")
        if any(None in row or any(value is None for value in row.values()) for row in rows):
            raise ValueError("CSV row width must match its header")
        return rows, headers


def spreadsheet_safe(row: dict) -> dict:
    return {key: "'" + str(value) if str(value).lstrip().startswith(("=", "+", "-", "@")) else value for key, value in row.items()}


def segment(
    input_path: Path,
    output_dir: Path,
    status_column: str,
    source_path: Path | None = None,
    excluded_ids: list[str] | None = None,
    source_email_column: str | None = None,
    result_email_column: str | None = None,
) -> dict:
    rows, headers = read_csv(input_path)
    if status_column not in headers:
        raise ValueError(f"status column not found: {status_column}")
    if source_path and SOURCE_ID not in headers:
        raise ValueError(f"result column not found: {SOURCE_ID}")
    if excluded_ids and not source_path:
        raise ValueError("excluded IDs require a source working copy")
    output_paths = {output_dir / f"{name}.csv" for name in [*STATUSES.values(), "unresolved", "excluded"]}
    output_paths.add(output_dir / "summary.json")
    output_paths.add(output_dir / "source_ledger.csv")
    protected = {input_path.resolve()}
    if source_path:
        protected.add(source_path.resolve())
    if protected & {path.resolve() for path in output_paths}:
        raise ValueError("output directory would overwrite an input file")

    source_rows: list[dict] = []
    source_headers: list[str] = headers
    source_ids: list[str] = []
    if source_path:
        source_rows, source_headers = read_csv(source_path)
        if not source_rows:
            raise ValueError("source working copy contains no rows")
        if SOURCE_ID not in source_headers:
            raise ValueError(f"source column not found: {SOURCE_ID}")
        source_ids = [str(row.get(SOURCE_ID, "") or "") for row in source_rows]
        if not all(source_ids) or len(source_ids) != len(set(source_ids)):
            raise ValueError("source IDs must be nonempty and unique")

    excluded = set(str(item) for item in (excluded_ids or []))
    if excluded - set(source_ids):
        raise ValueError("excluded IDs must exist in source")
    result_ids = [str(row.get(SOURCE_ID, "") or "") for row in rows] if source_path else []
    duplicates = sorted(item for item, count in Counter(result_ids).items() if item and count > 1)
    missing = sorted(set(source_ids) - set(result_ids) - excluded)
    unexpected = sorted(set(result_ids) - set(source_ids)) if source_path else []
    overlap = sorted(set(result_ids) & excluded)
    if bool(source_email_column) != bool(result_email_column):
        raise ValueError("both source and result email column names are required")
    email_mismatches = []
    if source_email_column:
        if not source_path or source_email_column not in source_headers or result_email_column not in headers:
            raise ValueError("email comparison requires source and valid email columns")
        def normalized(value):
            # Preserve local-part case; case-sensitive providers exist.
            local, sep, domain = str(value or "").strip().rpartition("@")
            return local + sep + domain.lower() if sep else ""
        expected_emails = {row[SOURCE_ID]: normalized(row[source_email_column]) for row in source_rows}
        email_mismatches = sorted({row.get(SOURCE_ID, "") for row in rows if row.get(SOURCE_ID) in expected_emails and (not normalized(row[result_email_column]) or normalized(row[result_email_column]) != expected_emails[row[SOURCE_ID]])})
    ambiguous_ids = set(duplicates + unexpected + overlap + email_mismatches)

    output_dir.mkdir(parents=True, exist_ok=True)
    buckets = {name: [] for name in [*STATUSES.values(), "unresolved"]}
    for row in rows:
        status = str(row.get(status_column, "") or "").strip().upper()
        ambiguous = source_path and (not row.get(SOURCE_ID) or row.get(SOURCE_ID) in ambiguous_ids)
        buckets["unresolved" if ambiguous else STATUSES.get(status, "unresolved")].append(row)

    for name, bucket in buckets.items():
        path = output_dir / f"{name}.csv"
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows(spreadsheet_safe(row) for row in bucket)

    excluded_rows = [row for row in source_rows if str(row.get(SOURCE_ID, "") or "") in excluded]
    with (output_dir / "excluded.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=source_headers)
        writer.writeheader()
        writer.writerows(spreadsheet_safe(row) for row in excluded_rows)

    # Provider rows may be duplicated or missing. Preserve one row per source
    # separately, so a missing response never disappears from the deliverable.
    ledger = []
    by_source = {}
    for row in rows:
        by_source.setdefault(row.get(SOURCE_ID, ""), []).append(row)
    ledger_fields = ["_ea_result_bucket", "_ea_resolution_reason", "_ea_result_count"]
    if source_path and any(field in source_headers for field in ledger_fields):
        raise ValueError("source contains reserved ledger fields")
    for source_row in source_rows:
        sid = source_row[SOURCE_ID]
        returned = by_source.get(sid, [])
        if sid in ambiguous_ids:
            bucket, reason = "unresolved", "ambiguous_result_identity_or_exclusion_overlap"
        elif sid in excluded:
            bucket, reason = "excluded", "explicit_exclusion"
        elif not returned:
            bucket, reason = "unresolved", "missing_result"
        else:
            status = str(returned[0].get(status_column, "") or "").strip().upper()
            bucket = STATUSES.get(status, "unresolved")
            reason = "terminal_result" if bucket != "unresolved" else "nonterminal_or_unknown_status"
        ledger.append({**source_row, "_ea_result_bucket": bucket,
                       "_ea_resolution_reason": reason, "_ea_result_count": len(returned)})
    if source_path:
        with (output_dir / "source_ledger.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=source_headers + ledger_fields)
            writer.writeheader()
            writer.writerows(spreadsheet_safe(row) for row in ledger)

    counts = {name: len(bucket) for name, bucket in buckets.items()}
    counts["excluded"] = len(excluded_rows)
    mapping_complete = bool(source_path) and not (missing or unexpected or duplicates or overlap or email_mismatches or "" in result_ids)
    terminal_results_complete = mapping_complete and not buckets["unresolved"]
    summary = {
        "input_rows": len(rows),
        "source_rows": len(source_rows) if source_path else None,
        "source_ledger_rows": len(ledger),
        "source_buckets": dict(Counter(row["_ea_result_bucket"] for row in ledger)),
        "provider_bucket_counts_are_source_counts": False,

        "segments": counts,
        "duplicate_result_ids": duplicates,
        "missing_source_ids": missing,
        "unexpected_result_ids": unexpected,
        "result_and_excluded_overlap": overlap,
        "email_identity_checked": bool(source_email_column),
        "email_mismatch_source_ids": email_mismatches,
        "outreach_permission_checked": False,
        "mapping_complete": mapping_complete,
        "terminal_results_complete": terminal_results_complete,
        "reconciled": terminal_results_complete,
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--status-column", default="email_address_status")
    parser.add_argument("--source", type=Path, help="preflight working CSV with stable source IDs")
    parser.add_argument("--excluded-ids", type=Path, help="JSON array of explicitly excluded source IDs")
    parser.add_argument("--source-email-column", help="source email column for identity cross-check")
    parser.add_argument("--result-email-column", help="returned email column for identity cross-check")
    args = parser.parse_args()
    excluded = json.loads(args.excluded_ids.read_text(encoding="utf-8")) if args.excluded_ids else None
    print(json.dumps(segment(args.input, args.output_dir, args.status_column, args.source, excluded, args.source_email_column, args.result_email_column), indent=2))


if __name__ == "__main__":
    main()
