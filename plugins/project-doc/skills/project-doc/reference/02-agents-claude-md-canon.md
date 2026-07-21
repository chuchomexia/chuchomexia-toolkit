# AGENTS.md / CLAUDE.md — canon

## Objetivo

Son routers de contexto del repositorio completo. Deben ser cortos, equivalentes al crearse y ubicarse únicamente en la raíz Git.

## Monorepos

No crear routers adicionales en `frontend/`, `backend/`, `apps/*` o `packages/*`. Esos ámbitos se descubren desde el router raíz y se especializan mediante `docs/INDEX.md` del frente.

## Lectura mínima

1. `NEXT_STEP.md` si existe.
2. `INDEX.md` raíz.
3. Solo los documentos condicionados por la tarea.

## Carga condicional

- Producto o dominio: `PRODUCT.md`, `PROJECT.md` o documento de dominio raíz.
- Ingeniería: `ENGINEER.md` raíz.
- UI/UX: `DESIGN.md` del frente propietario.
- Frente específico: `<frente>/docs/INDEX.md`.
- Contrato: OpenAPI y consumidores.
- Decisión o slice transversal: `docs/adrs/` o `docs/slices/`.

## Divergencia

`init` crea `AGENTS.md` y `CLAUDE.md` con el mismo contenido. `update` no iguala divergencias existentes sin informar al usuario.
