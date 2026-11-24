#!/usr/bin/env python3
"""Catálogo de medicamentos de CIMA / AEMPS (API de datos abiertos).

Actor: https://apify.com/innovito/cima-medicamentos-aemps
Campos de entrada: name, activeIngredient, laboratory, registrationNumber,
commercializedOnly, keywords, enrichDetails, maxItems.
Precio publicado: 1,50 $ / 1.000 medicamentos + 0,00005 $ por arranque.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/cima-medicamentos-aemps"

run_input = {
    "activeIngredient": "paracetamol",
    "commercializedOnly": True,
    "enrichDetails": False,
    "maxItems": 10,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        [
            "registrationNumber",
            "name",
            "activeIngredients",
            "laboratory",
            "prescriptionStatus",
            "cimaUrl",
        ],
    )
