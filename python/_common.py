"""Utilidad compartida para los ejemplos. No contiene secretos."""

from __future__ import annotations

import os
import sys
from typing import Any, Mapping

from apify_client import ApifyClient


def get_client() -> ApifyClient:
    token = os.environ.get("APIFY_TOKEN", "").strip()
    if not token:
        sys.exit(
            "Falta la variable de entorno APIFY_TOKEN.\n"
            "Copia .env.example a .env, pon tu token de la consola de Apify "
            "y exporta APIFY_TOKEN (o usa un gestor de secretos). "
            "No lo escribas en el código ni lo subas a GitHub."
        )
    return ApifyClient(token)


def run_actor(actor_id: str, run_input: Mapping[str, Any], timeout_secs: int = 180) -> list[dict[str, Any]]:
    """Lanza un Actor, espera a que termine y devuelve las filas del dataset por defecto.

    La firma de `call` / `iterate_items` sigue el cliente oficial documentado en
    https://docs.apify.com/api/client/python y en las fichas de Store
    (sección API de cada actor, p. ej. https://apify.com/innovito/licitaciones-placsp).
    """
    client = get_client()
    run = client.actor(actor_id).call(run_input=dict(run_input), timeout_secs=timeout_secs)
    dataset_id = run["defaultDatasetId"]
    print(f"Run {run['id']}  dataset {dataset_id}  estado {run.get('status')}")
    return list(client.dataset(dataset_id).iterate_items())


def print_rows(rows: list[dict[str, Any]], fields: list[str], limit: int = 5) -> None:
    if not rows:
        print("El dataset está vacío (filtros demasiado estrechos o no hay novedades).")
        return
    print(f"{len(rows)} fila(s). Mostrando hasta {limit}:")
    for row in rows[:limit]:
        snippet = {key: row.get(key) for key in fields if key in row}
        print(snippet)
