# PROJECT.md — especificación

## Qué es

El archivo raíz nombrado como el proyecto (ej. `COLSANITAS.md`, `ZEN.md`). Inspirado en el concepto "soul.md" descrito en la transcripción de [referencias/soul-md-transcripcion.md](referencias/soul-md-transcripcion.md): un volcado exhaustivo de todo el contexto que el humano tiene sobre el proyecto — reuniones, decisiones, manifiestos, notas sueltas — sin estructura forzada en el momento de escribir.

Es, por diseño, el archivo con el que el humano interactúa más. Es su braindump. Cuanta más información capture, mejor alimenta las decisiones futuras del agente.

## Quién escribe qué

- **El humano** es prácticamente el único que aporta contenido nuevo a `PROJECT.md`. Escribe como piensa, sin preocuparse por el orden.
- **El agente no añade contenido propio a `PROJECT.md` por iniciativa propia.** Puede hacerlo solo si el humano se lo pide explícitamente (ej. "anota en el PROJECT.md que decidimos X").
- **El agente sí puede reorganizar** `PROJECT.md` cuando el humano lo solicita (workflow "organizar", ver [01-invocacion-y-workflows.md](01-invocacion-y-workflows.md)) — con una regla no negociable:

> Reorganizar es ordenar, categorizar y hacer housekeeping. **Nunca es eliminar ni resumir contenido.** Si dos entradas parecen contradecirse, ambas se conservan, una junto a la otra o con una nota que señale la contradicción — no se decide cuál es la "correcta" sin preguntar al humano.

Se descartó explícitamente un sistema de etiquetas `origen: humano | agente` / `estado: activo | superado` por sobre-ingeniería: casi todo el contenido es humano, así que la etiqueta no aportaba señal suficiente para justificar el costo de mantenerla en cada entrada.

## Por qué existe el workflow "organizar" y no reglas de tagging por entrada

El riesgo real que motivó esta discusión es *context attention*: contenido desactualizado o mal ordenado compite por atención con contenido vigente y degrada la calidad de todo lo que el agente infiere del archivo. La solución elegida no es prevenir el desorden con reglas de escritura estrictas (que nadie sigue de forma consistente sesión tras sesión), sino aceptar que el desorden va a pasar y dar una herramienta explícita, pedida por el humano, para resolverlo periódicamente — igual que uno ordena un cajón de vez en cuando en lugar de forzarse a nunca desordenarlo.

## Relación con los archivos derivados

`PRODUCT.md`, `DESIGN.md` y `ENGINEER.md` son recortes de `PROJECT.md`, mantenidos únicamente por el agente (ver [04](04-engineer-md-especificacion.md), [05](05-design-md-especificacion.md)). El mecanismo de sincronización:

- Ocurre en el workflow **update**, no en "organizar" ni en "init" únicamente.
- El agente lee `PROJECT.md` completo (o las entradas nuevas desde la última sincronización, si el archivo ya es grande) y decide qué información pertenece a cada derivado, según el alcance definido de cada uno.
- El humano no edita los derivados a mano — si lo hace, esa edición puede perderse en la próxima sincronización. Esto debe advertirse en el propio archivo derivado (un comentario al inicio: "Este archivo es generado y mantenido por el agente a partir de PROJECT.md — no editar directamente").

## Riesgo de tamaño y ruido en diffs

Un archivo que crece indefinidamente con cada sesión genera diffs grandes y difíciles de revisar en PRs, y eventualmente se vuelve pesado de leer completo en cada sincronización.

Mitigación sugerida (no implementada, sin pilotar): cuando `PROJECT.md` supere un umbral razonable (a definir empíricamente, ej. ~500-800 líneas), el workflow "organizar" puede proponer mover secciones cerradas/antiguas a un archivo de historial aparte (`PROJECT-HISTORIAL.md`), siempre con la misma regla de no pérdida de información y siempre a propuesta explícita, nunca automática y silenciosa.

## Abierto / sin pilotar

- No hay evidencia real de en qué punto un `PROJECT.md` se vuelve difícil de navegar para el agente. El umbral de tamaño es una suposición.
- No se ha probado el workflow "organizar" contra un archivo con contradicciones reales entre entradas humanas — falta validar que la regla de "conservar ambas y señalar la contradicción" sea la mejor UX o si termina siendo ruidosa.
