# Agent Memory & Security OSS Landscape

**Catálogo público, independente e reproduzível de projetos open source para memória de IA, segurança de agentes, observabilidade e cadeia de suprimentos.**
Pesquisa editorial em português. Atualização inicial: **23 de outubro de 2026**.

> Este repositório **não é um fork, mirror ou reempacotamento** dos projetos listados. Os mantenedores originais conservam autoria, licenças e marcas. Inclusão aqui não comprova segurança, adequação para produção, parceria ou uso real.

## Navegação
- [Inventário de 45 repositórios](catalogo/catalogo.md) · [dados em CSV](catalogo/repositorios.csv)
- [9 análises novas e detalhadas](oportunidades/README.md)
- [Comparativo de arquitetura de memória](docs/comparativo-memoria.md)
- [Trilhas de segurança](docs/seguranca-agentes.md)
- [Critérios de triagem e filtro GitHub](docs/metodologia-filtros.md)
- [Como contribuir](CONTRIBUTING.md) · [Política de segurança](SECURITY.md)
- [Modelo reprodutível de avaliação](templates/avaliacao.md)

## Oportunidades da pesquisa
| Área | Ferramentas em análise | Objetivo |
|---|---|---|
| Memória | Hindsight, Cognee, Supermemory, Honcho | Memória temporal, relacional e contextual |
| Segurança do código e supply chain | GUAC, Bandit, in-toto | Auditoria e proveniência |
| Segurança de skills | NVIDIA SkillSpector | Sinalizar riscos em extensões de agentes |
| Observabilidade | Opik | Traces, avaliação e monitoramento |

### Como filtrar o catálogo local
Requer apenas Python 3, sem instalação de bibliotecas externas:

```bash
python3 scripts/filter_catalog.py --category memoria_ia --priority P1
python3 scripts/filter_catalog.py --category seguranca --min-stars 3000
python3 scripts/filter_catalog.py --query graph --output json
python3 scripts/filter_catalog.py --require-license-review
python3 -m unittest discover -s tests -v
```

### Como utilizar sem riscos desnecessários
Comece pelos READMEs dos autores, avalie licenças e CVEs e use dados sintéticos. Não execute scripts ou instaladores de terceiros automaticamente. Para extensões de agentes, adote revisão de permissões, isolamento de rede, scanner de segredos e validação humana. Não envie logs, tokens ou memória privada a provedores externos sem autorização.

## Definições importantes
- **P0/P1/P2** representam interesse de pesquisa editorial, **não** nível verificado de segurança.
- **Licença declarada** vem da API pública do GitHub e precisa ser conferida no commit escolhido. `NOASSERTION` **não** quer dizer automaticamente software não licenciado.
- **Popularidade de upstream** não equivale a downloads ou dependentes de quem organiza este catálogo.
- **OpenSSF Criticality Score** (0–1) é diferente de **OpenSSF Scorecard** (0–10); nenhum desses valores é imputado ao autor deste guia.
- Métricas de desempenho listadas nas fichas são **planos de benchmark**, não resultados medidos.

## Fontes e responsabilidade
Cada ficha aponta para o GitHub original e resume características declaradas pelos próprios mantenedores. Metadados coletados em **23/10/2026**; podem mudar sem aviso. Pull requests com correções, links de evidência, benchmarks reproduzíveis e alertas de segurança são bem-vindos.

**Licença editorial e do código original deste catálogo:** MIT (consulte [LICENSE](LICENSE)); **código-fonte dos projetos externos não incluído**.
