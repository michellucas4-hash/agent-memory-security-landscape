# Seu primeiro teste: do navegador ao filtro local

Este guia é para quem está conhecendo projetos de IA e segurança e quer **experimentar este catálogo sem instalar nenhum deles**.

## 1. Conheça as opções no navegador (sem instalar nada)

Abra o [catálogo por área](../catalogo/catalogo.md) e escolha uma ferramenta. Cada nome leva ao repositório do mantenedor original. Para os nove projetos avaliados com mais detalhe, navegue pelas [fichas individuais](../oportunidades/README.md).

Por exemplo: se sua dúvida é como uma IA pode lembrar de conversas anteriores, comece por [Hindsight](../oportunidades/hindsight.md), [Cognee](../oportunidades/cognee.md) e pelo [comparativo de memória](comparativo-memoria.md). Você encontrará perguntas de avaliação, não uma promessa de performance.

## 2. Teste o filtro sem baixar dependências dos projetos

Você só precisa ter **Git** e **Python 3.10+**. Clone este repositório (o *catálogo*, não os códigos dos projetos listados):

```bash
git clone https://github.com/michellucas4-hash/agent-memory-security-landscape.git
cd agent-memory-security-landscape
python3 scripts/filter_catalog.py --help
```

No Windows, `py -3` geralmente substitui `python3`.

Experimente três perguntas:

```bash
# Quais projetos de memória receberam prioridade de pesquisa P1?
python3 scripts/filter_catalog.py --category memoria_ia --priority P1

# Quais fontes declaram licença Apache-2.0 e têm ao menos 5.000 estrelas na foto histórica?
python3 scripts/filter_catalog.py --license Apache-2.0 --min-stars 5000

# Quais requerem leitura manual da licença?
python3 scripts/filter_catalog.py --require-license-review --output json
```

Os resultados apresentam **nome, URL e metadados históricos**, sem verificar em tempo real os servidores dos autores. O filtro não executa pacotes externos nem solicita credenciais.

## 3. Execute nossos testes

```bash
python3 -m unittest discover -s tests -v
```

Eles verificam a integridade do CSV, a documentação de referência e o funcionamento dos filtros. O GitHub também os executa automaticamente no [Catalog Quality](https://github.com/michellucas4-hash/agent-memory-security-landscape/actions/workflows/quality.yml).

Se algum comando falhar, confirme a versão do Python, confira se está na pasta clonada e abra uma issue incluindo a saída **sem** senhas, dados privados ou tokens.

## 4. Deseja testar uma ferramenta externa de verdade?

As ferramentas listadas **não são instaladas pelo catálogo**. Acesse o README oficial do projeto escolhido, leia a licença e suas dependências, escolha uma versão identificada, crie um ambiente de teste descartável e use somente dados sintéticos.

Anote o que estava tentando resolver, versão, hardware, RAM, tempo de resposta, critérios de acerto, custo e resultados negativos. Use nosso [modelo de avaliação](../templates/avaliacao.md) e publique somente evidências sem informações sensíveis.

**Importante:** estrelas no GitHub, licenças permissivas ou uma execução com sucesso não provam adequação à produção.
