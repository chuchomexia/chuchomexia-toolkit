# Recurso 14 — Motion physics, sistema de forma y herramientas (complemento 2026-07-21)

`authority: derived_from_secondary_sources` — Este archivo no viene de la documentación oficial línea por línea (esa sigue en `05-shape-and-motion.json` y `12-sources.json`), sino de reportaje técnico y comunidad sobre M3 Expressive. Úsalo para llenar los huecos P1 que `13-known-gaps-and-roadmap.json` marcaba como pendientes: springs concretos, escala de forma, y herramientas de generación de tema. Si necesitas el valor numérico exacto y certero, verifica siempre contra `https://m3.material.io/styles/motion/overview` y `https://m3.material.io/styles/shape/overview` antes de shippear a producción — esto es orientación, no la especificación.

## Motion physics: cómo funcionan los springs

M3 Expressive reemplaza el sistema anterior basado en curvas de easing y duración fija por un motor de física de resortes (springs). Dos propiedades controlan cada spring:

- **Stiffness (rigidez)**: qué tan rápido el resorte llega a su estado final. Más rigidez = movimiento más rápido y con más energía.
- **Damping ratio (amortiguación)**: qué tan rápido decae el rebote. `1.0` = críticamente amortiguado, sin rebote. Valores menores permiten overshoot (el elemento se pasa del destino y regresa).

### Dos familias de tokens de spring

- **Spatial springs** — para posición (x/y), rotación, escala, tamaño y radio de esquina. Aquí sí se permite overshoot; es lo que hace sentir el movimiento "vivo".
- **Effects springs** — para color y opacidad. Aquí nunca debe haber overshoot ni rebote (regla que ya está en `01-agent-contract.json` como hard constraint: "No aplicar rebote a color u opacidad").

Cada familia viene en tres velocidades: **default** (la mayoría de los casos), **fast** (elementos pequeños), **slow** (elementos grandes). Elegir la velocidad por el tamaño físico del elemento que se mueve, no por preferencia estética.

### Dos motion schemes

- **Expressive** (default recomendado por Google): damping más bajo, overshoot notorio. Bien para hero moments e interacciones clave.
- **Standard**: damping más alto, casi sin rebote. Mejor para contextos utilitarios, productividad y tareas repetitivas de alta frecuencia.

Regla práctica: si el componente se usa muchas veces por sesión (ej. checkbox de una lista larga), inclínate a Standard o a un spring effects sin overshoot. Si es un momento puntual y memorable (ej. confirmación de una acción importante), Expressive.

## Sistema de forma: 35 formas y escala de 10 pasos

- La librería de formas creció a **35 formas abstractas** (Material Shapes Library), pensadas sobre todo para morphing y elementos decorativos/hero — no para reemplazar el contenedor estándar de cada componente.
- El radio de esquina pasó de una escala fija (none/xs/s/m/l/xl/full) a una **escala granular de 10 pasos**, de 0dp (cuadrado perfecto) a full (completamente redondeado).
- Cambio importante: "fully rounded" ahora usa `full` como token — antes se calculaba como 50% del tamaño del componente. Si ves ese cálculo antiguo en un proyecto, es candidato a `refine` o `replace`, no a `preserve`.
- El shape morphing (transición animada entre dos siluetas) usa spatial springs, nunca effects springs.

Fuente de assets: Figma Community "M3 Expressive — Shapes set" y Jetpack Compose `androidx.graphics.shapes`. Si necesitas los paths SVG exactos, ese es el gap que sigue abierto (ver `13-known-gaps-and-roadmap.json`).

## Herramientas para generar tema y assets

- **Material Theme Builder** (`https://material-foundation.github.io/material-theme-builder/`, también plugin de Figma) — genera un esquema de color completo (paletas tonales + roles) a partir de un color semilla, imagen o wallpaper. Variante **"Expressive"** del generador: paletas de croma medio, tono pastel, con el hue de la paleta primaria deliberadamente distinto al seed para dar variedad — es la opción más alineada con esta filosofía frente a variantes más neutras (Fidelity, Content, etc.).
  - Exporta a: set de estilos Figma, Design System Package (DSP), código Android (Compose o Views). No exporta CSS/web tokens directo; para web hay que mapear los roles exportados a variables propias.
- **Figma Material 3 Design Kit** (`https://www.figma.com/community/file/1035203688168086460`) — componentes, estilos de color, tipografía y layouts ya alineados con Expressive; incluye los componentes nuevos (button groups, FAB menu, split button, loading indicator) y soporte XR (paneles y diálogos espaciales).
- **Material Web Components** — están en modo mantenimiento. Si el proyecto es web (no Android/Compose), trátalo como referencia de tokens, no como dependencia de producción a ocupar sin verificar estado actual.

## Nota de honestidad

Estos datos técnicos (stiffness, damping, "10 pasos", nombres de variantes del Theme Builder) vienen de reportaje de terceros y documentación de desarrollador, no de una cita directa palabra por palabra de las Motion Specs oficiales. Trátalos como **aproximación de alta confianza**, no como tabla oficial. Si el proyecto necesita fidelidad pixel/spring exacta, ese sigue siendo un hueco declarado — dilo explícitamente en vez de inventar el número exacto.
