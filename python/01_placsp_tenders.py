#!/usr/bin/env python3
"""Últimas licitaciones de la Plataforma de Contratación del Sector Público (PLACSP).

Actor: https://apify.com/innovito/licitaciones-placsp
Campos de entrada (input_schema del actor): maxItems, maxPages, statusCodes,
cpvPrefixes, autonomousCommunities, keywords, feedUrl.
Precio publicado en la ficha (nov 2026): 2,00 $ / 1.000 licitaciones + 0,00005 $ por arranque.
El Actor lee el feed oficial de datos abiertos (sindicación 643), no el buscador web.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/licitaciones-placsp"

# Input real, con topes bajos para no lanzar una corrida grande por accidente.
# statusCodes: PUB = publicado, RES = resuelto, ADJ = adjudicado.
run_input = {
    "maxItems": 10,
    "maxPages": 1,
    "statusCodes": ["PUB"],
    "cpvPrefixes": ["72"],  # informática / servicios IT (prefijo CPV)
    "autonomousCommunities": ["Madrid"],
    "keywords": [],
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        [
            "contractFolderId",
            "status",
            "title",
            "contractingAuthority",
            "estimatedValueEur",
            "autonomousCommunity",
            "submissionDeadline",
            "officialUrl",
        ],
    )
