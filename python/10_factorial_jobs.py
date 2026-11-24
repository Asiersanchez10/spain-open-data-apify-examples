#!/usr/bin/env python3
"""Ofertas de empleo en career sites alojados en Factorial HR.

Actor: https://apify.com/innovito/factorial-jobs-scraper
Campos de entrada (esquema público de la ficha): companies (obligatorio),
keywords, searchInDescription, locations, workplaceTypes, onlyNewJobs,
includeDescription, maxJobsPerCompany, maxItems, maxConcurrency.
Precio publicado: 2,00 $ / 1.000 ofertas + 0,00005 $ por arranque.

`companies` admite el subdominio o la URL del career site, según la ficha
https://apify.com/innovito/factorial-jobs-scraper/input
El valor "careers" es un ejemplo del prefill oficial del esquema. Cámbialo
por las empresas que quieras vigilar.
"""

from _common import print_rows, run_actor

ACTOR = "innovito/factorial-jobs-scraper"

run_input = {
    "companies": ["careers"],
    "keywords": ["engineer"],
    "searchInDescription": False,
    "locations": [],
    "workplaceTypes": [],
    "onlyNewJobs": False,
    "includeDescription": False,
    "maxJobsPerCompany": 5,
    "maxItems": 5,
    "maxConcurrency": 2,
}

if __name__ == "__main__":
    rows = run_actor(ACTOR, run_input)
    print_rows(
        rows,
        ["company", "title", "location", "workplaceType", "datePosted", "url"],
    )
