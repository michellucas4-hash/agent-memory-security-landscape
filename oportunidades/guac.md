# GUAC: um mapa para investigar a origem do software

**Projeto original:** [guacsec/guac](https://github.com/guacsec/guac) · **Área:** segurança da cadeia de suprimentos · **Licença declarada:** Apache-2.0 · **Prioridade de pesquisa:** P1.

## Por que existe
Um sistema pode incorporar centenas de bibliotecas. Quando uma falha é anunciada, uma lista de pacotes ajuda, mas nem sempre esclarece **qual produto depende de quê** e **de onde veio cada componente**.

## O que o GUAC faz
GUAC significa *Graph for Understanding Artifact Composition*. Ele reúne metadados de software e segurança — como dependências, SBOMs, informações de vulnerabilidade e atestações — em um grafo consultável, com identidades e relações normalizadas.

## Exemplo do dia a dia
Uma dependência transitiva apresenta CVE. O GUAC pode apoiar a análise de quais artefatos a incorporam e quais evidências de proveniência estão relacionadas, desde que os dados de entrada sejam completos e corretos.

## Não confunda
GUAC **não substitui** scanners como OSV Scanner ou Trivy. É uma camada de agregação e investigação: necessita das fontes de evidência e de uma operação do grafo.

## Primeira avaliação sugerida
Monte SBOMs sintéticas para três aplicações, com componentes compartilhados. Altere a versão de um componente e confira se a consulta identifica o impacto. Registre tempo de ingestão, relações ausentes, falsos vínculos e custo de manter o serviço.

## Cuidados
Não exponha grafos de dependências internos, chaves de assinatura ou SBOMs confidenciais em repositórios públicos.

**Leia o [README oficial e os exemplos](https://github.com/guacsec/guac#readme)**. Esta ficha descreve o potencial do projeto, não um serviço GUAC funcionando aqui.
