# Supermemory: contexto que acompanha o assistente

**Origem:** [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) · **Área:** memória e recuperação · **Licença declarada:** MIT · **Prioridade de pesquisa:** P1.

## O problema em linguagem simples
Uma IA sem memória precisa receber o mesmo contexto repetidamente. O Supermemory busca facilitar a organização, atualização e recuperação de informações relevantes para que aplicações consigam trabalhar com contexto persistente.

## Funcionalidades a investigar
Os componentes do ecossistema incluem memória, recursos de busca e integração com fluxos de agentes. A disponibilidade de cada componente pode variar entre projeto open source, SDK e serviço gerenciado; **não presuma que todas as funcionalidades de nuvem sejam auto-hospedáveis**.

## Exemplo concreto
Um usuário informa que prefere respostas curtas. Depois, pede uma explicação detalhada para uma questão técnica. A ferramenta de memória deve preservar a preferência geral sem impedir a instrução atual.

## Quando pode ajudar
Assistentes personalizados, recuperação de conhecimento e serviços que reutilizam contexto entre conversas.

## Cuidados importantes
Separar usuários, definir consentimento, retenção e exclusão, controlar integradores externos e checar o custo de embeddings. Evite memorizar credenciais, dados sensíveis ou conteúdo de clientes sem base legítima.

## Avaliação prática proposta
Use usuários fictícios e fatos conflitantes. Meça atualização correta de preferências, ausência de vazamento entre usuários, comportamento de esquecimento, tokens economizados e latência. Compare com um baseline simples de memória local.

**Referência para instalação e detalhes atuais:** [README oficial](https://github.com/supermemoryai/supermemory#readme). Não é uma integração pronta oferecida por este catálogo.
