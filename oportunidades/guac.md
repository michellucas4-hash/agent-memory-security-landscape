# guac — ficha de avaliação

**Categoria:** Segurança de cadeia de suprimentos
**Prioridade inicial:** P1
**Licença informada pelo GitHub em 23/10/2026:** Apache-2.0 (verificar arquivos/licença da versão exata)
**Origem:** [guacsec/guac](https://github.com/guacsec/guac)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
GUAC (Graph for Understanding Artifact Composition) agrega metadados de segurança, dependências e proveniência do software em um grafo que permite investigar relações entre componentes, vulnerabilidades e artefatos.

## Diferencial técnico
Correlaciona dados de múltiplas origens em vez de apenas executar scanner de vulnerabilidades isolado.

## Como poderia ser útil
Relacionar SBOM, versões, CVEs e proveniência de releases de uma biblioteca open source própria.

## Requisitos e dependências a conferir
Serviços GUAC, ingestores e armazenamento de grafo; validar arquitetura e ingestores disponíveis.

## Riscos e pontos de segurança
Complexidade operacional, dados externos incompletos, volume de eventos, identidades de pacote ambíguas e falsos vínculos.

## Benchmark proposto (ainda não executado)
Cobertura de artefatos/SBOM, tempo para identificar componente afetado, integridade da proveniência e tempo de consulta.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
