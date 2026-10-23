# Opik: enxergue o caminho percorrido por um agente de IA

**Projeto original:** [comet-ml/opik](https://github.com/comet-ml/opik) · **Área:** observabilidade e avaliação de LLMs · **Licença declarada:** Apache-2.0 · **Prioridade de pesquisa:** P1.

## Por que é interessante?
Quando um agente erra, olhar apenas a resposta final costuma ser insuficiente. O Opik ajuda a acompanhar a sequência de chamadas e decisões — *traces* — e avaliar resultados com experimentos e conjuntos de testes.

## Funções descritas pelo mantenedor
Rastreamento de chamadas de modelo e ferramentas, datasets de avaliação, experimentos, dashboards de monitoramento e acompanhamento de prompts. O projeto oferece opções auto-hospedadas e serviço em nuvem; condições e funcionalidades devem ser verificadas por versão.

## Exemplo de aplicação
Um assistente responde incorretamente a uma pergunta sobre um documento. Um trace pode mostrar qual trecho recuperou, que chamadas realizou e onde a informação se perdeu. Um experimento reproduzível ajuda a comparar uma correção com o comportamento anterior.

## Antes de começar
Consulte o [guia oficial de instalação](https://github.com/comet-ml/opik#readme), escolha ambiente isolado e desligue a coleta de dados reais. Logs de IA podem registrar prompts, dados pessoais e credenciais acidentalmente.

## O que medir
Cobertura de traces, overhead de latência p95, tamanho de armazenamento, taxa de amostragem, precisão das avaliações e qualidade do filtro de dados sensíveis.

**Atenção:** esta ficha não oferece um painel Opik hospedado e não contém avaliações operacionais próprias.
