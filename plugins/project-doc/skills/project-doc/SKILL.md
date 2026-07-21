---
name: project-doc
description: Genera y mantiene la documentaciÃ³n estructural de un proyecto (CLAUDE.md, AGENTS.md, PROJECT.md, PRODUCT.md, DESIGN.md, DESIGN.agent.md, ENGINEER.md, taxonomÃ­a de docs/, INDEX.md por carpeta). Ãšsala cuando el usuario pida iniciar la documentaciÃ³n de un proyecto nuevo o existente ("monta la documentaciÃ³n de este repo", "necesito un CLAUDE.md/AGENTS.md"), cuando pida refrescar los archivos derivados a partir de PROJECT.md ("actualiza los docs con lo que hicimos"), o cuando pida poner en orden PROJECT.md ("el PROJECT.md estÃ¡ muy desordenado, organÃ­zalo"). Funciona igual en Claude Code y en Codex CLI.
---

# project-doc

Skill de una sola entrada con tres workflows reconocidos por intenciÃ³n, no por subcomando literal. Todo el detalle vive en `reference/` â€” este archivo es solo el Ã­ndice (progressive disclosure, ver [reference/09-arquitectura-de-la-skill.md](reference/09-arquitectura-de-la-skill.md)).

## CÃ³mo decidir el workflow

| SeÃ±al en la peticiÃ³n del usuario | Workflow | Detalle |
|---|---|---|
| No existe `PROJECT.md`/`AGENTS.md`/`CLAUDE.md`, o pide arrancar documentaciÃ³n desde cero | **init** | [reference/08-cuestionario-init.md](reference/08-cuestionario-init.md), [reference/02-agents-claude-md-canon.md](reference/02-agents-claude-md-canon.md), [reference/06-taxonomia-docs.md](reference/06-taxonomia-docs.md), [reference/07-index-md-especificacion.md](reference/07-index-md-especificacion.md) |
| Ya existe la estructura; pide refrescar `PRODUCT.md`/`DESIGN.md`/`ENGINEER.md`, o el agente detecta cÃ³digo nuevo sin reflejo en los docs | **update** | [reference/03-project-md-especificacion.md](reference/03-project-md-especificacion.md), [reference/04-engineer-md-especificacion.md](reference/04-engineer-md-especificacion.md), [reference/05-design-md-especificacion.md](reference/05-design-md-especificacion.md) |
| Pide poner en orden `PROJECT.md` | **organizar** | [reference/03-project-md-especificacion.md](reference/03-project-md-especificacion.md) |

Antes de actuar, cargar [reference/01-invocacion-y-workflows.md](reference/01-invocacion-y-workflows.md) completo â€” define matices de cada workflow.

## QuÃ© hace `init`, paso a paso

`init` no es solo generar archivos raÃ­z â€” arma la estructura documental completa del proyecto en un solo paso:

1. Corre el cuestionario ([reference/08](reference/08-cuestionario-init.md)): nombre/propÃ³sito, stack, etapa (greenfield vs. existente), reglas operativas.
2. Crea `CLAUDE.md` y `AGENTS.md` espejo ([reference/02](reference/02-agents-claude-md-canon.md)).
3. Crea `ENGINEER.md` ([reference/04](reference/04-engineer-md-especificacion.md)), `DESIGN.md` y `DESIGN.agent.md` ([reference/05](reference/05-design-md-especificacion.md)) â€” vacÃ­os o mÃ­nimos si el proyecto es greenfield, poblados por inferencia del cÃ³digo si ya existe.
4. Crea `PROJECT.md` â€” vacÃ­o con nota de invitaciÃ³n al braindump si es greenfield; poblado por inferencia inicial (marcada como borrador a validar) si el proyecto ya tiene historia ([reference/03](reference/03-project-md-especificacion.md)).
5. **Crea el Ã¡rbol de carpetas de `docs/`** con la taxonomÃ­a estÃ¡ndar â€” `docs/adrs/`, `docs/slices/`, `docs/design/`, `docs/ideas/`, `docs/qa/` ([reference/06](reference/06-taxonomia-docs.md)) â€” no solo las menciona, las crea en el filesystem, cada una con su propio `INDEX.md` mÃ­nimo.
6. Crea `INDEX.md` en la raÃ­z del repo ([reference/07](reference/07-index-md-especificacion.md)).

NingÃºn paso de esta lista es opcional dentro de `init` â€” si el proyecto ya tiene alguna pieza (ej. ya existe `docs/adrs/`), ese paso se salta para esa pieza puntual, pero el resto se completa igual.

## Regla de espejo CLAUDE.md / AGENTS.md

`CLAUDE.md` y `AGENTS.md` **no tienen que ser idÃ©nticos en todo momento**. El usuario puede personalizar uno sin el otro despuÃ©s de creados â€” eso es vÃ¡lido y esperado.

- **`init`**: crea ambos archivos con contenido idÃ©ntico (ver [reference/02-agents-claude-md-canon.md](reference/02-agents-claude-md-canon.md)).
- **`update`**: antes de tocar cualquiera de los dos, comparar su contenido actual. Si difieren, **no igualarlos por defecto** â€” seÃ±alar la diferencia al usuario explÃ­citamente y preguntar quÃ© hacer (llevar ambos al mismo contenido, o mantener la divergencia y solo actualizar lo que corresponde a cada uno). Solo se igualan si el usuario lo pide en esa misma interacciÃ³n.
- **`organizar`**: no aplica a estos archivos, es exclusivo de `PROJECT.md`.
- Nunca sobrescribir uno de los dos en silencio. La divergencia es informaciÃ³n (alguien lo personalizÃ³ a propÃ³sito), no un error a corregir automÃ¡ticamente.

## Archivos que esta skill produce en el proyecto destino

```
PROJECT.md          (o <NOMBRE-PROYECTO>.md) â€” solo lo escribe el humano, ver reference/03
CLAUDE.md            â€” ver reference/02, regla de espejo arriba
AGENTS.md            â€” ver reference/02, regla de espejo arriba
ENGINEER.md          â€” derivado, solo el agente, ver reference/04
DESIGN.md            â€” resumen canónico visual, ver reference/05`r`nDESIGN.agent.md      â€” brief visual condicional para agentes, ver reference/05
PRODUCT.md           â€” derivado, solo el agente (recorte de producto de PROJECT.md)
INDEX.md             â€” raÃ­z + uno por carpeta de docs/, ver reference/07
docs/
  adrs/  slices/  design/  ideas/  qa/    â€” ver reference/06 (taxonomÃ­a completa)
```

## Estado

DiseÃ±o documentado y validado por discusiÃ³n; **sin pilotar aÃºn en un proyecto real**. Ver "Abierto / sin pilotar" en cada archivo de `reference/` antes de tratar cualquier regla como definitiva. Ver [README.md](../README.md) del repo para el estado general del proyecto.

