# project-doc

Skill para Claude Code y Codex CLI que monta y mantiene la documentación estructural de un proyecto: `CLAUDE.md`/`AGENTS.md`, un archivo de contexto vivo (`PROJECT.md`), sus derivados (`PRODUCT.md`, `DESIGN.md`, `ENGINEER.md`), una taxonomía estándar de `docs/`, e `INDEX.md` por carpeta.

Nace de destilar la metodología usada en un proyecto real (Colsanitas/Tikka) y generalizarla para cualquier proyecto, nuevo o existente, propio o de un equipo que hoy no tiene ninguna estructura de este tipo.

## Por qué existe

La mayoría de proyectos no tienen `CLAUDE.md`/`AGENTS.md`, y los que sí, casi nunca son consistentes entre sí ni se actualizan. `project-doc` estandariza esa documentación con dos objetivos:

1. Que sea fácil de adoptar para quien nunca ha escrito uno.
2. Que sea consistente entre todos tus proyectos, para no reinventar el patrón cada vez.

## Qué hace

Una sola skill, tres workflows reconocidos por intención (no por subcomando):

- **init** — monta la documentación desde cero: corre un cuestionario corto, crea `CLAUDE.md`/`AGENTS.md` (espejo), `PROJECT.md`, `ENGINEER.md`, la taxonomía de `docs/` e `INDEX.md` por carpeta.
- **update** — refresca los archivos derivados (`PRODUCT.md`/`DESIGN.md`/`ENGINEER.md`) a partir de lo que el humano fue agregando a `PROJECT.md`.
- **organizar** — pone en orden `PROJECT.md` cuando se volvió difícil de navegar, sin eliminar ni resumir contenido.

Detalle completo de cada workflow en [skill/reference/](skill/reference/INDEX.md).

## Funciona en Claude Code y Codex

Ambas herramientas soportan el mismo formato de skill (`SKILL.md` + carpeta de referencias), así que un solo paquete (`skill/`) sirve para las dos:

- Claude Code la descubre en `.claude/skills/<nombre>/SKILL.md`
- Codex CLI la descubre en `.codex/skills/<nombre>/SKILL.md`

Este repo trae ambos como symlinks a la misma carpeta (`skill/`), para que abrir el repo directamente ya exponga la skill en cualquiera de las dos herramientas.

## Instalación en otro proyecto

Manual por ahora — copia o symlinkea la carpeta `skill/` de este repo al destino que necesites:

```bash
# Claude Code
cp -r skill /ruta/a/tu-proyecto/.claude/skills/project-doc

# Codex CLI
cp -r skill /ruta/a/tu-proyecto/.codex/skills/project-doc
```

Un instalador propio (script o comando) queda pendiente para cuando este flujo manual demuestre ser suficiente fricción como para justificarlo.

## CLAUDE.md y AGENTS.md como espejo, no como gemelos idénticos para siempre

`init` los crea idénticos. Después de eso, pueden divergir si el usuario personaliza uno sin tocar el otro — eso es válido. `update` nunca los iguala en silencio: si detecta que ya divergieron, se lo señala al usuario y pregunta qué hacer. Ver la regla completa en [skill/reference/02-agents-claude-md-canon.md](skill/reference/02-agents-claude-md-canon.md).

## Estado

Diseño completo, documentado y discutido a fondo (incluyendo una ronda explícita de crítica brutal antes de darlo por bueno). **Sin pilotar todavía en un proyecto real.** Cada archivo de `skill/reference/` cierra con una sección "Abierto / sin pilotar" — léela antes de asumir que algo aquí está validado.

Próximo paso natural: pilotar `init` en un segundo proyecto real (no Colsanitas) antes de pensar en distribución vía marketplace privado.

## Estructura del repo

```
project-doc-skill/
  README.md
  skill/
    SKILL.md              — entrada delgada de la skill (frontmatter + índice de workflows)
    reference/             — especificación completa, cargada bajo demanda
  .claude/skills/project-doc   — symlink a ../../skill
  .codex/skills/project-doc    — symlink a ../../skill
```

Inspirado en la arquitectura de [Impeccable](https://github.com/pbakaus/impeccable) (entrada única + progressive disclosure + config compartida/local) — ver notas en [skill/reference/referencias/impeccable-arquitectura-notas.md](skill/reference/referencias/impeccable-arquitectura-notas.md).
