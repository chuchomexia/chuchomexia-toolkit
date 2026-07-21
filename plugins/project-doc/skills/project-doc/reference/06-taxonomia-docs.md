# Taxonomía documental por ámbito

## Raíz del monorepo

`docs/` raíz contiene solo material transversal:

- `adrs/`: decisiones que afectan varios frentes o el repositorio completo.
- `slices/`: entregables y cambios transversales.
- `ideas/` y `qa/`: opcionales, solo si su alcance es transversal.

## Frentes

Cada frente conserva su documentación propia en `<frente>/docs/`. Puede usar categorías adecuadas a su naturaleza: `design/`, `flows/`, `domains/`, `operations/`, `slices/` o equivalentes con propósito explícito.

No crear hubs raíz que dupliquen índices de los frentes. El índice raíz enlaza directamente a `<frente>/docs/INDEX.md`.

## Reglas de ownership

- Si solo un frente consume y mantiene el contenido, el documento pertenece a ese frente.
- Si coordina dos o más frentes, pertenece a `docs/` raíz.
- Los contratos compartidos son transversales; las guías de consumo son propias del consumidor.
- Toda carpeta tiene propósito y límite explícitos en su índice.
