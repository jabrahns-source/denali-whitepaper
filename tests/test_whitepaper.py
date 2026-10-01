"""Structural checks for the Denali whitepaper. Does not assert empirical claims."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "Denali_Architecture_Whitepaper_v1.md"


class WhitepaperStructureTest(unittest.TestCase):
    def test_required_files(self):
        for name in ("README.md", "LICENSE", ".zenodo.json", "index.html"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_zenodo_json(self):
        data = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)

    def test_paper_has_sections(self):
        text = PAPER.read_text(encoding="utf-8")
        self.assertGreater(len(text), 2000)
        self.assertIn("#", text)
        for needle in ("Denali", "deterministic"):
            self.assertIn(needle.lower(), text.lower())


if __name__ == "__main__":
    unittest.main()
