#!/usr/bin/env python3
"""Precios horarios PVPC de la electricidad en España (archivo público ESIOS / REE).

Actor: https://apify.com/innovito/precios-luz-pvpc
Campos de entrada: dateFrom, dateTo, lookbackDays, maxItems.
Precio publicado: 2,50 $ / 1.000 precios horarios + 0,00005 $ por arranque.
No requiere token de ESIOS.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/precios-luz-pvpc"

run_input = {
    "lookbackDays": 1,
    "maxItems": 24,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        ["date", "hour", "pcbEurPerMwh", "pcbEurPerKwh", "cymEurPerMwh", "sourceUrl"],
        limit=8,
    )
