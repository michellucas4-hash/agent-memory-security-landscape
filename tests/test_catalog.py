"""Verificações locais do catálogo de estudos open source."""
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class InventoryTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / "catalogo" / "repositorios.csv").open(encoding="utf-8") as handle:
            self.records = list(csv.DictReader(handle))

    def test_all_projects_have_unique_source(self):
        self.assertEqual(len(self.records), 45)
        self.assertEqual(len({item["repo"] for item in self.records}), 45)

    def test_each_reference_points_to_original_repository(self):
        for item in self.records:
            self.assertEqual(item["source_url"], "https://github.com/" + item["repo"])

if __name__ == "__main__":
    unittest.main()
