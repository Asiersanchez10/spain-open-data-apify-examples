# Flujo n8n: alertas diarias de licitaciones PLACSP

Archivo: `alertas-licitaciones-placsp-sheets.json`

Cada día laborable a las 8:00 (zona `Europe/Madrid`) el flujo:

1. Lee la configuración (filtros CPV, comunidad, estado, tope de filas).
2. Llama a `POST https://api.apify.com/v2/acts/innovito~licitaciones-placsp/runs?waitForFinish=180` con el input del actor ([documentación de la API de runs](https://docs.apify.com/api/v2/act-runs-post), ficha [innovito/licitaciones-placsp](https://apify.com/innovito/licitaciones-placsp)).
3. Descarga el dataset: `GET /v2/datasets/{defaultDatasetId}/items`.
4. Normaliza las columnas y, si has puesto el ID de una hoja, las añade al final de Google Sheets.

Se usa la API HTTP oficial, no un nodo de comunidad, para que el JSON se pueda importar en n8n Cloud o autoalojado sin instalar paquetes. Si prefieres el nodo oficial de Apify (`@apify/n8n-nodes-apify`, operaciones *Run an Actor* y *Get dataset items*), la guía está en [docs.apify.com/platform/integrations/n8n](https://docs.apify.com/platform/integrations/n8n).

## Importación

1. En n8n: *Workflows → Import from File* y elige este JSON.
2. Crea una credencial **Header Auth**:
   - Header name: `Authorization`
   - Header value: `Bearer ` + tu token de Apify (Consola → Settings → Integrations).
3. Asigna esa credencial a los nodos **Ejecutar actor PLACSP** y **Leer dataset del actor** (sustituye el id `REPLACE_APIFY_CREDENTIAL_ID` al importar, o selecciónala a mano).
4. Conecta Google Sheets OAuth en **Añadir a Google Sheets**.
5. En **Configuración**, cambia `spreadsheetId` por el ID real de tu hoja (el de la URL de Google Sheets). Mientras valga `REEMPLAZA_CON_EL_ID_DE_TU_HOJA`, el flujo no escribe nada y te avisa.
6. Ajusta `cpvPrefixes`, `autonomousCommunities`, `statusCodes` y `maxItems`. Empieza bajo: el actor cobra 2,00 $ por cada 1.000 licitaciones escritas, más 0,00005 $ por arranque (precio de la ficha en noviembre de 2026).
7. Crea en la hoja las columnas: `contractFolderId`, `status`, `title`, `contractingAuthority`, `estimatedValueEur`, `autonomousCommunity`, `submissionDeadline`, `officialUrl`, `sourceAttribution`.
8. Ejecuta a mano una vez antes de dejarlo programado.

El JSON no lleva `pinData`, tokens, correos ni IDs reales, de acuerdo con las [pautas de plantillas de n8n](https://docs.n8n.io/contribute/create-templates/submission-guidelines).
