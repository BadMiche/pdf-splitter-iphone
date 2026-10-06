"""Divide um PDF em capítulos por marcadores (nível 1) ou por intervalos manuais."""
import argparse
import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def nome_seguro(s):
    return re.sub(r"[^\w\- ]", "", s).strip().replace(" ", "_")[:60] or "capitulo"


def marcadores(reader):
    caps = []
    for item in reader.outline:
        if not isinstance(item, list):
            caps.append((item.title, reader.get_destination_page_number(item)))
    return sorted(caps, key=lambda c: c[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--saida", default="capitulos")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--intervalos", help='"nome:ini-fim;nome:ini-fim" (páginas a partir de 1)')
    a = ap.parse_args()

    reader = PdfReader(a.pdf)
    total = len(reader.pages)

    if a.intervalos:
        partes = []
        for p in a.intervalos.split(";"):
            nome, faixa = p.rsplit(":", 1)
            ini, fim = (int(x) for x in faixa.split("-"))
            partes.append((nome, ini - 1, fim))
    else:
        caps = marcadores(reader)
        if a.listar or not caps:
            for t, pg in caps:
                print(f"p.{pg + 1}\t{t}")
            print(f"{len(caps)} marcadores, {total} páginas")
            return
        partes = [(t, pg, caps[i + 1][1] if i + 1 < len(caps) else total) for i, (t, pg) in enumerate(caps)]

    out = Path(a.saida)
    out.mkdir(parents=True, exist_ok=True)
    for i, (nome, ini, fim) in enumerate(partes, 1):
        w = PdfWriter()
        for n in range(ini, fim):
            w.add_page(reader.pages[n])
        arq = out / f"{i:02d}_{nome_seguro(nome)}.pdf"
        with open(arq, "wb") as f:
            w.write(f)
        print(f"{arq}  (p.{ini + 1}-{fim})")


if __name__ == "__main__":
    main()
