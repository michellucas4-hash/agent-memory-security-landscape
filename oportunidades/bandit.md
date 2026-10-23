# Bandit: perguntas de segurança antes do código Python chegar à produção

**Projeto original:** [PyCQA/bandit](https://github.com/PyCQA/bandit) · **Área:** análise estática Python · **Licença declarada:** Apache-2.0 · **Prioridade editorial:** P0.

## O que ele faz?
O Bandit examina a estrutura do código Python sem precisar executar o programa. Seus plugins detectam **padrões que merecem revisão**, por exemplo chamadas perigosas ou opções de segurança inadequadas.

## Exemplo simples
Um colaborador propõe uma alteração que chama programas externos. Antes da aprovação, o Bandit pode sinalizar que aquela forma de chamada precisa ser revisada. Nem toda ocorrência é vulnerabilidade; a equipe deve analisar o contexto.

## Para quem serve
Projetos Python e pipelines de revisão de pull requests que querem tornar problemas recorrentes visíveis antes do deploy.

## Como testar
Consulte [instalação e comandos oficiais](https://github.com/PyCQA/bandit#readme), crie um ambiente virtual descartável e use **um arquivo Python de exemplo que você controla**. Execute a ferramenta no exemplo, interprete os alertas e confira manualmente se fazem sentido.

## Medições úteis
Tempo de verificação, cobertura dos arquivos, taxa de alertas realmente relevantes e facilidade de integrar o resultado ao CI.

## Limitações
Bandit não detecta todas as vulnerabilidades, não substitui auditoria humana, escaneamento de dependências, testes dinâmicos ou revisão de permissões.

**Status nesta coleção:** referência documentada para estudo. O catálogo não executa Bandit quando você roda seu filtro de repositórios.
