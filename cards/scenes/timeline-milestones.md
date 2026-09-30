---
description: "Una línea desde «Hoy» con cinco hitos, cada uno con su periodo, su nombre y un ícono de su sector, alternando a un lado y al otro."
description_en: "Timeline scene, layout «left», for any decks. It lands at a glance, then breathes in a slow loop; its args (events, now) carry every visible word, so the same scene serves a new client once the texts are rewritten."
family: "scenes"
id: "timeline-milestones"
intent: ["roadmap", "timeline"]
keywords: ["cronologia", "fases", "hitos", "hoja de ruta", "linea de tiempo", "roadmap", "timeline"]
layout: "left"
path: "scenes/story/intents_s09_16.py"
portrait: true
previews: ["previews/timeline-milestones.desktop.png", "previews/timeline-milestones.mobile.png"]
related: ["timeline-tracks", "roadmap-phases", "roadmap-road"]
sha256: "cf63c59191824836ec4d86f8bb1ba6cdb5367445f112af3d946dc5ace3f1ba93"
size_bytes: 35288
tags: ["Cualquiera", "any", "cualquiera", "generico", "left", "roadmap", "timeline", "todas"]
title: "timeline-milestones · Línea de tiempo"
title_en: "timeline-milestones · Timeline"
vertical: ["cualquiera"]
---
# timeline-milestones · Línea de tiempo

![desktop](../../previews/timeline-milestones.desktop.png) ![mobile](../../previews/timeline-milestones.mobile.png)

## Qué cuenta

Una línea desde «Hoy» con cinco hitos, cada uno con su periodo, su nombre y un ícono de su sector, alternando a un lado y al otro.

## Cómo respira

Un cursor recorre la línea y la deja encendida; cada hito se enciende al paso. Queda: los cinco hitos alcanzados.

## Cuándo usarla

Intención: **Línea de tiempo** (timeline, roadmap). Verticales: cualquiera. Layout `left`. Origen: dcd 0.6.0 · escena de catálogo. El snippet completo, listo para pegar en un storyboard: [`snippets/timeline-milestones.json`](../../snippets/timeline-milestones.json).

## Args

```json
{
 "layout": "left",
 "scene": "timeline-milestones",
 "args": {
  "now": "‹como: Hoy›",
  "events": [
   [
    "‹como: Semana 1›",
    "‹como: Taller de arranque›"
   ],
   [
    "‹como: Semana 2›",
    "‹como: Datos conectados›"
   ],
   [
    "‹como: Semana 4›",
    "‹como: Prototipo en uso›"
   ],
   [
    "‹como: Mes 2›",
    "‹como: Primer resultado medido›"
   ],
   [
    "‹como: Mes 3›",
    "‹como: Decisión de escalar›"
   ]
  ]
 }
}
```

## What it is

Timeline scene, layout «left», for any decks. It lands at a glance, then breathes in a slow loop; its args (events, now) carry every visible word, so the same scene serves a new client once the texts are rewritten.

## Relacionadas · Related

- [timeline-tracks · Línea de tiempo](timeline-tracks.md)
- [roadmap-phases · Hoja de ruta](roadmap-phases.md)
- [roadmap-road · Hoja de ruta](roadmap-road.md)

Fuente · source: [`scenes/story/intents_s09_16.py`](../../scenes/story/intents_s09_16.py) · sha256 `cf63c5919182`
