# DESIGN.md — especificación

## Ownership

`DESIGN.md` vive donde se implementa y mantiene el sistema visual. En un monorepo con un único frontend, la ubicación normal es `frontend/DESIGN.md`; con varias UIs, cada frente puede tener su propio `DESIGN.md` si sus sistemas visuales son realmente independientes.

No crear `DESIGN.md` en backend ni duplicarlo en raíz y frontend.

## Alcance

Tokens, tipografía, espaciado, componentes, estados, accesibilidad y reglas visuales. Producto y dominio viven en documentos raíz.

## Detalle

Patrones, catálogo, ejemplos, prototipos y referencias viven en `<frente>/docs/design/`. `DESIGN.md` permanece corto y enlaza el detalle.

## Actualización

Derivar de evidencia real de código/UI. Si cambia el frente propietario, mover el documento y registrar la decisión de ownership.
