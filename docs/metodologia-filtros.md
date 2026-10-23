# Metodologia e filtros GitHub

## Origem
Metadados públicos consultados pela API GitHub em 23/10/2026. Critérios: repositório público, atividade recente, fonte identificável, compatibilidade e licença passível de conferência. Links e tags podem mudar; o CSV registra um **instantâneo**, não inventário em tempo real.

## Pesquisas diretas no GitHub
Cole estas consultas na busca de repositórios do GitHub:
```text
topic:ai-memory archived:false pushed:>=2026-04-23
topic:security-scanner archived:false pushed:>=2026-04-23
topic:software-supply-chain archived:false pushed:>=2026-04-23
topic:llm-observability archived:false pushed:>=2026-04-23
topic:postgresql archived:false pushed:>=2026-04-23
```

## Filtro local
```bash
python3 scripts/filter_catalog.py --category memoria_ia
python3 scripts/filter_catalog.py --priority P0
python3 scripts/filter_catalog.py --min-stars 5000 --license Apache-2.0
python3 scripts/filter_catalog.py --query telemetry --output json
python3 scripts/filter_catalog.py --require-license-review
```

Campos do CSV: `repo,category,priority,license_claim,license_review_required,stars_snapshot,source_url,checked_at,origin`. Os valores de estrelas são históricos e servem para descoberta, **não para afirmações de elegibilidade**.

## Elegibilidade a programas para mantenedores OSS
Projetos de terceiros listados aqui não contam como propriedade do curador. Métricas como dependentes, downloads mensais, número de PRs externos aceitos e OpenSSF Criticality Score devem ser verificadas **no projeto próprio do candidato** e com URLs/intervalos auditáveis. Forks e cópias não geram essas métricas automaticamente. Não apresentar popularidade deste catálogo como adoção de um pacote.

## Limitações
`NOASSERTION` sinaliza que a API não mapeou licença SPDX; revisar o arquivo de licença no commit exato. Licença permissiva não é sinônimo de código seguro; a falta de alerta de CVE não é garantia de ausência de risco. As avaliações de benefícios futuros são hipóteses de pesquisa.
