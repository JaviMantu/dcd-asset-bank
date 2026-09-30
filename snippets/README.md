# Snippets: una escena lista para pegar, por intención

> GENERADO por `python3 scripts/snippets.py build` desde `references/scenes.json`. No se edita a mano.

Cada `<alias>.json` es una diapositiva del storyboard con la forma exacta de los args de su escena. Cada texto
es un «‹como: …›» con el ejemplo de donde salió: reescríbelo para el cliente (el check falla mientras quede uno).

- **Cambiar la escena de una diapositiva del shape:** copia solo `layout`, `scene` y `args`.
- **Agregar una diapositiva:** pega el snippet entero, cambia `id` y pon en `min` la clave de `meta.versions`.
- **Rellenar sin editar JSON a mano:** `python3 scripts/snippets.py holes <work>` lista lo que falta y
  `python3 scripts/snippets.py fill <work> <patch.json>` lo escribe.

## Portada: su promesa

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`hero`](hero.json) | left | Se enciende una sola operación: arriba, las decisiones de negocio; en el horizonte, la línea de gas con turbina, compresor, bomba y válvula; abajo, el negocio de sus clientes con las luces encendidas. | dcd · escena de catálogo (energía) |
| [`hero-network`](hero-network.json) | left | Una calle al anochecer, vista detrás de cuatro personas: en el horizonte, comercios de todo tamaño y, al fondo, cientos de pequeñas vitrinas encendidas; sobre los techos, un flujo de datos y conocimiento; arriba, una constelación apagada. | dcd · escena de catálogo (pagos) |
| [`paper-hero`](paper-hero.json) | left | El logo del cliente, el calendario de la semana y la hoja del informe sobre el viernes aparecen en menos de dos segundos. | dcd · escena de catálogo (fidelización) |
| [`prospect-cover`](prospect-cover.json) | left | Sobre la mesa, una plantilla gris: «Quiénes somos», «Líderes en tecnología» y un hueco para el logo; al otro lado, una gerente sin rostro. | Clase VR (formación) · diapositiva «Tu prospecto sabe en un minuto si es para él» |
| [`hero-care`](hero-care.json) | left | Una región al anochecer, vista detrás de cuatro personas con su teléfono: en el horizonte, sus casas y las de toda la región; arriba, un solo pulso del cuidado. | dcd · escena de catálogo (salud) |
| [`luz-hero`](luz-hero.json) | left | La chispa «IA» encendida a la derecha del escenario, sobre un cielo de estrellas lejanas; dos órbitas punteadas, un plano orbital inclinado que pasa por detrás y por delante, y una estela magenta que la rodea en tres vueltas, cada una más ceñida; abajo, «Foro y panel · 55 minutos». | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «IA: ¿el fin del piloto eterno?» |
| [`hero-bank`](hero-bank.json) | left | Una ciudad al anochecer detrás de una persona, vista de espaldas, con la app del banco en la mano; sobre los techos esperan cuatro sueños apagados: una casa, un negocio, un auto y un birrete. | dcd · escena de catálogo (banca) |
| [`hypotheses-quarter`](hypotheses-quarter.json) | left | Diez tarjetas de hipótesis, numeradas y cada una con su «?», sobre un embudo que baja a «Su laboratorio»; debajo, la línea del trimestre con octubre, noviembre y diciembre y diez casillas vacías. El contador es texto fijo: «10 hipótesis». | dcd · escena de catálogo (banca) |
| [`arq-hero`](arq-hero.json) | left | La plataforma en el centro; a la izquierda, quienes la usan; a la derecha, los sistemas con los que conversa. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Reclamos resueltos en línea, de principio a fin» |
| [`simple-hero`](simple-hero.json) | left | Arriba, para quién es; debajo, sus tres preocupaciones (el presupuesto, la meta del trimestre y el KPI que prometió), cada una con su medidor; abajo, su operación en cuatro estaciones con los íconos de su sector, camino a su promesa. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Que cada pedido llegue a tiempo, sin subir el costo» |

## Desde afuera: lo que vimos en fuentes públicas

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`outside`](outside.json) | left | Arriba, afuera, tres fuentes públicas y nuestro cuaderno; abajo, tras una línea punteada, su operación dibujada como una silueta que no vemos. | dcd · escena de catálogo (energía) |
| [`outside-teams`](outside-teams.json) | left | Arriba, afuera, tres fuentes públicas y nuestro cuaderno; abajo, tras una línea punteada, sus cuatro equipos dibujados como una silueta que no vemos. | dcd · escena de catálogo (pagos) |
| [`outside-business`](outside-business.json) | left | Arriba, afuera, tres fuentes públicas del prospecto (su sitio y su estrategia, sus resultados publicados, la prensa del sector) y tu dossier; abajo, tras una línea punteada, su operación como una silueta que no vemos. | Clase VR2 · diapositiva «Primero investigas al prospecto en lo que él publica» |
| [`simple-outside`](simple-outside.json) | left | Arriba, afuera, tres fuentes públicas y nuestro dossier; una línea punteada; abajo, sus cuatro áreas dibujadas en tenue: lo de adentro no lo vemos. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Esto es lo que vemos desde afuera, en fuentes públicas» |

