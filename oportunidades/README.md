# Nove ferramentas para conhecer — e como escolher o que testar

É fácil acumular projetos interessantes no GitHub. O desafio é descobrir **qual problema cada um resolve de verdade**. Nesta seção, reunimos nove ferramentas externas com explicações em português, cenários do cotidiano e pontos de atenção antes de instalar.

| Se sua necessidade é... | Vale conhecer | O que procurar na ficha |
|---|---|---|
| Lembrar decisões com contexto temporal | [Hindsight](hindsight.md) | Como atualiza e recupera fatos antigos |
| Ligar conceitos espalhados por documentos | [Cognee](cognee.md) | Construção e consultas em grafos |
| Reaproveitar informações de conversas | [Supermemory](supermemory.md) | Memória persistente e opções de hospedagem |
| Isolar memória entre participantes e sessões | [Honcho](honcho.md) | Workspaces, peers e licença AGPL |
| Entender dependências de aplicações | [GUAC](guac.md) | Grafo de componentes e proveniência |
| Detectar padrões inseguros em Python | [Bandit](bandit.md) | Alertas de análise estática e limites |
| Descobrir por que um agente falhou | [Opik](opik.md) | Traces, experimentos e avaliação |
| Inspecionar uma skill antes da instalação | [NVIDIA SkillSpector](skillspector.md) | Sinais de prompt injection e exfiltração |
| Comprovar etapas de um build | [in-toto-golang](in-toto-golang.md) | Atestações e integridade |

## Por onde eu começaria?

Se você pesquisa **memória de IA**, compare Hindsight, Cognee, Supermemory e Honcho com uma solução vetorial simples. Não instale os quatro de uma vez: escolha uma hipótese, fixe uma versão e meça resultados.

Se a preocupação é **segurança**, Bandit e SkillSpector atendem necessidades diferentes: o primeiro procura padrões arriscados em código Python; o segundo analisa riscos em skills de agentes. GUAC e in-toto ajudam a entender **de onde veio o software**.

Se busca **qualidade operacional**, o Opik merece estudo para entender os passos executados por uma aplicação de IA — com atenção aos dados que vão para os traces.

## O que cada ficha informa?

Todas apresentam a função, um exemplo concreto, riscos e um roteiro sugerido de avaliação. A documentação indica o **repositório original** de cada autor. São pesquisas documentais: não declaramos instalação, homologação ou benchmarks próprios.

**Quer tentar agora?** Siga o [primeiro teste do catálogo](../docs/primeiro-teste.md) e depois consulte o [modelo de avaliação](../templates/avaliacao.md).
