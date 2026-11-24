#!/usr/bin/env python3
"""Licitaciones europeas del TED (Tenders Electronic Daily), API oficial de búsqueda v3.

Actor: https://apify.com/innovito/ted-eu-tenders
Campos de entrada: dateFrom, dateTo, lookbackDays, buyerCountry, noticeTypes,
cpvPrefixes, keywords, language, expertQuery, maxItems, maxPages.
Precio publicado: 1,50 $ / 1.000 licitaciones + 0,00005 $ por arranque.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/ted-eu-tenders"

run_input = {
    "lookbackDays": 3,
    "buyerCountry": "ESP",
    "language": "spa",
    "cpvPrefixes": ["72"],
    "keywords": [],
    "maxItems": 10,
    "maxPages": 1,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        [
            "publicationNumber",
            "publicationDate",
            "title",
            "buyerName",
            "buyerCountry",
            "cpvCodes",
            "deadline",
            "htmlUrl",
        ],
    )
