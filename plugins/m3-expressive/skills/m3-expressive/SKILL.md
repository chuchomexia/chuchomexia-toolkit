---
name: m3-expressive
description: >
  Diseña o corrige cualquier interfaz, componente, pantalla, layout o sistema de diseño usando
  Material 3 Expressive de Google como filosofía rectora — no solo su versión "M3" clásica.
  Úsala siempre que el trabajo toque UI/UX: crear un componente nuevo, maquetar una pantalla,
  definir un design system, elegir colores/tipografía/formas/spacing/motion, escribir CSS o
  componentes de un framework (React, Vue, Compose, Flutter, SwiftUI, HTML/CSS puro), revisar o
  auditar una interfaz existente, o cuando el usuario pida que algo se vea "más expresivo",
  "con más personalidad", "menos genérico" o "con hero moments". Aplica incluso si el usuario no
  menciona "Material" explícitamente: si la tarea es de interfaz visual, esta skill debe
  cargarse por defecto salvo que el usuario pida explícitamente otro sistema de diseño.
---

# M3 Expressive — filosofía rectora para interfaces

Este skill empaqueta una guía completa (13 módulos JSON + cheatsheet + un módulo complementario)
sobre Material 3 y su evolución M3 Expressive, para que uses sus principios como referencia
rectora al diseñar o corregir cualquier interfaz — no como un tema visual que se copia y pega.

