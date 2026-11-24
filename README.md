# Spain open data examples for Apify / Ejemplos de datos abiertos de España en Apify

Python scripts and an n8n workflow that call the public, pay-per-event Apify Actors published by [innovito](https://apify.com/innovito). This repository contains **usage examples only**. The Actor source code stays on Apify and is not included here.

Scripts de Python y un flujo de n8n que llaman a los actores públicos de pago por uso publicados en [apify.com/innovito](https://apify.com/innovito). Este repositorio contiene **solo ejemplos de uso**. El código de los actores permanece en Apify y no se incluye aquí.

> **Not an official government product / No es un producto oficial de la Administración.**
> The data comes from official open-data APIs and feeds (PLACSP, TED, BOE, BDNS / SNPSAP, Cadastre, CIMA / AEMPS, AEMET, ESIOS / REE). You must credit the official source. The Cadastre Actor never returns owners or cadastral value. The BDNS Actor returns grant *calls* only, not awards to people. The public-employment Actor does not return applicant lists.
>
> Los datos salen de APIs y feeds oficiales de datos abiertos. Hay que citar la fuente. El Catastro no devuelve titulares ni valor catastral; la BDNS, solo convocatorias; el empleo público, sin listas de personas.

This repo is ready to publish, but it has **not** been created or pushed on GitHub.

---

## English

### What is in this repo

| Path | What it does |
|---|---|
| `python/01_placsp_tenders.py` | Latest Spanish public tenders (PLACSP) |
| `python/02_convenios_boe.py` | Collective agreements from the BOE |
| `python/03_bdns_calls.py` | Grant *calls* from BDNS / SNPSAP |
| `python/04_empleo_publico_boe.py` | Public-employment notices (BOE II.B) |
| `python/05_ted_tenders.py` | EU TED tenders |
| `python/06_catastro_publico.py` | Public Cadastre parcel data (no owners) |
| `python/07_cima_medicamentos.py` | Spanish medicines catalogue (CIMA / AEMPS) |
| `python/08_aemet_avisos.py` | AEMET Meteoalerta warnings (no API key) |
| `python/09_pvpc_precios.py` | Hourly PVPC electricity prices |
| `python/10_factorial_jobs.py` | Job postings from Factorial HR career sites |
| `n8n/alertas-licitaciones-placsp-sheets.json` | Daily PLACSP alerts into Google Sheets |

Actor pages (price and input schema live here — always check the page before a large run):

- https://apify.com/innovito/licitaciones-placsp — $2.00 / 1,000 tenders + $0.00005 start
- https://apify.com/innovito/convenios-colectivos-boe — $2.50 / 1,000 + $0.00005 start
- https://apify.com/innovito/bdns-convocatorias — $1.50 / 1,000 + $0.00005 start
- https://apify.com/innovito/empleo-publico-boe — $2.00 / 1,000 + $0.00005 start
- https://apify.com/innovito/ted-eu-tenders — $1.50 / 1,000 + $0.00005 start
- https://apify.com/innovito/catastro-publico — $2.00 / 1,000 + $0.00005 start
- https://apify.com/innovito/cima-medicamentos-aemps — $1.50 / 1,000 + $0.00005 start
- https://apify.com/innovito/aemet-avisos-predicciones — $4.00 / 1,000 + $0.00005 start
- https://apify.com/innovito/precios-luz-pvpc — $2.50 / 1,000 + $0.00005 start
- https://apify.com/innovito/factorial-jobs-scraper — $2.00 / 1,000 + $0.00005 start

Prices are those published on the Actor READMEs in November 2026. They can change; the Store page is the source of truth.

### Setup

1. Create an [Apify](https://console.apify.com) account and an API token (Console → Settings → Integrations / API tokens).
2. Copy `.env.example` to `.env` and set `APIFY_TOKEN`. Never commit `.env`.
3. `python3 -m venv .venv && source .venv/bin/activate`
4. `pip install -r python/requirements.txt`
5. `export APIFY_TOKEN=...` (or load `.env` with your usual tool)
6. `python python/01_placsp_tenders.py`

Examples cap `maxItems` (and feed pages) so a first run stays small. You are billed per event on Apify, not by this repository.

The Cadastre example does not ship a cadastral reference. Set `CADASTRAL_REFERENCES` yourself (a property you own, or another reference you are allowed to look up).

### n8n

Import `n8n/alertas-licitaciones-placsp-sheets.json` into n8n (self-hosted or Cloud). Create:

- an HTTP Header Auth credential named **Apify API token** (`Authorization` = `Bearer YOUR_TOKEN`);
- a Google Sheets OAuth credential;
- your spreadsheet ID in the **Configuración** node (replace `REEMPLAZA_CON_EL_ID_DE_TU_HOJA`).

The workflow timezone is `Europe/Madrid`. It runs weekdays at 08:00. Details are in `n8n/README.md`. You can also use the official Apify community node (`@apify/n8n-nodes-apify`) described at [docs.apify.com/platform/integrations/n8n](https://docs.apify.com/platform/integrations/n8n).

### License

MIT, see `LICENSE`. The official datasets remain under their own reuse terms (for example Ley 37/2007 and each body's legal notice).

---

## Español

### Qué hay en este repositorio

La tabla de arriba lista un script por actor y un flujo de n8n para volcar licitaciones de PLACSP a Google Sheets cada día laborable.

### Cómo ejecutarlo

1. Crea una cuenta en [Apify](https://console.apify.com) y un token de API.
2. Copia `.env.example` a `.env` y pon `APIFY_TOKEN`. No subas `.env` a GitHub.
3. `python3 -m venv .venv && source .venv/bin/activate`
4. `pip install -r python/requirements.txt`
5. `export APIFY_TOKEN=...`
6. `python python/01_placsp_tenders.py`

Los ejemplos llevan un `maxItems` bajo a propósito. El cobro es el de cada ficha de Apify (pago por evento). Revisa el precio actual en la página del actor antes de una corrida grande.

El ejemplo del Catastro no incluye ninguna referencia catastral: define `CADASTRAL_REFERENCES` con una referencia que te pertenezca o que puedas consultar.

### n8n

Importa `n8n/alertas-licitaciones-placsp-sheets.json`. Configura la credencial de Apify (cabecera `Authorization: Bearer ...`), la de Google Sheets y el ID de tu hoja en el nodo **Configuración**. La zona horaria del flujo es `Europe/Madrid`. Más detalle en `n8n/README.md`.

Si quieres conectar estas plantillas con el trabajo de Flujito (o enviar una versión al Creator Hub de n8n), lee `CONNECTING-FLUJITO.md`. Las tres plantillas ya preparadas de Flujito (TicketBAI, remesa SEPA y recordatorios de cobro) son otro producto y no están en este repositorio.

### Licencia

MIT, ver `LICENSE`. Los conjuntos de datos oficiales siguen sus propias condiciones de reutilización.