## La brecha: su idea y lo que pasa cuando no se cumple

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`cascade`](cascade.json) | left | La línea de gas y sus cuatro equipos se arman; debajo esperan, apagados, los tres pasos de una cascada. | dcd · escena de catálogo (energía) |
| [`pinned-request`](pinned-request.json) | left | El corcho con sus primeros post-its y un reloj de papel que marca 3:30. | dcd · escena de catálogo (fidelización) |
| [`week-calendar`](week-calendar.json) | left | Tu semana de martes a jueves: el martes hasta las 4 pm ya pasó, un reloj marca las 4:00 y el jueves a las 10:00 brilla la reunión con el prospecto. | Clase VR (formación) · diapositiva «Martes, 4 pm: el jueves conoces a un prospecto» |
| [`generic-template`](generic-template.json) | left | Arriba, una línea en el chat: «Hazme una presentación de Amaris»; debajo, diez diapositivas grises con sus títulos. | Clase VR (formación) · diapositiva «Pides una presentación y recibes la de todos» |
| [`client-worries`](client-worries.json) | left | Una manager sin rostro en su escritorio, detrás de su portátil; arriba aparece su primera preocupación, «Un proveedor dentro de mi presupuesto»; al lado, pequeño y apagado, el logo de Amaris. | Clase VR (formación) · diapositiva «Al cliente le importa su meta del trimestre, no Amaris» |
| [`repeat-story`](repeat-story.json) | left | El cliente a la izquierda y, a su lado, tres canales vacíos, cada uno con su propio sistema; abajo, otro sistema aparte y la barra de la espera. | dcd · escena de catálogo (salud) |
| [`luz-divider`](luz-divider.json) | left | Una órbita grande de luz magenta se traza sola; dentro, «Capacidad» en grande y tres órbitas interiores con muchos satélites pequeños, apagados, que giran cada uno a su ritmo; afuera, tenue y hueco, un punto que dice «Operación». | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «El piloto eterno» |
| [`luz-loop`](luz-loop.json) | left | El anillo Idea → POC → Demo con sus tres nodos y la chispa girando con su estela magenta; fuera del anillo, la puerta «Operar» apagada y un trazo punteado que no llega; debajo, el hilo magenta baja de «Demo» a un estante con tres lugares vacíos. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «¿Por qué el ciclo no llega a operar?» |
| [`quality-drivers`](quality-drivers.json) | left | Cuatro tarjetas: disponibilidad, seguridad, escalabilidad y trazabilidad, cada una con su meta. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Cuatro atributos de calidad guían cada decisión técnica» |
| [`simple-gap`](simple-gap.json) | left | Tres columnas con sus tarjetas: hechos con su fuente, hipótesis con su «?» y, cerrada, lo que no suponemos; abajo, la conversación de hoy, con sus casillas vacías. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Separamos lo que sabemos de lo que suponemos» |

## Una cifra pública (estática, con fuente)

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`figure-context`](figure-context.json) | left | La cifra aparece quieta en su marco y, debajo, la línea de gas va de la producción a la demanda. | dcd · escena de catálogo (energía) |
| [`figure-growth`](figure-growth.json) | left | La cifra queda quieta en su marco, con su fuente; debajo, dos carriles de pagos digitales, 2018 y 2026, y los cuatro equipos: producto, comercial, riesgo y atención. | dcd · escena de catálogo (pagos) |
| [`cost-drop`](cost-drop.json) | left | Dos barras de papel, 2022 alta y 2024 apenas una línea, y la cifra «280× menos» fija en su marco de papel. | dcd · escena de catálogo (fidelización) |
| [`noise-vs-evidence`](noise-vs-evidence.json) | left | Un feed de papel con tres publicaciones exageradas a la izquierda y dos notas a la derecha, cada una con sus cifras fijas. | dcd · escena de catálogo (fidelización) |
| [`figure-door`](figure-door.json) | left | La cifra quieta en su marco; debajo, la puerta digital abierta con sus servicios y, detrás, el dato del cliente y dos caminos. | dcd · escena de catálogo (salud) |
| [`luz-figures`](luz-figures.json) | left | Tres cifras grandes y quietas en tarjetas de vidrio oscuro, cada una con su alcance y su fuente; a la derecha, un muro de luz punteado con una sola puerta alta y estrecha: «Operación». | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «¿Por qué escalar sigue siendo la excepción?» |
| [`luz-wave`](luz-wave.json) | left | El mismo anillo Idea → POC → Demo de la diapositiva 5, ahora con tres agentes visibles (un pequeño robot de luz en cada uno) girando en él y la leyenda «Agentes» al centro; afuera, la puerta «Operar» apagada; abajo, la cifra quieta y grande: más del 40 %, con su alcance y su fuente. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «La próxima ola: ¿escala o repite el ciclo?» |
| [`figure-rank`](figure-rank.json) | left | La cifra quieta en su marco, junto a un ranking de cinco barras donde la quinta, la del banco, está encendida, con sus dos participaciones; debajo, el banco y dos caminos. | dcd · escena de catálogo (banca) |

