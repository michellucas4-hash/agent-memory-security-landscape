# Honcho: memória sobre participantes, não apenas mensagens

**Projeto original:** [plastic-labs/honcho](https://github.com/plastic-labs/honcho) · **Área:** memória multiagente · **Licença declarada:** AGPL-3.0 · **Prioridade editorial:** P2.

## Em poucas palavras
Em uma conversa com vários agentes, não basta lembrar o texto: importa saber **quem afirmou algo**, em qual sessão e qual contexto pode ser reutilizado. O Honcho organiza mensagens e representações de participantes.

## Conceitos centrais
A documentação apresenta **workspaces**, **peers** (participantes) e **sessions**. Uma sessão guarda a interação; representações de participantes podem resumir informações através de sessões, respeitando os limites de isolamento configurados.

## Exemplo de aplicação
Um agente de suporte e outro de planejamento colaboram num projeto fictício. Ambos precisam preservar fatos sobre o projeto sem misturar a memória de duas organizações diferentes. O limite entre workspaces precisa ser comprovado por teste, nunca suposto.

## O que avaliar primeiro
Segregação entre workspaces e sessões, configurações de observação, atualização de representações, processamento assíncrono e dependências de inferência.

## Atenção especial à licença
A **AGPL-3.0** exige avaliação jurídica cuidadosa antes de distribuição ou prestação de serviço em rede com modificações. Além disso, memória de pessoas pode exigir regras de privacidade, consentimento e exclusão.

## Teste recomendado
Crie dois workspaces sintéticos com participantes homônimos. Registre fatos incompatíveis, consulte a memória de cada ambiente e procure qualquer vazamento cruzado. Registre latência, custo, qualidade das representações e comportamento após reinício.

**Leitura recomendada:** [documentação e repositório oficial](https://github.com/plastic-labs/honcho#readme). Sem instalação nem homologação realizada aqui.
