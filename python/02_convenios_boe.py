#!/usr/bin/env python3
"""Convenios colectivos de trabajo publicados en el BOE (sección III).

Actor: https://apify.com/innovito/convenios-colectivos-boe
Campos de entrada: dateFrom, dateTo, lookbackDays, keywords, maxItems.
Precio publicado: 2,50 $ / 1.000 convenios + 0,00005 $ por arranque.
Usa la API oficial de datos abiertos del BOE. No incluye nombramientos ni edictos.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/convenios-colectivos-boe"

run_input = {
    "lookbackDays": 14,  # por defecto en el esquema si no hay dateFrom
    "keywords": ["hostelería"],
    "maxItems": 10,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        ["agreementId", "publicationDate", "department", "title", "htmlUrl", "pdfUrl"],
    )
