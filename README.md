# Agent Memory & Security — Guia aberto de ferramentas para IA

**Escolha com mais segurança ferramentas open source para memória de agentes de IA, RAG, segurança de skills, observabilidade e software supply chain.** Este projeto reúne explicações em português, links oficiais e um catálogo pesquisável. Foi feito para desenvolvedores, estudantes, pesquisadores e equipes que querem **entender antes de instalar**.

[![Catalog Quality](https://github.com/michellucas4-hash/agent-memory-security-landscape/actions/workflows/quality.yml/badge.svg)](https://github.com/michellucas4-hash/agent-memory-security-landscape/actions/workflows/quality.yml)
[![License MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-blue)](LICENSE)
[![Python 3](https://img.shields.io/badge/Python-3.10%2B-blue)](scripts/filter_catalog.py)

> **O que você encontra aqui:** documentação, comparativos, dados públicos em CSV e um pequeno filtro Python que funciona sem API, cadastro ou bibliotecas adicionais. **O que você não encontra:** os códigos-fonte dos 45 projetos externos, ferramentas de segurança instaladas ou métricas de desempenho que não foram medidas.

## Por onde começar?

| Quero... | Comece aqui |
|---|---|
| Descobrir bibliotecas de memória para IA | [Comparativo de memória](docs/comparativo-memoria.md) |
| Saber o que fazem as nove oportunidades recentes | [Fichas explicadas, uma por projeto](oportunidades/README.md) |
| Ver todos os 45 repositórios por categoria | [Catálogo em Markdown](catalogo/catalogo.md) |
| Filtrar por licença, popularidade ou categoria | [CSV público](catalogo/repositorios.csv) e [script](scripts/filter_catalog.py) |
| Entender segurança de agentes e dependências | [Trilha de segurança](docs/seguranca-agentes.md) |
| Avaliar um projeto de modo reproduzível | [Modelo de análise](templates/avaliacao.md) |
| Contribuir com correções e novas fontes | [Guia de contribuição](CONTRIBUTING.md) |

## Experimente em dois minutos

**Pré-requisito:** Python 3.10 ou mais recente. Os comandos abaixo **só leem os dados deste repositório**; não instalam os pacotes catalogados, não usam sua chave de API e não fazem chamadas de rede após o clone.

```bash
git clone https://github.com/michellucas4-hash/agent-memory-security-landscape.git
cd agent-memory-security-landscape

# Veja as opções de filtro disponíveis
python3 scripts/filter_catalog.py --help

# Encontre projetos de memória priorizados para estudo
python3 scripts/filter_catalog.py --category memoria_ia --priority P1

# Liste os que precisam de revisão manual da licença declarada
python3 scripts/filter_catalog.py --require-license-review

# Saída em JSON para seus próprios relatórios
python3 scripts/filter_catalog.py --category seguranca --output json

# Confira o inventário com testes automatizados
python3 -m unittest discover -s tests -v
```

No Windows, substitua `python3` por `py -3` se necessário. **Exemplo do que o filtro retorna:** `P1 mem0ai/mem0 https://github.com/mem0ai/mem0`. São **referências para estudar** — não instalações nem recomendações automáticas.

Não tem Python? Explore o [catálogo diretamente no navegador](catalogo/catalogo.md). Consulte também o [guia do primeiro teste](docs/primeiro-teste.md).

## As nove novas fichas de pesquisa

| Memória e contexto | Segurança e confiabilidade |
|---|---|
| [Hindsight](oportunidades/hindsight.md) — recuperação e síntese de memória | [GUAC](oportunidades/guac.md) — mapa de dependências e proveniência |
| [Cognee](oportunidades/cognee.md) — grafo de conhecimento | [Bandit](oportunidades/bandit.md) — análise estática Python |
| [Supermemory](oportunidades/supermemory.md) — memória e recuperação | [SkillSpector](oportunidades/skillspector.md) — verificação de skills |
| [Honcho](oportunidades/honcho.md) — contexto de participantes e sessões | [in-toto-golang](oportunidades/in-toto-golang.md) — integridade de builds |
| | [Opik](oportunidades/opik.md) — monitoramento e avaliação de agentes |

As fichas explicam **o problema**, **quando considerar**, **o que verificar antes de adotar**, **riscos** e **como medir resultados**. São avaliações documentais, não testes de desempenho já realizados.

## Como o catálogo é organizado

- `catalogo/`: inventário das 45 fontes, com categoria, prioridade editorial, URL oficial, licença declarada e um registro histórico de estrelas.
- `oportunidades/`: nove textos individuais com explicações acessíveis e questões técnicas.
- `docs/`: roteiro para começar, critérios de pesquisa, comparativos e boas práticas.
- `scripts/`: filtro local e utilitários do repositório (sem acesso automático a sistemas externos).
- `tests/`: verificações de consistência do inventário.
- `.github/workflows/`: validação automática dos arquivos publicados.
- `templates/`: formulário para quem quiser publicar avaliações reproduzíveis.

## Limites e transparência

**Este repositório é uma curadoria independente**, não um produto dos mantenedores das ferramentas citadas. Todos os nomes, marcas, códigos e licenças dos projetos externos pertencem aos respectivos autores. A licença [MIT](LICENSE) aplica-se ao conteúdo editorial e ao código original **deste** catálogo.

Os dados de popularidade e licenças são um **retrato coletado em 23/10/2026** e podem mudar. Uma classificação `P0`, `P1` ou `P2` indica nossa **ordem de pesquisa**, não uma nota de segurança. `NOASSERTION` significa que o GitHub não informou um identificador SPDX conclusivo: é preciso ler a licença original.

Nenhum repositório de terceiros listado aqui conta como autoria, manutenção ou dependentes do curador. Não publicamos dados privados, chaves, memórias empresariais ou código proprietário. Leia a [política de segurança](SECURITY.md) antes de enviar informações.

## Participe

Encontrou um link desatualizado, uma explicação confusa ou um experimento bem documentado? Abra uma [issue](https://github.com/michellucas4-hash/agent-memory-security-landscape/issues) ou envie um pull request seguindo o [CONTRIBUTING.md](CONTRIBUTING.md). Dê preferência a fontes oficiais e resultados que outras pessoas consigam reproduzir.

**Palavras-chave:** AI agent memory, RAG, LLM observability, open-source security, agent skills, SBOM, software supply chain, Python, GitHub.
