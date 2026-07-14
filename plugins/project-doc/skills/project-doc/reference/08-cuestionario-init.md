# Cuestionario del workflow `init`

Cuatro preguntas, no más. Se descartó explícitamente un quinto eje sobre tamaño/composición del equipo por no aportar señal clara sobre qué generar.

## 1. Nombre y propósito del proyecto

Una línea: qué es el proyecto y para quién. Alimenta directamente el "propósito de una línea" del `AGENTS.md`/`CLAUDE.md` (ver [02](02-agents-claude-md-canon.md)) y el nombre del archivo `PROJECT.md` (ej. `COLSANITAS.md`).

## 2. Stack

Lenguaje, framework, base de datos, herramientas principales. Alimenta la sección de comandos y arquitectura de `ENGINEER.md` (ver [04](04-engineer-md-especificacion.md)).

## 3. Etapa del proyecto

Greenfield (día cero, sin código aún) vs. proyecto existente con historia. Determina cómo arranca `PROJECT.md`:

- **Greenfield**: arranca vacío, con una nota invitando al humano a volcar su braindump inicial.
- **Existente**: el agente puede poblarlo por inferencia inicial del código y del historial de git (con cuidado de marcarlo como punto de partida a validar por el humano, no como verdad asentada — el humano sigue siendo quien decide qué queda).

## 4. Reglas operativas no negociables

Restricciones del tipo KISS, sin microservicios, sin infraestructura adicional, límites de alcance — lo que en Colsanitas ya vive en `AGENTS.md` como reglas de trabajo. Alimenta directamente la sección "Reglas de trabajo" del canon (ver [02](02-agents-claude-md-canon.md)).

## Eje descartado

Un quinto eje sobre tamaño y composición del equipo (¿cuántas personas, qué roles?) se consideró y se descartó: el usuario aclaró que sus colegas son usuarios avanzados de IA a quienes solo les falta estructura, no simplicidad — el cuestionario no necesita ajustar su complejidad según el tamaño del equipo, el mismo cuestionario completo sirve para todos.

## Abierto / sin pilotar

- No se ha probado el flujo de inferencia inicial de `PROJECT.md` en un proyecto existente real. El riesgo principal: que el agente infiera demasiado y el archivo termine pareciendo "verdad asentada" cuando en realidad es una hipótesis del agente sobre un código que no vivió — hay que ser explícito en el propio archivo de que ese contenido inicial es un borrador a validar.
