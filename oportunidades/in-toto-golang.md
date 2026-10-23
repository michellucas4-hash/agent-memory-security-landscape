# in-toto-golang: evidências sobre como um artefato foi construído

**Projeto original:** [in-toto/in-toto-golang](https://github.com/in-toto/in-toto-golang) · **Área:** proveniência de software · **Licença na API GitHub:** NOASSERTION — requer leitura do arquivo LICENSE · **Prioridade:** P2.

## Para que serve?
Um pacote pode chegar acompanhado de uma assinatura, mas uma equipe também pode precisar entender **como ele foi produzido**: etapas de construção, materiais utilizados e atestações relacionadas.

## O que encontrar neste projeto
Implementações em Go ligadas ao ecossistema in-toto, voltadas a evidências verificáveis da cadeia de suprimentos. As APIs disponíveis dependem da versão exata; consulte o repositório antes de copiar exemplos.

## Exemplo
Uma equipe gera um pacote em seu pipeline. Ela quer demonstrar que veio do código e da sequência de etapas esperados, e detectar se uma evidência foi adulterada.

## Como iniciar a avaliação
Abra a [documentação original](https://github.com/in-toto/in-toto-golang#readme), confirme a licença de fato e analise exemplos e versões publicadas. Em sandbox isolado, prepare metadados **sintéticos**, altere deliberadamente uma evidência e teste se a verificação rejeita o caso.

## Cuidados
Não exponha chaves privadas, segredos de build ou descrições de infraestrutura sensível. Defina quem assina, quem verifica e o que cada atestação realmente prova.

**Nota sobre a licença:** `NOASSERTION` é um resultado de metadados do GitHub, não conclusão de que o software não tem licença. Esta ficha não afirma que algum build real foi atestado por nós.
