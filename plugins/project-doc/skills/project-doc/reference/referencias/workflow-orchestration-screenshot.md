# Transcripción — captura de pantalla "Workflow Orchestration"

Transcripción del contenido de la imagen provista por el usuario. Es la referencia base para los módulos de comportamiento del agente en [02-agents-claude-md-canon.md](../02-agents-claude-md-canon.md).

## Workflow Orchestration

### 1. Plan Mode Default
- Entrar en plan mode para CUALQUIER tarea no trivial (3+ pasos o decisiones arquitectónicas).
- Si algo se desvía, PARAR y replanear inmediatamente.
- Usar plan mode también para pasos de verificación, no solo para construir.
- Escribir specs detallados por adelantado para reducir ambigüedad.

### 2. Subagent Strategy
- Usar subagentes liberalmente para mantener limpia la ventana de contexto principal.
- Delegar investigación, exploración y análisis paralelo a subagentes.
- Para problemas complejos, lanzar más cómputo vía subagentes.
- Un agente por tarea, para ejecución enfocada.

### 3. Self-Improvement Loop
- Tras CUALQUIER corrección del usuario: actualizar tasks/lessons.md con el patrón.
- Escribir reglas para uno mismo que prevengan repetir el mismo error.
- Iterar sin piedad sobre esas lecciones hasta que baje la tasa de error.
- Revisar lecciones al inicio de sesión para el proyecto relevante.

### 4. Verification Before Done
- Nunca marcar una tarea completa sin probar que funciona.
- Diferenciar comportamiento entre main y los cambios propios cuando sea relevante.
- Preguntarse: "¿aprobaría esto un ingeniero senior?"
- Correr tests, revisar logs, demostrar corrección.

### 5. Demand Elegance (Balanced)
- Para cambios no triviales: pausar y preguntar "¿hay una forma más elegante?"
- Si un fix se siente hacky: "sabiendo todo lo que sé, implementa la solución elegante."
- Saltar esto para fixes simples y obvios — no sobre-ingenierizar.
- Cuestionar el propio trabajo antes de presentarlo.

### 6. Autonomous Bug Fixing
- Cuando se recibe un reporte de bug: arreglarlo directamente, sin pedir mano a mano.
- Señalar logs, errores, tests fallidos — luego resolver.
- Cero cambio de contexto requerido del usuario.
- Resolver tests fallidos de CI sin que se lo pidan.

## Task Management
1. Plan First: escribir el plan en tasks/todo.md con ítems verificables.
2. Verify Plan: confirmar antes de empezar la implementación.
3. Track Progress: marcar ítems completos sobre la marcha.
4. Explain Changes: resumen de alto nivel en cada paso.
5. Document Results: agregar sección de revisión a tasks/todo.md.
6. Capture Lessons: actualizar tasks/lessons.md tras correcciones.

## Core Principles
- **Simplicity First**: cada cambio lo más simple posible. Impacto mínimo en el código.
- **No Laziness**: encontrar causas raíz. Sin fixes temporales. Estándares de desarrollador senior.
- **Minimal Impact**: tocar solo lo necesario. Sin efectos secundarios ni bugs nuevos.

## Adaptaciones hechas en esta metodología

No se copió tal cual. Cambios explícitos acordados con el usuario:

- **Autonomous Bug Fixing**: se agrega la regla de que si, con sentido crítico, no hay información suficiente para resolver el bug con confianza, el agente debe **señalarlo claramente al usuario** en vez de forzar un parche.
- **Subagent Strategy**: no se hereda de la skill `/delegation` del usuario (la está dando de baja por malos resultados). Se basa en el patrón ya validado en este entorno: Explore para investigación de solo lectura, un agente por tarea acotada, proteger el contexto principal, no delegar tareas ambiguas o de alto juicio.
- **Task Management** y **Core Principles**: se toman como base pero se mejoran en el canon final (ver [02-agents-claude-md-canon.md](../02-agents-claude-md-canon.md)).
