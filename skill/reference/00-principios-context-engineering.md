# Principios de context engineering

Estos cuatro principios guían todas las decisiones de esta carpeta. Cualquier archivo, taxonomía o regla que se proponga debe justificarse contra estos principios, no al revés.

## 1. Contexto estructurado

Jerarquía clara, categorización y etiquetado explícito reducen la ambigüedad. Un contexto mal estructurado produce agentes que actúan de forma inconsistente entre sesiones — el mismo problema en dos días distintos puede resolverse de dos formas distintas si el contexto que lo describe no tiene una forma predecible.

Aplicación en esta metodología: la jerarquía `PROJECT.md → PRODUCT.md / DESIGN.md / ENGINEER.md` (ver [03](03-project-md-especificacion.md), [04](04-engineer-md-especificacion.md), [05](05-design-md-especificacion.md)) y la taxonomía fija de `docs/` (ver [06](06-taxonomia-docs.md)) existen para esto.

## 2. Mejorar findability

El objetivo es que el agente tenga a la mano la información correcta y no gaste pasos innecesarios buscándola. Esto se logra, entre otras cosas, limitando cuánta información irrelevante se procesa por sesión.

Aplicación: `INDEX.md` en cada carpeta documental (ver [07](07-index-md-especificacion.md)), archivos cortos con nombres directos, evitar carpetas cuyo propósito nadie recuerda (la razón real por la que se elimina `contracts/` en la taxonomía: si ni el propio equipo recuerda para qué sirve, no está ayudando a la findability).

## 3. Alinear al modelo mental del usuario

Estructurar el contexto alrededor de cómo el usuario describe naturalmente el problema, no alrededor de categorías técnicas abstractas. Etiquetas inconsistentes dificultan que el agente mapee correctamente el lenguaje del usuario a la salida esperada.

Aplicación: `PROJECT.md` (ver [03](03-project-md-especificacion.md)) está diseñado explícitamente para que el humano vuelque su pensamiento tal como lo tiene en la cabeza — sin forzar estructura de entrada — porque forzar estructura en el momento de la captura rompe el modelo mental de quien escribe.

## 4. Diseñar la memoria

Definir qué se recuerda, cómo se indexa y cuándo se recupera. Reglas de scope previenen que historial irrelevante contamine interacciones futuras — este es el principio que más tensión generó en el diseño de esta metodología (ver la discusión resuelta en [03-project-md-especificacion.md](03-project-md-especificacion.md) sobre *context attention*: contenido desactualizado que compite por atención con contenido vigente degrada la calidad de todo lo demás, no solo la de sí mismo).

## Prior art a revisar antes de publicar la skill

Antes de dar por definitivo el diseño de memoria de esta metodología, vale la pena revisar la skill nativa `anthropic-skills:consolidate-memory` ("reflective pass over your memory files — merge duplicates, fix stale facts, prune the index"). No se revisó a fondo durante el diseño de `project-doc-skill` y hay riesgo real de estar reinventando un patrón que Claude Code ya resuelve de otra forma. **Pendiente, sin pilotar.**
