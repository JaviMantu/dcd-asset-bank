# Graph report · dcd-asset-bank

Built by `scripts/bank-export.py` from the bank's metadata (catalog, arcs, examples, icon sets, knowledge);
every edge is `EXTRACTED`, none inferred. Query it with `graphify explain` / `graphify path` or `search.py --related`.

- nodes: 427 · links: 4531 · communities: 60 · orphans: 0

## Nodes by type

| type | nodes |
|---|---|
| arc | 192 |
| example | 3 |
| icon | 18 |
| intent | 28 |
| knowledge | 16 |
| scene | 128 |
| template | 12 |
| type | 12 |
| vertical | 16 |
| world | 2 |

## Links by relation

| relation | links |
|---|---|
| example_of | 3 |
| for_vertical | 357 |
| has_intent | 201 |
| in_world | 30 |
| pairs_with | 208 |
| part_of_arc | 1568 |
| uses_icon | 340 |
| uses_scene | 1603 |
| variant_of | 221 |

## Hubs (top 15 by degree)

| node | degree |
|---|---|
| discovery | 409 |
| hypotheses-live | 349 |
| repeat-story | 315 |
| criterion | 310 |
| tickets-live | 246 |
| hypotheses-quarter | 228 |
| outside-business | 196 |
| chain-tap | 143 |
| vertical cualquiera | 109 |
| evidence | 105 |
| shared-asset | 105 |
| knowledge-spaces | 73 |
| icons generico | 69 |
| delivery-cycle | 63 |
| icons uso | 53 |

## Communities

### 0 · examples (3)

example arquitectura-demo, example simple-demo, example webinar-piloto-eterno

### 1 · icons (6)

icon library, icons arquitectura, icons entrega, icons generico, icons ia, icons uso

### 2 · intent agenda (2)

intent agenda, luz-agenda

### 3 · intent architecture (13)

adr-decisions, c4-code, c4-component, c4-container, c4-context, chain-tap, component-diagram, data-architecture, infra-topology, intent architecture, luz-ladder, risks-tradeoffs, solution-layers

### 4 · intent before-after (3)

before-after-lanes, before-after-split, intent before-after

### 5 · intent criterion (5)

criterion, criterion-b, intent criterion, luz-escala, simple-criterion

### 6 · intent cta (7)

arq-roadmap, discovery, discovery-b, intent cta, simple-next, ways, ways-b

### 7 · intent data (4)

data-lifecycle, facts-columns, intent data, shared-asset

### 8 · intent demo (4)

build-deliver, intent demo, live-steps, skill-handoff

### 9 · intent figure (9)

cost-drop, figure-context, figure-door, figure-growth, figure-rank, intent figure, luz-figures, luz-wave, noise-vs-evidence

### 10 · intent funnel (3)

funnel-gates, funnel-stages, intent funnel

### 11 · intent gap (11)

cascade, client-worries, generic-template, intent gap, luz-divider, luz-loop, pinned-request, quality-drivers, repeat-story, simple-gap, week-calendar

### 12 · intent governance (5)

federated-live, intent governance, knowledge-spaces, luz-console, review-lens

### 13 · intent hands-on (4)

diagnostic, hands-on-timer, intent hands-on, pair-read

### 14 · intent hero (11)

arq-hero, hero, hero-bank, hero-care, hero-network, hypotheses-quarter, intent hero, luz-hero, paper-hero, prospect-cover, simple-hero

### 15 · intent hypotheses (7)

funnel-weeks, hypotheses-bank, hypotheses-care, hypotheses-live, hypotheses-live-b, intent hypotheses, simple-hypotheses

### 16 · intent journey (3)

intent journey, journey-loop, journey-path

### 17 · intent kpi (3)

intent kpi, kpi-card, luz-bridge

### 18 · intent map (3)

intent map, map-hub, map-lines

### 19 · intent matrix (3)

intent matrix, matrix-quadrants, matrix-table

### 20 · intent org (3)

intent org, org-squad, org-tree

### 21 · intent outside (5)

intent outside, outside, outside-business, outside-teams, simple-outside

### 22 · intent panel (4)

intent panel, luz-panel, panel-questions, panel-questions-list

### 23 · intent process (12)

automation-stairs, delivery-cycle, explain-cards, intent process, mechanism, mechanism-teams, mirroring, route-named, simple-path, strategy-map, titles-thread, two-seconds

