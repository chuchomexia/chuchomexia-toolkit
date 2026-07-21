# DESIGN.md y DESIGN.agent.md — especificación

## Separación de responsabilidades

`DESIGN.md` es el resumen canónico del sistema visual. `DESIGN.agent.md` es su versión operativa para agentes: una o dos páginas que se carga solo en tareas visuales, de UX o accesibilidad.

`DESIGN.agent.md` debe incluir únicamente principios no negociables, sistema visual dominante, requisitos de accesibilidad, estados de interacción y enlaces al detalle. No debe duplicar catálogos, ejemplos o patrones extensos.

## Fuente de detalle

`docs/design/` contiene patrones detallados, catálogo de componentes, ejemplos, wireframes y decisiones visuales. Cada carpeta debe tener un `INDEX.md` corto que oriente al archivo pertinente.

## Alcance

Mantener aquí tokens, tipografía, espaciado, patrones de componente, estados y reglas visuales. El producto y alcance funcional viven en `PRODUCT.md`.

## Mantenimiento

El agente deriva y actualiza estos documentos desde evidencia de código y UI. Si `DESIGN.agent.md` y `DESIGN.md` entran en conflicto, `DESIGN.md` y los documentos específicos de `docs/design/` son la referencia para corregir el resumen.