## El mecanismo: cómo cambiaría su operación

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`mechanism`](mechanism.json) | left | De arriba abajo, la cadena en cuatro pasos: la vibración del compresor, los datos conectados, tres decisiones de negocio y la línea con sus cuatro estaciones. | dcd · escena de catálogo (energía) |
| [`delivery-cycle`](delivery-cycle.json) | left | El ciclo se arma: los agentes arriba, los cuatro pasos, las personas en cada punto de decisión y la regla del pedido a producción. | dcd · escena de catálogo (energía) |
| [`mechanism-teams`](mechanism-teams.json) | left | De arriba abajo: la norma nueva, lo que Pagalia ya sabe, los cuatro equipos (producto, comercial, riesgo y atención a comercios) y la línea del tiempo hasta que la norma entra en vigor. | dcd · escena de catálogo (pagos) |
| [`strategy-map`](strategy-map.json) | left | El post-it rojo clavado a la izquierda, una persona tranquila a su lado y un mapa de papel doblado. | dcd · escena de catálogo (fidelización) |
| [`explain-cards`](explain-cards.json) | left | A la izquierda, pequeño, el pedido «Hazme el informe» y su plantilla hueca con tres huecos «insertar»; a la derecha, una hoja de chat de papel con el mismo pedido y tres huecos vacíos; abajo, el mapa pequeño de tres paradas. | dcd · escena de catálogo (fidelización) |
| [`route-named`](route-named.json) | left | Tres paneles de papel plegados en acordeón, con los dibujos de las tres paradas del mapa, y la cinta magenta que los atraviesa. | dcd · escena de catálogo (fidelización) |
| [`automation-stairs`](automation-stairs.json) | left | Una escalera de cuatro peldaños de papel y, en la esquina, el mapa de la estrategia con dos paradas recorridas. | dcd · escena de catálogo (fidelización) |
| [`mirroring`](mirroring.json) | left | A la izquierda, su sitio web con su frase «Operación confiable»; a la derecha, tu diapositiva para el jueves, aún vacía. | Clase VR (formación) · diapositiva «Usa su vocabulario, pero no le leas sus frases» |
| [`titles-thread`](titles-thread.json) | left | Una columna de cinco títulos cortos, numerados y unidos por un hilo punteado, cada uno con su conteo de palabras bajo «≤10 palabras»; a la derecha, una persona sin rostro que los lee en voz alta. | Clase VR (formación) · diapositiva «Lee tus títulos seguidos: deben contar la historia» |
| [`two-seconds`](two-seconds.json) | left | Una diapositiva en la pantalla del proyector: un cronómetro corre y, antes de 2 s, están el título, la escena y la cifra «12.000» con su candado; la presentadora, sin rostro, la señala. | Clase VR (formación) · diapositiva «Cada diapositiva se entiende en dos segundos, sin esperar» |
| [`simple-path`](simple-path.json) | left | Una ruta de tres pasos numerados (discovery, prototipo y decisión), cada uno con lo que pasa y cuánto dura; abajo, los dos equipos juntos y la persona que revisa. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Tres pasos cortos, y ustedes deciden en cada uno» |

## Lo que sus equipos comparten: el dato

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`shared-asset`](shared-asset.json) | left | Las cuatro líneas, una en cada esquina, se unen por tuberías a un mismo centro: el dato del activo. | dcd · escena de catálogo (energía) |
| [`facts-columns`](facts-columns.json) | left | Tu dossier arriba, tres columnas debajo (Hecho con fuente, Hipótesis por validar, No se dice) con sus huecos, y tu diapositiva abajo; la primera frase ya cae en su columna. | Clase VR (formación) · diapositiva «Separas lo que sabes de lo que supones» |
| [`data-lifecycle`](data-lifecycle.json) | left | Un ciclo de vida del dato en cuatro etapas (Ingesta, Calidad, Documentación, Catálogo) bajo la línea por la que viaja el dato; abajo, de espaldas, una persona del equipo de datos con su tablet, y la frase «El equipo aprueba lo que los agentes preparan». | dcd · escena de catálogo (banca) |

