# Monorepos y ownership documental

## Detección

1. Localizar la raíz Git.
2. Buscar workspaces y carpetas de primer nivel con código (`apps`, `packages`, `frontend`, `backend`, servicios).
3. Detectar repositorios Git anidados: cada raíz Git independiente tiene su propio canon.
4. Inventariar documentación existente y enlaces entrantes.

## Canon de una raíz Git

- Un `AGENTS.md`.
- Un `CLAUDE.md`.
- Un `ENGINEER.md`.
- Documentos de producto y dominio compartido en raíz.
- Un `INDEX.md` que enruta a los frentes.

## Ownership

| Contenido | Ubicación |
|---|---|
| Reglas y contexto técnico compartido | raíz |
| Decisiones y slices multi-frente | `docs/` raíz |
| Sistema visual | frente UI propietario |
| Arquitectura y operación exclusiva | `<frente>/docs/` |
| Contrato compartido | `docs/slices/` o ADR; fuente ejecutable junto al productor |
| Guía de consumo | documentación del consumidor |

## Migración de estructuras existentes

1. Elegir el documento canónico por tema.
2. Mover, no copiar.
3. Actualizar todos los enlaces entrantes.
4. Conservar material histórico bajo un slice identificado como histórico.
5. Registrar cambios de ownership relevantes en ADR.
6. Validar duplicados, enlaces e índices.

## Anti-patrones

- Un router por carpeta del monorepo.
- Un `ENGINEER.md` por frente dentro de la misma raíz Git.
- Hubs `docs/frontend` y `docs/backend` que duplican los índices propietarios.
- Taxonomía idéntica forzada sobre frentes con necesidades diferentes.
