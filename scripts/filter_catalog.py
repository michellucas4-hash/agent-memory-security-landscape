#!/usr/bin/env python3
"""Pesquise um catálogo público de OSS: 100% offline, sem dependências extras.

Este comando NÃO instala, executa ou pontua a segurança dos projetos listados.
Dados históricos: 23/10/2026. Python 3.10+.
"""
import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "catalogo" / "repositorios.csv"
FIELDS = (
    "repo", "category", "priority", "license_claim",
    "license_review_required", "stars_snapshot", "source_url",
    "checked_at", "origin"
)
PRIORITY = {"P0": 0, "P1": 1, "P2": 2}


def load_catalog(path=CATALOG):
    """Valida estrutura e conteúdo antes de mostrar resultados."""
    with Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or list(reader.fieldnames) != list(FIELDS):
            raise ValueError("Cabeçalho do CSV incompatível com o formato esperado.")
        items = list(reader)

    seen = set()
    for number, row in enumerate(items, 2):
        name = row["repo"]
        if not name or "/" not in name or name.casefold() in seen:
            raise ValueError(f"Repositório vazio, repetido ou inválido na linha {number}.")
        seen.add(name.casefold())
        if row["source_url"] != "https://github.com/" + name:
            raise ValueError(f"URL de origem incompatível na linha {number}.")
        if row["origin"] != "THIRD_PARTY_UPSTREAM":
            raise ValueError(f"Origem desconhecida na linha {number}.")
        if row["priority"] not in PRIORITY:
            raise ValueError(f"Prioridade inválida na linha {number}.")
        if row["license_review_required"] not in ("true", "false"):
            raise ValueError(f"Flag de licença inválida na linha {number}.")
        try:
            stars = int(row["stars_snapshot"])
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Contagem de estrelas inválida na linha {number}.") from exc
        if stars < 0:
            raise ValueError(f"Contagem negativa de estrelas na linha {number}.")
    return items


def filter_rows(rows, category=None, priority=None, license_name=None,
                query=None, min_stars=0, require_review=False):
    """Filtra um instantâneo, sem fazer requisições ao GitHub."""
    for row in rows:
        if category and row["category"].casefold() != category.casefold():
            continue
        if priority and row["priority"] != priority.upper():
            continue
        if license_name and row["license_claim"].casefold() != license_name.casefold():
            continue
        haystack = " ".join((row["repo"], row["category"], row["license_claim"]))
        if query and query.casefold() not in haystack.casefold():
            continue
        if int(row["stars_snapshot"]) < min_stars:
            continue
        if require_review and row["license_review_required"] != "true":
            continue
        yield row


def render(rows, output):
    if output == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    elif output == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    else:
        print(f"Resultados: {len(rows)} | Metadados históricos, não avaliação de segurança")
        for row in rows:
            review = " [revisar licença]" if row["license_review_required"] == "true" else ""
            print(f"{row['priority']:2} | {row['category']:20} | "
                  f"{row['repo']:43} | {row['license_claim']}{review} | "
                  f"{row['stars_snapshot']} stars | {row['source_url']}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Encontre bibliotecas OSS por categoria, prioridade, licença e popularidade histórica."
    )
    parser.add_argument("--category", help="Ex.: memoria_ia, seguranca, observabilidade")
    parser.add_argument("--priority", type=str.upper, choices=PRIORITY)
    parser.add_argument("--license", dest="license_name", help="Identificador informado pelo GitHub")
    parser.add_argument("--query", help="Pesquisa no nome, categoria ou licença")
    parser.add_argument("--min-stars", type=int, default=0, help="Estrelas na data de coleta")
    parser.add_argument("--require-license-review", action="store_true")
    parser.add_argument("--output", choices=["table", "json", "csv"], default="table")
    parser.add_argument("--sort", choices=["name", "stars", "priority"], default="name")
    parser.add_argument("--limit", type=int, help="Mostra apenas N resultados")
    parser.add_argument("--list-categories", action="store_true", help="Lista categorias disponíveis")
    args = parser.parse_args(argv)
    if args.min_stars < 0 or (args.limit is not None and args.limit < 1):
        parser.error("--min-stars precisa ser >= 0 e --limit precisa ser >= 1.")

    try:
        rows = load_catalog()
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f"Erro ao ler o catálogo: {error}\n")

    if args.list_categories:
        for name, count in sorted(Counter(row["category"] for row in rows).items()):
            print(f"{name}: {count}")
        return 0

    categories = {row["category"].casefold() for row in rows}
    if args.category and args.category.casefold() not in categories:
        parser.error("Categoria não encontrada. Use --list-categories para consultar as opções.")

    found = list(filter_rows(rows, args.category, args.priority, args.license_name,
                             args.query, args.min_stars, args.require_license_review))
    if args.sort == "stars":
        found.sort(key=lambda r: (-int(r["stars_snapshot"]), r["repo"].casefold()))
    elif args.sort == "priority":
        found.sort(key=lambda r: (PRIORITY[r["priority"]], r["repo"].casefold()))
    else:
        found.sort(key=lambda r: r["repo"].casefold())
    if args.limit:
        found = found[:args.limit]
    render(found, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
