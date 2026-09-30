# Verticales: una ficha por vertical

Una sección `## <id>` por vertical (el id canónico de `references/vocab.json`; «cualquiera» no tiene ficha). Cada una
abre con tres campos, `label:`, `keywords:` e `icons:`, y sigue con sus secciones `###`. Lee solo la sección del
vertical del deck.

Cómo usarla: `scripts/intake.py` lee `keywords:` (y la sección «Palabras para detectar el vertical» cuando la hay) para
detectar el vertical; tú lees el resto para escribir el brief, las hipótesis y los títulos. Nada aquí es una cifra:
solo nombres de KPI. Una cifra entra al deck solo como hecho confirmado en `<work>/facts.json`. Lectores:
`scripts/vocab.py` (`fichas()`, `ficha_text()`, y `check` valida los ids y los campos), `intake.py` y `templates.py`.

## banca

label: Banca
keywords: banco, bancaria, bancario, crédito, créditos, préstamo, préstamos, hipotecario, ahorro, cuenta de ahorros, depósitos, tarjeta de crédito, sucursal, oficinas, cartera, colocaciones, superintendencia financiera, entidad financiera, banca digital, cooperativa de ahorro
icons: banca/credito, banca/ahorro, banca/tarjeta, banca/sucursal, banca/riesgo

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de atender a cada cliente (oficina, centro de contacto, operación) tiene que bajar sin
  perder cercanía.
- **Meta del trimestre:** colocación de crédito y captación de depósitos; cumplir el plan comercial por segmento.
- **KPI prometido al jefe:** tiempo de aprobación de un crédito, calidad de la cartera, clientes digitales activos.

