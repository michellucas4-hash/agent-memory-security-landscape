# Cognee: de documentos espalhados a conhecimento conectado

**Projeto original:** [topoteretes/cognee](https://github.com/topoteretes/cognee) · **Área:** memória e grafos de conhecimento · **Licença declarada:** Apache-2.0 · **Prioridade editorial:** P1.

## Em poucas palavras
Guardar documentos não é o mesmo que compreender como eles se relacionam. O Cognee oferece uma maneira de transformar textos, código e conversas em conhecimento estruturado que um agente consegue consultar depois.

## Como funciona
O projeto combina extração de entidades e relações, construção de grafo, índices de busca e recuperação contextual. O README atual descreve também um caminho local com modelos menores; os requisitos exatos dependem da versão e dos extras escolhidos.

## Exemplo de aplicação
Você tem relatórios de incidentes, documentos de API e decisões de arquitetura. Ao perguntar “quais serviços dependem da versão que será alterada?”, um grafo bem alimentado pode conectar componentes que não aparecem juntos no mesmo arquivo.

## Para quem faz sentido
Equipes com documentação dispersa, bases técnicas extensas e perguntas que exigem conectar várias fontes. Para pesquisas simples de similaridade, uma solução vetorial menor pode ser suficiente.

## Limitações e riscos
A construção do grafo pode ser custosa; relações geradas podem estar erradas ou duplicadas. Confira se a configuração usa modelos locais ou externos, onde os dados persistem, como retirá-los e quais conectores têm acesso aos documentos.

## Primeira experiência sugerida
Em ambiente descartável, use 20 textos públicos ou sintéticos, com nomes e relações que você já conhece. Compare respostas multi-etapas, relações incorretas, tempo de ingestão, consumo de memória e exclusão de documentos. **Não utilize dados empresariais como corpus de estreia.**

**Veja antes de instalar:** [documentação e quickstart oficiais](https://github.com/topoteretes/cognee#readme). Esta ficha resume possibilidades, não validação operacional.
