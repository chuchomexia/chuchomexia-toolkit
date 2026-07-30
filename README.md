# chuchomexia-toolkit

Marketplace privado de skills de Claude Code / Codex. Empezó con una sola skill (`project-doc`)
pero está pensado para crecer — hoy incluye también `m3-expressive` (diseño de UI) y `anti-slop`
(estilo de escritura).

## Skills en este marketplace

| Skill | Qué hace |
|---|---|
| [`project-doc`](plugins/project-doc/skills/project-doc/SKILL.md) | Monta y mantiene `CLAUDE.md`/`AGENTS.md`, un archivo de contexto vivo (`PROJECT.md`), sus derivados (`PRODUCT.md`, `DESIGN.md`, `ENGINEER.md`), una taxonomía estándar de `docs/`, e `INDEX.md` por carpeta. |
| [`m3-expressive`](plugins/m3-expressive/skills/m3-expressive/SKILL.md) | Diseña o corrige cualquier interfaz usando Material 3 Expressive de Google como filosofía rectora — color, tipografía, forma, motion y accesibilidad. |
| [`anti-slop`](plugins/anti-slop/skills/anti-slop/SKILL.md) | Filtro anti-"IA slop" para texto en prosa (emails, reportes, posts, specs) en inglés y español, con un validador determinístico (`scripts/validate.py`). |

