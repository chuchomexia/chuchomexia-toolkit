# Invocación y workflows

## Modelo: una skill, tres workflows

`project-doc` es una sola skill. No se invoca con un subcomando literal — el agente reconoce por lenguaje natural cuál de los tres workflows aplica:

| Workflow | Se activa cuando... | Qué hace |
|---|---|---|
| **init** | El proyecto no tiene `PROJECT.md`/`AGENTS.md`/`docs/` estructurado, o el usuario pide arrancar documentación desde cero. | Corre el cuestionario ([08](08-cuestionario-init.md)), crea `AGENTS.md`/`CLAUDE.md` ([02](02-agents-claude-md-canon.md)), `ENGINEER.md` ([04](04-engineer-md-especificacion.md)), `PROJECT.md` vacío o poblado por inferencia si el proyecto ya tiene código ([03](03-project-md-especificacion.md)), la taxonomía de `docs/` ([06](06-taxonomia-docs.md)) e `INDEX.md` por carpeta ([07](07-index-md-especificacion.md)). |
| **update** | Ya existe la estructura y el agente detecta drift (código nuevo sin reflejo en `PROJECT.md`/`INDEX.md`), o el usuario pide explícitamente refrescar los derivados. | Revisa `PROJECT.md` en busca de información nueva que deba reflejarse en `PRODUCT.md`/`DESIGN.md`/`ENGINEER.md`, y los actualiza. Nunca reescribe `PROJECT.md` en este workflow — solo lee de él. |
| **organizar** | El usuario pide explícitamente poner en orden `PROJECT.md` (típicamente porque hizo varios braindumps seguidos y el archivo se volvió difícil de navegar). | Reordena, categoriza y hace housekeeping de `PROJECT.md` **sin eliminar ni resumir contenido**. Ver reglas exactas en [03-project-md-especificacion.md](03-project-md-especificacion.md). |

## Por qué no es un subcomando literal

Se consideró un formato tipo `/project-doc init`, pero el usuario prefiere que la skill entienda la intención directamente desde una petición natural ("ayúdame a montar la documentación de este proyecto", "actualiza los docs con lo que hicimos hoy", "el PROJECT.md ya está muy desordenado, ponlo en orden"). Esto reduce fricción de adopción para colegas que no memorizan comandos de skills.

## Choque con la skill nativa `init`

Existe una skill nativa de Claude Code llamada `init`: *"Initialize a new CLAUDE.md file with codebase documentation"*. Decisión: `project-doc` **no** se llama `init` ni intenta redefinir esa skill nativa. Es una skill separada, con su propio nombre y trigger, que hace un trabajo más amplio (no solo `CLAUDE.md`, sino toda la jerarquía documental). Si en el futuro se empaqueta en un marketplace privado, esto evita colisión de nombre con el marketplace público de Anthropic.

## Abierto / sin pilotar

- No se ha probado en un proyecto real si el reconocimiento por lenguaje natural es suficientemente confiable para distinguir `update` de `organizar` cuando el usuario pide algo ambiguo como "arregla el PROJECT.md". Puede requerir una pregunta de desambiguación la primera vez que ocurra.
- El criterio de "detecta drift" en `update` no está especificado a nivel de implementación (¿cómo sabe el agente que hay drift sin releer todo el código en cada sesión?). Queda pendiente para la fase de construcción de la skill.