## Gobierno, permisos y control

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`knowledge-spaces`](knowledge-spaces.json) | left | Tres espacios del conocimiento de Pagalia, uno abierto y dos restringidos con candado, cada uno con su agente y sus fuentes; arriba pregunta atención, abajo pregunta riesgo. | dcd · escena de catálogo (pagos) |
| [`federated-live`](federated-live.json) | left | Arriba, la consola de TI con el registro de actividad, los permisos por espacio y el uso por equipo; abajo, tres espacios de equipo (atención, riesgo y producto), cada uno con su persona, sus fuentes y sus agentes. | dcd · escena de catálogo (pagos) |
| [`review-lens`](review-lens.json) | left | El borrador de papel con sus líneas y una cifra resaltada; al lado, el procedimiento con sus tres pasos y, debajo, la cifra de 42,7 % fija en su marco; en la esquina, el mapa con la primera parada encendida. | dcd · escena de catálogo (fidelización) |
| [`luz-console`](luz-console.json) | left | Una consola de tres paneles (antes de actuar, mientras actúa, cuando falla) con sus controles apagados; la estela del trabajo delegado entra por la izquierda y la cruza; debajo, la línea del presupuesto y su intercambio: fichas, una flecha, un reloj y tres barras. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «La autonomía cuesta» |

## Diseño técnico por capas

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`chain-tap`](chain-tap.json) | top | Cuatro capas en cadena, cada una con su pregunta; abajo, un campo luminoso que escribe «Hoy estamos en…» y espera. | dcd · escena de catálogo (energía) |
| [`luz-ladder`](luz-ladder.json) | left | Una escalera de luz de seis peldaños, Prompt abajo y Multiagente arriba; cada peldaño con su riel de cuatro celdas (objetivo, pasos, ejecución, revisión) todavía vacío, su nombre y su frase; debajo, la leyenda (usted, pactado, la IA) y «El objetivo siempre lo pone usted.». | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «No todo problema necesita un agente» |
| [`c4-context`](c4-context.json) | left | Arriba, el asegurado y el ajustador; al centro, la plataforma; abajo, tres sistemas externos; la leyenda C4 al pie. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Contexto: quién usa la plataforma y con qué conversa» |
| [`c4-container`](c4-container.json) | left | El recuadro de la plataforma con seis contenedores: portal, app, API, base de datos, bus de eventos y motor; fuera, personas y sistemas externos. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Seis contenedores que se despliegan y escalan por separado» |
| [`c4-component`](c4-component.json) | left | El recuadro de la API con cinco componentes en tres niveles; arriba, el portal y la app; abajo, el core, la base de datos y el bus. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Dentro de la API: cinco componentes con una sola responsabilidad» |
| [`c4-code`](c4-code.json) | left | Cinco clases: el controlador arriba, el servicio al centro y, abajo, dos interfaces y la entidad del reclamo. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «El código del núcleo: clases y dependencias del reclamo» |
| [`solution-layers`](solution-layers.json) | left | Cinco bandas apiladas, de los canales a la plataforma, y dos pilares verticales: seguridad y observabilidad. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Cinco capas, de los canales a la plataforma» |
| [`data-architecture`](data-architecture.json) | left | Cinco filas del dato, de las fuentes al consumo, y a la derecha el pilar de gobierno con catálogo, linaje, calidad y acceso. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «El dato del reclamo, del evento al tablero, con gobierno» |
| [`infra-topology`](infra-topology.json) | left | La región en la nube con tres zonas de seguridad y sus nodos; abajo, desarrollo, pruebas y producción. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Tres zonas de seguridad y tres ambientes idénticos» |
| [`adr-decisions`](adr-decisions.json) | left | Tres tarjetas de decisión, cada una con su contexto, su decisión, su consecuencia y su estado. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Tres decisiones que tomamos y lo que cuestan» |
| [`risks-tradeoffs`](risks-tradeoffs.json) | left | Una matriz de probabilidad por impacto con cuatro riesgos numerados y, debajo, la lista con su mitigación. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Cada riesgo tiene su mitigación y su costo» |
| [`component-diagram`](component-diagram.json) | left | Cajas con sus puertos, ordenadas por sus dependencias, dentro de un marco punteado; cada arista con su etiqueta. | Arquitectura demo (Aseguradora Andina, ficticia) · ejemplo de references/architecture.md |