### Vocabulario público de KPI (nombres, sin cifras)
Tiempo de aprobación de crédito · cartera vencida · colocaciones · captaciones · clientes digitales activos ·
costo por transacción · satisfacción del cliente (NPS) · tiempo de respuesta a un reclamo.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Crédito", "¿Preaprobar con los datos que ya tienen?", "Respuesta en menos tiempo"]` · retorno
2. `["Cobranza", "¿Priorizar a quién llamar primero y con qué oferta?", "Cartera más sana"]` · retorno
3. `["Servicio", "¿Resolver el reclamo repetido sin pasar por tres áreas?", "Menos reclamos abiertos"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del cliente para todos los canales?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`banca/credito` · `banca/ahorro` · `banca/tarjeta` · `banca/sucursal` · `banca/riesgo` · genéricos: `generico/dato`,
`generico/meta`, `generico/equipo`.

### Palabras que no van
«fraude de sus clientes», «riesgo de quiebra», «multas», «sanción», el nombre de su core bancario o de sus proveedores,
«bancarizar a la fuerza», siglas que la sala no trajo (NPL, LTV, KYC), «transformación digital».

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa, informe anual), el informe de gestión o sostenibilidad, el regulador financiero de
su país y el gremio bancario (cifras del sector, con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Tiempo de aprobación de un crédito:** lo que pasa desde que el cliente pide el crédito hasta que recibe la respuesta.
- **Cartera vencida:** la parte de los créditos con pagos atrasados, frente al total de la cartera.
- **Clientes digitales activos:** clientes que usaron un canal digital en el período.
- **Tiempo de respuesta a un reclamo:** días desde que entra un reclamo hasta que se cierra con respuesta.
- **Costo por transacción:** lo que cuesta atender una operación, según el canal (nunca con cifra en el deck).

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Preaprobar con los datos que ya tienen podría acortar la respuesta de un crédito.
2. Priorizar a quién llamar primero y con qué oferta podría mantener la cartera más sana.
3. Un resumen del caso para el asesor podría cerrar el reclamo repetido sin pasar por tres áreas.
4. Un solo dato del cliente para todos los canales podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La regulación no nos deja usar IA con datos de clientes.» → ¿Qué parte del proceso no toca un dato sensible? Por ahí podría empezar el discovery, con cumplimiento en la sala.
- «Ya tenemos un proveedor de analítica.» → ¿Qué decisión de la semana todavía se toma sin ese dato? La pregunta no es la herramienta: es el proceso que cambia.
- «Esto ya lo intentamos y no escaló.» → ¿Qué faltó para pasar de piloto a operación? Un criterio de retorno claro desde el primer día cambia la conversación.
- «No es prioridad este trimestre.» → ¿Qué meta del trimestre depende de este proceso? Si ninguna, tiene sentido esperar; si alguna, una semana de discovery lo aclara.

## seguros

label: Seguros
keywords: seguro, seguros, aseguradora, póliza, pólizas, siniestro, siniestros, asegurado, asegurados, prima, primas, reaseguro, cobertura, indemnización, suscripción, corredor de seguros, vida, autos, hogar
icons: seguros/poliza, seguros/siniestro, seguros/proteccion, seguros/suscripcion

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de gestionar cada siniestro y cada póliza, sin sumar personas al centro de operación.
- **Meta del trimestre:** primas emitidas y renovaciones; que el cliente renueve sin llamar.
- **KPI prometido al jefe:** tiempo de pago de un siniestro, índice de renovación, satisfacción del asegurado.

### Vocabulario público de KPI (nombres, sin cifras)
Primas emitidas · índice de siniestralidad · tiempo de liquidación de un siniestro · tasa de renovación ·
índice combinado · satisfacción del asegurado (NPS) · pólizas por cliente.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Siniestros", "¿Leer los documentos del siniestro y armar el expediente solo?", "Pago en menos días"]` · retorno
2. `["Suscripción", "¿Resumir el riesgo antes de cotizar?", "Cotización más rápida"]` · retorno
3. `["Renovación", "¿Avisar a tiempo a quien podría no renovar?", "Más renovaciones"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del asegurado para todos los canales?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`seguros/poliza` · `seguros/siniestro` · `seguros/proteccion` · `seguros/suscripcion` · genéricos: `generico/documento`,
`generico/reloj`, `generico/check`.

### Palabras que no van
«rechazar siniestros», «fraude de sus asegurados», «letra pequeña», nombres de sus reaseguradores o corredores, siglas
que la sala no trajo, «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa), el informe anual, el regulador de seguros de su país y el gremio asegurador (cifras
del sector con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Tiempo de liquidación de un siniestro:** días desde el aviso del siniestro hasta el pago.
- **Tasa de renovación:** pólizas que se renuevan frente a las que vencen en el período.
- **Índice de siniestralidad:** lo pagado en siniestros frente a las primas del mismo período.
- **Tiempo de cotización:** desde que llega la solicitud hasta que sale la oferta.
- **Satisfacción del asegurado:** lo que dice el asegurado después de un trámite, en su escala (NPS u otra).

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Armar el expediente con los documentos que ya llegaron podría acortar el pago de un siniestro.
2. Un resumen del riesgo antes de cotizar podría dar una cotización más rápida.
3. Avisar a tiempo a quien podría no renovar podría sostener la cartera de pólizas.
4. Un solo dato del asegurado para todos los canales podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Los siniestros los revisa una persona, siempre.» → Así sigue siendo: la persona decide. ¿Cuánto de su día se va en reunir documentos antes de decidir?
- «Nuestros datos están en sistemas distintos.» → Es el punto de partida más común. ¿Qué pregunta del negocio respondería primero un dato unido?
- «El riesgo reputacional es alto.» → ¿Qué proceso interno, lejos del asegurado, podría probar la idea primero?

## salud

label: Salud
keywords: salud, clínica, clínicas, hospital, hospitales, paciente, pacientes, médico, médicos, consulta, consultas, cita médica, eps, ips, laboratorio, diagnóstico, farmacia, medicamento, medicamentos, historia clínica, afiliados, bienestar
icons: salud/consulta, salud/pulso, salud/medicamento, salud/historia

### Lo que le preocupa a la sala
- **Presupuesto:** el costo por paciente atendido y el tiempo administrativo de cada profesional.
- **Meta del trimestre:** citas atendidas, ocupación y que el paciente vuelva al control.
- **KPI prometido al jefe:** tiempo de espera para una cita, reingresos evitables, satisfacción del paciente.

### Vocabulario público de KPI (nombres, sin cifras)
Tiempo de espera para cita · ocupación de camas · tasa de inasistencia · reingresos · tiempo de atención ·
satisfacción del paciente · adherencia al tratamiento.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Agenda", "¿Recordar y reagendar antes de que el paciente falte?", "Menos citas perdidas"]` · retorno
2. `["Atención", "¿Preparar el resumen de la historia antes de la consulta?", "Más tiempo con el paciente"]` · retorno
3. `["Autorizaciones", "¿Armar la autorización con los documentos que ya llegaron?", "Respuesta en menos tiempo"]` · retorno
4. `["Datos y tecnología", "¿Un dato del paciente que viaje con él?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`salud/consulta` · `salud/pulso` · `salud/medicamento` · `salud/historia` · genéricos: `generico/reloj`,
`generico/documento`, `generico/equipo`.

### Palabras que no van
«errores médicos», «pacientes mal atendidos», «diagnóstico automático», «reemplazar al médico», datos de pacientes
(ni uno), nombres de médicos, «garantiza», siglas que la sala no trajo.

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa), el informe de gestión, el ministerio o la superintendencia de salud de su país y
los gremios del sector (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Tiempo de espera para una cita:** días desde que el paciente pide la cita hasta que lo atienden.
- **Tasa de inasistencia:** citas a las que el paciente no llega, frente a las agendadas.
- **Reingresos evitables:** pacientes que vuelven por la misma causa en poco tiempo, cuando se pudo prevenir.
- **Tiempo del profesional con el paciente:** minutos de la consulta dedicados al paciente y no al registro.
- **Adherencia al tratamiento:** pacientes que siguen el tratamiento indicado, frente a los tratados.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Recordar y reagendar antes de que el paciente falte podría reducir las citas perdidas.
2. Preparar el resumen de la historia antes de la consulta podría dar más tiempo con el paciente.
3. Armar la autorización con los documentos que ya llegaron podría acortar la respuesta.
4. Un dato del paciente que viaje con él podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La IA no puede decidir sobre un paciente.» → Nunca decide: prepara. ¿Qué tarea administrativa le quita hoy tiempo al profesional?
- «Los datos de pacientes no salen de aquí.» → Bien dicho. ¿Qué podría probarse con datos de la operación, sin un solo dato de paciente?
- «Los médicos no van a usar otra herramienta.» → ¿Y si no es otra herramienta, sino menos pasos en la que ya usan?

## energia

label: Energía
keywords: energía, energética, eléctrica, electricidad, gas natural, glp, petróleo, hidrocarburos, transmisión, distribución de energía, generación, subestación, solar, eólica, renovables, oleoducto, gasoducto, turbina, compresor, confiabilidad, mantenimiento de activos
icons: energia/torre, energia/solar, energia/ducto, energia/medidor

El ejemplo de referencia es el deck de energía de `examples/` en la raíz del repo (privado, nunca en el paquete); en el
catálogo, el cliente ficticio es Voltiara.

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de mantenimiento de los activos y de las compras de emergencia.
- **Meta del trimestre:** disponibilidad de los activos y cumplimiento del plan de mantenimiento.
- **KPI prometido al jefe:** paradas no planeadas, tiempo medio entre fallas, cumplimiento de entregas.

### Vocabulario público de KPI (nombres, sin cifras)
Disponibilidad de activos · paradas no planeadas · tiempo medio entre fallas · tiempo medio de reparación ·
cumplimiento del plan de mantenimiento · pérdidas de energía · incidentes de seguridad.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Confiabilidad", "¿Priorizar las alarmas que importan primero?", "Menos paradas"]` · retorno
2. `["Repuestos", "¿Tener el repuesto listo antes de que se pida?", "Menos urgencias"]` · retorno
3. `["Documentos", "¿Llenar el reporte de campo con lo que ya se midió?", "Menos trabajo manual"]` · retorno
4. `["Datos y tecnología", "¿Conectar los datos de todos los equipos?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`energia/torre` · `energia/solar` · `energia/ducto` · `energia/medidor` · genéricos: `generico/alerta`, `generico/dato`,
`generico/reloj`.

### Palabras que no van
«apagón», «accidente», «explosión», nombres de sus proveedores de equipos o software, su casa matriz como si fuera el
cliente, «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, líneas de servicio, sala de prensa), el regulador de energía o gas de su país, el operador del
sistema y los gremios del sector (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Paradas no planeadas:** detenciones de un activo que no estaban en el plan, por período.
- **Disponibilidad de activos:** tiempo en que el activo está listo para operar, frente al tiempo total.
- **Tiempo medio entre fallas:** horas de operación, en promedio, entre una falla y la siguiente.
- **Tiempo medio de reparación:** horas, en promedio, desde la falla hasta que el activo vuelve a operar.
- **Cumplimiento del plan de mantenimiento:** órdenes de mantenimiento cerradas a tiempo, frente a las planeadas.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Priorizar las alarmas que importan primero podría reducir las paradas no planeadas.
2. Tener el repuesto listo antes de que se pida podría bajar las compras de emergencia.
3. Llenar el reporte de campo con lo que ya se midió podría quitar trabajo manual.
4. Conectar los datos de todos los equipos podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La operación es crítica: no probamos nada en campo.» → Por eso el primer paso podría ser de escritorio, con los reportes y alarmas que ya existen. ¿Cuál revisan hoy a mano?
- «Ya tenemos un sistema de mantenimiento.» → ¿Qué decisión se toma todavía fuera de ese sistema, en una hoja o en una llamada?
- «Nuestros datos no están listos.» → Casi nunca lo están del todo. ¿Qué pregunta concreta pediría solo los datos que ya tienen?

## mineria

label: Minería
keywords: minería, minera, minero, mina, minas, mineral, minerales, cobre, oro, carbón, níquel, litio, extracción, yacimiento, tajo, concentrado, relaves, acarreo, perforación, voladura, planta concentradora
icons: mineria/casco, mineria/mina, mineria/volqueta, mineria/mineral

### Lo que le preocupa a la sala
- **Presupuesto:** el costo por tonelada movida y el mantenimiento de la flota.
- **Meta del trimestre:** toneladas producidas y disponibilidad de la flota y de la planta.
- **KPI prometido al jefe:** seguridad de las personas, recuperación en planta, cumplimiento del plan minero.

### Vocabulario público de KPI (nombres, sin cifras)
Toneladas movidas · disponibilidad de flota · utilización de equipos · recuperación metalúrgica · costo por tonelada ·
índice de frecuencia de incidentes · consumo de agua y energía.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Flota", "¿Anticipar la falla del camión antes del turno?", "Más horas disponibles"]` · retorno
2. `["Planta", "¿Sugerir el ajuste de la planta según el mineral que entra?", "Mejor recuperación"]` · retorno
3. `["Seguridad", "¿Leer los reportes de turno y avisar lo que se repite?", "Menos incidentes"]` · retorno
4. `["Datos y tecnología", "¿Unir los datos de mina y planta?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`mineria/casco` · `mineria/mina` · `mineria/volqueta` · `mineria/mineral` · genéricos: `generico/alerta`,
`generico/dato`, `generico/equipo`.

### Palabras que no van
«accidente», «fatalidad», «conflicto social», «impacto ambiental» como acusación, nombres de sus contratistas o
proveedores de equipos, precios de los metales, «garantiza».

### Dónde buscar lo público
Su sitio (nosotros, sostenibilidad, sala de prensa), el reporte de sostenibilidad, el ministerio o la agencia minera de
su país y el gremio minero (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Disponibilidad de flota:** tiempo en que los equipos están listos para operar, frente al tiempo total.
- **Utilización de equipos:** tiempo en que el equipo disponible trabaja de verdad.
- **Recuperación metalúrgica:** mineral valioso que la planta recupera, frente al que entra.
- **Índice de frecuencia de incidentes:** incidentes por cada millón de horas trabajadas.
- **Consumo de agua y energía por tonelada:** recursos usados para mover o procesar cada tonelada.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Anticipar la falla del camión antes del turno podría dar más horas disponibles.
2. Sugerir el ajuste de la planta según el mineral que entra podría mejorar la recuperación.
3. Leer los reportes de turno y avisar lo que se repite podría prevenir incidentes.
4. Unir los datos de mina y planta podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «En la mina manda la seguridad, no la tecnología.» → De acuerdo en el orden. ¿Qué señal de seguridad se repite en los reportes y nadie alcanza a leer completa?
- «La conectividad en faena es limitada.» → ¿Qué parte podría correr con los datos que ya bajan al final del turno?
- «Cada mina es distinta.» → Por eso se empieza en una. ¿Cuál tiene la pregunta más clara?

## retail

label: Retail
keywords: retail, tienda, tiendas, supermercado, supermercados, almacén, almacenes, cadena de tiendas, comercio, e-commerce, tienda en línea, carrito, góndola, inventario en tienda, surtido, promociones, programa de lealtad, puntos, compradores, omnicanal
icons: retail/carrito, retail/tienda, retail/etiqueta, retail/lealtad

### Lo que le preocupa a la sala
- **Presupuesto:** el margen de cada categoría y el costo de las promociones que no rinden.
- **Meta del trimestre:** ventas por tienda y por canal; la temporada que viene.
- **KPI prometido al jefe:** productos agotados en góndola, ticket promedio, clientes que vuelven.

### Vocabulario público de KPI (nombres, sin cifras)
Ventas mismas tiendas · ticket promedio · agotados en góndola · rotación de inventario · margen por categoría ·
frecuencia de compra · clientes activos del programa de lealtad.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Surtido", "¿Pedir a tiempo lo que cada tienda va a vender?", "Menos agotados"]` · retorno
2. `["Promociones", "¿Saber qué promoción rinde antes de lanzarla?", "Mejor margen"]` · retorno
3. `["Clientes", "¿Una oferta distinta para cada comprador?", "Clientes que vuelven"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato de venta, tienda y canal?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`retail/carrito` · `retail/tienda` · `retail/etiqueta` · `retail/lealtad` · genéricos: `generico/dato`, `generico/meta`,
`generico/equipo`.

### Palabras que no van
«tiendas vacías», «clientes perdidos», «guerra de precios», precios o descuentos concretos, nombres de sus proveedores o
marcas propias de terceros, «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa, inversionistas), el informe anual, el gremio de comercio de su país y las
estadísticas oficiales de comercio (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Agotados en góndola:** referencias que el comprador no encuentra en el estante, frente a las del surtido.
- **Rotación de inventario:** veces que el inventario se vende y se repone en el período.
- **Frecuencia de compra:** compras de un mismo cliente en el período.
- **Ventas mismas tiendas:** ventas de las tiendas comparables frente al mismo período anterior.
- **Margen por categoría:** lo que deja cada categoría después de su costo (nunca con cifra en el deck).

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Pedir a tiempo lo que cada tienda va a vender podría reducir los agotados.
2. Saber qué promoción rinde antes de lanzarla podría cuidar el margen.
3. Una oferta distinta para cada comprador podría traer clientes que vuelven.
4. Un solo dato de venta, tienda y canal podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Ya personalizamos con nuestro programa de lealtad.» → ¿Qué decisión de surtido o de promoción todavía no usa ese dato?
- «Las promociones las define la negociación con cada marca.» → ¿Qué sabría esa mesa si viera antes qué promoción rinde?
- «Tenemos demasiadas tiendas para empezar.» → ¿Y si se empieza por una categoría en pocas tiendas, con un criterio claro para seguir o parar?

## pagos

label: Pagos
keywords: pagos, pago, pasarela de pagos, adquirente, adquirencia, datáfono, datáfonos, pos, comercios afiliados, billetera, billetera digital, transferencias, pago qr, procesamiento de pagos, liquidación, contracargo, transacciones, fintech, medios de pago
icons: pagos/pos, pagos/billetera, pagos/transferencia, pagos/qr

El ejemplo de referencia es el caso de pagos (cliente ficticio Pagalia; `scenes.md`, aliases `-b`).

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de atender a cada comercio y de resolver cada reclamo.
- **Meta del trimestre:** comercios activos y volumen procesado; nuevas reglas del regulador que llegan.
- **KPI prometido al jefe:** disponibilidad del servicio, tiempo de afiliación de un comercio, tickets resueltos.

### Vocabulario público de KPI (nombres, sin cifras)
Comercios activos · volumen procesado · tasa de aprobación · disponibilidad del servicio · tiempo de afiliación ·
tiempo de resolución de un ticket · contracargos.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Comercios", "¿Afiliar a un comercio en un solo paso?", "Más comercios activos"]` · retorno
2. `["Soporte", "¿Responder el ticket repetido con lo que ya se sabe?", "Tickets resueltos antes"]` · retorno
3. `["Operación", "¿Ver la caída de aprobación antes de que el comercio llame?", "Más transacciones aprobadas"]` · retorno
4. `["Conocimiento", "¿El conocimiento de cada equipo a mano de todos?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`pagos/pos` · `pagos/billetera` · `pagos/transferencia` · `pagos/qr` · genéricos: `generico/dato`, `generico/alerta`,
`generico/equipo`.

### Palabras que no van
«fraude» como acusación, comisiones o tarifas (son precios), el banco accionista como si fuera el cliente (su billetera
no es del procesador), nombres de sus comercios, «garantiza».

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa), el banco central o regulador de pagos de su país y las cifras oficiales de pagos
digitales (con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Comercios activos:** comercios afiliados que procesaron al menos una transacción en el período.
- **Tasa de aprobación:** transacciones aprobadas frente a las intentadas.
- **Tiempo de afiliación de un comercio:** días desde la solicitud hasta la primera transacción.
- **Tiempo de resolución de un ticket:** horas desde que el comercio reporta hasta que queda resuelto.
- **Contracargos:** transacciones que el tarjetahabiente disputa, frente a las procesadas.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Afiliar a un comercio en un solo paso podría sumar comercios activos.
2. Responder el ticket repetido con lo que ya se sabe podría resolverlo antes.
3. Ver la caída de aprobación antes de que el comercio llame podría sostener las transacciones.
4. El conocimiento de cada equipo a mano de todos podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «El riesgo transaccional no se toca.» → Tiene sentido. ¿Qué proceso alrededor, como soporte o afiliación, podría probar la idea primero?
- «Nuestro equipo de datos ya está copado.» → ¿Qué pedido repetido le llega cada semana que podría resolverse sin ellos?
- «Los comercios no piden IA.» → Piden respuestas rápidas. ¿Qué pregunta de un comercio tarda hoy más de lo que debería?

## telco

label: Telecomunicaciones
keywords: telecomunicaciones, telco, operador móvil, telefonía, móvil, internet hogar, fibra óptica, fibra, banda ancha, antena, antenas, cobertura, 5g, 4g, planes pospago, prepago, líneas, red móvil, espectro, televisión por cable
icons: telco/antena, telco/fibra, telco/sim, telco/cobertura

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de cada visita técnica y de cada llamada al centro de contacto.
- **Meta del trimestre:** altas netas de líneas y de hogares conectados.
- **KPI prometido al jefe:** clientes que se van, disponibilidad de la red, instalaciones a tiempo.

### Vocabulario público de KPI (nombres, sin cifras)
Clientes que se van (tasa de abandono) · altas netas · ingreso por usuario · disponibilidad de la red · instalaciones
a tiempo · visitas técnicas repetidas · satisfacción del cliente (NPS).

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Clientes", "¿Avisar a tiempo quién podría irse?", "Menos clientes que se van"]` · retorno
2. `["Campo", "¿Resolver a distancia antes de enviar al técnico?", "Menos visitas repetidas"]` · retorno
3. `["Red", "¿Ver la falla de la red antes de que llamen?", "Más disponibilidad"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del cliente, la red y la factura?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`telco/antena` · `telco/fibra` · `telco/sim` · `telco/cobertura` · genéricos: `generico/alerta`, `generico/dato`,
`generico/equipo`.

### Palabras que no van
«mala cobertura», «clientes furiosos», «churn» (se dice «clientes que se van»), tarifas o planes con precio, nombres
de sus proveedores de red, «garantiza», siglas que la sala no trajo.

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa, inversionistas), el regulador de telecomunicaciones de su país y sus reportes
trimestrales del sector (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Clientes que se van (tasa de abandono):** clientes que cancelan en el período, frente a la base.
- **Disponibilidad de la red:** tiempo en que el servicio está arriba, frente al tiempo total.
- **Instalaciones a tiempo:** instalaciones hechas en la fecha acordada, frente a las programadas.
- **Visitas técnicas repetidas:** visitas a un mismo cliente por la misma falla.
- **Ingreso por usuario:** lo que factura en promedio cada línea (nunca con cifra en el deck).

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Avisar a tiempo quién podría irse podría retener clientes.
2. Resolver a distancia antes de enviar al técnico podría evitar visitas repetidas.
3. Ver la falla de la red antes de que llamen podría sostener la disponibilidad.
4. Un solo dato del cliente, la red y la factura podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Ya tenemos modelos de abandono.» → ¿Qué pasa entre la alerta del modelo y la llamada al cliente? A menudo el cambio está ahí.
- «La red la opera un tercero.» → ¿Qué dato de la red ya llega a su lado y podría usarse antes de que el cliente llame?
- «Cada área tiene su sistema.» → ¿Qué pregunta de un cliente cruza tres áreas hoy? Esa podría ser la primera.

## industria

label: Industria
keywords: industria, industrial, manufactura, fábrica, fábricas, planta de producción, plantas, producción, línea de producción, ensamble, maquinaria, mantenimiento, calidad, cemento, acero, químicos, plásticos, papel, metalmecánica, automatización industrial
icons: industria/fabrica, industria/engranaje, industria/robot, industria/silo

### Lo que le preocupa a la sala
- **Presupuesto:** el costo por unidad producida, la energía y los repuestos.
- **Meta del trimestre:** volumen producido a tiempo para los pedidos del trimestre.
- **KPI prometido al jefe:** eficiencia de los equipos, paradas no planeadas, producto fuera de especificación.

### Vocabulario público de KPI (nombres, sin cifras)
Eficiencia general de los equipos (OEE) · paradas no planeadas · producto no conforme · cumplimiento del plan de
producción · consumo de energía por unidad · tiempo de cambio de formato · incidentes de seguridad.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Mantenimiento", "¿Anticipar la falla de la máquina que para la línea?", "Menos paradas"]` · retorno
2. `["Calidad", "¿Ver el defecto antes del final de la línea?", "Menos producto no conforme"]` · retorno
3. `["Planeación", "¿Ajustar el plan de producción cuando cambia un pedido?", "Pedidos a tiempo"]` · retorno
4. `["Datos y tecnología", "¿Conectar los datos de la planta con los del negocio?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`industria/fabrica` · `industria/engranaje` · `industria/robot` · `industria/silo` · genéricos: `generico/alerta`,
`generico/dato`, `generico/check`.

### Palabras que no van
«reemplazar operarios», «despidos», «accidente», nombres de sus proveedores de maquinaria o software, «industria 4.0»
como consigna, «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, plantas, sostenibilidad, sala de prensa), el reporte de sostenibilidad, el gremio industrial de su
país y las estadísticas oficiales de producción (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Eficiencia general de los equipos (OEE):** disponibilidad, rendimiento y calidad de un equipo, en una sola medida.
- **Paradas no planeadas:** horas de línea detenida que no estaban en el plan.
- **Producto no conforme:** lo producido que no cumple la especificación, frente al total.
- **Cumplimiento del plan de producción:** lo producido frente a lo planeado en el período.
- **Tiempo de cambio de formato:** lo que tarda una línea en pasar de un producto a otro.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Anticipar la falla de la máquina que para la línea podría reducir las paradas.
2. Ver el defecto antes del final de la línea podría bajar el producto no conforme.
3. Ajustar el plan de producción cuando cambia un pedido podría entregar a tiempo.
4. Conectar los datos de la planta con los del negocio podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La planta no se detiene para pruebas.» → No hace falta: se empieza con los datos que la planta ya registra. ¿Cuál revisan después de cada parada?
- «Nuestras máquinas son antiguas.» → ¿Qué se anota hoy a mano sobre ellas? Ese registro podría ser el primer dato.
- «Calidad ya tiene su método.» → ¿En qué punto de la línea llega tarde la señal del defecto?

## publico

label: Sector público
keywords: ministerio, secretaría, alcaldía, gobernación, entidad pública, gobierno, estado, ciudadano, ciudadanos, trámite, trámites, servicio al ciudadano, contratación pública, normativa, decreto, política pública, instituto nacional, agencia nacional, municipio
icons: publico/edificio, publico/ciudadano, publico/tramite, publico/normativa

### Lo que le preocupa a la sala
- **Presupuesto:** ejecutar el presupuesto aprobado del año, con el equipo que ya tienen.
- **Meta del trimestre:** las metas del plan de desarrollo o del plan institucional.
- **KPI prometido al jefe:** tiempo de respuesta a un trámite, trámites en línea, satisfacción del ciudadano.

### Vocabulario público de KPI (nombres, sin cifras)
Tiempo de respuesta a un trámite · trámites disponibles en línea · peticiones resueltas a tiempo · ejecución
presupuestal · satisfacción del ciudadano · cumplimiento de metas del plan.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Trámites", "¿Revisar que el trámite llegue completo desde el primer día?", "Respuesta en menos días"]` · retorno
2. `["Peticiones", "¿Clasificar cada petición y enviarla al área que responde?", "Peticiones a tiempo"]` · retorno
3. `["Documentos", "¿Resumir la norma y el expediente para quien decide?", "Menos tiempo de lectura"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del ciudadano entre entidades?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`publico/edificio` · `publico/ciudadano` · `publico/tramite` · `publico/normativa` · genéricos: `generico/documento`,
`generico/reloj`, `generico/check`.

### Palabras que no van
«corrupción», «ineficiencia del Estado», «burocracia», nombres de funcionarios o de partidos, opiniones políticas,
contratos o licitaciones concretas, precios, «garantiza».

### Dónde buscar lo público
Su sitio (la entidad, transparencia, noticias), el plan de desarrollo o institucional, los informes de gestión y los
datos abiertos del gobierno (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Tiempo de respuesta a un trámite:** días hábiles desde la radicación hasta la respuesta.
- **Trámites disponibles en línea:** trámites que el ciudadano completa sin ir a una oficina, frente al total.
- **Peticiones resueltas a tiempo:** peticiones respondidas dentro del plazo de ley, frente a las recibidas.
- **Satisfacción del ciudadano:** lo que dice el ciudadano después de un trámite, en la escala de la entidad.
- **Ejecución presupuestal:** lo ejecutado frente a lo apropiado en el período (nunca con cifra sin fuente).

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Revisar que el trámite llegue completo desde el primer día podría responder en menos días.
2. Clasificar cada petición y enviarla al área que responde podría cumplir los plazos.
3. Resumir la norma y el expediente para quien decide podría ahorrar tiempo de lectura.
4. Un solo dato del ciudadano entre entidades podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La contratación pública tarda.» → Por eso conviene saber antes qué se quiere contratar. ¿Qué pregunta aclararía un discovery corto?
- «La norma no contempla la IA.» → ¿Qué tarea interna de lectura o clasificación no decide nada por el ciudadano y podría probarse primero?
- «El cambio de administración lo frena todo.» → ¿Qué resultado visible para el ciudadano cabe dentro de este período?

## consumo

label: Consumo masivo
keywords: consumo masivo, bebidas, alimentos, snacks, cuidado personal, productos de consumo, marcas, portafolio de marcas, canal tradicional, tenderos, distribuidores, anaquel, sell out, sell in, empaque, empaques, embotelladora, lácteos, cervecería, consumidores
icons: consumo/empaque, consumo/anaquel, consumo/marca, consumo/demanda

### Lo que le preocupa a la sala
- **Presupuesto:** la inversión en trade marketing y el costo de llegar a cada punto de venta.
- **Meta del trimestre:** volumen vendido y cobertura en el canal tradicional.
- **KPI prometido al jefe:** participación de mercado, disponibilidad en anaquel, precisión del pronóstico.

### Vocabulario público de KPI (nombres, sin cifras)
Participación de mercado · cobertura numérica · disponibilidad en anaquel · precisión del pronóstico de demanda ·
días de inventario · retorno de la inversión en trade (se dice «qué rindió la inversión», nunca ROI).

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Demanda", "¿Pronosticar cada semana lo que pedirá cada canal?", "Menos agotados"]` · retorno
2. `["Punto de venta", "¿Sugerir al vendedor qué ofrecer en cada tienda?", "Más cobertura"]` · retorno
3. `["Trade", "¿Saber qué actividad rindió antes de repetirla?", "Inversión mejor usada"]` · retorno
4. `["Datos y tecnología", "¿Unir los datos de venta propia y del canal?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`consumo/empaque` · `consumo/anaquel` · `consumo/marca` · `consumo/demanda` · genéricos: `generico/dato`,
`generico/meta`, `generico/equipo`.

### Palabras que no van
«guerra de precios», «marcas que pierden», precios o descuentos, nombres de sus distribuidores o de las cadenas que les
compran, «ROI», «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, marcas, sostenibilidad, sala de prensa), el informe anual, el gremio de alimentos o bebidas de su
país y las estadísticas oficiales de consumo (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Disponibilidad en anaquel:** puntos de venta donde el producto está en el estante cuando el comprador lo busca.
- **Precisión del pronóstico de demanda:** qué tan cerca estuvo lo pronosticado de lo vendido.
- **Cobertura numérica:** puntos de venta donde está el producto, frente al total del canal.
- **Días de inventario:** días de venta que cubre el inventario disponible.
- **Participación de mercado:** lo que vende la marca frente al total de su categoría, según una fuente pública o sindicada.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Pronosticar cada semana lo que pedirá cada canal podría reducir los agotados.
2. Sugerir al vendedor qué ofrecer en cada tienda podría ampliar la cobertura.
3. Saber qué actividad de trade rindió antes de repetirla podría usar mejor la inversión.
4. Unir los datos de venta propia y del canal podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Los datos del canal no son nuestros.» → ¿Qué parte sí lo es, y qué pregunta respondería sola?
- «El pronóstico ya lo hace planeación.» → ¿Con qué frecuencia se ajusta cuando cambia la demanda? Ahí podría estar la diferencia.
- «Trade marketing trabaja con su experiencia y le va bien.» → ¿Qué actividad repetirían con más confianza si supieran antes cuál rindió?

## logistica

label: Logística
keywords: logística, logístico, transporte de carga, carga, despacho, despachos, bodega, bodegas, almacenamiento, centro de distribución, flota, camiones, rutas, última milla, entregas, trazabilidad, envíos, paquetería, operador logístico, cadena de suministro, guías
icons: logistica/camion, logistica/bodega, logistica/ruta, logistica/caja

### Lo que le preocupa a la sala
- **Presupuesto:** el costo por entrega y por kilómetro, y las horas extra de bodega.
- **Meta del trimestre:** entregas a tiempo en la temporada alta y los clientes nuevos que llegan.
- **KPI prometido al jefe:** entregas a tiempo y completas, saber dónde está cada despacho, reclamos por novedad.

### Vocabulario público de KPI (nombres, sin cifras)
Entregas a tiempo y completas (OTIF) · trazabilidad del despacho · costo por entrega · ocupación de la flota ·
exactitud del inventario · tiempo de preparación del pedido · novedades por cada cien entregas.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Despachos", "¿Avisar al cliente antes de que el despacho se retrase?", "Menos reclamos"]` · retorno
2. `["Rutas", "¿Reordenar la ruta del día cuando algo cambia?", "Más entregas a tiempo"]` · retorno
3. `["Bodega", "¿Preparar primero el pedido que sale primero?", "Pedidos listos antes"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del despacho, de la bodega a la entrega?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`logistica/camion` · `logistica/bodega` · `logistica/ruta` · `logistica/caja` · genéricos: `generico/reloj`,
`generico/alerta`, `generico/dato`.

### Palabras que no van
«mercancía perdida», «robos», «retrasos por culpa de», nombres de sus clientes o de sus transportadores aliados,
tarifas de flete (son precios), «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, servicios, sala de prensa), el ministerio de transporte de su país, el gremio logístico y los
índices públicos de desempeño logístico (cifras con entidad y fecha).

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Entregas a tiempo y completas (OTIF):** entregas que llegan en la fecha y con todo lo pedido, frente al total.
- **Trazabilidad del despacho:** despachos que se pueden seguir en línea de la bodega a la entrega.
- **Novedades por cada cien entregas:** entregas con un problema (dirección, faltante, daño) por cada cien.
- **Tiempo de preparación del pedido:** horas desde que entra el pedido hasta que sale de la bodega.
- **Ocupación de la flota:** capacidad usada de cada vehículo, frente a la disponible.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Avisar al cliente antes de que el despacho se retrase podría reducir los reclamos.
2. Reordenar la ruta del día cuando algo cambia podría sumar entregas a tiempo.
3. Preparar primero el pedido que sale primero podría tener los pedidos listos antes.
4. Un solo dato del despacho, de la bodega a la entrega, podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Nuestros márgenes no dan para tecnología nueva.» → Por eso el criterio: solo se construye si hay retorno claro. ¿Qué novedad de entrega les pesa más cada semana?
- «Los conductores no usan aplicaciones nuevas.» → ¿Y si el cambio es en la oficina y el conductor solo recibe una ruta mejor?
- «El cliente final no ve la diferencia.» → ¿Qué pasaría si el aviso llegara antes que la queja?

## formacion

label: Formación
icons: generico/equipo, generico/documento, generico/meta, generico/check

La sala: el área de aprendizaje de una empresa, una academia corporativa o una institución que forma personas.

### Lo que le preocupa a la sala
- **Presupuesto:** el costo de cada persona formada y las horas que pasa fuera de su puesto.
- **Meta del trimestre:** que los participantes terminen su ruta y apliquen lo aprendido.
- **KPI prometido al jefe:** tasa de finalización, aplicación en el puesto, tiempo hasta la autonomía de un nuevo ingreso.

### Vocabulario público de KPI (nombres, sin cifras)
Tasa de finalización · aplicación en el puesto · tiempo hasta la autonomía · horas de formación por persona ·
satisfacción del participante · cobertura de la ruta de aprendizaje.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Rutas", "¿Armar la ruta de cada persona según su rol y lo que ya sabe?", "Menos horas repetidas"]` · retorno
2. `["Práctica", "¿Un caso de práctica con el trabajo real de cada participante?", "Más aplicación en el puesto"]` · retorno
3. `["Seguimiento", "¿Avisar a tiempo a quien podría no terminar?", "Más participantes que terminan"]` · retorno
4. `["Datos y tecnología", "¿Un solo registro de lo que cada persona aprendió?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`generico/equipo` · `generico/documento` · `generico/meta` · `generico/check` (el vertical aún no tiene set propio).

### Palabras que no van
«clases» y «alumnos» cuando la sala es corporativa (se dice «sesión» y «participantes»), «como vimos», «en la clase
anterior», nombres de participantes, notas o evaluaciones de personas, «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (academia, oferta de programas), el informe de gestión o de sostenibilidad (horas de formación), el
ministerio de educación o de trabajo de su país y los gremios de talento humano (cifras con entidad y fecha).

### Palabras para detectar el vertical
Aún no van en el frontmatter: `intake.py selftest` espera los doce verticales que ya detecta. Cuando se
amplíe, estas son las palabras (se cruzan con otras fichas: revísalas antes de sumarlas):
formación, capacitación, academia corporativa, aprendizaje, ruta de aprendizaje, programa de formación, curso, cursos,
participantes, talento humano, entrenamiento, universidad corporativa.

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Tasa de finalización:** participantes que terminan la ruta, frente a los inscritos.
- **Aplicación en el puesto:** lo que el participante usa en su trabajo después, según su jefe o su propio reporte.
- **Tiempo hasta la autonomía:** desde el ingreso hasta que la persona trabaja sin acompañamiento.
- **Horas de formación por persona:** horas dedicadas a aprender en el período.
- **Satisfacción del participante:** lo que dice el participante al terminar, en la escala del área.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Armar la ruta de cada persona según su rol y lo que ya sabe podría ahorrar horas repetidas.
2. Un caso de práctica con el trabajo real de cada participante podría llevar más aprendizaje al puesto.
3. Avisar a tiempo a quien podría no terminar podría sumar participantes que terminan.
4. Un solo registro de lo que cada persona aprendió podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «La gente no tiene tiempo para formarse.» → ¿Y si la práctica es su trabajo de la semana, no una tarea aparte?
- «Ya tenemos una plataforma de aprendizaje.» → ¿Qué pasa después del curso? La pregunta es cuánto de lo aprendido llega al puesto.
- «La formación no se puede medir.» → ¿Qué cambio en el trabajo notaría un jefe al mes? Ese podría ser el indicador.

## farmacia

label: Farmacia
icons: salud/medicamento, retail/tienda, generico/dato, generico/reloj

La sala: una cadena de farmacias, un gestor farmacéutico o un laboratorio con red de distribución.

### Lo que le preocupa a la sala
- **Presupuesto:** el inventario inmovilizado y el producto que vence antes de salir.
- **Meta del trimestre:** medicamentos disponibles en cada punto y fórmulas entregadas completas.
- **KPI prometido al jefe:** faltantes, producto vencido, tiempo de dispensación.

### Vocabulario público de KPI (nombres, sin cifras)
Disponibilidad de medicamentos · faltantes · producto vencido · rotación de inventario · tiempo de dispensación ·
fórmulas completas entregadas · adherencia del paciente.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Inventario", "¿Pedir a tiempo lo que cada punto va a dispensar?", "Menos faltantes"]` · retorno
2. `["Vencimientos", "¿Mover antes el lote que está por vencer?", "Menos producto vencido"]` · retorno
3. `["Atención", "¿Responder la consulta repetida con lo que ya se sabe?", "Atención en menos tiempo"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato de inventario, punto y fórmula?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`salud/medicamento` · `retail/tienda` · `generico/dato` · `generico/reloj` (el vertical aún no tiene set propio).

### Palabras que no van
«automedicación», recomendar un medicamento, datos de pacientes o de fórmulas (ni uno), nombres de laboratorios o de
proveedores, «diagnóstico automático», «garantiza», «transformación».

### Dónde buscar lo público
Su sitio (nosotros, sala de prensa), el informe anual, la agencia sanitaria o reguladora de medicamentos de su país y
los gremios farmacéuticos (cifras con entidad y fecha).

### Palabras para detectar el vertical
Aún no van en el frontmatter: `intake.py selftest` espera los doce verticales que ya detecta. Cuando se
amplíe, estas son las palabras (se cruzan con otras fichas: revísalas antes de sumarlas):
farmacia, farmacias, droguería, droguerías, farmacéutica, farmacéutico, dispensación, medicamentos, fórmula médica,
laboratorio farmacéutico, gestor farmacéutico, cadena de farmacias.

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Faltantes:** fórmulas o pedidos que no se entregan completos por falta de producto.
- **Producto vencido:** unidades que vencen antes de venderse o dispensarse.
- **Tiempo de dispensación:** desde que llega la fórmula hasta que el paciente recibe el medicamento.
- **Rotación de inventario:** veces que el inventario se vende y se repone en el período.
- **Fórmulas completas entregadas:** fórmulas entregadas con todo lo prescrito en una sola visita, frente al total.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Pedir a tiempo lo que cada punto va a dispensar podría reducir los faltantes.
2. Mover antes el lote que está por vencer podría bajar el producto vencido.
3. Responder la consulta repetida con lo que ya se sabe podría atender en menos tiempo.
4. Un solo dato de inventario, punto y fórmula podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Lo regulatorio no deja espacio para probar.» → ¿Qué proceso de inventario o de logística no toca la decisión clínica y podría probarse primero?
- «El químico farmacéutico ya sabe qué pedir.» → Sin duda. ¿Cuánto de su tiempo se va en contar y pedir en vez de atender?
- «Nuestros puntos tienen sistemas distintos.» → ¿Qué pregunta de inventario respondería primero un dato unido de pocos puntos?

## fidelizacion

label: Fidelización
icons: retail/lealtad, retail/bolsa, generico/equipo, generico/dato

La sala: un programa de lealtad o de puntos, propio de una marca o de una coalición de comercios aliados.

### Lo que le preocupa a la sala
- **Presupuesto:** lo que cuestan los puntos que se emiten y los que se redimen.
- **Meta del trimestre:** socios activos y aliados que venden más gracias al programa.
- **KPI prometido al jefe:** socios activos, tasa de redención, frecuencia de acumulación.

### Vocabulario público de KPI (nombres, sin cifras)
Socios activos · tasa de redención · frecuencia de acumulación · puntos por vencer · comercios aliados activos ·
satisfacción del socio.

### Cuatro semillas de hipótesis (3 de retorno + 1 habilitador)
Formato de la tarjeta de `hypotheses-live`: `[área, qué podría hacer la IA (con «?»), retorno posible]`.
1. `["Socios", "¿Una oferta distinta para cada socio, cuando compra?", "Socios que vuelven"]` · retorno
2. `["Aliados", "¿Mostrar a cada aliado qué campaña le rindió?", "Aliados más activos"]` · retorno
3. `["Redención", "¿Recordar a tiempo los puntos por vencer?", "Más redención"]` · retorno
4. `["Datos y tecnología", "¿Un solo dato del socio entre todos los aliados?", "Habilitador de las otras tres"]` · habilitador

### Íconos (assets/scenes/icons.py)
`retail/lealtad` · `retail/bolsa` · `generico/equipo` · `generico/dato` (el vertical aún no tiene set propio).

### Palabras que no van
datos personales de socios (ni uno), nombres de aliados sin su permiso, «puntos gratis», «regalar puntos», «garantiza»,
«transformación».

### Dónde buscar lo público
Su sitio (cómo funciona, aliados), el informe de sostenibilidad, la autoridad de protección de datos y de protección
al consumidor de su país y los gremios de comercio (cifras con entidad y fecha).

### Palabras para detectar el vertical
Aún no van en el frontmatter: `intake.py selftest` espera los doce verticales que ya detecta. Cuando se
amplíe, estas son las palabras (se cruzan con otras fichas: revísalas antes de sumarlas):
fidelización, lealtad, programa de lealtad, programa de puntos, puntos, acumular puntos, redimir, redención, socios,
aliados, coalición, recompensas.

### KPI típicos
Solo nombres y qué miden; la cifra, si llega, es un hecho confirmado en `facts.json`.
- **Socios activos:** socios que acumularon o redimieron en el período, frente a los inscritos.
- **Tasa de redención:** puntos redimidos frente a los emitidos.
- **Frecuencia de acumulación:** veces que un socio acumula en el período.
- **Puntos por vencer:** puntos que vencen pronto sin haberse usado.
- **Comercios aliados activos:** aliados que emitieron o redimieron puntos en el período.

### Semillas de hipótesis
Se dicen como hipótesis por validar en el discovery, nunca como diagnóstico.
1. Una oferta distinta para cada socio, en el momento en que compra, podría traer socios que vuelven.
2. Mostrar a cada comercio aliado qué campaña le rindió podría tener aliados más activos.
3. Recordar a tiempo los puntos por vencer, con una opción útil, podría aumentar la redención.
4. Un solo dato del socio entre todos los aliados podría habilitar las otras tres ideas.

### Objeciones típicas
Se responden con una pregunta o un contraste que deja pensando; nunca con presión ni urgencia.
- «Nuestros aliados no comparten sus datos.» → ¿Qué podría mostrarles el programa con sus propios datos, que los anime a compartir más?
- «La personalización ya la hacemos por segmentos.» → ¿Qué oferta del último mes les llegó igual a socios que compran distinto?
- «La privacidad del socio es lo primero.» → Para nosotros también. ¿Qué idea funciona con datos agregados y sin un solo dato personal?
