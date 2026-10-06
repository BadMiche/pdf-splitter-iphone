"""Lê um capítulo em PDF (inclusive digitalizado) e gera um .md resumido via Claude.

Uso: python resumir.py capitulo.pdf [saida.md]
Requer: pip install anthropic  |  export ANTHROPIC_API_KEY=...
"""
import base64
import sys
from pathlib import Path

import anthropic

MODELO = "claude-sonnet-5-5"

PROMPT = """Este PDF é um capítulo de livro digitalizado. Leia todas as páginas e produza um resumo em Markdown, em português:

- Mantenha só o conteúdo importante: conceitos, definições, critérios, classificações, números, condutas.
- Remova: referências/bibliografia, agradecimentos, cabeçalhos/rodapés, números de página, legendas sem conteúdo, exercícios e qualquer trecho sem informação.
- Corrija erros de digitalização.
- Use títulos (##) seguindo a estrutura do capítulo, listas e tabelas quando ajudarem.
- Não invente informação que não está no texto.

Responda apenas com o Markdown."""


def main():
    if len(sys.argv) < 2:
        sys.exit("Uso: python resumir.py capitulo.pdf [saida.md]")
    pdf = Path(sys.argv[1])
    saida = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf.with_suffix(".md")

    dados = base64.standard_b64encode(pdf.read_bytes()).decode()
    cliente = anthropic.Anthropic()
    with cliente.messages.stream(
        model=MODELO,
        max_tokens=16000,
        messages=[{
            "role": "user",
            "content": [
                {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": dados}},
                {"type": "text", "text": PROMPT},
            ],
        }],
    ) as stream:
        resposta = stream.get_final_message()

    texto = "".join(b.text for b in resposta.content if b.type == "text")
    saida.write_text(texto, encoding="utf-8")
    print(f"Salvo em {saida}")


if __name__ == "__main__":
    main()
