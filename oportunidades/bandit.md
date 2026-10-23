# bandit — ficha de avaliação

**Categoria:** Segurança Python
**Prioridade inicial:** P0
**Licença informada pelo GitHub em 23/10/2026:** Apache-2.0 (verificar arquivos/licença da versão exata)
**Origem:** [PyCQA/bandit](https://github.com/PyCQA/bandit)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Ferramenta de análise estática que inspeciona AST de código Python para localizar padrões comuns de insegurança, como subprocessos perigosos, criptografia problemática e credenciais inseridas no código.

## Diferencial técnico
Baixo custo de adoção em pipelines de revisão de código Python; resultados estruturáveis para CI.

## Como poderia ser útil
Adicionar como verificação isolada de segurança em projetos Python públicos e exemplos reproduzíveis.

## Requisitos e dependências a conferir
Interpretador Python compatível e instalação controlada somente em ambiente de CI/homologação.

## Riscos e pontos de segurança
Falsos positivos e falsos negativos; não substitui threat modeling, scanner de dependências, pentest ou revisão humana.

## Benchmark proposto (ainda não executado)
Tempo de varredura, resultados confirmados por severidade, cobertura de arquivos e regressões no CI.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
