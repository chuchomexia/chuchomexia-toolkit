# project-doc

Marketplace privado de skills para estandarizar documentación de proyectos, empezando por `project-doc`: monta y mantiene `CLAUDE.md`/`AGENTS.md`, un archivo de contexto vivo (`PROJECT.md`), sus derivados (`PRODUCT.md`, `DESIGN.md`, `ENGINEER.md`), una taxonomía estándar de `docs/`, e `INDEX.md` por carpeta.

Nace de destilar la metodología usada en un proyecto real (Colsanitas/Tikka) y generalizarla para cualquier proyecto, nuevo o existente, propio o de un equipo que hoy no tiene ninguna estructura de este tipo.

## Por qué existe

La mayoría de proyectos no tienen `CLAUDE.md`/`AGENTS.md`, y los que sí, casi nunca son consistentes entre sí ni se actualizan. `project-doc` estandariza esa documentación con dos objetivos:

1. Que sea fácil de adoptar para quien nunca ha escrito uno.
2. Que sea consistente entre todos tus proyectos, para no reinventar el patrón cada vez.

## Qué hace `project-doc`

Una sola skill, tres workflows reconocidos por intención (no por subcomando):

- **init** — monta la documentación desde cero: corre un cuestionario corto, crea `CLAUDE.md`/`AGENTS.md` (espejo), `PROJECT.md`, `ENGINEER.md`, `DESIGN.md`, **y el árbol completo de carpetas de `docs/`** (`adrs/`, `slices/`, `design/`, `ideas/`, `qa/`) con su `INDEX.md` cada una.
- **update** — refresca los archivos derivados (`PRODUCT.md`/`DESIGN.md`/`ENGINEER.md`) a partir de lo que el humano fue agregando a `PROJECT.md`.
- **organizar** — pone en orden `PROJECT.md` cuando se volvió difícil de navegar, sin eliminar ni resumir contenido.

Detalle completo de cada workflow en [plugins/project-doc/skills/project-doc/reference/](plugins/project-doc/skills/project-doc/reference/INDEX.md).

## Instalar en Claude Code (vía marketplace)

Este repo **es** un marketplace de Claude Code (`.claude-plugin/marketplace.json` en la raíz). Como es privado, cada persona necesita acceso de lectura al repo en GitHub antes de poder agregarlo.

```
/plugin marketplace add chuchomexia/project-doc-skill
/plugin install project-doc@chuchomexia-tools
```

O desde la CLI, sin sesión interactiva:

```bash
claude plugin marketplace add chuchomexia/project-doc-skill
claude plugin install project-doc@chuchomexia-tools
```

Para que un equipo lo reciba automáticamente al abrir un repo (sin correr `/plugin marketplace add` a mano), se puede declarar en `.claude/settings.json` de ese repo:

```json
{
  "extraKnownMarketplaces": {
    "chuchomexia-tools": {
      "source": { "source": "github", "repo": "chuchomexia/project-doc-skill" }
    }
  },
  "enabledPlugins": {
    "project-doc@chuchomexia-tools": true
  }
}
```

## Instalar en Codex CLI

Codex no tiene el concepto de marketplace — sus Skills se descubren copiando la carpeta directamente a `.codex/skills/<nombre>/`. Instalación manual:

```bash
git clone https://github.com/chuchomexia/project-doc-skill.git /tmp/project-doc-skill
cp -r /tmp/project-doc-skill/plugins/project-doc/skills/project-doc /ruta/a/tu-proyecto/.codex/skills/project-doc
```

## CLAUDE.md y AGENTS.md como espejo, no como gemelos idénticos para siempre

`init` los crea idénticos. Después de eso, pueden divergir si el usuario personaliza uno sin tocar el otro — eso es válido. `update` nunca los iguala en silencio: si detecta que ya divergieron, se lo señala al usuario y pregunta qué hacer. Ver la regla completa en [reference/02-agents-claude-md-canon.md](plugins/project-doc/skills/project-doc/reference/02-agents-claude-md-canon.md).

## Estado

Diseño completo, documentado y discutido a fondo (incluyendo una ronda explícita de crítica brutal antes de darlo por bueno). Instalación end-to-end verificada localmente (`claude plugin validate`, `marketplace add`, `install`). **Sin pilotar todavía en un proyecto real** (nadie ha corrido `init`/`update`/`organizar` de punta a punta sobre un repo de trabajo). Cada archivo de `reference/` cierra con una sección "Abierto / sin pilotar" — léela antes de asumir que algo aquí está validado.

Próximo paso natural: pilotar `init` en un proyecto real (no Colsanitas) antes de invitar a más gente al marketplace.

## Compartir con el equipo

El repo es privado en GitHub. Para que un compañero pueda instalar desde acá, primero necesita acceso de lectura al repo (agregarlo como colaborador, o mover el repo a una organización con acceso compartido). El marketplace en sí no gestiona permisos — solo el repo de GitHub que lo hospeda.

## Agregar más skills a este marketplace

Este repo está pensado para crecer más allá de `project-doc`. Para sumar una nueva skill:

1. Crear `plugins/<nombre-skill>/.claude-plugin/plugin.json` y `plugins/<nombre-skill>/skills/<nombre-skill>/SKILL.md`.
2. Agregar una entrada en `plugins` dentro de `.claude-plugin/marketplace.json` con `"source": "./plugins/<nombre-skill>"`.
3. Validar con `claude plugin validate .` antes de hacer commit.

## Estructura del repo

```
project-doc-skill/
  README.md
  .claude-plugin/
    marketplace.json          — catálogo del marketplace
  plugins/
    project-doc/
      .claude-plugin/
        plugin.json            — manifiesto del plugin
      skills/
        project-doc/
          SKILL.md              — entrada delgada (frontmatter + índice de workflows)
          reference/            — especificación completa, cargada bajo demanda
  .claude/skills/project-doc  — symlink a plugins/project-doc/skills/project-doc (dogfooding)
  .codex/skills/project-doc   — symlink a plugins/project-doc/skills/project-doc (dogfooding)
```

Inspirado en la arquitectura de [Impeccable](https://github.com/pbakaus/impeccable) (entrada única + progressive disclosure) y en la [documentación oficial de marketplaces de Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).
