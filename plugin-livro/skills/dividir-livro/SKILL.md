---
name: dividir-livro
description: Divide um livro em PDF em um PDF por capítulo. Use quando o usuário enviar um livro e pedir para dividir, separar ou quebrar em capítulos. É a etapa 1 do fluxo livro → capítulos → .md → resumo.
---

# Dividir livro em capítulos

1. Liste os marcadores do PDF: `python scripts/dividir.py livro.pdf --listar`.
2. Se houver marcadores de capítulo, divida: `python scripts/dividir.py livro.pdf --saida capitulos/`.
3. Se não houver, leia o sumário com Read (primeiras páginas), monte os intervalos e confirme com o usuário. Depois divida: `python scripts/dividir.py livro.pdf --saida capitulos/ --intervalos "1-Introdução:1-18;2-Anatomia:19-45"`. As páginas são as do arquivo, não as impressas, então ajuste pelo deslocamento.
4. Se faltar o pypdf, instale com `pip install pypdf`.
5. Informe quantos capítulos foram gerados e ofereça a próxima etapa: extrair o texto para .md.
