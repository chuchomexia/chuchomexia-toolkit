# Notas — arquitectura de Impeccable

Fuente: [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable), consultado por fetch el 2026-07-13. Resumen generado, no cita textual del repo.

## Organización de archivos

- Carpetas específicas por herramienta/distribución (`.agents/`, `.claude/`, `.cursor/`, `.gemini/`, etc.).
- `skill/`: código principal del skill.
- `cli/`: interfaz de línea de comandos independiente.
- `plugin/`: implementaciones de plugin.
- `docs/`: documentación del proyecto.
- `tests/`: pruebas automatizadas.

## Progressive disclosure

1. **Entrada única**: `/impeccable <command>` como punto de acceso unificado.
2. **Comandos especializados**: ~23 subcomandos organizados por función (`audit`, `polish`, `critique`, etc.), no un solo archivo gigante con todo.
3. **Pinning dinámico**: el usuario puede crear atajos (`/impeccable pin audit`) para acceso directo a un subcomando frecuente.

## Separación principal / referencia

- Archivos principales generados en `init` (`PRODUCT.md`, `DESIGN.md`) — cortos, de alto uso.
- Documentación extensa vive en `docs/` y en archivos de configuración bajo `.impeccable/`, cargados solo cuando el subcomando los necesita.
- Config compartida vs. local: `.impeccable/config.json` (contexto del proyecto, versionado) vs. `config.local.json` (gitignored, preferencias por desarrollador).

## Qué tomamos para `project-doc`

- **Entrada única + subcomandos**: nuestra skill `project-doc` sigue el mismo patrón — no expone 3 skills separadas para init/update/organizar, sino una sola con reconocimiento de intención (ver [01-invocacion-y-workflows.md](../01-invocacion-y-workflows.md)).
- **Progressive disclosure**: el futuro `SKILL.md` debe ser delgado (frontmatter + índice de qué hace cada workflow) y remitir a archivos de referencia cargados bajo demanda — el mismo principio que ya aplicamos en esta carpeta de metodología (cada archivo es corto y enlaza a los demás en vez de repetir contenido). Ver [09-arquitectura-de-la-skill.md](../09-arquitectura-de-la-skill.md).
- **Config compartida vs. local**: útil para nuestro cuestionario de `init` (ver [08-cuestionario-init.md](../08-cuestionario-init.md)) — las respuestas del proyecto pueden versionarse, mientras que preferencias individuales (ej. nivel de verbosidad, si el desarrollador usa subagentes intensivamente) podrían vivir en un archivo local gitignored, evitando que preferencias personales contaminen el contexto compartido del equipo.

## Advertencia

Esto es una lectura de la arquitectura pública del repo al momento del fetch, no una copia de su código o texto. No se reproduce ningún archivo de Impeccable aquí — solo el patrón arquitectónico, que es lo que el usuario pidió tomar como inspiración.
