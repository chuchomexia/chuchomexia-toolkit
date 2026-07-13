# ENGINEER.md — especificación

## Rol

Complemento técnico del `AGENTS.md`/`CLAUDE.md` raíz — mismo principio que `DESIGN.md` pero para ingeniería. Existe para que el archivo raíz se mantenga corto: todo el detalle pesado de "cómo está armado el repo y cómo se trabaja en él" vive aquí, referenciado desde el raíz (ver [02-agents-claude-md-canon.md](02-agents-claude-md-canon.md), sección "Pointers documentales").

Es **generado y mantenido por el agente**, derivado de `PROJECT.md` y del código real del repo (ver sincronización en [03-project-md-especificacion.md](03-project-md-especificacion.md)). El humano no lo edita directamente.

## Contenido

- **Comandos**: dev, build, lint, test, typecheck — siempre verificados contra `package.json`/scripts reales, nunca inventados.
- **Arquitectura**: stack, capas principales, cómo fluyen las peticiones/datos a alto nivel.
- **Encarpetado**: mapa de carpetas principales y su propósito (equivalente a la sección "Project Structure & Module Organization" de [agents-md-angular-referencia.md](referencias/agents-md-angular-referencia.md)).
- **Rutas/módulos principales**: qué áreas del código son el corazón del producto vs. periféricas.
- **Convenciones de código y naming**: patrones de nombres de archivo, estilo, qué se prefiere/evita (ej. "usar `@if`/`@for`, no `*ngIf`/`*ngFor`" en el proyecto Angular de referencia).
- **Testing**: framework usado, dónde viven los specs, cuándo correrlos, expectativas de verificación por tipo de cambio (este bloque puede vivir aquí en detalle, mientras que el raíz solo lo resume).
- **Commits**: formato de mensaje, convenciones de PR.

## Por qué separado de DESIGN.md

`DESIGN.md` cubre el sistema de diseño **visual** (tokens, tipografía, patrones de componente). `ENGINEER.md` cubre cómo se construye y verifica el código. Un cambio de arquitectura no debería tocar `DESIGN.md`, y un cambio de paleta de color no debería tocar `ENGINEER.md` — mantenerlos separados evita que ambos se vuelvan un cajón de sastre.

## Abierto / sin pilotar

- No está definido con qué frecuencia el agente debe releer el código real (vs. confiar en lo que ya tiene documentado) para mantener `ENGINEER.md` fiel al estado actual del repo. Es el mismo problema de "detectar drift" mencionado en [01-invocacion-y-workflows.md](01-invocacion-y-workflows.md), sin resolver a nivel de implementación.
