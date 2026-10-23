# opik — ficha de avaliação

**Categoria:** Observabilidade e avaliação
**Prioridade inicial:** P1
**Licença informada pelo GitHub em 23/10/2026:** Apache-2.0 (verificar arquivos/licença da versão exata)
**Origem:** [comet-ml/opik](https://github.com/comet-ml/opik)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Plataforma para rastreamento de agentes, chamadas de modelos, experimentos, gestão de prompts, avaliações e monitoramento de fluxos RAG/LLM.

## Diferencial técnico
Reúne traces, avaliações automatizadas e acompanhamento de experimentos em uma plataforma self-hostable.

## Como poderia ser útil
Comparar com Langfuse e Phoenix para identificar erros de agentes e regressões de resposta antes de promoção.

## Requisitos e dependências a conferir
Servidor Opik ou serviço externo, SDKs e sistema de armazenamento; avaliar requisitos de implantação por versão.

## Riscos e pontos de segurança
Exposição inadvertida de prompts, logs, dados pessoais e credenciais; aumento do armazenamento e custo operacional.

## Benchmark proposto (ainda não executado)
Cobertura de traces, impacto p95, taxa de amostragem, política de redação de dados, rastreabilidade e custo.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
