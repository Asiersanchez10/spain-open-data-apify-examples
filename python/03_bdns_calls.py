#!/usr/bin/env python3
"""Convocatorias de subvenciones de la BDNS / SNPSAP (solo convocatorias, no concesiones).

Actor: https://apify.com/innovito/bdns-convocatorias
Campos de entrada: dateFrom, dateTo, lookbackDays, administrationLevels, keywords,
maxItems, maxPages.
Precio publicado: 1,50 $ / 1.000 convocatorias + 0,00005 $ por arranque.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/bdns-convocatorias"

run_input = {
    "lookbackDays": 7,
    "administrationLevels": ["ESTATAL", "AUTONOMICA"],
    "keywords": ["digitalización", "formación"],
    "maxItems": 10,
    "maxPages": 2,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        [
            "bdnsCode",
            "title",
            "receptionDate",
            "administrationLevel",
            "regionOrDepartment",
            "grantingBody",
            "officialUrl",
        ],
    )
