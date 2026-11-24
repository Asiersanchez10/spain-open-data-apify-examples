# Cómo encaja este repo con las plantillas de Flujito

Flujito ya tiene tres plantillas n8n listas en `/workspace/negocio/plantillas-n8n/` (facturas TicketBAI, remesa SEPA y recordatorios de cobro). Son otro producto, para gestorías, y **no deben mezclarse en este repositorio** salvo que Asier lo pida.

Este archivo solo describe cómo reutilizar el flujo de licitaciones (y los que Flujito prepare después) junto a ese trabajo:

1. El flujo `n8n/alertas-licitaciones-placsp-sheets.json` es un punto de partida. Antes de enviarlo al [Creator Hub de n8n](https://docs.n8n.io/contribute/create-templates/submission-guidelines) hay que: probarlo de verdad en n8n, poner notas adhesivas de sección si el número de nodos lo exige, sustituir los ids de credencial por el flujo de importación de n8n, y no incluir secretos.
2. Flujito no debe colarlo delante de las tres plantillas que ya esperan el alta de Asier en [creators.n8n.io](https://creators.n8n.io/register). El Hub solo admite una plantilla en revisión por creador nuevo.
3. La credencial de Apify es un token personal de Asier (o del usuario final). Nunca se hardcodea. En un template público se documenta cómo crearla, igual que en las plantillas de Gmail o Sheets que Flujito ya usa.
4. Si se publica el repo en GitHub, el JSON de n8n de este directorio es el que debe enlazarse desde r/n8n o desde community.n8n.io (las normas piden el código en GitHub, Gist o n8n.io/workflows).
5. Ideas de plantillas siguientes, sin enviarlas todavía, están en `/workspace/difusion-apify/04-brief-flujito-plantillas-n8n.md`.
