# DESIGN.md — especificación

## Alcance

Solo sistema de diseño **visual**: tokens (color, espaciado, tipografía), fuentes, radios, patrones de componente, estados (loading/empty/error), y lo estrictamente inseparable de una decisión visual (ej. "los estados de carga siempre muestran skeleton, nunca spinner, porque..." — la razón es de producto, pero la regla es visual y no tiene sentido separarla).

Todo lo demás de producto (qué hace el producto, para quién, alcance funcional) vive en `PRODUCT.md`, no aquí. Esta separación se acordó explícitamente para no solapar `DESIGN.md` con `PRODUCT.md` ni con `PROJECT.md`.

## Origen de la idea

Inspirado en la referencia que aportó el usuario de un `DESIGN.md` estilo Google Stitch — una guía del sistema de diseño definida para el proyecto. La versión original incluía algo de producto; en esta metodología se recorta deliberadamente para evitar el solapamiento.

## Quién escribe qué

Igual que `ENGINEER.md`: es un derivado, mantenido por el agente a partir de `PROJECT.md` y de evidencia real del código/UI (wireframes, prototipos en `docs/design/`, ver [06-taxonomia-docs.md](06-taxonomia-docs.md)). El humano no lo edita a mano.

## Cuándo madurarlo

Consistente con la lección ya validada en Colsanitas (`07-lecciones-aprendidas.md` del paquete metodológico general): `DESIGN.md` no debería exigirse desde el día cero. Generarlo bien requiere evidencia funcional y visual real. Se recomienda crearlo vacío o mínimo en `init`, y madurarlo durante el proyecto conforme haya decisiones de diseño reales que documentar — el workflow `update` es el que lo va llenando.

## Abierto / sin pilotar

- No se ha validado en la práctica si "lo estrictamente inseparable de producto" es un límite claro de aplicar consistentemente sesión tras sesión, o si en la práctica el agente termina colando contenido de producto de todos modos. Vale la pena revisar esto tras el primer piloto.