## Hipótesis por validar

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`hypotheses-live`](hypotheses-live.json) | left | Tres hipótesis con su retorno posible se apoyan sobre una cuarta, tecnología, que las habilita; cada una con su «?». | dcd · escena de catálogo (energía) |
| [`hypotheses-live-b`](hypotheses-live-b.json) | left | Tres hipótesis con su retorno posible se apoyan en una cuarta, tecnología, que las habilita; cada tarjeta lleva su «?». | dcd · escena de catálogo (pagos) |
| [`hypotheses-care`](hypotheses-care.json) | left | Tres hipótesis con su retorno posible (atención al cliente, reembolsos y cuidado proactivo) se apoyan en una cuarta, tecnología, que las habilita; cada tarjeta lleva su «?». | dcd · escena de catálogo (salud) |
| [`hypotheses-bank`](hypotheses-bank.json) | left | Tres hipótesis con su retorno posible (banca personas, comercio exterior y ofertas a su medida) se apoyan en una cuarta, tecnología, que las habilita; cada tarjeta lleva su «?». | dcd · escena de catálogo (banca) |
| [`funnel-weeks`](funnel-weeks.json) | left | Diez candidatas caen en la boca de un embudo; arriba, un riel con las semanas; a la derecha, el estante «Validadas»; abajo, la bandeja «Por ahora, no». | dcd · escena de catálogo (banca) |
| [`simple-hypotheses`](simple-hypotheses.json) | left | Tres tarjetas con su ícono, su idea y su retorno posible, cada una con su «?», se apoyan en una cuarta, el habilitador, unida a las tres. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Cuatro lugares donde la IA podría ayudar, por validar» |

## La prueba y la evidencia

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`evidence`](evidence.json) | left | La cifra queda quieta con su etiqueta y su fuente; debajo, dos caminos de la prueba de concepto al valor. | dcd · escena de catálogo (energía) |
| [`orbit`](orbit.json) | left | La cifra 12.000 aparece quieta en el centro de la órbita y, sobre ella, seis colegas sin rostro, cada uno con su disciplina: datos, IA, software, cloud, ciberseguridad y analytics. | dcd · escena de catálogo (energía) |
| [`internal-case`](internal-case.json) | left | Tres columnas se arman (las personas de todos los equipos, cada una con su disciplina; los agentes que crean y comparten; y nuestro conocimiento, conectado y gobernado) y, al pie, el sello de socios estratégicos de Dust. | dcd · escena de catálogo (pagos) |
| [`mondays-sent`](mondays-sent.json) | left | El calendario de papel con cuatro lunes, el tablero de estado vacío y el sobre sellado listo para salir. | dcd · escena de catálogo (fidelización) |
| [`success-case`](success-case.json) | left | Un rollo de papel que se desenrolla con nueve casos de uso con nombre: resumir correos, redactar actas, clasificar solicitudes y seis más. | dcd · escena de catálogo (fidelización) |
| [`proof-paths`](proof-paths.json) | left | El cliente, detrás de su mesa, pregunta «¿Y cómo sé que funciona?»; a la izquierda, dos caminos punteados llegan a su mesa: una referencia de cliente que puedas nombrar y un prototipo a su medida. | Clase VR (formación) · diapositiva «Demuestras con una referencia de cliente o un prototipo» |
| [`report-before-after`](report-before-after.json) | left | Dos paneles lado a lado con sus cifras fijas: «20 min», atenuado, y «160 s», encendido; en cada uno, los mismos pasos del reporte, la hoja que llenan y, abajo, de espaldas, una persona con su tablet. Arriba, «Caso Amaris · sin nombre de cliente». | dcd · escena de catálogo (banca) |
| [`capacity-join`](capacity-join.json) | left | A la izquierda, cinco solicitudes con su reloj esperan en la puerta de «Su laboratorio», donde trabajan dos personas; a la derecha, tres ingenieros de IA aumentados, cada uno con su chispa; debajo de todo, su método y su plataforma. | dcd · escena de catálogo (banca) |
| [`simple-proof`](simple-proof.json) | left | Arriba, su pregunta: «¿Y cómo sabemos que funciona?»; dos caminos, una referencia o un prototipo en una semana; abajo, el caso de éxito con su KPI: indicador, de cuánto a cuánto, dueño y fecha. | Simple · Andina Logística (demo 0.5.0) · diapositiva «La prueba: un caso que movió las entregas a tiempo» |

## KPI y casos de éxito

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`kpi-card`](kpi-card.json) | left | La tarjeta «Caso de uso · Responder dudas por chat» con cuatro campos vacíos; a su lado, quieta en su marco, la cifra «1 de cada 4» con su fuente. | Clase VR (formación) · diapositiva «Un caso de éxito dice qué KPI movió y cuánto» |
| [`luz-bridge`](luz-bridge.json) | top | La tabla Piloto / Operación con sus cinco filas (datos, usuarios, control, dueño, éxito): el piloto encendido, la operación apagada; por su borde derecho baja la estela magenta hasta un medidor «KPI de negocio» con la aguja abajo. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «Piloto y operación no se parecen» |

