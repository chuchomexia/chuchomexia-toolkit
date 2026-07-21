# Invocación y workflows

## Paso cero: resolver alcance

Antes de cualquier workflow, localizar la raíz Git y detectar frentes (`apps/`, `packages/`, `frontend/`, `backend/`, etc.). No asumir que cada carpeta es un repositorio independiente. Cargar [10-monorepos-y-ownership.md](10-monorepos-y-ownership.md) cuando exista más de un frente.

## Workflows

### init

1. Resolver topología y ownership.
2. Ejecutar el cuestionario.
3. Crear un solo par `AGENTS.md`/`CLAUDE.md` y un solo `ENGINEER.md` en la raíz Git.
4. Crear documentos de producto/dominio en raíz.
5. Crear `docs/` transversal y `docs/` por frente según ownership.
6. Crear `DESIGN.md` en el frente propietario de UI.
7. Crear índices y validar enlaces.

### update

Revisar drift por ámbito. Actualizar el documento propietario; no crear una copia en otro frente. Si cambia ownership, mover el archivo, reparar enlaces y registrar un ADR.

### organizar

Ordenar `PROJECT.md` sin eliminar ni resumir contenido. No cambia ownership documental salvo petición explícita.

## Validación obligatoria

- No hay `AGENTS.md`, `CLAUDE.md` o `ENGINEER.md` duplicados dentro del mismo repositorio Git.
- Todos los enlaces locales resuelven.
- Todos los índices permanecen debajo de 200 líneas.
- La raíz no contiene documentación exclusiva de un frente y viceversa.
