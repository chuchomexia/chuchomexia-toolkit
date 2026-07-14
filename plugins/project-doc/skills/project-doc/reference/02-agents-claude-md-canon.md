# AGENTS.md / CLAUDE.md — canon

## Objetivo

El archivo raíz debe ser **corto**. El detalle técnico pesado (comandos, arquitectura, testing, commits) vive en [ENGINEER.md](04-engineer-md-especificacion.md), referenciado desde aquí — no inline. Esto es lo que mantiene el archivo raíz legible en una sola pasada, coherente con la lección ya validada en Colsanitas de que "la documentación corta gana".

Fusiona patrones de dos referencias — [workflow-orchestration-screenshot.md](referencias/workflow-orchestration-screenshot.md) y [agents-md-angular-referencia.md](referencias/agents-md-angular-referencia.md) — más lo ya validado en el proyecto Colsanitas/Tikka que originó esta metodología.

## CLAUDE.md y AGENTS.md son dos archivos espejo, no uno

Esta skill crea **ambos** archivos, `CLAUDE.md` y `AGENTS.md`, con el mismo contenido — así el proyecto queda igual de bien documentado sea que se abra con Claude Code o con Codex CLI (ambos leen su propio nombre de archivo de forma nativa).

Regla de divergencia (importante, decisión explícita del usuario): una vez creados, **no tienen que seguir siendo idénticos para siempre**. El usuario puede personalizar uno sin tocar el otro — es válido, no es un error a corregir.

- El workflow `init` los crea idénticos.
- El workflow `update` **nunca iguala silenciosamente**: antes de tocar cualquiera de los dos, compara su contenido actual. Si ya divergieron, se lo señala al usuario explícitamente y pregunta qué hacer — no asume que la divergencia es un descuido.
- Ningún workflow sobrescribe uno de los dos sin decírselo al usuario primero.

## Esqueleto de secciones

1. **Propósito de una línea** — qué es el proyecto, qué se espera del agente aquí.
2. **Pointers documentales** — dónde está `INDEX.md`, `PROJECT.md`, `PRODUCT.md`, `DESIGN.md`, `ENGINEER.md`, y en qué orden leerlos. Esta sección va temprano a propósito: es lo primero que el agente necesita para saber dónde buscar el resto.
3. **Reglas de trabajo** (de [agents-md-angular-referencia.md](referencias/agents-md-angular-referencia.md)): KISS/DRY, menor diff útil, reutilizar patrones existentes antes de crear nuevos, no cruzar límites de módulo sin revisar impacto, no mezclar feature work con limpieza cosmética, no revertir cambios ajenos, no ejecutar comandos destructivos sin aprobación explícita.
4. **Vocabulario y dominio protegido** — nombres heredados o ambiguos que no deben dominar el modelo (lección de Colsanitas: evitar que `Caso` o `ATEL` se vuelvan la entidad central cuando el dominio real pide otra cosa). Cada proyecto define su propia lista aquí.
5. **Módulos de comportamiento del agente** (de [workflow-orchestration-screenshot.md](referencias/workflow-orchestration-screenshot.md), adaptados):
   - **Plan Mode**: para tareas de 3+ pasos o decisiones arquitectónicas; replanear si algo se desvía.
   - **Subagent Strategy**: usar subagentes para proteger el contexto principal — investigación, exploración, análisis paralelo. Un agente por tarea acotada. **No se hereda ninguna skill de delegación previa** (ver nota abajo).
   - **Self-Improvement Loop**: tras cualquier corrección del usuario, registrar el patrón donde el proyecto lleve sus lecciones (equivalente a `tasks/lessons.md`), para no repetir el error.
   - **Verification Before Done**: nunca marcar completo sin probar que funciona; correr tests, revisar logs.
   - **Demand Elegance (Balanced)**: para cambios no triviales, preguntarse si hay una forma más elegante — saltar esto en fixes simples.
   - **Autonomous Bug Fixing**: resolver bugs directamente sin pedir mano a mano, **salvo que con sentido crítico no haya información suficiente para resolverlo con confianza — en ese caso, señalarlo claramente al usuario en vez de forzar un parche.**
   - **Task Management**: plan primero, verificar antes de implementar, trackear progreso, explicar cambios de alto nivel, documentar resultados, capturar lecciones.
   - **Core Principles**: simplicidad primero, sin pereza (causas raíz, no fixes temporales), impacto mínimo (tocar solo lo necesario).
6. **Testing y verificación por tipo de cambio** (de [agents-md-angular-referencia.md](referencias/agents-md-angular-referencia.md)): bugfix → reproducir primero; cambio de lógica → test enfocado; comportamiento compartido → correr tests relacionados; cambio de contrato → revisar consumidores; cambio visual → inspección manual o screenshot. Si no se puede verificar, decirlo explícitamente y explicar el riesgo que queda.
7. **Commits y PRs** — formato esperado, qué debe incluir una descripción de PR.
8. **Disciplina de contexto** (adaptado de "Token Discipline"): empezar con el contexto mínimo relevante, leer antes de editar, grep antes de tocar código compartido, preferir referencias exactas de archivo/línea sobre relecturas amplias, parar y preguntar antes de ampliar el alcance.

## Qué se descarta explícitamente

- **La skill `/delegation`** referenciada en el AGENTS.md de Angular no se hereda: el usuario la está dando de baja por malos resultados. La sección de Subagent Strategy se basa en el patrón ya usado en este mismo entorno (Explore para investigación de solo lectura, un agente por tarea acotada, proteger el contexto principal, no delegar tareas ambiguas o de alto juicio) — no en esa skill.
- Detalle técnico pesado (project structure, coding style, comandos de build) no vive en este archivo — vive en `ENGINEER.md`, solo referenciado aquí.

## Abierto / sin pilotar

- No se ha probado este esqueleto completo en un proyecto real. Es una síntesis de dos referencias más las reglas ya usadas en Colsanitas, pero nunca se ha generado de punta a punta con el cuestionario de `init` (ver [08](08-cuestionario-init.md)).
- La sección de "Self-Improvement Loop" asume que el proyecto tiene un lugar para llevar lecciones (tipo `tasks/lessons.md`). No está definido si esto es un archivo nuevo que crea `init`, o si vive dentro de `PROJECT.md` como una sub-sección. Pendiente de decidir en una siguiente iteración.
- La lógica exacta de "comparar contenido actual" de CLAUDE.md/AGENTS.md en `update` (diff completo vs. hash vs. comparación semántica) no está especificada a nivel de implementación.
