# hindsight — ficha de avaliação

**Categoria:** Memória de IA
**Prioridade inicial:** P1
**Licença informada pelo GitHub em 23/10/2026:** MIT (verificar arquivos/licença da versão exata)
**Origem:** [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Motor de memória persistente para agentes. Processa eventos e conversas por **retain**, recupera por **recall** (busca semântica, lexical/BM25, entidades/grafo e temporalidade) e sintetiza respostas por **reflect**. Permite isolamento em bancos de memória (banks) por agente, cliente ou projeto.

## Diferencial técnico
Relacionamentos temporais e consolidação de observações, além de integração documentada com PostgreSQL/pgvector.

## Como poderia ser útil
Estudar como camada de memória episódica que preserva origem, sequência temporal e evidências de decisões; comparar com pgvector puro e Graphiti.

## Requisitos e dependências a conferir
PostgreSQL/pgvector e serviço de processamento; algumas operações dependem de modelos de linguagem e embeddings. Confirmar topologia exata por versão.

## Riscos e pontos de segurança
Migrações automáticas, consumo de banco e embeddings, contradições, uso de APIs de terceiros, retenção de informações pessoais.

## Benchmark proposto (ainda não executado)
Recall@k por pergunta temporal, acerto da origem, p95, RAM, custo por 1.000 interações e restauração do banco.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
