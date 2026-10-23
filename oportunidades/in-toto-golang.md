# in-toto-golang — ficha de avaliação

**Categoria:** Proveniência de builds
**Prioridade inicial:** P2
**Licença informada pelo GitHub em 23/10/2026:** NOASSERTION (revisar LICENSE) (verificar arquivos/licença da versão exata)
**Origem:** [in-toto/in-toto-golang](https://github.com/in-toto/in-toto-golang)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Biblioteca Go do ecossistema in-toto, orientada a metadados e verificação da cadeia de fornecimento de software, conectando passos de build e evidências verificáveis.

## Diferencial técnico
Permite trabalhar com informações estruturadas de proveniência e integridade de etapas, complementando assinaturas de artefatos.

## Como poderia ser útil
Estudar atestações de build e política de verificação para releases públicos auditáveis.

## Requisitos e dependências a conferir
Toolchain Go, formatos compatíveis e chaves de assinatura protegidas; definir modelo de ameaça antes da integração.

## Riscos e pontos de segurança
Ausência de verificação da licença pela identificação SPDX da API, risco de falsas atestações, gestão de chaves e compatibilidade de formatos.

## Benchmark proposto (ainda não executado)
Validação de atestação autêntica versus adulterada, integridade do encadeamento e reprodutibilidade do build.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
