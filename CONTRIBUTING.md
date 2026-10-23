# Como contribuir — seja bem-vindo!

Este catálogo é feito para quem quer entender ferramentas open source de IA com clareza. **Não é necessário ser especialista em segurança ou inteligência artificial** para contribuir: uma correção de link, uma explicação melhor ou um exemplo honesto de teste já ajuda.

## Três formas de participar

**Encontrou algo errado?** Abra uma [issue](https://github.com/michellucas4-hash/agent-memory-security-landscape/issues/new/choose) com o link da página, a correção sugerida e uma fonte confiável.

**Descobriu uma ferramenta interessante?** Use o modelo “Sugerir uma ferramenta OSS”. Diga o que ela resolve, quem a mantém, a licença e por que vale avaliá-la. Não há obrigação de instalar o software para enviar uma sugestão.

**Quer publicar um comparativo?** Use o [modelo de avaliação](templates/avaliacao.md), com versão exata, dados sintéticos, indicadores claros e resultados que outra pessoa consiga reproduzir.

## Enviando um pull request

1. Crie um fork deste repositório pela interface do GitHub.
2. Faça as alterações numa branch separada e escreva claramente o que mudou.
3. Preserve créditos, nomes e links para os autores originais.
4. Execute **somente os testes do catálogo** em seu computador:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/filter_catalog.py --category memoria_ia --output json
```

5. Confira se os links internos funcionam e se os exemplos correspondem ao que está publicado.
6. Abra um PR descrevendo a mudança em linguagem simples. Os testes de **Catalog Quality** rodam automaticamente.

## Critérios de revisão

Valorizamos informação verificável, linguagem acessível, bom senso sobre riscos, fontes oficiais e compatibilidade com usuários de Windows, Linux e macOS.

Não inclua chaves, tokens, credenciais, endereços de redes internas, dados de clientes, logs privados ou material copiado de terceiros sem licença compatível. Caso descubra algo sensível, leia [SECURITY.md](SECURITY.md) e não divulgue detalhes numa issue pública.

**Transparência:** não transforme um plano de benchmark em resultado medido. Não apresente downloads, forks, estrelas ou contribuições dos autores dos projetos externos como se fossem do catálogo.

Obrigado por colaborar. Uma documentação que evita uma instalação arriscada já faz diferença.
