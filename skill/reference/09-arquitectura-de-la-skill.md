# Arquitectura de la skill

Este archivo documenta las decisiones de empaquetado ya aplicadas en este repo (`project-doc-skill`), para que quede explícito el porqué de la estructura de carpetas.

## Problema a evitar

Meter las especificaciones de [02](02-agents-claude-md-canon.md) a [08](08-cuestionario-init.md) completas dentro de un solo `SKILL.md` produciría un archivo larguísimo, difícil de mantener y costoso de cargar en cada invocación (aunque solo se necesite, por ejemplo, el workflow "organizar").

## Patrón adoptado: progressive disclosure, inspirado en Impeccable

Ver detalle del fetch en [referencias/impeccable-arquitectura-notas.md](referencias/impeccable-arquitectura-notas.md). Se adopta:

1. **Entrada única con subcomandos reconocidos por intención** — `project-doc` es una sola skill; internamente distingue `init` / `update` / `organizar` (ver [01-invocacion-y-workflows.md](01-invocacion-y-workflows.md)), igual que Impeccable expone `/impeccable <command>` en vez de una skill por comando.
2. **`SKILL.md` delgado** — frontmatter de descripción (para que el enrutamiento automático de Claude Code triggeree bien en los tres casos) + un índice corto de qué hace cada workflow y a qué archivo de referencia remitir. El contenido pesado (el esqueleto completo del canon, la taxonomía, el cuestionario) vive en archivos de referencia dentro de la skill, cargados solo cuando el workflow activo los necesita.
3. **Separación de configuración compartida vs. local** — las respuestas del cuestionario de `init` (ver [08](08-cuestionario-init.md)) se guardan en un archivo versionado del proyecto (ej. `.project-doc/config.json`), mientras que preferencias individuales del desarrollador (verbosidad, uso intensivo de subagentes, etc.) irían en un archivo gitignored (`.project-doc/config.local.json`) — mismo patrón que `.impeccable/config.json` vs. `config.local.json`.

## Estructura real de este repo

```
project-doc-skill/              (repo raíz, futuro ítem de marketplace)
  README.md                     — cara pública: qué es, cómo instalarla, en qué tools funciona
  skill/
    SKILL.md                    — delgado: frontmatter + índice de workflows
    reference/                  — este mismo árbol de archivos (00–09 + referencias/)
  .claude/skills/project-doc    — symlink a ../../skill (para que Claude Code la descubra al abrir este repo)
  .codex/skills/project-doc     — symlink a ../../skill (para que Codex la descubra al abrir este repo)
```

Los symlinks son solo para dogfooding — que abrir este propio repo en Claude Code o Codex ya exponga la skill sin pasos extra. Para instalarla en *otro* proyecto, el mecanismo (todavía manual) es copiar o symlinkear `skill/` a `.claude/skills/project-doc/` y/o `.codex/skills/project-doc/` de ese proyecto.

## Abierto / sin pilotar

- No se ha probado la skill en un proyecto real todavía — ni el `SKILL.md`, ni la lógica de los tres workflows. Existe la estructura y el contenido de referencia, no evidencia de que funcione en la práctica.
- El mecanismo de "detectar drift" del workflow `update` (mencionado como pendiente en [01](01-invocacion-y-workflows.md) y [04](04-engineer-md-especificacion.md)) sigue sin resolverse a nivel de implementación.
- El proceso de instalación en otro proyecto es manual (copiar/symlinkear `skill/`). Un instalador (script o comando propio) queda pendiente — vale la pena solo si el uso manual demuestra ser suficientemente fricción como para justificarlo.
- No se ha decidido el mecanismo concreto de distribución en un marketplace privado — se deja fuera de alcance hasta pilotar la skill en al menos un proyecto real distinto a Colsanitas.
