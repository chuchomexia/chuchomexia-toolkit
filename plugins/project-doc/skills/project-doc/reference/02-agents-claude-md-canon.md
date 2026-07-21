# AGENTS.md / CLAUDE.md — canon

## Objetivo

`AGENTS.md` y `CLAUDE.md` son routers de contexto, no manuales del proyecto. Deben poder leerse en una pasada y cargar únicamente el contexto necesario para la tarea actual.

## Regla de espejo

`init` crea ambos archivos con el mismo contenido. En `update`, si ya divergen, no igualarlos en silencio: señalarlo y pedir decisión al usuario.

## Lectura mínima obligatoria

1. `NEXT_STEP.md` o equivalente, solo si existe.
2. `INDEX.md` de la raíz.

## Carga condicional

- Cambio técnico, datos, pruebas, comandos o despliegue: `ENGINEER.md`.
- Cambio visual, UX o accesibilidad: `DESIGN.agent.md`.
- Cambio de contrato: OpenAPI y consumidores afectados.
- Cambio de flujo: solo el documento o slice afectado.
- Contexto de producto: `PRODUCT.md` solo si la tarea cambia comportamiento, alcance o reglas de negocio.

## Reglas de trabajo

- Mantener el diff mínimo; reutilizar patrones existentes; no revertir cambios ajenos.
- Verificar el cambio en proporción a su riesgo.
- Referenciar archivos concretos en vez de cargar árboles documentales completos.

## Qué no incluir

No incluir arquitectura detallada, comandos, catálogo de componentes, ejemplos extensos ni guías de testing. Esos contenidos viven en `ENGINEER.md` o `docs/`.
