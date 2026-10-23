#!/usr/bin/env python3
"""Filtros de pesquisa para o inventário público, sem dependências de terceiros."""
import argparse
import csv
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "catalogo" / "repositorios.csv"

def search(rows, category=None, priority=None, license_name=None, query=None, min_stars=0, require_review=False):
    for item in rows:
        if category and item["category"] != category:
            continue
        if priority and item["priority"] != priority:
            continue
        if license_name and item["license_claim"] != license_name:
            continue
        if query and query.casefold() not in item["repo"].casefold():
            continue
        if int(item["stars_snapshot"]) < min_stars:
            continue
        if require_review and item["license_review_required"] != "true":
            continue
        yield item

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--category")
    parser.add_argument("--priority", choices=["P0", "P1", "P2"])
    parser.add_argument("--license", dest="license_name")
    parser.add_argument("--query")
    parser.add_argument("--min-stars", type=int, default=0)
    parser.add_argument("--require-license-review", action="store_true")
    parser.add_argument("--output", choices=["table", "json"], default="table")
    a = parser.parse_args()
    with DATA.open(encoding="utf-8", newline="") as source:
        data = list(csv.DictReader(source))
    result = list(search(data, a.category, a.priority, a.license_name, a.query,
                         a.min_stars, a.require_license_review))
    if a.output == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Resultados:", len(result))
        for row in result:
            print(row["priority"], row["repo"], row["source_url"])

if __name__ == "__main__":
    main()