## El criterio: retorno o habilitador

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`criterion`](criterion.json) | left | Arriba, retorno claro y habilitador clave unidos por una «o»; debajo, un lugar vacío que pregunta «¿Retorno o habilitador?» y dos destinos: «Construimos» y «Por ahora, no». | dcd · escena de catálogo (energía) |
| [`criterion-b`](criterion-b.json) | left | Arriba, retorno claro y habilitador clave unidos por una «o»; debajo, un lugar vacío que pregunta «¿Retorno o habilitador?» y dos destinos: «Construimos» y «Por ahora, no». | dcd · escena de catálogo (pagos) |
| [`luz-escala`](luz-escala.json) | top | Seis letras grandes de luz en fila, E-S-C-A-L-A, apagadas (solo su contorno) sobre una línea magenta tenue, cada una con su palabra debajo. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «¿Qué hace que una iniciativa esté lista para escalar?» |
| [`simple-criterion`](simple-criterion.json) | left | Tres ideas arriba; en el medio, dos puertas, «Retorno claro» o «Habilitador clave»; abajo, dos bandejas: «Construimos» y «Por ahora, no». | Simple · Andina Logística (demo 0.5.0) · diapositiva «Solo construimos si hay retorno claro o habilitador clave» |

## Próximo paso: formas de empezar y discovery

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`ways`](ways.json) | top | Cuatro columnas se abren (desarrollo, capacidades, proyecto y servicio) y, debajo, un árbol une sus bases con una sola raíz que pregunta «¿Qué necesitan hoy?». | dcd · escena de catálogo (energía) |
| [`discovery`](discovery.json) | top | Sus opciones a la izquierda y, sobre una línea de tiempo, el taller de discovery, el prototipo y su decisión. | dcd · escena de catálogo (energía) |
| [`ways-b`](ways-b.json) | top | Cuatro columnas se abren (desarrollo, capacidades, proyecto y servicio) y, debajo, un árbol une sus bases con una sola raíz que pregunta «¿Qué necesitan hoy?». | dcd · escena de catálogo (pagos) |
| [`discovery-b`](discovery-b.json) | top | Sus opciones a la izquierda y, sobre una línea de tiempo, el taller de discovery, el prototipo y su decisión. | dcd · escena de catálogo (pagos) |
| [`arq-roadmap`](arq-roadmap.json) | left | Cuatro fases en una línea de tiempo; la primera, validar la arquitectura, marcada como próximo paso. | Arquitectura demo (Aseguradora Andina, ficticia) · diapositiva «Cada reclamo, resuelto en línea y a tiempo» |
| [`simple-next`](simple-next.json) | left | Arriba, la invitación con su fecha en un calendario y su botón; en el medio, su operación de la portada; abajo, sus tres preocupaciones y la firma de quien la prepara. | Simple · Andina Logística (demo 0.5.0) · diapositiva «Empecemos por su meta: en una semana, un prototipo» |

## Cierre: su futuro, funcionando (el lema)

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`controlroom-live`](controlroom-live.json) | left | El prototipo crece hasta la sala de control: la pantalla en vivo con el pronóstico y el mapa de bodega a estación; delante, dos operadores en su consola. | dcd · escena de catálogo (energía) |
| [`tickets-live`](tickets-live.json) | left | El prototipo crece hasta la pantalla de atención a comercios en vivo: cuatro tickets, el espacio restringido del agente con su candado y sus fuentes y, abajo, el monitoreo de TI; delante, de espaldas, dos personas en su consola. | dcd · escena de catálogo (pagos) |
| [`lema-signer`](lema-signer.json) | left | El logo del cliente arriba, grande y al centro; debajo, el mapa de la estrategia con sus tres paradas en la cinta magenta, y la foto del trainer. | dcd · escena de catálogo (fidelización) |
| [`lema-conversation`](lema-conversation.json) | left | La mesa del jueves de la diapositiva 1: detrás, en la pantalla, la portada hecha para ella; a un lado tú y al otro la gerente, sin rostro, frente a frente. | Clase VR (formación) · diapositiva «Planea la conversación. Las diapositivas vienen solas.» |
| [`care-center`](care-center.json) | left | El centro de cuidado de mañana: la pantalla con las señales de Cuida y la cola de consultas, el teléfono del cliente con Cuida y, delante, una persona del equipo de cuidado con su tablet. | dcd · escena de catálogo (salud) |
| [`luz-end`](luz-end.json) | left | El anillo del piloto, más grande, con «Piloto» en su centro; a la derecha, el puente de cinco pilares hacia la operación; abajo, el retrato de Javier en un anillo de luz, con su nombre y su rol; al fondo, estrellas y una cámara que respira. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «Make it happen, together.» |
| [`ops-center`](ops-center.json) | left | El centro de operaciones de mañana, en vivo: a la izquierda, la cola de consultas y el conocimiento gobernado; a la derecha, los tres pasos de una respuesta; debajo, el teléfono del cliente y una persona del equipo con su tablet. | dcd · escena de catálogo (banca) |

