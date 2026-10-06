---
name: resumir-capitulo
description: Resume um capítulo de livro em PDF (inclusive digitalizado) para um arquivo .md só com o conteúdo importante, sem referências nem trechos vazios. Use quando o usuário enviar um PDF de capítulo e pedir resumo, "passar para md", "extrair o texto" ou "resumir capítulo".
---

# Resumir capítulo em PDF → Markdown

1. Leia o PDF inteiro com a ferramenta Read (para mais de 20 páginas, leia em blocos com `pages`, ex.: "1-20", "21-40"). Páginas digitalizadas são lidas como imagem; não é preciso OCR.
2. Escreva o resumo em português, em Markdown:
   - Mantenha: conceitos, definições, critérios, classificações, números, doses, condutas.
   - Remova: referências/bibliografia, agradecimentos, cabeçalhos/rodapés, números de página, legendas sem conteúdo, exercícios e qualquer trecho sem informação.
   - Corrija erros de digitalização.
   - Use `#` para o título do capítulo, `##` para as seções originais, e listas e tabelas quando ajudarem.
   - Não invente nada que não esteja no texto.
3. Salve como `<nome-do-pdf>.md` no diretório de trabalho e envie o arquivo ao usuário. No chat, responda só com uma linha e o arquivo.
