---
name: extrair-md
description: Converte o PDF de um capítulo (inclusive digitalizado) em .md com o texto completo e limpo, sem resumir. Use quando o usuário pedir para extrair o texto, transcrever ou "passar para md". É a etapa 2 do fluxo livro → capítulos → .md → resumo.
---

# Extrair texto do capítulo para .md

Para cada PDF de capítulo (por exemplo, os da pasta `capitulos/`):

1. Leia todas as páginas com Read, em blocos de até 20 (`pages: "1-20"`). Páginas digitalizadas são lidas como imagem; não é preciso OCR.
2. Transcreva o texto **completo**, sem resumir:
   - Corrija erros de digitalização e junte as palavras hifenizadas na quebra de linha.
   - Remova cabeçalhos/rodapés repetidos e números de página.
   - Mantenha a estrutura em Markdown (`#` para o capítulo, `##` e `###` para as seções), as listas e as tabelas.
   - Mantenha as referências nesta etapa, numa seção `## Referências` no fim.
3. Salve como `<mesmo-nome>.md` ao lado do PDF.
4. Ao terminar, liste os .md gerados e ofereça a próxima etapa: os resumos.
