# Biblioteca de KPI por vertical

Solo nombres, unidad y dirección. **Nunca una cifra:** una cifra llega a una diapositiva solo como hecho confirmado
(`facts.json`, `facts.py confirm`) con su fuente. Dirección: ↑ = mejor si sube · ↓ = mejor si baja.

Uso: el KPI de un caso de éxito (`args.kpi` de `success-case`) y el KPI que se acuerda en el discovery (`discovery`,
arg `kpi`) salen de aquí, dichos en palabras del cliente: «KPI · menos paradas no planeadas». Un caso de éxito dice
indicador, de cuánto a cuánto, dueño y fecha; si no hay cifra confirmada, no es un caso de éxito.

| Vertical | KPI | Unidad | Dirección |
|---|---|---|---|
| banca | Tiempo de aprobación de un crédito | horas o días | ↓ |
| banca | Cartera vencida | % de la cartera | ↓ |
| banca | Clientes digitales activos | clientes | ↑ |
| banca | Tiempo de respuesta a un reclamo | días | ↓ |
| seguros | Tiempo de liquidación de un siniestro | días | ↓ |
| seguros | Tasa de renovación | % de pólizas | ↑ |
| seguros | Índice de siniestralidad | % de las primas | ↓ |
| seguros | Satisfacción del asegurado | puntos NPS | ↑ |
| salud | Tiempo de espera para una cita | días | ↓ |
| salud | Tasa de inasistencia | % de citas | ↓ |
| salud | Reingresos evitables | % de egresos | ↓ |
| salud | Tiempo del profesional con el paciente | minutos por consulta | ↑ |
| energia | Paradas no planeadas | paradas por mes | ↓ |
| energia | Disponibilidad de activos | % del tiempo | ↑ |
| energia | Tiempo medio entre fallas | horas | ↑ |
| energia | Cumplimiento del plan de mantenimiento | % de órdenes | ↑ |
| mineria | Disponibilidad de flota | % del tiempo | ↑ |
| mineria | Recuperación metalúrgica | % | ↑ |
| mineria | Costo por tonelada movida | moneda por tonelada (nunca en el deck) | ↓ |
| mineria | Índice de frecuencia de incidentes | incidentes por millón de horas | ↓ |
| retail | Agotados en góndola | % de referencias | ↓ |
| retail | Ticket promedio | moneda por compra (nunca en el deck) | ↑ |
| retail | Rotación de inventario | veces por año | ↑ |
| retail | Frecuencia de compra | compras por cliente al mes | ↑ |
| pagos | Comercios activos | comercios | ↑ |
| pagos | Tasa de aprobación | % de transacciones | ↑ |
| pagos | Tiempo de afiliación de un comercio | días | ↓ |
| pagos | Tiempo de resolución de un ticket | horas | ↓ |
| telco | Clientes que se van | % por mes | ↓ |
| telco | Disponibilidad de la red | % del tiempo | ↑ |
| telco | Instalaciones a tiempo | % de órdenes | ↑ |
| telco | Visitas técnicas repetidas | % de visitas | ↓ |
| industria | Eficiencia general de los equipos (OEE) | % | ↑ |
| industria | Paradas no planeadas | horas por mes | ↓ |
| industria | Producto no conforme | % de lo producido | ↓ |
| industria | Cumplimiento del plan de producción | % | ↑ |
| publico | Tiempo de respuesta a un trámite | días hábiles | ↓ |
| publico | Trámites disponibles en línea | % de trámites | ↑ |
| publico | Peticiones resueltas a tiempo | % | ↑ |
| publico | Satisfacción del ciudadano | puntos | ↑ |
| consumo | Disponibilidad en anaquel | % de puntos de venta | ↑ |
| consumo | Precisión del pronóstico de demanda | % | ↑ |
| consumo | Cobertura numérica | % de puntos de venta | ↑ |
| consumo | Días de inventario | días | ↓ |
| logistica | Entregas a tiempo y completas (OTIF) | % de entregas | ↑ |
| logistica | Despachos con trazabilidad en línea | % de despachos | ↑ |
| logistica | Novedades por cada cien entregas | novedades | ↓ |
| logistica | Tiempo de preparación del pedido | horas | ↓ |
| todos | Tiempo del equipo en tareas repetitivas | horas por semana | ↓ |
| todos | Tiempo de entrega de software | días del requerimiento al despliegue | ↓ |

Una unidad de moneda nunca se muestra con un número en el deck: el gate de página falla un precio (`forbid_visible`).
