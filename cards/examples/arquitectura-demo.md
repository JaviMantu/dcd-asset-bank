---
description: "Deck de ejemplo (arquitectura, 12 diapositivas): Aseguradora Andina · Amaris"
description_en: "A complete neutral example deck of type «arquitectura» (12 slides): storyboard, brief, guion and titles, fictional client, ready to read as a model."
family: "examples"
id: "example/arquitectura-demo"
intent: []
keywords: []
layout: ""
path: "examples/arquitectura-demo/storyboard.json"
portrait: false
previews: []
related: ["adr-decisions", "arq-hero", "arq-roadmap", "c4-code", "c4-component", "c4-container"]
sha256: "2a55d126eda96478a26b5ba70672ad46c03efa3195db3aa12d101589a8515130"
size_bytes: 32870
tags: ["adr-decisions", "arq-hero", "arq-roadmap", "arquitectura", "arquitectura-demo", "c4-code", "c4-component", "c4-container", "c4-context", "data-architecture", "infra-topology", "quality-drivers", "risks-tradeoffs", "solution-layers"]
title: "Ejemplo · Aseguradora Andina · Amaris"
title_en: "Example · arquitectura-demo"
vertical: []
---
# Ejemplo · Aseguradora Andina · Amaris

## Brief

# Brief · Arquitectura de la plataforma de reclamos en línea (demo) > Ejemplo del tipo `arquitectura` (0.5.0). Cliente y sistema **ficticios**: «Aseguradora Andina» y su «Plataforma de > reclamos en línea». Sirve para ver las escenas de arquitectura funcionando, no como caso real. - **Sala.** El comité de arquitectura y el equipo de TI de la aseguradora: arquitectos, líderes de desarrollo, datos, infraestructura y seguridad. Sala técnica: el perfil de voz es `tecnico` y la palabra «arquitectura» se dice. - **Dolor.** Un reclamo hoy pasa por papel, correos y llamadas; tras una tormenta el volumen se triplica y el registro se atasca. (Hipótesis del ejemplo, no un dato.) - **Decisión que buscamos.** Validar la arquitectura propuesta y aprobar un taller de dos semanas con su comité. - **Prueba.** Las vistas C4 de contexto a código, las capas, el dato, la infraestructura, tres decisiones con su costo y cuatro riesgos con su mitigación; las metas de calidad (99,9 %, 3× en picos) se dicen como metas por validar. - **Límites.** Sin precios, sin ROI, sin fechas más allá del próximo paso (las fases siguientes son «Fase 2…4»); ninguna tecnología del cliente real, porque no hay cliente real. - **Minutos.** 40 (12 diapositivas, versión `full`). Cortes: `meta.simple` (8) y `meta.focus` (solucion, software, datos, infraestructura, c4). - **Firma.** Manager responsable: Javier Montaño. ## Cómo se construye ```bash python3 scripts/new.py /tmp/dcd-arq --type arquitectura --size full --client…

## Diapositivas

1. Reclamos resueltos en línea, de principio a fin · `arq-hero`
2. Cuatro atributos de calidad guían cada decisión técnica · `quality-drivers`
3. Contexto: quién usa la plataforma y con qué conversa · `c4-context`
4. Seis contenedores que se despliegan y escalan por separado · `c4-container`
5. Dentro de la API: cinco componentes con una sola responsabilidad · `c4-component`
6. El código del núcleo: clases y dependencias del reclamo · `c4-code`
7. Cinco capas, de los canales a la plataforma · `solution-layers`
8. El dato del reclamo, del evento al tablero, con gobierno · `data-architecture`
9. Tres zonas de seguridad y tres ambientes idénticos · `infra-topology`
10. Tres decisiones que tomamos y lo que cuestan · `adr-decisions`
11. Cada riesgo tiene su mitigación y su costo · `risks-tradeoffs`
12. Cada reclamo, resuelto en línea y a tiempo · `arq-roadmap`

## What it is

A complete neutral example deck of type «arquitectura» (12 slides): storyboard, brief, guion and titles, fictional client, ready to read as a model.

## Relacionadas · Related

- [adr-decisions · Diseño técnico por capas](../scenes/adr-decisions.md)
- [arq-hero · Portada: su promesa](../scenes/arq-hero.md)
- [arq-roadmap · Próximo paso: formas de empezar y discovery](../scenes/arq-roadmap.md)
- [c4-code · Diseño técnico por capas](../scenes/c4-code.md)
- [c4-component · Diseño técnico por capas](../scenes/c4-component.md)
- [c4-container · Diseño técnico por capas](../scenes/c4-container.md)

Fuente · source: [`examples/arquitectura-demo/storyboard.json`](../../examples/arquitectura-demo/storyboard.json) · sha256 `2a55d126eda9`
