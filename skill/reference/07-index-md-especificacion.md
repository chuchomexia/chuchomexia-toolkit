# INDEX.md — especificación

## Regla general

Cada carpeta documental (raíz de `docs/` y cada subcarpeta de la taxonomía en [06-taxonomia-docs.md](06-taxonomia-docs.md)) tiene su propio `INDEX.md`, siempre bajo 200 líneas. Esta regla ya existe y está validada en Colsanitas — aquí solo se optimiza qué debe y no debe contener.

## INDEX.md raíz del repo

Es la entrada documental principal — no `README.md`. Orienta a agentes y humanos sobre qué leer primero. Contenido mínimo:

1. Una línea de propósito del repo.
2. Orden de lectura recomendado (típicamente: `AGENTS.md`/`CLAUDE.md` → `PROJECT.md`/`PRODUCT.md` según la tarea → `docs/<carpeta>` según el flujo afectado).
3. Mapa de un nivel de las carpetas principales (`app/`, `lib/`, `docs/`, etc.), una línea cada una — no una descripción exhaustiva.
4. Pointers a `NEXT_STEP.md` (o equivalente) si el proyecto lo usa.

## INDEX.md por carpeta de `docs/`

Debe responder, en este orden:

1. Qué contiene esta carpeta (una o dos líneas, no una definición larga).
2. Qué NO contiene — la lección de `contracts/` en [06-taxonomia-docs.md](06-taxonomia-docs.md) es que la ambigüedad de alcance mata a una carpeta con el tiempo. Ser explícito sobre el límite previene que se vuelva cajón de sastre.
3. Lista de archivos con una línea de descripción cada uno — no resúmenes de contenido.
4. Si la carpeta tiene un orden de lectura recomendado (como este mismo paquete metodológico), listarlo.

## Qué NO debe llevar un INDEX.md

- Contenido sustantivo (decisiones, contexto de dominio, especificaciones) — eso vive en los archivos que indexa, no en el índice.
- Historial de cambios o changelog — no es su función.
- Nada que dependa de mantenerse sincronizado con el detalle interno de cada archivo indexado, más allá del título/propósito — si el índice necesita actualizarse cada vez que cambia el contenido interno de un archivo, está haciendo demasiado.

## Por qué el límite de 200 líneas

No es arbitrario: un índice que necesita más de 200 líneas para orientar sobre una carpeta es señal de que la carpeta tiene demasiadas cosas sin categorizar, o de que el índice se está usando para contenido que no le corresponde. En ambos casos, la solución es reestructurar la carpeta o su taxonomía (ver [06](06-taxonomia-docs.md)), no alargar el índice.

## Abierto / sin pilotar

- No se ha probado el `INDEX.md` raíz en un proyecto donde la estructura de carpetas técnicas (no documentales) sea muy distinta a Next.js/App Router — el formato asume implícitamente esa forma de organizar código.
