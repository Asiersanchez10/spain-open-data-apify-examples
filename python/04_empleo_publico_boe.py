#!/usr/bin/env python3
"""Convocatorias de empleo público y oposiciones del BOE, sección II.B.

Actor: https://apify.com/innovito/empleo-publico-boe
Campos de entrada: dateFrom, dateTo, lookbackDays, keywords, maxItems.
Precio publicado: 2,00 $ / 1.000 vacantes + 0,00005 $ por arranque.
No incluye listas de aspirantes, calificaciones ni nombramientos.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/empleo-publico-boe"

run_input = {
    "lookbackDays": 7,
    "keywords": ["informática"],
    "maxItems": 10,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        ["noticeId", "publicationDate", "department", "title", "htmlUrl", "pdfUrl"],
    )