## En vivo: panel

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`panel-questions`](panel-questions.json) | top | Cinco tarjetas altas de pregunta en fila, numeradas del 1 al 5, con las preguntas grandes y un medidor de voz quieto al pie, sobre una línea de luz magenta; al fondo, estrellas lejanas. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «Cinco preguntas» |
| [`panel-questions-list`](panel-questions-list.json) | left | Las preguntas del panel, numeradas, en una columna; las dos de reserva, punteadas y con su etiqueta. | any world · library scene (webinar-panel, 2026-10) |
| [`luz-panel`](luz-panel.json) | left | Una mesa de luz en perspectiva con tres siluetas sin rostro sentadas detrás y una lámpara en su riel arriba; frente a cada una, una tarjeta con su rol y «Por confirmar»; el trazo magenta cruza el frente de la mesa. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «Panel» |

## En vivo: reflexiones y preguntas

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`unfold-describe`](unfold-describe.json) | left | La hoja del informe, doblada. | dcd · escena de catálogo (fidelización) |
| [`time-freed`](time-freed.json) | left | El calendario de papel de la semana, con el lunes en la mañana resaltado y su bloque de dos horas: el informe. | dcd · escena de catálogo (fidelización) |
| [`time-back`](time-back.json) | left | La misma semana de la diapositiva 2: el martes a las 4 pm, el jueves 10:00 con el prospecto y, el miércoles, tus dos horas para preparar ocupadas por «Mover cajas», «Buscar una plantilla» y «Ajustar el formato». | Clase VR (formación) · diapositiva «¿Qué harías con las horas que ya no pasas diagramando?» |
| [`reflections-live`](reflections-live.json) | top | Cinco momentos sobre un mismo hilo de luz, en el orden del cierre: a la izquierda el chat «Sus preguntas, por el chat»; al centro, tres tarjetas de vidrio oscuro boca abajo, «Reflexión 1», «Reflexión 2» y «Reflexión 3»; a la derecha, la encuesta con su marco de QR. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «Tres reflexiones de hoy» |
| [`reflections-cards`](reflections-cards.json) | left | Tres tarjetas boca abajo, «Reflexión 1», «Reflexión 2» y «Reflexión 3», y debajo la encuesta. | any world · library scene (webinar-panel, 2026-10) |
| [`luz-question`](luz-question.json) | left | Un embudo de luz en profundidad (su boca, dos cortes y una pared que se estrecha): arriba, el chip «La IA», abierto sobre la estela; abajo, el cuello «Nosotros» alrededor de tres personas sin rostro; debajo, la burbuja del chat. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «¿El cuello de botella es la IA… o somos nosotros?» |

## Formación y webinar: agenda

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`luz-agenda`](luz-agenda.json) | top | Cuatro tarjetas de vidrio a lo ancho, cada una del tamaño de su parte de los 55 minutos, con su duración grande y su nombre: «5 min» Chat, «10 min» Contexto, «30 min» Panel y «10 min» Cierre, cada una con sus contenidos; debajo, una línea de tiempo de luz con sus marcas 00:00 · 05:00 · 15:00 · 45:00 · 55:00. | webinar «IA: ¿el fin del piloto eterno?» · diapositiva «55 minutos» |

## Formación: la demo en vivo

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`skill-handoff`](skill-handoff.json) | left | El facilitador, sin rostro, sostiene el paquete «dynamic-commercial-decks.zip»; en su pantalla, «Comparto el zip en el chat del equipo»; abajo, tres portátiles con sus asistentes de espaldas y los tres pasos de instalación por marcar. | Clase VR (formación) · diapositiva «Demo en vivo: el facilitador te entrega el skill» |
| [`live-steps`](live-steps.json) | left | Tu pantalla en vivo con tres etapas en columna: Contexto (su sitio y tus notas, el skill, hechos e hipótesis), Confirmas (la tabla de hechos y las cinco preguntas) y Títulos. | Clase VR (formación) · diapositiva «Le das contexto, confirmas hechos y apruebas títulos» |
| [`build-deliver`](build-deliver.json) | left | Tres columnas de izquierda a derecha: «Construye» con cuatro diapositivas vacías, «Revisa» con cinco revisiones apagadas y «Entrega», una bandeja vacía. | Clase VR (formación) · diapositiva «El skill construye, revisa y entrega; tú presentas» |

## Formación: práctica

