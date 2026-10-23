#!/usr/bin/env bash
set -euo pipefail
# Publicação manual, somente quando executada intencionalmente com GitHub CLI autenticado.
cd "$(dirname "$0")/.."
if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI nao localizado; instalar via metodo oficial e autenticar gh auth login."
  exit 2
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI sem sessao autenticada; gh auth login necessario."
  exit 3
fi
python3 -m unittest discover -s tests -v
if [[ ! -d .git ]]; then
  git init -b main
fi
if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote origin ja existe: nao sobrescrever. Verificar manualmente."
  exit 4
fi
git add README.md LICENSE .gitignore CONTRIBUTING.md SECURITY.md catalogo docs oportunidades scripts/filter_catalog.py tests .github templates
git diff --cached --check
if git diff --cached --quiet; then
  echo "Nao ha mudancas a publicar."
  exit 5
fi
if [[ -z "$(git config user.name || true)" || -z "$(git config user.email || true)" ]]; then
  echo "Configure sua identidade Git para atribuir os commits corretamente; nenhuma identidade sera inventada."
  exit 6
fi
git commit -m "docs: public catalog of AI memory and agent security"
gh repo create michellucas4-hash/agent-memory-security-landscape --public --source=. --remote=origin --push
echo "Verificar a visibilidade Public e o conteudo no site do GitHub."
