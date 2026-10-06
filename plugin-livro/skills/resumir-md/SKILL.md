---
name: resumir-md
description: Gera um resumo a partir de arquivos .md de capítulos. Só trabalha com .md; se o usuário enviar PDF, encaminha para a skill extrair-md antes. Use quando o usuário pedir para resumir capítulos ou .md. É a etapa 3 do fluxo livro → capítulos → .md → resumo.
---

# Resumir capítulos a partir do .md

**Regra:** leia somente arquivos `.md`. Se a entrada for PDF ou outro formato, não resuma: execute antes a skill `extrair-md`, ou peça ao usuário que a execute.

Para cada `.md` de capítulo:

1. Leia o arquivo inteiro.
2. Escreva o resumo em português, em Markdown:
   - Mantenha: conceitos, definições, critérios, classificações, números, doses, condutas.
   - Remova: a seção de referências, agradecimentos, exercícios, legendas sem conteúdo e trechos sem informação.
   - Siga as seções do capítulo (`##`), em listas diretas; use tabelas para comparações.
   - Não invente nada que não esteja no .md.
3. Salve como `<nome>_resumo.md` na pasta `resumos/`.
4. No fim, informe os arquivos gerados em uma linha.
