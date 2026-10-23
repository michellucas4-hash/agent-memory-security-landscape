# honcho — ficha de avaliação

**Categoria:** Memória de IA
**Prioridade inicial:** P2
**Licença informada pelo GitHub em 23/10/2026:** AGPL-3.0 (verificar arquivos/licença da versão exata)
**Origem:** [plastic-labs/honcho](https://github.com/plastic-labs/honcho)
**Situação:** pesquisa documental; não é indicação de instalação nem homologação.

## O que faz
Infraestrutura de memória contextual com organização por workspaces, peers, sessões e mensagens. Produz representações de participantes, raciocina sobre interações e permite consultas e busca.

## Diferencial técnico
Modelagem explícita de quem sabe o quê sobre pessoas, agentes e sessões, com processamento de memória em segundo plano.

## Como poderia ser útil
Benchmark em ambientes de múltiplos agentes e contextos compartilhados, sem importar dados reais.

## Requisitos e dependências a conferir
Servidor/CLI/SDKs do projeto; validar necessidades de backend, filas, modelos e forma de implantação.

## Riscos e pontos de segurança
Licença AGPL-3.0 exige revisão jurídica antes de integração/distribuição em rede; processamento assíncrono e segregação de tenants.

## Benchmark proposto (ainda não executado)
Acurácia por agente, isolamento cross-tenant, tempo de consolidação, custo de inferência e repetibilidade.

## Critérios de aprovação
1. Procedência e licença verificadas no commit/release exato, SBOM e CVEs triados.
2. Instalação exclusivamente em sandbox descartável, com permissões mínimas e dados sintéticos.
3. Comparação reprodutível com baseline definido; documentar custos e medições reais.
4. Evidência de rollback, teste de isolamento e revisão independente antes de integrar qualquer produção.

## Atribuição
Descrição editorial original de projeto externo. Código e marcas permanecem sob direitos e licenças dos respectivos mantenedores. Não se atribuem downloads, contribuições ou estatísticas do upstream aos curadores deste catálogo.
