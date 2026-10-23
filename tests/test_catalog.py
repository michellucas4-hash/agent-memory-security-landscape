"""Testes offline para que qualquer colaborador valide o catálogo sem API nem tokens."""
import csv
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from filter_catalog import FIELDS, filter_rows, load_catalog, main


class InventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_catalog()

    def test_expected_count_and_no_duplicate_names(self):
        self.assertEqual(len(self.records), 45)
        self.assertEqual(len({r["repo"].casefold() for r in self.records}), 45)

    def test_sources_are_links_to_real_originals_not_claimed_as_ours(self):
        for item in self.records:
            self.assertEqual(item["source_url"], "https://github.com/" + item["repo"])
            self.assertEqual(item["origin"], "THIRD_PARTY_UPSTREAM")

    def test_categories_priorities_and_licenses(self):
        allowed = {"seguranca", "memoria_ia", "orquestracao", "engenharia_agente",
                   "observabilidade", "dados_postgres", "backup", "elegibilidade"}
        for item in self.records:
            self.assertIn(item["category"], allowed)
            self.assertIn(item["priority"], {"P0", "P1", "P2"})
            if item["license_claim"] == "NOASSERTION":
                self.assertEqual(item["license_review_required"], "true")

    def test_memory_filter(self):
        result = list(filter_rows(self.records, category="memoria_ia", priority="P1"))
        self.assertTrue(result)
        self.assertTrue(all(x["category"] == "memoria_ia" for x in result))
        self.assertEqual(len(result), 6)

    def test_case_insensitive_filter_and_stars(self):
        result = list(filter_rows(self.records, category="MEMORIA_IA", license_name="mit",
                                  min_stars=1000))
        self.assertTrue(result)
        self.assertTrue(all(x["license_claim"] == "MIT" for x in result))

    def test_reviews_are_flagged(self):
        result = list(filter_rows(self.records, require_review=True))
        self.assertTrue(result)
        self.assertTrue(all(x["license_review_required"] == "true" for x in result))

    def test_cli_json_and_csv_outputs(self):
        for format_name in ("json", "csv"):
            run = subprocess.run(
                [sys.executable, str(ROOT / "scripts/filter_catalog.py"),
                 "--category", "memoria_ia", "--output", format_name],
                cwd=ROOT, text=True, capture_output=True, timeout=15
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn("mem0ai/mem0", run.stdout)

    def test_cli_rejects_invalid_category(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/filter_catalog.py"),
             "--category", "categoria_inexistente"],
            cwd=ROOT, text=True, capture_output=True, timeout=15
        )
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("Categoria não encontrada", run.stderr)

    def test_cli_list_categories(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/filter_catalog.py"),
             "--list-categories"],
            cwd=ROOT, text=True, capture_output=True, timeout=15
        )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("memoria_ia: 12", run.stdout)
        self.assertIn("seguranca: 16", run.stdout)

    def test_schema_rejects_duplicate_repositories(self):
        sample = self.records[0]
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "bad.csv"
            with p.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows([sample, sample])
            with self.assertRaises(ValueError):
                load_catalog(p)

    def test_all_nine_profiles_present(self):
        profiles = ("hindsight", "cognee", "supermemory", "honcho", "guac",
                    "bandit", "opik", "skillspector", "in-toto-golang")
        for name in profiles:
            path = ROOT / "oportunidades" / (name + ".md")
            self.assertTrue(path.is_file(), path)
            self.assertGreater(path.stat().st_size, 500, path)

    def test_local_markdown_links_exist(self):
        pat = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for doc in ROOT.rglob("*.md"):
            if ".git" in doc.parts:
                continue
            for link in pat.findall(doc.read_text(encoding="utf-8")):
                if link.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                target = link.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                resolved = (doc.parent / target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), f"{doc}: {link}")
                self.assertTrue(resolved.exists(), f"Link quebrado em {doc}: {link}")


if __name__ == "__main__":
    unittest.main()
