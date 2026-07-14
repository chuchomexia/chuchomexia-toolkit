# Taxonomía de `docs/`

Basada en la estructura real usada en Colsanitas (ver `../04-estructura-del-repo.md` del paquete metodológico general), corregida con lo aprendido de qué funcionó y qué no.

| Carpeta | Qué contiene | Absorbe / reemplaza | Razón |
|---|---|---|---|
| `adrs/` | Toda decisión con trade-offs: arquitectura, seguridad, deuda técnica aceptada. Deuda técnica se registra como un ADR más (prefijo o etiqueta), no como carpeta aparte. | `security/`, `criteria/`, `decisions/` | Los tres eran el mismo concepto (decisión + justificación) con nombres distintos — generaban duda sobre dónde escribir cada cosa. |
| `slices/` | Salida de cada slice de specs-driven development: qué se especificó, qué se construyó, qué cambió del plan original. | `brief/` (renombrado) | `brief/` había terminado siendo esto en la práctica; el nombre nuevo refleja lo que realmente contiene. |
| `design/` | Visual + producto de diseño: wireframes, prototipos, referencias, preguntas abiertas — insumos que alimentan `DESIGN.md`. | `prototipo/` | Tener wireframes y prototipos en carpetas separadas fragmentaba el material de una misma decisión de diseño. |
| `ideas/` | Backlog puro de ideas futuras, fuera del camino crítico. Sin deuda técnica (esa va a `adrs/`). | — | En Colsanitas terminó mezclando backlog con deuda técnica; se separa para que cada una tenga un lugar inequívoco. |
| `qa/` | Evidencia mínima curada: casos de prueba, contradicciones HU vs. realidad, videos solo si aportan evidencia concreta. | — | Se mantiene, pero se recorta: en Colsanitas se salió de control por falta de un criterio de qué entra y qué no. |

## Se eliminan de la plantilla base

- **`contracts/`** — nadie en el equipo recordaba su propósito original al momento de esta retrospectiva. Señal clara de que no aportó findability y no debe replicarse.
- **`security/`** — se fusiona en `adrs/` (ver arriba).
- **`superpowers/`** — es un artefacto de ejecución de un proyecto específico, no una carpeta de metodología. No se replica en proyectos nuevos.

## Regla general

Cada carpeta de `docs/` lleva su propio `INDEX.md` (ver [07-index-md-especificacion.md](07-index-md-especificacion.md)), bajo 200 líneas. No se crean carpetas nuevas fuera de esta lista sin una razón documentada — la lección de `contracts/` es que una carpeta sin propósito claro y sin uso constante es peor que no tenerla.

## Abierto / sin pilotar

- Esta taxonomía nunca se ha aplicado desde cero a un proyecto nuevo — solo se ha reconstruido retrospectivamente sobre lo que pasó en Colsanitas. Falta validar que cubra necesidades reales de un proyecto distinto (ej. uno sin flujo de carga de datos ni certificados, donde `slices/` o `adrs/` puedan necesitar ajuste).