### 24 · intent proof (10)

capacity-join, evidence, intent proof, internal-case, mondays-sent, orbit, proof-paths, report-before-after, simple-proof, success-case

### 25 · intent reflection (7)

intent reflection, luz-question, reflections-cards, reflections-live, time-back, time-freed, unfold-describe

### 26 · intent roadmap (3)

intent roadmap, roadmap-phases, roadmap-road

### 27 · intent timeline (3)

intent timeline, timeline-milestones, timeline-tracks

### 28 · intent vision (8)

care-center, controlroom-live, intent vision, lema-conversation, lema-signer, luz-end, ops-center, tickets-live

### 29 · intent who (1)

intent who

### 30 · knowledge (1)

knowledge kpi-library

### 31 · type arquitectura (18)

arc arquitectura banca, arc arquitectura consumo, arc arquitectura cualquiera, arc arquitectura energia, arc arquitectura farmacia, arc arquitectura fidelizacion, arc arquitectura formacion, arc arquitectura industria, arc arquitectura logistica, arc arquitectura mineria, arc arquitectura pagos, arc arquitectura publico, arc arquitectura retail, arc arquitectura salud, arc arquitectura seguros, arc arquitectura telco, template arquitectura, type arquitectura

### 32 · type cierre-training (18)

arc cierre-training banca, arc cierre-training consumo, arc cierre-training cualquiera, arc cierre-training energia, arc cierre-training farmacia, arc cierre-training fidelizacion, arc cierre-training formacion, arc cierre-training industria, arc cierre-training logistica, arc cierre-training mineria, arc cierre-training pagos, arc cierre-training publico, arc cierre-training retail, arc cierre-training salud, arc cierre-training seguros, arc cierre-training telco, template cierre-training, type cierre-training

### 33 · type comercial (18)

arc comercial banca, arc comercial consumo, arc comercial cualquiera, arc comercial energia, arc comercial farmacia, arc comercial fidelizacion, arc comercial formacion, arc comercial industria, arc comercial logistica, arc comercial mineria, arc comercial pagos, arc comercial publico, arc comercial retail, arc comercial salud, arc comercial seguros, arc comercial telco, template comercial, type comercial

### 34 · type defensa-funcional (18)

arc defensa-funcional banca, arc defensa-funcional consumo, arc defensa-funcional cualquiera, arc defensa-funcional energia, arc defensa-funcional farmacia, arc defensa-funcional fidelizacion, arc defensa-funcional formacion, arc defensa-funcional industria, arc defensa-funcional logistica, arc defensa-funcional mineria, arc defensa-funcional pagos, arc defensa-funcional publico, arc defensa-funcional retail, arc defensa-funcional salud, arc defensa-funcional seguros, arc defensa-funcional telco, template defensa-funcional, type defensa-funcional

### 35 · type defensa-hibrida (18)

arc defensa-hibrida banca, arc defensa-hibrida consumo, arc defensa-hibrida cualquiera, arc defensa-hibrida energia, arc defensa-hibrida farmacia, arc defensa-hibrida fidelizacion, arc defensa-hibrida formacion, arc defensa-hibrida industria, arc defensa-hibrida logistica, arc defensa-hibrida mineria, arc defensa-hibrida pagos, arc defensa-hibrida publico, arc defensa-hibrida retail, arc defensa-hibrida salud, arc defensa-hibrida seguros, arc defensa-hibrida telco, template defensa-hibrida, type defensa-hibrida

### 36 · type defensa-negocio (18)

arc defensa-negocio banca, arc defensa-negocio consumo, arc defensa-negocio cualquiera, arc defensa-negocio energia, arc defensa-negocio farmacia, arc defensa-negocio fidelizacion, arc defensa-negocio formacion, arc defensa-negocio industria, arc defensa-negocio logistica, arc defensa-negocio mineria, arc defensa-negocio pagos, arc defensa-negocio publico, arc defensa-negocio retail, arc defensa-negocio salud, arc defensa-negocio seguros, arc defensa-negocio telco, template defensa-negocio, type defensa-negocio

### 37 · type defensa-tecnica (18)

