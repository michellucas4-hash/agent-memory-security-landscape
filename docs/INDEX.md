# Central de documentação

Bem-vindo! Este projeto não instala as bibliotecas que apresenta. Nosso objetivo é ajudar você a **escolher o que merece um teste** e registrar os resultados de maneira verificável.

## Começando

| Documento | O que você vai encontrar |
|---|---|
| [Seu primeiro teste](primeiro-teste.md) | Como explorar os 45 projetos e executar o filtro, mesmo sem experiência com ferramentas de IA |
| [Comparativo de memória](comparativo-memoria.md) | Diferenças entre busca vetorial, grafos e memórias persistentes |
| [Segurança de agentes](seguranca-agentes.md) | Como revisar código, dependências, skills e proveniência |
| [Metodologia e filtros](metodologia-filtros.md) | Como os dados foram selecionados, como pesquisar no GitHub e limitações |
| [Próximos passos](proximos-passos.md) | O que falta medir antes de recomendar a adoção de qualquer pacote |
| [Publicação](publicacao.md) | O que é público e como o conteúdo do catálogo é organizado |

## Conteúdo fora de `docs/`

- **[45 referências de projetos](../catalogo/catalogo.md):** categorias, descrição breve, prioridade de pesquisa, licenças informadas e links oficiais.
- **[Nove fichas em linguagem simples](../oportunidades/README.md):** quando usar, exemplos e riscos.
- **[Exemplo de registro de avaliação](../templates/avaliacao.md):** perguntas para comprovar ganhos em vez de apenas supor.
- **[Filtro Python](../scripts/filter_catalog.py):** busca offline em um CSV público, sem bibliotecas adicionais.
- **[Política de segurança](../SECURITY.md):** como reportar informações sensíveis.

## O que significa “testado”?

Os **testes automatizados deste repositório verificam o catálogo**, os links internos e o filtro Python. Eles não comprovam que as bibliotecas de terceiros foram executadas, são seguras ou funcionam em qualquer ambiente.

Para testar um projeto externo, leia a documentação do respectivo autor, registre a versão exata e use ambiente descartável com dados sintéticos. Caso publique um resultado, explique como outra pessoa poderá reproduzi-lo.
