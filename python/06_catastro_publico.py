#!/usr/bin/env python3
"""Datos públicos no protegidos del Catastro (dirección, superficie, año, coordenadas).

Actor: https://apify.com/innovito/catastro-publico
Campos de entrada: cadastralReferences, includeCoordinates, maxItems.
Precio publicado: 2,00 $ / 1.000 fichas + 0,00005 $ por arranque.
Nunca solicita ni devuelve el titular, el NIF ni el valor catastral.

Pon TÚ una referencia catastral de prueba que te pertenezca o que sea
públicamente reutilizable. Este ejemplo no incluye ninguna referencia inventada.
"""

import os
import sys

from _common import print_rows, run_actor

ACTOR = "innovito/catastro-publico"


def main() -> None:
    raw = os.environ.get("CADASTRAL_REFERENCES", "").strip()
    references = [part.strip() for part in raw.split(",") if part.strip()]
    if not references:
        sys.exit(
            "Define CADASTRAL_REFERENCES con una o varias referencias catastrales "
            "separadas por comas (por ejemplo, una de un inmueble propio). "
            "El actor no devuelve titulares ni valor catastral."
        )
    run_input = {
        "cadastralReferences": references,
        "includeCoordinates": True,
        "maxItems": 5,
    }
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        [
            "cadastralReference",
            "address",
            "municipality",
            "province",
            "use",
            "floorAreaM2",
            "constructionYear",
            "latitude",
            "longitude",
        ],
    )


if __name__ == "__main__":
    main()