| Snippet | Layout | Aterriza (≤2 s) | Origen |
|---|---|---|---|
| [`diagnostic`](diagnostic.json) | left | Una hoja de diagnóstico de papel con siete preguntas, cada una con su ícono y su casilla, todas a la vista; debajo, tres bandejas (delegar a la IA, automatizar, cambiar el proceso), la ficha «Consolidar el informe semanal» junto a la primera pregunta y un reloj de papel de dos minutos. | dcd · escena de catálogo (fidelización) |
| [`hands-on-timer`](hands-on-timer.json) | left | Un escritorio con el portátil abierto en el skill, tres pasos por marcar en la pantalla y, al lado, un reloj de 15 minutos. | Clase VR (formación) · diapositiva «Tu próxima prospección, en quince minutos» |
| [`pair-read`](pair-read.json) | left | Dos personas frente a frente con la lista de títulos entre ellas y, arriba, tres relojes de 40 segundos: leer, reformular y compromiso. | Clase VR (formación) · diapositiva «Lee tus títulos a otra persona: ¿se entiende?» |
| [`journey-path`](journey-path.json) | left | Arriba, para quién es; debajo, el recorrido de su cliente en cinco estaciones con los íconos de su sector, cada una con su nombre y lo que pasa ahí; en una de ellas, un «?»; abajo, la promesa. | dcd 0.6.0 · escena de catálogo |
| [`journey-loop`](journey-loop.json) | left | Su cliente al centro de un anillo con seis puntos de contacto, cada uno con un ícono de su sector y su nombre; abajo, la lección del ciclo. | dcd 0.6.0 · escena de catálogo |
| [`roadmap-phases`](roadmap-phases.json) | left | Una línea de tiempo con tres fases (su nombre, su periodo y dos entregables cada una) y un rombo de decisión entre fase y fase; abajo, la meta. | dcd 0.6.0 · escena de catálogo |
| [`roadmap-road`](roadmap-road.json) | left | Un camino sube serpenteando desde «Hoy» hasta la meta, arriba; a los lados, cuatro banderas con su hito, su periodo y un ícono de su sector. | dcd 0.6.0 · escena de catálogo |
| [`before-after-split`](before-after-split.json) | left | Dos paneles: «Antes», con cuatro pasos a mano y su reloj, y «Después», punteado, con tres pasos por encender. | dcd 0.6.0 · escena de catálogo |
| [`before-after-lanes`](before-after-lanes.json) | left | Dos carriles con las mismas cuatro estaciones y los íconos de su sector: «Hoy», con una vuelta atrás marcada, y «Con el cambio», derecho; abajo, el resultado. | dcd 0.6.0 · escena de catálogo |
| [`matrix-quadrants`](matrix-quadrants.json) | left | Una matriz de dos por dos, esfuerzo a lo ancho e impacto a lo alto, con sus cuatro cuadrantes nombrados. | dcd 0.6.0 · escena de catálogo |
| [`matrix-table`](matrix-table.json) | left | Una tabla: tres opciones con el ícono de su sector en las filas, tres criterios en las columnas y sus círculos vacíos; debajo, la leyenda. | dcd 0.6.0 · escena de catálogo |
| [`funnel-stages`](funnel-stages.json) | left | Un embudo de cuatro etapas, cada una con un ícono de su sector y su nombre a la derecha; a la izquierda, las salidas punteadas; abajo, el resultado. | dcd 0.6.0 · escena de catálogo |
| [`funnel-gates`](funnel-gates.json) | left | A la izquierda, cinco ideas con los íconos de su sector; al medio, tres preguntas como compuertas; abajo, la bandeja «Por ahora no»; al final, «Construimos». | dcd 0.6.0 · escena de catálogo |
| [`timeline-milestones`](timeline-milestones.json) | left | Una línea desde «Hoy» con cinco hitos, cada uno con su periodo, su nombre y un ícono de su sector, alternando a un lado y al otro. | dcd 0.6.0 · escena de catálogo |
| [`timeline-tracks`](timeline-tracks.json) | left | Cuatro frentes en filas, con un ícono de su sector, y cuatro semanas en columnas; cada frente con su tramo punteado; abajo, la decisión. | dcd 0.6.0 · escena de catálogo |
| [`org-tree`](org-tree.json) | left | Arriba, el patrocinador; debajo, tres líderes (cada uno con el ícono de un área de su negocio) y los roles de cada equipo, todos sin rostro; abajo, la meta. | dcd 0.6.0 · escena de catálogo |
| [`org-squad`](org-squad.json) | left | Sus roles a un lado y los nuestros al otro, sin rostro, unidos por puentes punteados a una meta compartida al centro; abajo, el ritmo del trabajo. | dcd 0.6.0 · escena de catálogo |
| [`map-hub`](map-hub.json) | left | Una tierra abstracta de puntos (nunca un mapa real), su oficina central al medio y cinco regiones con un ícono de su sector y su nombre; abajo, la nota. | dcd 0.6.0 · escena de catálogo |
| [`map-lines`](map-lines.json) | left | Dos rutas dibujadas como un mapa de transporte, una a lo ancho y otra hacia abajo, con sus paradas e íconos de su sector; se cruzan en una estación compartida. | dcd 0.6.0 · escena de catálogo |
