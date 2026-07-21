# Principios de context engineering

Estos principios guían todas las decisiones de esta carpeta.

## 1. Contexto estructurado

La jerarquía `PROJECT.md → PRODUCT.md / DESIGN.md / ENGINEER.md` y la taxonomía fija de `docs/` reducen ambigüedad y hacen predecible el contexto.

## 2. Contexto mínimo y recuperable

El agente debe cargar primero solo `NEXT_STEP.md` (si existe) e `INDEX.md`. El resto se recupera bajo condición: `ENGINEER.md` para cambios técnicos, `DESIGN.agent.md` para cambios visuales, OpenAPI para contratos y el documento específico para un flujo. Un archivo relevante que no se lee es un problema de findability; uno irrelevante que siempre se carga también lo es.

## 3. Alinear al modelo mental del usuario

Estructurar el contexto alrededor de cómo el usuario describe el problema. `PROJECT.md` permite captura libre antes de que el agente derive estructura.

## 4. Diseñar la memoria

Definir qué se recuerda, cómo se indexa y cuándo se recupera. Evitar que historial o detalle obsoleto compita con las decisiones vigentes.
