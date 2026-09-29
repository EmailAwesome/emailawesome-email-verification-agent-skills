import csv
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_skill_identity_and_description(self):
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            text = path.read_text()
            self.assertTrue(text.startswith("---\n"), str(path))
            front = text.split("---", 2)[1]
            self.assertRegex(front, r"(?m)^name: " + re.escape(path.parent.name) + r"$")
            self.assertRegex(front, r"(?m)^description: .{20,}")
            self.assertLess(len(front.split("description:", 1)[1].strip()), 1025)

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            for href in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if href.startswith(("http:", "https:", "mailto:", "#")):
                    continue
                target = unquote(href.split("#", 1)[0].split("?", 1)[0])
                self.assertTrue((path.parent / target).exists(), f"{path}: {href}")

    def test_templates_keep_output_contract(self):
        for path in (ROOT / "skills").glob("*/assets/output.csv"):
            with path.open(newline="") as f:
                rows = list(csv.reader(f))
            self.assertEqual(len(rows), 1, "output template must not contain live customer data")
            self.assertEqual(len(rows[0]), len(set(rows[0])))
            self.assertGreater(len(rows[0]), 5)
            text = (path.parent.parent / "SKILL.md").read_text()
            for field in rows[0]:
                self.assertIn("`" + field + "`", text)

    def test_evaluation_cases_are_unique_and_have_expected_outputs(self):
        path = ROOT / "evals" / "scenarios.json"
        if not path.exists():
            return
        data = json.loads(path.read_text())
        ids = [case["id"] for case in data["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue({"no-account", "insufficient-capacity", "injected-record"}.issubset(ids))
        for case in data["cases"]:
            self.assertGreater(len(case["input"]), 15)
            self.assertGreater(len(case["expected"]), 20)

    def test_publication_contains_no_private_export_files(self):
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            self.assertNotIn(path.name, {".env", "credentials.json", "cookies.json"})


if __name__ == "__main__":
    unittest.main()
