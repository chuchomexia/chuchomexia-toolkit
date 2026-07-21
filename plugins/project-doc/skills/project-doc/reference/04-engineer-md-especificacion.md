# ENGINEER.md — especificación

## Rol

Guía técnica transversal del repositorio. Existe una sola por raíz Git y complementa el router de agentes.

## Monorepos

Debe incluir mapa de frentes, comandos ejecutables desde raíz, contratos entre frentes, fuentes de verdad y estrategia de verificación transversal. El detalle exclusivo de un frente vive en `<frente>/docs/`, no en otro `ENGINEER.md`.

## Contenido

- Comandos verificados por frente.
- Arquitectura y flujo de datos de alto nivel.
- Ownership de código, datos, contratos y documentación.
- Fuentes de verdad.
- Verificación por tipo de cambio.
- Convenciones compartidas.

Si un frente se convierte en un repositorio Git independiente, pasa a tener su propio canon raíz.
