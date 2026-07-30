---
name: project-doc
description: Genera y mantiene documentación estructural para repositorios simples y monorepos (AGENTS.md, CLAUDE.md, PROJECT/PRODUCT, ENGINEER, DESIGN, ownership por frente, docs/adrs, docs/slices e INDEX). Úsala al iniciar, ordenar, auditar o actualizar documentación de un proyecto, especialmente cuando existen frontend/backend/apps/packages con documentación propia.
---

# project-doc

Skill de una sola entrada con workflows reconocidos por intención. Antes de actuar, cargar [reference/01-invocacion-y-workflows.md](reference/01-invocacion-y-workflows.md).

## Workflows

| Señal | Workflow | Referencias |
|---|---|---|
| Falta estructura documental o se pide iniciar | **init** | [08-cuestionario](reference/08-cuestionario-init.md), [10-monorepos](reference/10-monorepos-y-ownership.md) |
| Existe estructura y se pide refrescar o corregir drift | **update** | [03-project](reference/03-project-md-especificacion.md), [04-engineer](reference/04-engineer-md-especificacion.md), [05-design](reference/05-design-md-especificacion.md) |
| Se pide ordenar PROJECT.md | **organizar** | [03-project](reference/03-project-md-especificacion.md) |

## Regla previa: detectar topología

Antes de crear o mover archivos, identificar si el alcance es un repositorio simple o un monorepo. En monorepos, construir un mapa de frentes y ownership documental; ver [reference/10-monorepos-y-ownership.md](reference/10-monorepos-y-ownership.md).

## Invariantes

- Un repositorio Git tiene un solo `AGENTS.md`, un solo `CLAUDE.md` y un solo `ENGINEER.md` canónicos, ubicados en su raíz.
- Los frentes no duplican esos archivos; especializan mediante su propio `docs/INDEX.md`.
- `docs/` raíz contiene solo documentación transversal; la documentación exclusiva vive con el frente propietario.
- `DESIGN.md` vive en el frente que posee la UI; en repos simples puede vivir en raíz.
- Cada `INDEX.md` tiene menos de 200 líneas; la meta habitual es 20–60.
- No mover ni sobrescribir documentación existente sin actualizar enlaces y registrar decisiones de ownership con trade-offs.

## Salida típica de monorepo

```text
AGENTS.md
CLAUDE.md
ENGINEER.md
PROJECT.md o <DOMINIO>.md
PRODUCT.md
INDEX.md
docs/
  INDEX.md
  adrs/
  slices/
frontend/
  DESIGN.md
  docs/
    INDEX.md
backend/
  docs/
    INDEX.md
```

La estructura exacta se adapta a los frentes detectados; `frontend` y `backend` son ejemplos, no nombres obligatorios.

## Feedback

Si esta skill te dio una instrucción incorrecta o incompleta, o tuviste que ir en contra de ella
para lograr el resultado correcto, abre un issue en el repo del marketplace (protocolo completo
en `FEEDBACK.md` en la raíz del repo, si está presente en tu checkout):

```bash
gh issue create --repo chuchomexia/chuchomexia-toolkit \
  --title "[project-doc] <resumen corto>" --label skill-feedback \
  --body "Qué decía la skill / qué pasó / qué hiciste en su lugar"
```

Si `gh` no está disponible o autenticado, dile al usuario que hay feedback pendiente y sugiere
abrirlo manualmente en `github.com/chuchomexia/chuchomexia-toolkit/issues/new?labels=skill-feedback`.
