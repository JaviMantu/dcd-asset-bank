# Brief · Arquitectura de la plataforma de reclamos en línea (demo)

> Ejemplo del tipo `arquitectura` (0.5.0). Cliente y sistema **ficticios**: «Aseguradora Andina» y su «Plataforma de
> reclamos en línea». Sirve para ver las escenas de arquitectura funcionando, no como caso real.

- **Sala.** El comité de arquitectura y el equipo de TI de la aseguradora: arquitectos, líderes de desarrollo, datos,
  infraestructura y seguridad. Sala técnica: el perfil de voz es `tecnico` y la palabra «arquitectura» se dice.
- **Dolor.** Un reclamo hoy pasa por papel, correos y llamadas; tras una tormenta el volumen se triplica y el registro
  se atasca. (Hipótesis del ejemplo, no un dato.)
- **Decisión que buscamos.** Validar la arquitectura propuesta y aprobar un taller de dos semanas con su comité.
- **Prueba.** Las vistas C4 de contexto a código, las capas, el dato, la infraestructura, tres decisiones con su costo y
  cuatro riesgos con su mitigación; las metas de calidad (99,9 %, 3× en picos) se dicen como metas por validar.
- **Límites.** Sin precios, sin ROI, sin fechas más allá del próximo paso (las fases siguientes son «Fase 2…4»);
  ninguna tecnología del cliente real, porque no hay cliente real.
- **Minutos.** 40 (12 diapositivas, versión `full`). Cortes: `meta.simple` (8) y `meta.focus` (solucion, software,
  datos, infraestructura, c4).
- **Firma.** Manager responsable: Javier Montaño.

## Cómo se construye

```bash
python3 scripts/new.py /tmp/dcd-arq --type arquitectura --size full --client "Aseguradora Andina" \
  --audience "el comité de arquitectura y TI" --manager "Javier Montaño"
cp examples/arquitectura-demo/storyboard.json /tmp/dcd-arq/storyboard.json
python3 scripts/build.py /tmp/dcd-arq && bash scripts/qa.sh /tmp/dcd-arq
```

Esperado: `story check: PASS`, `gate PASS` y `cross gates PASS` (desktop y mobile), `banned: OK`, `voice: VOZ: PASS ·
perfil tecnico`, `ui OK`, `motion OK`, `qa: OK`. Los args de cada escena y la notación C4:
[references/architecture.md](../../references/architecture.md).
