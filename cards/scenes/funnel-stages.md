---
description: "Un embudo de cuatro etapas, cada una con un ícono de su sector y su nombre a la derecha; a la izquierda, las salidas punteadas; abajo, el resultado."
description_en: "Funnel scene, layout «left», for any decks. It lands at a glance, then breathes in a slow loop; its args (focus, focus_label, levels, out, result) carry every visible word, so the same scene serves a new client once the texts are rewritten."
family: "scenes"
id: "funnel-stages"
intent: ["data", "funnel", "gap"]
keywords: ["brecha", "data", "dato", "datos", "dolor", "embudo", "funnel", "gap", "problema"]
layout: "left"
path: "scenes/story/intents_s09_16.py"
portrait: true
previews: ["previews/funnel-stages.desktop.png", "previews/funnel-stages.mobile.png"]
related: ["before-after-split", "cascade", "client-worries", "data-architecture", "data-lifecycle", "facts-columns"]
sha256: "cf63c59191824836ec4d86f8bb1ba6cdb5367445f112af3d946dc5ace3f1ba93"
size_bytes: 35288
tags: ["Cualquiera", "any", "cualquiera", "data", "funnel", "gap", "generico", "left", "todas"]
title: "funnel-stages · Embudo"
title_en: "funnel-stages · Funnel"
vertical: ["cualquiera"]
---
# funnel-stages · Embudo

![desktop](../../previews/funnel-stages.desktop.png) ![mobile](../../previews/funnel-stages.mobile.png)

## Qué cuenta

Un embudo de cuatro etapas, cada una con un ícono de su sector y su nombre a la derecha; a la izquierda, las salidas punteadas; abajo, el resultado.

## Cómo respira

El flujo cae por el embudo; en cada etapa una parte sale por el costado y la etapa se enciende; al final la etapa señalada recibe su «?» y se enciende el resultado. Queda: las etapas encendidas y la pregunta en su lugar. Sin cifras: solo el orden.

## Cuándo usarla

Intención: **Embudo** (funnel, gap, data). Verticales: cualquiera. Layout `left`. Origen: dcd 0.6.0 · escena de catálogo. El snippet completo, listo para pegar en un storyboard: [`snippets/funnel-stages.json`](../../snippets/funnel-stages.json).

## Args

```json
{
 "layout": "left",
 "scene": "funnel-stages",
 "args": {
  "levels": [
   "‹como: Llegan›",
   "‹como: Se interesan›",
   "‹como: Piden propuesta›",
   "‹como: Deciden›"
  ],
  "out": "‹como: Se van sin respuesta›",
  "focus": 2,
  "focus_label": "‹como: ¿Por qué se van aquí?›",
  "result": "‹como: Clientes que se quedan›"
 }
}
```

## What it is

Funnel scene, layout «left», for any decks. It lands at a glance, then breathes in a slow loop; its args (focus, focus_label, levels, out, result) carry every visible word, so the same scene serves a new client once the texts are rewritten.

## Relacionadas · Related

- [before-after-split · Antes y después](before-after-split.md)
- [cascade · La brecha: su idea y lo que pasa cuando no se cumple](cascade.md)
- [client-worries · La brecha: su idea y lo que pasa cuando no se cumple](client-worries.md)
- [data-architecture · Diseño técnico por capas](data-architecture.md)
- [data-lifecycle · Lo que sus equipos comparten: el dato](data-lifecycle.md)
- [facts-columns · Lo que sus equipos comparten: el dato](facts-columns.md)

Fuente · source: [`scenes/story/intents_s09_16.py`](../../scenes/story/intents_s09_16.py) · sha256 `cf63c5919182`