`project-doc` nace de destilar la metodología usada en un proyecto real (Colsanitas/Tikka) y generalizarla para cualquier proyecto, nuevo o existente, propio o de un equipo que hoy no tiene ninguna estructura de este tipo.

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
/plugin marketplace add chuchomexia/chuchomexia-toolkit
/plugin install project-doc@chuchomexia-toolkit
/plugin install m3-expressive@chuchomexia-toolkit
/plugin install anti-slop@chuchomexia-toolkit
```

O desde la CLI, sin sesión interactiva:

```bash
claude plugin marketplace add chuchomexia/chuchomexia-toolkit
claude plugin install project-doc@chuchomexia-toolkit
claude plugin install m3-expressive@chuchomexia-toolkit
claude plugin install anti-slop@chuchomexia-toolkit
```

Para que un equipo lo reciba automáticamente al abrir un repo (sin correr `/plugin marketplace add` a mano), se puede declarar en `.claude/settings.json` de ese repo:

```json
{
  "extraKnownMarketplaces": {
    "chuchomexia-toolkit": {
      "source": { "source": "github", "repo": "chuchomexia/chuchomexia-toolkit" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": {
    "project-doc@chuchomexia-toolkit": true,
    "m3-expressive@chuchomexia-toolkit": true,
    "anti-slop@chuchomexia-toolkit": true
  }
}
```

`autoUpdate: true` hace que Claude Code refresque el catálogo del marketplace solo — ver la
sección "Cómo se enteran los agentes de una actualización" más abajo para lo que sí y no cubre.

## Instalar en Codex CLI (vía marketplace)

Codex también tiene marketplaces, con su propio formato de manifiesto (`.agents/plugins/marketplace.json` + `.codex-plugin/plugin.json` por plugin — distinto al de Claude Code, por eso este repo trae ambos en paralelo). Verificado end-to-end con `codex plugin marketplace add` + `codex plugin add`.

Desde la CLI:

```bash
codex plugin marketplace add chuchomexia/chuchomexia-toolkit
codex plugin add project-doc@chuchomexia-toolkit
codex plugin add m3-expressive@chuchomexia-toolkit
codex plugin add anti-slop@chuchomexia-toolkit
```

Desde la UI de Codex ("Add plugin marketplace"):

| Campo | Valor |
|---|---|
| Source | `chuchomexia/chuchomexia-toolkit` |
| Git ref | `main` |
| Sparse paths | (opcional) `.agents/plugins`, `plugins/project-doc`, `plugins/m3-expressive` y `plugins/anti-slop`, uno por línea — limita el clone a lo que el marketplace necesita |

Como el repo es privado, Codex necesita las mismas credenciales de git/GitHub que ya uses en tu terminal para acceder a él (igual que Claude Code).

## CLAUDE.md y AGENTS.md como espejo, no como gemelos idénticos para siempre

`init` los crea idénticos. Después de eso, pueden divergir si el usuario personaliza uno sin tocar el otro — eso es válido. `update` nunca los iguala en silencio: si detecta que ya divergieron, se lo señala al usuario y pregunta qué hacer. Ver la regla completa en [reference/02-agents-claude-md-canon.md](plugins/project-doc/skills/project-doc/reference/02-agents-claude-md-canon.md).

## Estado

Diseño completo, documentado y discutido a fondo (incluyendo una ronda explícita de crítica brutal antes de darlo por bueno). Instalación end-to-end verificada localmente en ambas herramientas (`claude plugin validate`/`marketplace add`/`install`, y `codex plugin marketplace add`/`codex plugin add`). **Sin pilotar todavía en un proyecto real** (nadie ha corrido `init`/`update`/`organizar` de punta a punta sobre un repo de trabajo). Cada archivo de `reference/` cierra con una sección "Abierto / sin pilotar" — léela antes de asumir que algo aquí está validado.

Próximo paso natural: pilotar `init` en un proyecto real (no Colsanitas) antes de invitar a más gente al marketplace.

## Compartir con el equipo

El repo es privado en GitHub. Para que un compañero pueda instalar desde acá, primero necesita acceso de lectura al repo (agregarlo como colaborador, o mover el repo a una organización con acceso compartido). El marketplace en sí no gestiona permisos — solo el repo de GitHub que lo hospeda.

## Cómo se enteran los agentes de una actualización

No hay push: nadie recibe un aviso cuando cambias una skill. Es pull, y hay dos capas que
actualizar por separado.

1. **El catálogo del marketplace** (qué plugins existen y en qué commit está cada uno). Se
   refresca con `/plugin marketplace update chuchomexia-toolkit` (o el equivalente `claude
   plugin marketplace update` en CLI), o solo si cada persona configuró `"autoUpdate": true` en
   `extraKnownMarketplaces` (ver ejemplo arriba) — con eso Claude Code lo revisa
   periódicamente sin comando manual. Un marketplace agregado con un tag o branch fijo se
   actualiza al último commit de esa ref, no necesariamente a `main` si se ancló distinto.
2. **El plugin instalado en cada proyecto**, que no se mueve solo aunque el catálogo ya esté
   actualizado — hay que correr `/plugin install <skill>@chuchomexia-toolkit` de nuevo (o su
   equivalente Codex) para tomar la versión nueva. Claude Code normalmente pide reiniciar con
   `/reload-plugins` después de una actualización.

En la práctica: si le pides a alguien del equipo que confirme que tiene la última versión de una
skill, la pregunta correcta es "¿corriste `/plugin marketplace update` y reinstalaste?", no
"¿tienes el repo actualizado?" — el checkout de git y el estado de Claude Code/Codex son cosas
separadas.

## Feedback automático de los agentes

Cada skill de este marketplace termina con una sección "Feedback" que le dice al agente que, si
detectó que la skill le dio información incorrecta o incompleta, abra un issue en este repo con
`gh issue create --label skill-feedback`. Esto no es telemetría — depende de que el agente
efectivamente lo haga y tenga `gh` autenticado contra este repo. Protocolo completo, plantilla y
qué hacer si `gh` no está disponible en [FEEDBACK.md](FEEDBACK.md).

Para revisar lo acumulado: `gh issue list --repo chuchomexia/chuchomexia-toolkit --label skill-feedback`.

## Agregar más skills a este marketplace

Este repo está pensado para crecer más allá de `project-doc`. Para sumar una nueva skill, en ambas herramientas a la vez:

1. Crear `plugins/<nombre-skill>/skills/<nombre-skill>/SKILL.md` (compartido por ambas).
2. Crear `plugins/<nombre-skill>/.claude-plugin/plugin.json` (Claude Code — sin `version` si quieres que cada commit cuente como versión nueva).
3. Crear `plugins/<nombre-skill>/.codex-plugin/plugin.json` (Codex — `version` es obligatorio ahí, hay que subirla a mano en cada release).
4. Agregar una entrada en `.claude-plugin/marketplace.json` (`"source": "./plugins/<nombre-skill>"`).
5. Agregar una entrada equivalente en `.agents/plugins/marketplace.json` (`"source": {"source": "local", "path": "./plugins/<nombre-skill>"}`).
6. Agregar al final del `SKILL.md` la sección "Feedback" (copiar el bloque de `plugins/m3-expressive/skills/m3-expressive/SKILL.md`) para que la skill quede conectada al protocolo de [FEEDBACK.md](FEEDBACK.md).
7. Opcional: symlinks de dogfooding `.claude/skills/<nombre-skill>` y `.codex/skills/<nombre-skill>` apuntando a `../../plugins/<nombre-skill>/skills/<nombre-skill>`.
8. Validar con `claude plugin validate .` antes de hacer commit. Codex no trae un comando de validación equivalente todavía — probar con `codex plugin marketplace add ./` + `codex plugin add <nombre>@chuchomexia-toolkit` localmente.
9. Revisar periódicamente los issues con label `skill-feedback` (`gh issue list --repo chuchomexia/chuchomexia-toolkit --label skill-feedback`) antes de decidir qué corregir en cada skill.

## Asimetría entre Claude Code y Codex (a tener presente)

Ambas herramientas leen `SKILL.md` igual, pero el resto del empaquetado difiere:

| | Claude Code | Codex |
|---|---|---|
| Manifiesto de marketplace | `.claude-plugin/marketplace.json` | `.agents/plugins/marketplace.json` |
| Manifiesto de plugin | `plugins/<n>/.claude-plugin/plugin.json` | `plugins/<n>/.codex-plugin/plugin.json` |
| `version` en el manifiesto | Opcional (se recomienda omitir en desarrollo activo) | Obligatorio |
| Comando de instalación | `/plugin install <n>@<marketplace>` | `codex plugin add <n>@<marketplace>` |

Esto significa que **cada release toca dos archivos de versión** (`.claude-plugin/plugin.json` no necesita bump si se omite `version`, pero `.codex-plugin/plugin.json` sí). Fácil de olvidar — vale la pena revisar antes de cada push si cambió algo sustancial en `skills/project-doc/`.

## Estructura del repo

```
project-doc-skill/
  README.md
  FEEDBACK.md                     — protocolo de feedback de agentes hacia el mantenedor
  .claude-plugin/
    marketplace.json              — catálogo del marketplace (Claude Code), name: chuchomexia-toolkit
  .agents/plugins/
    marketplace.json              — catálogo del marketplace (Codex)
  plugins/
    project-doc/
      .claude-plugin/
        plugin.json                — manifiesto del plugin (Claude Code)
      .codex-plugin/
        plugin.json                — manifiesto del plugin (Codex)
      skills/
        project-doc/
          SKILL.md                  — entrada delgada (frontmatter + índice de workflows) + sección Feedback
          reference/                — especificación completa, cargada bajo demanda, compartida
    m3-expressive/
      .claude-plugin/
        plugin.json
      .codex-plugin/
        plugin.json
      skills/
        m3-expressive/
          SKILL.md                  — filosofía, tácticas y mapa de referencias + sección Feedback
          references/                — 14 módulos JSON + cheatsheet, cargados bajo demanda
    anti-slop/
      .claude-plugin/
        plugin.json
      .codex-plugin/
        plugin.json
      skills/
        anti-slop/
          SKILL.md                   — flujo, reglas prácticas y las tres capas de detección + sección Feedback
          reference/                 — patrones delatores en/es, cargados bajo demanda
          scripts/validate.py        — linter determinístico (score + exit code)
  .claude/skills/project-doc    — symlink a plugins/project-doc/skills/project-doc (dogfooding)
  .claude/skills/m3-expressive  — symlink a plugins/m3-expressive/skills/m3-expressive (dogfooding)
  .claude/skills/anti-slop      — symlink a plugins/anti-slop/skills/anti-slop (dogfooding)
  .codex/skills/project-doc     — symlink a plugins/project-doc/skills/project-doc (dogfooding)
  .codex/skills/m3-expressive   — symlink a plugins/m3-expressive/skills/m3-expressive (dogfooding)
  .codex/skills/anti-slop       — symlink a plugins/anti-slop/skills/anti-slop (dogfooding)
```

Inspirado en la arquitectura de [Impeccable](https://github.com/pbakaus/impeccable) (entrada única + progressive disclosure), en la [documentación oficial de marketplaces de Claude Code](https://code.claude.com/docs/en/plugin-marketplaces) y en la [documentación oficial de plugins de Codex](https://developers.openai.com/codex/plugins/build).