Fuente principal: [m3.material.io/blog/building-with-m3-expressive](https://m3.material.io/blog/building-with-m3-expressive),
más la documentación oficial de foundations, styles y components de m3.material.io
(lista completa en `references/12-sources.json`).

## Por qué esto importa (y por qué no es un reskin)

M3 Expressive **no es una versión nueva del sistema** ("no es M4"): es un conjunto de tácticas,
componentes nuevos y un motor de motion basado en física, dentro de M3. Está respaldado por
46 estudios y más de 18,000 participantes: los diseños expresivos se perciben con más energía,
creatividad y calidez, y en ciertas pantallas la gente encontró elementos clave hasta 4 veces
más rápido. La expresión útil no es decoración — refuerza jerarquía, utilidad y conexión
emocional. Cárgala pensando en eso, no en "poner formas bonitas".

## Regla de oro: Material dirige, el proyecto es evidencia

Cuando trabajes dentro de un proyecto real, Material define la filosofía, la estructura, el
layout, los componentes, los estados, la accesibilidad y la expresividad. El proyecto aporta
identidad de marca, contenido, restricciones técnicas y elementos rescatables — pero **su
implementación visual actual no se asume correcta solo porque ya existe**. Audítala.

Para cada elemento del proyecto (color, tipografía, radio, espaciado, componente), clasifícalo en:

| Decisión | Cuándo |
|---|---|
| `preserve` | Marca, fuentes legibles, contenido, restricciones técnicas reales, comportamiento correcto |
| `map_to_material_role` | Un color o token existente es válido pero le falta semántica de rol M3 |
| `refine` | Casi correcto pero inconsistente (radios arbitrarios, spacing improvisado) |
| `replace` | Contradice Material, accesibilidad o la jerarquía necesaria |
| `create` | No existe nada equivalente y Material lo requiere |

Si dos fuentes entran en conflicto, este es el orden de prioridad:
**accesibilidad y semántica > intención del usuario > principios M3 > identidad/restricciones
reales del proyecto > implementación existente > protocolo derivado de este skill > preferencia
estética.**

## Empieza aquí

1. Lee `references/01-agent-contract.json` — reglas duras y anti-alucinación. Son no negociables.
2. Lee `references/02-philosophy-and-tactics.json` — las 7 tácticas expresivas y el modelo de
   intensidad (0 funcional → 3 hero). Esto es el corazón del skill; resumen abajo.
3. Según la tarea, carga el resto según la tabla de "Dónde buscar". No necesitas cargar los 14
   archivos siempre — usa los perfiles de carga de `references/00-manifest.json`
   (`loading_profiles`: `minimum_orientation`, `create_component`, `visual_system_only`,
   `layout_only`, `audit_result`, `implement_material_in_project`, etc.)
4. Si vas a crear un componente nuevo desde cero, sigue el protocolo de 10 fases en
   `references/10-generation-protocol.json`.
5. Antes de afirmar fidelidad exacta a Material, revisa `references/13-known-gaps-and-roadmap.json`
   — hay valores (springs exactos, geometría de las 35 formas) que son aproximaciones, no specs
   oficiales palabra por palabra.

## Las 7 tácticas expresivas (resumen — detalle en `02-philosophy-and-tactics.json`)

1. **Variedad de formas** — combina formas redondas y cuadradas con intención; rompe el patrón
   para enfatizar, no para decorar todo.
2. **Color rico y matizado** — usa roles (primary/secondary/tertiary/superficies tonales) para
   jerarquía, nunca valores de color directos ni tonos que hagan que texto y controles se mezclen.
3. **Tipografía que guía la atención** — estilos "emphasized" en titulares o acciones clave, no
   en todo el texto.
4. **Contención para enfatizar** — agrupa lo relacionado; no fragmentes cada dato en su propia
   card ni le des la misma prominencia a todo.
5. **Motion fluido y natural** — springs espaciales (posición, escala, rotación, forma) con
   overshoot permitido; springs de efectos (color, opacidad) SIN rebote nunca. Respeta
   `prefers-reduced-motion`.
6. **Flexibilidad de componentes** — el mismo patrón no tiene que escalar igual en los 5
   breakpoints (compact/medium/expanded/large/extra-large); a veces hay que revelar, dividir,
   redimensionar, reposicionar o sustituir el componente.
7. **Hero moments** — combina 2-4 tácticas coordinadas en 1-2 momentos por producto o flujo.
   Nunca en acciones destructivas o repetitivas. Si todo es hero, nada lo es.

Regla de coordinación: elige entre 2 y 4 ejes expresivos principales por componente o pantalla.
Puntuar alto en todo produce ruido, no expresividad.

## Restricciones duras (de `01-agent-contract.json`, aplican siempre)

- No llames al sistema "M4"; es una evolución de M3.
- No uses valores de color directos dentro de un componente — todo mapea a roles.
- No codifiques tipografía, forma, elevación, spacing o motion sin pasar por una capa de tokens.
- No dependas solo de color, forma, motion o posición para comunicar estado — mínimo dos señales
  cuando la accesibilidad lo requiere.
- No sacrifiques legibilidad, contraste, tamaño de objetivo, foco o navegación por teclado/lector
  de pantalla por expresividad.
- No apliques rebote a color u opacidad — el overshoot es solo para movimiento espacial.
- No llenes toda la interfaz de hero moments.
- No diseñes para un dispositivo específico — diseña para el espacio de ventana y sus breakpoints.
- No uses title case en texto de UI — sentence case salvo términos de marca.
- Si un valor exacto no está confirmado como oficial, decláralo como aproximación o token de
  producto — nunca lo presentes como spec oficial.

## Mapa de referencias

| Necesitas | Archivo |
|---|---|
| Reglas duras y anti-alucinación | `references/01-agent-contract.json` |
| Filosofía y las 7 tácticas | `references/02-philosophy-and-tactics.json` |
| Arquitectura de tokens (capas, naming) | `references/03-token-architecture.json` |
| Roles de color y sistema tipográfico | `references/04-color-and-typography.json` |
| Forma, morphing, motion y límites de fidelidad | `references/05-shape-and-motion.json` |
| Spacing, elevación, iconos | `references/06-spacing-elevation-icons.json` |
| Breakpoints y layouts canónicos | `references/07-layout-adaptive.json` |
| UX writing, estados, accesibilidad | `references/08-content-and-accessibility.json` |
| Catálogo de 36 componentes + 14 actualizaciones expresivas | `references/09-components-catalog.json` |
| Inventario humano rápido de componentes | `references/COMPONENTS-CHEATSHEET.md` |
| Protocolo de 10 fases para inventar un componente | `references/10-generation-protocol.json` |
| Criterios de aceptación y soporte de plataforma | `references/11-quality-gates-and-platforms.json` |
| Fuentes oficiales (citar siempre que afirmes un dato) | `references/12-sources.json` |
| Huecos conocidos y honestidad sobre fidelidad | `references/13-known-gaps-and-roadmap.json` |
| Motion physics (springs), 35 formas, Theme Builder, Figma kit | `references/14-motion-shape-and-tools.md` |

## Al entregar una solución, deja explícito

No hace falta un reporte largo, pero sí sé explícito en el código o la respuesta sobre:
qué principios Material guiaron la solución, qué se rescató del proyecto tal cual, qué se
corrigió porque interpretaba Material mal, y qué valores son aproximaciones (no specs oficiales
citadas palabra por palabra). Esto evita que el resultado se presente con más fidelidad de la
que realmente tiene — ver `references/13-known-gaps-and-roadmap.json` para el balance honesto
de qué tan lejos llega este skill (alto en filosofía/estructura/proceso, medio en fidelidad
visual exacta sin referencias, bajo-medio en fidelidad de motion/pixel).

## Feedback

Si esta skill te dio una instrucción incorrecta o incompleta, presentó una aproximación como si
fuera spec oficial, o tuviste que ir en contra de ella para lograr el resultado correcto, abre un
issue en el repo del marketplace (protocolo completo en `FEEDBACK.md` en la raíz del repo, si
está presente en tu checkout):

```bash
gh issue create --repo chuchomexia/project-doc-skill \
  --title "[m3-expressive] <resumen corto>" --label skill-feedback \
  --body "Qué decía la skill / qué pasó / qué hiciste en su lugar"
```

Si `gh` no está disponible o autenticado, dile al usuario que hay feedback pendiente y sugiere
abrirlo manualmente en `github.com/chuchomexia/project-doc-skill/issues/new?labels=skill-feedback`.
