# Base de conocimiento: dónde vive cada cosa

Lee solo el archivo (o la sección) que el paso necesita. Esta carpeta tiene tres archivos: este, `verticals.md` y
`kpi-library.md`. Nada de esta carpeta es una cifra del cliente: son nombres, reglas y
semillas. Una cifra entra al deck solo como hecho confirmado en `<work>/facts.json`.

## Para escribir (en este orden)

| Necesito | Archivo |
|---|---|
| Lo que le preocupa a la sala, los KPI que nombra, 4 hipótesis semilla, íconos y palabras que no van, por vertical | la sección `## <vertical>` de `knowledge/verticals.md` (banca, seguros, salud, energia, mineria, retail, pagos, telco, industria, publico, consumo, logistica, formacion, farmacia, fidelizacion: los 15 verticales de `references/vocab.json`; «cualquiera» no tiene sección) |
| Los KPI típicos del vertical con qué mide cada uno, semillas de hipótesis con «podría» y las objeciones típicas con cómo responderlas (una pregunta o un contraste, nunca presión) | las subsecciones «KPI típicos», «Semillas de hipótesis» y «Objeciones típicas» de cada vertical (las revisa `scripts/templates.py check`; los campos e ids, `scripts/vocab.py check`) |
| El KPI de un caso o del discovery, con unidad y dirección | `knowledge/kpi-library.md` |
| La voz, el tono y las palabras de la casa, en una página | `references/tono-estilo.md` |
| Qué puede decir el deck y qué nunca (cifras, marca, casos) | `references/copy-rules.md` |
| Cada lección aprendida y el script o gate que la hace cumplir | `references/lecciones.md` |
| El método de siete pasos y el pase «Mensajes sutiles» | `references/method.md` |
| Cómo se ingiere y se confirma el contexto (kinds de `facts.json`) | `references/ingest-confirm.md` |
| El arco de cada tipo de deck | `references/deck-types.md` |
| Los modos (simple, guiado, freestyle, coach, arquitectura) | `references/modes.md` |

## Para componer

| Necesito | Archivo |
|---|---|
| Una escena lista para pegar, por intención (portada, hipótesis, cierre…) | `python3 scripts/snippets.py show <alias>` · todas, con su README por intención: `snippets.py build --out <work>/snippets` (se generan, no vienen en el skill) |
| Qué aterriza y qué cuenta cada escena en 12 s | `references/scenes.md` · `references/scenes.json` |
| El esquema del storyboard y lo que revisa `story.py check` | `references/storyboard.md` |
| Los íconos (vertical/clave) | `assets/scenes/icons.py` (`ICONS`) |

## Plantillas y patrones

| Necesito | Archivo |
|---|---|
| Las preguntas de entrada (≤5) y el mínimo que se pide | `templates/intake.md` · `inputs/intake.schema.json` |
| Brief de una página | `templates/brief.md` |
| Guion (tres aperturas, una elegida) | `templates/guion.md` |
| Títulos que cuentan la historia | `templates/titulos.md` |
| Tabla de confirmación de hechos | `templates/confirmacion.md` |
| El arco simple (6–10 diapositivas), con la guía de cada campo | `templates/arc.json` |
| Un arco listo por tipo y vertical (12 × 16), para copiar como `<work>/arc.json` y seguir con `arc.py apply` | `python3 scripts/templates.py show …` o `templates.py build --out <work>/templates` (se genera, no viene en el skill) |
| Brief, guion y títulos de un tipo, con su corte simple, sus actos, sus minutos, quién firma y la voz | lo mismo: `templates.py show …` · `build --out <dir>` |
| Revisar esas plantillas contra su generador | `python3 scripts/templates.py check` |
| Un deck real completo, paso por paso | en el skill: `examples/simple-demo/` y `examples/arquitectura-demo/`; el de energía (01-contexto … 07-escenas) vive en `examples/` del repo privado, nunca en el paquete; las demos neutrales, en el banco (`python3 scripts/bank.py list`) |

## Rúbricas (lo que revisa `dcd-reviewer`)

| Rúbrica | Dónde |
|---|---|
| Gates y sensores: qué revisa cada uno y cómo leer una falla | `references/gates.md` |
| Los títulos leídos en orden cuentan la historia (≤10 palabras, cada uno afirma algo) | `templates/titulos.md` «Revisión» · `scripts/compare.py` |
| Hechos: ninguna cifra sin hecho confirmado | `scripts/facts.py check` · `story.py check --facts` |
| Voz y tono | `scripts/audit-voz.py` (en `qa.sh`) · `references/tono-estilo.md` |
| Casos de prueba del kit | `evals/evals.json` · `python3 evals/run.py` |

## Flujos para un modelo pequeño

`workflows/simple.md` (el camino por defecto: una URL, la sala y el dolor) · `workflows/guiado.md` · `workflows/freestyle.md` ·
`workflows/coach.md` · `workflows/arquitectura.md`.
