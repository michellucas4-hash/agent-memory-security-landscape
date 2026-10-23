# NVIDIA SkillSpector: revise uma skill antes de confiá-la ao agente

**Projeto original:** [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) · **Área:** segurança de skills de IA · **Licença declarada:** Apache-2.0 · **Prioridade:** P1.

## O problema que tenta resolver
Uma skill pode parecer apenas um conjunto de instruções, mas também pode pedir permissões excessivas, executar código perigoso ou tentar enviar dados para fora do ambiente. Antes de instalar uma extensão num agente com acesso a arquivos, vale inspecioná-la.

## O que oferece
Segundo o projeto oficial, o SkillSpector analisa skills e extensões procurando indícios de **prompt injection, exfiltração, falhas de segurança e riscos de dependências**. Possui análise estática e análise semântica opcional por modelo; pode produzir relatórios estruturados. Ele **não executa** a skill inspecionada.

## Exemplo prático
Você recebe uma skill que promete organizar arquivos. O scanner pode identificar instruções que tentam enviar esses arquivos para um serviço remoto. Um alerta assim pede investigação humana antes de qualquer instalação.

## Como testar com cuidado
Leia o [quickstart oficial](https://github.com/NVIDIA/SkillSpector#readme) e use uma **skill sintética ou publicamente autorizada**, em ambiente descartável. Para evitar envio do conteúdo a modelos externos, examine o modo estático `--no-llm`; verifique que consultas de dependências ao OSV.dev ainda podem transmitir nomes e versões dos pacotes.

## Limites importantes
Um relatório sem alertas **não certifica a segurança**; o projeto é análise preventiva, não isolamento de execução. Confirme permissões de rede, versão instalada, padrões suportados e privacidade antes do uso corporativo.

## O que medir
Detecção de casos conhecidos em corpus sintético, falsos positivos, tempo por skill e decisões efetivamente revisáveis.

**Status:** pesquisa de segurança e proposta de teste, não endosso de instalação.
