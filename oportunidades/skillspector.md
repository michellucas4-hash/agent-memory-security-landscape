# SkillSpector — ficha de avaliação

**Categoria:** Segurança de agentes
**Prioridade inicial:** P1
**Licença informada pelo GitHub em 23/10/2026:** Apache-2.0 (verificar arquivos/licença da versão exata)
**Origem:** [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Scanner de segurança de habilidades (skills) e pacotes usados por agentes de IA. Procura indicadores de prompt injection, exfiltração, permissões excessivas e problemas de cadeia de suprimentos.

## Diferencial técnico
Voltado especificamente ao risco de instalar skills de agentes, com análise estática e recursos opcionais de avaliação semântica.

## Como poderia ser útil
Utilizar como referência de triagem antes de qualquer habilitação de skill ou plugin proveniente de terceiros.

## Requisitos e dependências a conferir
Verificar modos estático e semântico, modelos utilizados, formatos de entrada e política de execução.

## Riscos e pontos de segurança
Scanner não garante segurança, pode não detectar ataques inéditos; análise LLM opcional pode enviar código a terceiros; preservar sandbox.

## Benchmark proposto (ainda não executado)
Detecção em corpus sintético controlado, falsos positivos, duração por pacote e rastreio de evidências.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