arc defensa-tecnica banca, arc defensa-tecnica consumo, arc defensa-tecnica cualquiera, arc defensa-tecnica energia, arc defensa-tecnica farmacia, arc defensa-tecnica fidelizacion, arc defensa-tecnica formacion, arc defensa-tecnica industria, arc defensa-tecnica logistica, arc defensa-tecnica mineria, arc defensa-tecnica pagos, arc defensa-tecnica publico, arc defensa-tecnica retail, arc defensa-tecnica salud, arc defensa-tecnica seguros, arc defensa-tecnica telco, template defensa-tecnica, type defensa-tecnica

### 38 · type formacion (18)

arc formacion banca, arc formacion consumo, arc formacion cualquiera, arc formacion energia, arc formacion farmacia, arc formacion fidelizacion, arc formacion formacion, arc formacion industria, arc formacion logistica, arc formacion mineria, arc formacion pagos, arc formacion publico, arc formacion retail, arc formacion salud, arc formacion seguros, arc formacion telco, template formacion, type formacion

### 39 · type prospeccion (18)

arc prospeccion banca, arc prospeccion consumo, arc prospeccion cualquiera, arc prospeccion energia, arc prospeccion farmacia, arc prospeccion fidelizacion, arc prospeccion formacion, arc prospeccion industria, arc prospeccion logistica, arc prospeccion mineria, arc prospeccion pagos, arc prospeccion publico, arc prospeccion retail, arc prospeccion salud, arc prospeccion seguros, arc prospeccion telco, template prospeccion, type prospeccion

### 40 · type simple (18)

arc simple banca, arc simple consumo, arc simple cualquiera, arc simple energia, arc simple farmacia, arc simple fidelizacion, arc simple formacion, arc simple industria, arc simple logistica, arc simple mineria, arc simple pagos, arc simple publico, arc simple retail, arc simple salud, arc simple seguros, arc simple telco, template simple, type simple

### 41 · type tecnico (18)

arc tecnico banca, arc tecnico consumo, arc tecnico cualquiera, arc tecnico energia, arc tecnico farmacia, arc tecnico fidelizacion, arc tecnico formacion, arc tecnico industria, arc tecnico logistica, arc tecnico mineria, arc tecnico pagos, arc tecnico publico, arc tecnico retail, arc tecnico salud, arc tecnico seguros, arc tecnico telco, template tecnico, type tecnico

### 42 · type webinar-panel (18)

arc webinar-panel banca, arc webinar-panel consumo, arc webinar-panel cualquiera, arc webinar-panel energia, arc webinar-panel farmacia, arc webinar-panel fidelizacion, arc webinar-panel formacion, arc webinar-panel industria, arc webinar-panel logistica, arc webinar-panel mineria, arc webinar-panel pagos, arc webinar-panel publico, arc webinar-panel retail, arc webinar-panel salud, arc webinar-panel seguros, arc webinar-panel telco, template webinar-panel, type webinar-panel

### 43 · vertical banca (3)

icons banca, knowledge banca, vertical banca

### 44 · vertical consumo (3)

icons consumo, knowledge consumo, vertical consumo

### 45 · vertical cualquiera (1)

vertical cualquiera

### 46 · vertical energia (3)

icons energia, knowledge energia, vertical energia

### 47 · vertical farmacia (2)

knowledge farmacia, vertical farmacia

### 48 · vertical fidelizacion (2)

knowledge fidelizacion, vertical fidelizacion

### 49 · vertical formacion (2)

knowledge formacion, vertical formacion

### 50 · vertical industria (3)

icons industria, knowledge industria, vertical industria

### 51 · vertical logistica (3)

icons logistica, knowledge logistica, vertical logistica

### 52 · vertical mineria (3)

icons mineria, knowledge mineria, vertical mineria

### 53 · vertical pagos (3)

icons pagos, knowledge pagos, vertical pagos

### 54 · vertical publico (3)

icons publico, knowledge publico, vertical publico

### 55 · vertical retail (3)

icons retail, knowledge retail, vertical retail

### 56 · vertical salud (3)

icons salud, knowledge salud, vertical salud

### 57 · vertical seguros (3)

icons seguros, knowledge seguros, vertical seguros

### 58 · vertical telco (3)

icons telco, knowledge telco, vertical telco

### 59 · worlds (2)

world luz, world papel

## Orphans

none

Icon sets no scene, arc or ficha uses yet (linked only to the library): icons/entrega
