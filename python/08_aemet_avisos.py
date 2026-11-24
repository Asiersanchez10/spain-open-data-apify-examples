#!/usr/bin/env python3
"""Avisos meteorológicos oficiales de AEMET Meteoalerta (feed CAP, sin clave).

Actor: https://apify.com/innovito/aemet-avisos-predicciones
Campos de entrada: mode, feedUrl, language, minSeverity, areas, apiKey,
municipalities, maxItems.
Precio publicado: 4,00 $ / 1.000 avisos o días de predicción + 0,00005 $ por arranque.

Este ejemplo usa mode=warnings, que no necesita apiKey. Las predicciones
municipales (mode=forecasts o both) sí exigen tu clave gratuita de OpenData.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/aemet-avisos-predicciones"

run_input = {
    "mode": "warnings",
    "language": "es",
    "minSeverity": "Moderate",
    "areas": ["Madrid"],
    "maxItems": 10,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        ["headline", "event", "severity", "area", "onset", "expires", "webUrl"],
    )
