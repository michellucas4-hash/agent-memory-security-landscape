# Metodologia: como pesquisar e comparar projetos open source

Este catálogo nasceu de uma pergunta prática: **qual ferramenta realmente merece uma avaliação antes de entrar em um sistema de IA?** Em vez de baixar tudo, registramos opções de estudo, classificamos por problema e apontamos fontes oficiais para aprofundamento.

## De onde vieram os dados

O inventário contém **45 repositórios GitHub de terceiros** identificados até **23/10/2026**. Para cada um, registramos nome, URL, categoria, prioridade editorial, licença informada, estrelas na data de coleta e indicação de revisão manual. A coleta não representa recomendação nem certificação de segurança.

As nove fichas mais detalhadas explicam cenários e riscos com linguagem humana. Elas **não afirmam que realizamos benchmarks funcionais** das ferramentas.

## Como interpretar os campos

| Campo | Significado | O que não significa |
|---|---|---|
| `repo` | Organização e projeto originais | Que somos mantenedores |
| `category` | Área de uso mais relevante nesta pesquisa | Que o projeto tenha apenas essa função |
| `priority` | P0 = pesquisar antes; P1 = estudar depois; P2 = acompanhar | Nível de segurança ou nota de qualidade |
| `license_claim` | SPDX informado pelo GitHub no snapshot | Aprovação jurídica automática |
| `license_review_required` | Necessidade de verificar manualmente licença | Que o uso está proibido |
| `stars_snapshot` | Estrelas observadas na data da coleta | Downloads, usuários ativos ou dependentes |
| `source_url` | Endereço do repositório original | Garantia de que o link nunca mudará |

`NOASSERTION` significa que a API não mapeou uma licença conclusiva. Leia o arquivo de licença e eventuais termos do release escolhido.

## Pesquisando no próprio GitHub

Abra [github.com/search](https://github.com/search) e selecione a aba **Repositories**. Exemplos de consultas que ajudam a encontrar novos candidatos:

```text
topic:ai-memory archived:false pushed:>=2026-04-23
topic:security-scanner archived:false pushed:>=2026-04-23
topic:software-supply-chain archived:false pushed:>=2026-04-23
topic:llm-observability archived:false pushed:>=2026-04-23
topic:postgresql archived:false pushed:>=2026-04-23
```

Essas buscas são **descoberta**, não homologação. Examine README, releases, histórico de manutenção, licenças, CVEs, issues e mudanças incompatíveis antes de instalar.

## Pesquisando nosso catálogo offline

Com Python 3.10+, execute no diretório clonado:

```bash
python3 scripts/filter_catalog.py --list-categories
python3 scripts/filter_catalog.py --category memoria_ia --priority P1
python3 scripts/filter_catalog.py --min-stars 5000 --license Apache-2.0
python3 scripts/filter_catalog.py --query telemetry --output json
python3 scripts/filter_catalog.py --sort stars --limit 10
python3 scripts/filter_catalog.py --category seguranca --output csv
python3 scripts/filter_catalog.py --require-license-review
```

O filtro **só acessa `catalogo/repositorios.csv`**; não consulta GitHub em tempo real e não instala nenhum software externo. Veja o [guia do primeiro teste](primeiro-teste.md).

## Como passar de hipótese a evidência

1. Declare um problema verificável (ex.: recordar a decisão mais recente).
2. Defina a alternativa atual e uma métrica de sucesso (ex.: acerto em 50 perguntas).
3. Compare uma ferramenta por vez em ambiente isolado, com corpus **sintético idêntico**.
4. Meça qualidade, latência p95, RAM, custo, exclusão de dados e recuperação.
5. Documente versão e commit, scripts do teste, resultados positivos e falhas.
6. Submeta a avaliação para revisão independente, preservando o direito de rejeitar a solução.

Use o [modelo de avaliação](../templates/avaliacao.md). Se a ferramenta processa dados pessoais ou comunica com provedores externos, isso precisa constar no relatório.

## Uma distinção importante sobre autoria e programas OSS

Catálogo e biblioteca de terceiros não contam como manutenção própria. Métricas de downloads, repositórios dependentes, colaboradores aceitos e **OpenSSF Criticality Score (0–1)** exigem evidências referentes a um projeto **realmente mantido** pelo candidato. Isso é diferente do OpenSSF Scorecard de segurança (0–10).

É positivo contribuir com documentação, issues e PRs de valor real para projetos upstream, mas contribuição não pode ser inventada a partir de forks ou clones.
