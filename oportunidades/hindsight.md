# Hindsight: memória que considera o contexto e o tempo

**Projeto original:** [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) · **Área:** memória de agentes · **Licença declarada:** MIT · **Nossa prioridade de pesquisa:** P1.

## Em poucas palavras
Imagine um assistente que lembra de uma decisão antiga, mas percebe que ela foi substituída por outra ontem. O Hindsight pesquisa informações guardadas e busca organizá-las com contexto temporal, em vez de tratar toda lembrança como uma nota solta.

## O que o projeto oferece
A arquitetura documentada pelo autor usa operações de retenção (**retain**), recuperação (**recall**) e reflexão (**reflect**). Pode combinar busca semântica, busca lexical, entidades e contexto temporal. Consulte a documentação original para ver as APIs e requisitos da versão escolhida.

## Exemplo de uso
Em um projeto de software, a equipe registra que uma integração foi planejada, depois adiada e finalmente aprovada. A pergunta “qual é a decisão mais recente e por quê?” exige recuperar a sequência inteira, não somente o registro com palavras parecidas.

## Quando vale pesquisar
Memória persistente entre sessões, histórico de decisões e sistemas que precisam distinguir **informação atual** de informações superadas.

## Cuidados antes de adotar
O processamento pode consumir banco, modelos de embedding e inferência. Verifique se dados vão a provedores externos, como funciona a exclusão e qual componente controla a persistência. Use apenas uma base de testes isolada.

## Como avaliar de forma reproduzível
Crie 50 fatos sintéticos com datas, atualizações e contradições. Pergunte por decisões atuais, referências históricas e fatos que deveriam ter sido esquecidos. Meça acerto, citações de origem, latência p95, RAM e custo por consulta; compare com uma busca simples em PostgreSQL/pgvector.

**Comece pela fonte oficial:** [README e instruções do mantenedor](https://github.com/vectorize-io/hindsight#readme). Nenhum teste funcional desse projeto é reivindicado por este catálogo; a proposta acima é um roteiro de avaliação.
