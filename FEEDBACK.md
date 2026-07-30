# Feedback de agentes sobre las skills de este marketplace

Este repo no tiene telemetría: nadie se entera si una skill dio una instrucción incorrecta,
incompleta, o si un agente tuvo que trabajar en contra de lo que decía. La única señal posible
es que el propio agente, al detectarlo, deje constancia. Este documento es el protocolo — cada
`SKILL.md` de este marketplace enlaza aquí en vez de repetirlo.

## Cuándo dejar feedback

Cuando, usando cualquier skill de este repo, el agente:

- siguió una instrucción y el resultado fue incorrecto o el usuario lo corrigió,
- encontró un hueco (la skill no cubría un caso que sí ocurrió),
- tuvo que improvisar o contradecir la skill para lograr el resultado correcto,
- detectó una contradicción entre dos partes de la misma skill o entre skills.

No es para dudas de una sola vez ni para pedir features especulativas — es para fricción real
que ocurrió en una sesión real.

## Cómo dejarlo: issue en GitHub

```bash
gh issue create --repo chuchomexia/project-doc-skill \
  --title "[<nombre-skill>] <resumen corto del problema>" \
  --label skill-feedback \
  --body "**Qué decía la skill:** ...
**Qué pasó / qué esperaba el usuario:** ...
**Qué hice en su lugar:** ...
**Archivo o sección relevante:** plugins/<skill>/skills/<skill>/... "
```

Si `gh issue create --label skill-feedback` falla porque el label no existe todavía en el repo
(pasa la primera vez), créalo una sola vez y reintenta:

```bash
gh label create skill-feedback --color FFA500 \
  --description "Feedback generado por un agente al usar una skill del marketplace"
```

Si `gh` no está autenticado o no está disponible en el entorno del agente, no inventes una
alternativa silenciosa: dile al usuario en la respuesta que hay feedback pendiente y sugiere que
abra el issue manualmente en
`https://github.com/chuchomexia/project-doc-skill/issues/new?labels=skill-feedback`, con el mismo
contenido de la plantilla de arriba.

## Qué hace Jesús con esto

Revisar issues con `skill-feedback` periódicamente (o filtrar por label) y decidir si el gap se
corrige en la skill. No hay analítica agregada — es una bitácora de casos concretos, no métricas
de uso.
