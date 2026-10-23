# Matriz comparativa — memória persistente para agentes

Comparativo conceitual, **não** benchmark. Cada opção precisa de provas de performance e uma arquitetura de referência antes de qualquer escolha.

| Projeto | Ênfase | Modelo de armazenamento/retrieval (alto nível) | Ponto de atenção |
|---|---|---|---|
| [pgvector](https://github.com/pgvector/pgvector) | Índices vetoriais dentro do PostgreSQL | Pesquisa por embeddings e operações PostgreSQL | Não oferece memória episódica pronta |
| [Graphiti](https://github.com/getzep/graphiti) | Grafos temporais de conhecimento | Entidades, relações e contexto temporal | Desenho do grafo, banco/embeddings, custo |
| [Hindsight](../oportunidades/hindsight.md) | Memória temporal e síntese | Retain/recall/reflect; semântica, BM25, grafo, tempo | Processamento e modelo auxiliar |
| [Cognee](../oportunidades/cognee.md) | Aprendizado de relacionamentos | Grafo mais memória vetorial e ingestão estruturada | Ingestão e atualização coerentes |
| [Supermemory](../oportunidades/supermemory.md) | Memória/perfis + RAG | Extração de fatos, busca híbrida, ciclo de vida | Edição local versus serviços hospedados |
| [Honcho](../oportunidades/honcho.md) | Memória entre peers/sessões | Representações contextualizadas por participante | AGPL-3.0, isolamento, processamento |
| [Mem0](https://github.com/mem0ai/mem0) | Memória de longo prazo para agentes | Extração e recuperação de fatos relevantes | Governança da memória e provedores |
| [Letta](https://github.com/letta-ai/letta) | Agentes com estado persistente | Gerenciamento de memória/estado dos agentes | Complexidade do framework |
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | RAG baseado em grafo | Conhecimento estruturado a partir de documentos | Custo de indexação |
| [Qdrant](https://github.com/qdrant/qdrant) | Banco de busca vetorial | Semântica em coleção vetorial | Serviço adicional e sincronismo |
| [Chroma](https://github.com/chroma-core/chroma) | Busca e armazenamento de embeddings | Coleções de vetores e metadados | Duplicação de persistência |

## Protocolo de benchmarking sugerido
1. Usar **dados sintéticos idênticos**, corpus com perguntas temporais, contradições, múltiplas entidades e contextos por usuário.
2. Comparar baseline simples (PostgreSQL/pgvector) versus **uma** tecnologia candidata por vez.
3. Medir recall@5/10, precisão factual, fidelidade de citação, comportamento ao esquecer, isolamento de clientes e restauração após reinício.
4. Capturar p50/p95, uso máximo de RAM, tamanho de banco, ingestão/hora, custo de inferência e esforço operacional.
5. Bloquear integração se ocorrer vazamento entre clientes, perda não recuperável de memória ou incompatibilidade de licença.

Sem esses resultados, a ordem P0/P1/P2 não prova superioridade.
