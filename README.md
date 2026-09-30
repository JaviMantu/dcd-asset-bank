# dcd-asset-bank v0.7.0

**ES.** Banco de assets y base de conocimiento de la skill *dynamic-commercial-decks* (dcd): escenas animadas en SVG
(código Python legible), su catálogo, snippets listos para pegar, arcos por tipo × vertical, fichas de conocimiento
por vertical, ejemplos neutrales, íconos, previsualizaciones y los assets de marca que ya son públicos. Encima de los
assets hay capas para indexar y buscar: una tarjeta por asset (`cards/`), `index.jsonl`, un grafo de conocimiento
(`graphify-out/`), `llms.txt` y `search.py`. dcd fija un tag de este repo y verifica el sha256 de `manifest.json` (y el de
cada archivo que lista) antes de usarlo; fuera de dcd se clona y se consulta como referencia.

**EN.** Asset bank and knowledge base of the *dynamic-commercial-decks* (dcd) skill: animated SVG scenes (readable
Python), their catalog, paste-ready snippets, arcs per type × vertical, per-vertical knowledge, neutral examples,
icons, previews and the brand assets that are already public. On top of the assets: one card per asset (`cards/`),
`index.jsonl`, a knowledge graph (`graphify-out/`), `llms.txt` and `search.py`. dcd pins a tag and verifies the sha256
of `manifest.json` (and of every file it lists); outside dcd, clone it and query it as a reference.

## Assets

| Carpeta · folder | archivos · files |
|---|---|
| `brand/` | 2 |
| `cards/` | 368 |
| `catalog/` | 1 |
| `examples/` | 10 |
| `graphify-out/` | 2 |
| `icons/` | 1 |
| `knowledge/` | 3 |
| `previews/` | 256 |
| `scenes/` | 37 |
| `schema/` | 2 |
| `snippets/` | 129 |
| `templates/` | 228 |

## Tarjetas · cards

| familia · family | tarjetas · cards |
|---|---|
| scenes | 128 |
| arcs | 192 |
| templates | 12 |
| knowledge | 16 |
| examples | 3 |
| icons | 17 |

Grafo · graph: 427 nodos · 4531 enlaces · 60 comunidades
(`graphify-out/GRAPH_REPORT.md`).

## Buscar · search

```bash
python3 search.py "cifra pública con fuente"                 # BM25: palabras de la intención ×4, título ×3, tags ×2, resto ×1
python3 search.py "portada energía" --family scenes --k 5
python3 search.py "crédito" --vertical banca --json
python3 search.py --related hero                              # vecinos en el grafo, con su relación
graphify explain "hero" --graph graphify-out/graph.json
graphify path "hero" "hypotheses-bank" --graph graphify-out/graph.json   # --undirected: any pair
```

- `llms.txt` (convención llmstxt.org) enlaza cada tarjeta; `llms-full.txt` las concatena en un orden estable.
- `index.jsonl`: un registro por línea (`schema/index.schema.json`), listo para cargarlo en el vector store que se quiera.
- Cada tarjeta es un fragmento autocontenido (< ~1,5 k tokens) con frontmatter YAML (`schema/card.schema.json`).

## Usar con dcd · use with dcd

1. **Automático · automatic:** `python3 scripts/bank.py sync` clona este tag por git desde github.com al caché
   `~/.dcd/bank/v0.7.0/` y lo verifica.
2. **Manual:** descarga `dcd-asset-bank-v0.7.0.zip` de la release y corre `python3 scripts/bank.py install <zip>`, o adjunta el
   zip en el chat. / Download the release zip and install it, or attach it in the chat.
3. **Persistente · persistent:** `python3 scripts/bank.py clone <dir>` deja un clon propio; `python3 scripts/bank.py
   update` lo lleva al tag que fija dcd.

La fuente General Sans no viaja (ITF Free Font License, https://www.fontshare.com/licenses/itf-ffl): se descarga de
Fontshare. / The General Sans font is not included; get it from Fontshare.

Sin licencia de código abierto. / No open-source license.

© Amaris Consulting · todos los derechos reservados · all rights reserved

Topics: presentations, storytelling, svg-animation, slide-deck, scene-library, knowledge-base, llms-txt, bm25, knowledge-graph, graphify, consulting, spanish
