---
name: project-doc
description: Genera y mantiene la documentación estructural de un proyecto (CLAUDE.md, AGENTS.md, PROJECT.md, PRODUCT.md, DESIGN.md, ENGINEER.md, taxonomía de docs/, INDEX.md por carpeta). Úsala cuando el usuario pida iniciar la documentación de un proyecto nuevo o existente ("monta la documentación de este repo", "necesito un CLAUDE.md/AGENTS.md"), cuando pida refrescar los archivos derivados a partir de PROJECT.md ("actualiza los docs con lo que hicimos"), o cuando pida poner en orden PROJECT.md ("el PROJECT.md está muy desordenado, organízalo"). Funciona igual en Claude Code y en Codex CLI.
---

# project-doc

Skill de una sola entrada con tres workflows reconocidos por intención, no por subcomando literal. Todo el detalle vive en `reference/` — este archivo es solo el índice (progressive disclosure, ver [reference/09-arquitectura-de-la-skill.md](reference/09-arquitectura-de-la-skill.md)).

## Cómo decidir el workflow

| Señal en la petición del usuario | Workflow | Detalle |
|---|---|---|
| No existe `PROJECT.md`/`AGENTS.md`/`CLAUDE.md`, o pide arrancar documentación desde cero | **init** | [reference/08-cuestionario-init.md](reference/08-cuestionario-init.md), [reference/02-agents-claude-md-canon.md](reference/02-agents-claude-md-canon.md), [reference/06-taxonomia-docs.md](reference/06-taxonomia-docs.md), [reference/07-index-md-especificacion.md](reference/07-index-md-especificacion.md) |
| Ya existe la estructura; pide refrescar `PRODUCT.md`/`DESIGN.md`/`ENGINEER.md`, o el agente detecta código nuevo sin reflejo en los docs | **update** | [reference/03-project-md-especificacion.md](reference/03-project-md-especificacion.md), [reference/04-engineer-md-especificacion.md](reference/04-engineer-md-especificacion.md), [reference/05-design-md-especificacion.md](reference/05-design-md-especificacion.md) |
| Pide poner en orden `PROJECT.md` | **organizar** | [reference/03-project-md-especificacion.md](reference/03-project-md-especificacion.md) |

Antes de actuar, cargar [reference/01-invocacion-y-workflows.md](reference/01-invocacion-y-workflows.md) completo — define matices de cada workflow.

## Qué hace `init`, paso a paso

`init` no es solo generar archivos raíz — arma la estructura documental completa del proyecto en un solo paso:

1. Corre el cuestionario ([reference/08](reference/08-cuestionario-init.md)): nombre/propósito, stack, etapa (greenfield vs. existente), reglas operativas.
2. Crea `CLAUDE.md` y `AGENTS.md` espejo ([reference/02](reference/02-agents-claude-md-canon.md)).
3. Crea `ENGINEER.md` ([reference/04](reference/04-engineer-md-especificacion.md)) y `DESIGN.md` ([reference/05](reference/05-design-md-especificacion.md)) — vacíos o mínimos si el proyecto es greenfield, poblados por inferencia del código si ya existe.
4. Crea `PROJECT.md` — vacío con nota de invitación al braindump si es greenfield; poblado por inferencia inicial (marcada como borrador a validar) si el proyecto ya tiene historia ([reference/03](reference/03-project-md-especificacion.md)).
5. **Crea el árbol de carpetas de `docs/`** con la taxonomía estándar — `docs/adrs/`, `docs/slices/`, `docs/design/`, `docs/ideas/`, `docs/qa/` ([reference/06](reference/06-taxonomia-docs.md)) — no solo las menciona, las crea en el filesystem, cada una con su propio `INDEX.md` mínimo.
6. Crea `INDEX.md` en la raíz del repo ([reference/07](reference/07-index-md-especificacion.md)).

Ningún paso de esta lista es opcional dentro de `init` — si el proyecto ya tiene alguna pieza (ej. ya existe `docs/adrs/`), ese paso se salta para esa pieza puntual, pero el resto se completa igual.

## Regla de espejo CLAUDE.md / AGENTS.md

`CLAUDE.md` y `AGENTS.md` **no tienen que ser idénticos en todo momento**. El usuario puede personalizar uno sin el otro después de creados — eso es válido y esperado.

- **`init`**: crea ambos archivos con contenido idéntico (ver [reference/02-agents-claude-md-canon.md](reference/02-agents-claude-md-canon.md)).
- **`update`**: antes de tocar cualquiera de los dos, comparar su contenido actual. Si difieren, **no igualarlos por defecto** — señalar la diferencia al usuario explícitamente y preguntar qué hacer (llevar ambos al mismo contenido, o mantener la divergencia y solo actualizar lo que corresponde a cada uno). Solo se igualan si el usuario lo pide en esa misma interacción.
- **`organizar`**: no aplica a estos archivos, es exclusivo de `PROJECT.md`.
- Nunca sobrescribir uno de los dos en silencio. La divergencia es información (alguien lo personalizó a propósito), no un error a corregir automáticamente.

## Archivos que esta skill produce en el proyecto destino

```
PROJECT.md          (o <NOMBRE-PROYECTO>.md) — solo lo escribe el humano, ver reference/03
CLAUDE.md            — ver reference/02, regla de espejo arriba
AGENTS.md            — ver reference/02, regla de espejo arriba
ENGINEER.md          — derivado, solo el agente, ver reference/04
DESIGN.md            — derivado, solo el agente, ver reference/05
PRODUCT.md           — derivado, solo el agente (recorte de producto de PROJECT.md)
INDEX.md             — raíz + uno por carpeta de docs/, ver reference/07
docs/
  adrs/  slices/  design/  ideas/  qa/    — ver reference/06 (taxonomía completa)
```

## Estado

Diseño documentado y validado por discusión; **sin pilotar aún en un proyecto real**. Ver "Abierto / sin pilotar" en cada archivo de `reference/` antes de tratar cualquier regla como definitiva. Ver [README.md](../README.md) del repo para el estado general del proyecto.
