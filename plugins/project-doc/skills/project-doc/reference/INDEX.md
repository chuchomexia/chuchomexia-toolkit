# reference/

## Qué contiene

Especificación completa de la skill `project-doc`: los tres workflows (init/update/organizar), el esqueleto de `CLAUDE.md`/`AGENTS.md`, la especificación de `PROJECT.md` y sus derivados (`PRODUCT.md`, `DESIGN.md`, `ENGINEER.md`), la taxonomía de `docs/`, las reglas de `INDEX.md`, el cuestionario de `init` y la arquitectura de empaquetado de la skill.

`SKILL.md` (en la carpeta padre) es el punto de entrada delgado que remite aquí — este árbol es lo que se carga bajo demanda, no de una sola vez.

## Origen

Esta metodología nació documentando el proyecto Colsanitas/Tikka y se generalizó en conversación explícita para funcionar en cualquier proyecto. Todo lo aquí escrito nace de una sola sesión de diseño (incluyó una ronda de crítica brutal pedida explícitamente antes de continuar). Nada de esto se ha pilotado todavía en un proyecto real — ver "Abierto / sin pilotar" al final de cada archivo antes de tratar cualquier decisión como definitiva.

## Orden de lectura recomendado

1. [00-principios-context-engineering.md](00-principios-context-engineering.md) — por qué existe todo lo demás.
2. [01-invocacion-y-workflows.md](01-invocacion-y-workflows.md) — cómo se activa la skill (init / update / organizar).
3. [02-agents-claude-md-canon.md](02-agents-claude-md-canon.md) — esqueleto del archivo raíz, incluida la regla de espejo CLAUDE.md/AGENTS.md.
4. [03-project-md-especificacion.md](03-project-md-especificacion.md) — el archivo de contexto vivo, la pieza más nueva de esta metodología.
5. [04-engineer-md-especificacion.md](04-engineer-md-especificacion.md) y [05-design-md-especificacion.md](05-design-md-especificacion.md) — los dos derivados técnico/visual.
6. [06-taxonomia-docs.md](06-taxonomia-docs.md) — estructura de `docs/`.
7. [07-index-md-especificacion.md](07-index-md-especificacion.md) — reglas de `INDEX.md`.
8. [08-cuestionario-init.md](08-cuestionario-init.md) — las preguntas del workflow `init`.
9. [09-arquitectura-de-la-skill.md](09-arquitectura-de-la-skill.md) — cómo está empaquetado este mismo repo.

`referencias/` no es de lectura obligatoria — contiene el material fuente (transcripciones, un `AGENTS.md` de otro proyecto, notas de arquitectura de Impeccable) que alimentó las decisiones de los archivos 00–09. Consultar solo cuando un archivo de contenido remite a ella explícitamente.

## Reglas de uso

- Cada archivo de contenido termina, cuando aplica, con una sección "Abierto / sin pilotar" — léela antes de tratar cualquier decisión aquí como definitiva.
- Mantener esta carpeta corta y sin secretos.
- Cambios a esta especificación deben mantener consistencia entre archivos (ej. quién escribe `PROJECT.md` no puede contradecirse entre [01](01-invocacion-y-workflows.md) y [03](03-project-md-especificacion.md)).
