---
name: anti-slop
description: >
  Aplica un filtro anti-"IA slop" a cualquier texto que Claude escriba o revise —
  emails, reportes, posts, specs, mensajes, código con comentarios, lo que sea —
  para que no suene a IA genérica. Úsala SIEMPRE que la salida sea texto en prosa
  destinado a un humano, no solo cuando el usuario lo pida explícitamente. Cubre
  inglés y español (los patrones delatores cambian por idioma). Dispara también
  con frases como "que no suene a IA", "hazlo sonar más humano", "revisa el tono",
  "esto suena a ChatGPT", "quita el em dash", "no me gusta cómo quedó el texto",
  o cuando el usuario pida un borrador/redacción/copy/reporte de cualquier tipo.
  Incluye un validador (scripts/validate.py) que detecta patrones delatores
  automáticamente y da un score — úsalo para autocorregir antes de entregar.
---

# Anti-slop: escribir como humano, no como IA

## Por qué existe esto

Los modelos de lenguaje convergen hacia un estilo reconocible: simetría excesiva,
contrastes tipo "no es A, es B", cierres redondos que repiten lo ya dicho, listas
donde cabría prosa, y un vocabulario "inflado" (crucial, robusto, multifacético).
No es que cada patrón sea malo en sí — es que su repetición y acumulación es lo
que delata el texto como generado. El objetivo de esta skill no es prohibir
palabras sueltas por decreto, sino que el texto que Claude entrega suene a alguien
que sabe lo que dice y lo dice directo, sin la muletilla constante de "pulir" cada
frase con una estructura de manual.

## Cuándo aplica

Cualquier texto en prosa que un humano vaya a leer como si lo hubiera escrito
una persona: emails, mensajes, reportes, posts, specs, resúmenes, comentarios de
código dirigidos a otro dev, copy de producto. No aplica a estructuras que son
legítimamente listas por naturaleza (checklists técnicos, tablas de datos,
changelogs) — ahí el formato de lista no es el problema.

## Flujo de trabajo

1. Escribe el borrador normalmente, priorizando que diga algo concreto.
2. Antes de entregarlo, revisa mental o literalmente contra `reference/patterns_en.md`
   o `reference/patterns_es.md` según el idioma (ver "Las tres capas" abajo).
3. Si el texto es largo (>150 palabras) o el usuario pidió explícitamente que
   "no suene a IA", corre el validador:
   ```
   python scripts/validate.py <archivo_o_texto> --lang es
   ```
   (o `--lang en`, o `--lang auto` para que lo detecte). Lee el reporte y corrige
   lo que el script marque con severidad alta antes de considerar el texto terminado.
4. No optimices el score a cero mecánicamente — el validador es una señal, no la
   meta. Un texto puede tener un "además" legítimo. Usa juicio.

## Las tres capas para detectar (o evitar) el estilo IA

Cuando revises un texto, pregúntate si tiene estas tres capas apiladas:

- **Contraste de manual**: "No es A, es B" / "It's not A — it's B". Útil una vez
  cada mil palabras; sospechoso si aparece más de una vez en un texto corto.
- **Orden artificialmente simétrico**: listas o pasos donde el contenido cabría
  perfectamente en una frase con "y", pero se separó en bullets para que se vea
  "organizado".
- **Cierre redondo**: una frase final que resume lo que ya se dijo en vez de
  aportar algo nuevo ("En resumen...", "Overall...", "En pocas palabras...").

Si un texto tiene las tres, reescríbelo. Si tiene una, probablemente está bien.

## Reglas prácticas (aplican a ambos idiomas)

- Preferir prosa a bullets salvo que el contenido sea genuinamente una lista
  (pasos secuenciales, opciones paralelas, datos tabulares).
- Variar la longitud de las frases. Si todas las oraciones de un párrafo miden
  parecido, se nota artificial — meter una frase corta rompe el patrón.
  Es simplemente cómo escribe la gente cuando no está siguiendo una plantilla.
- No cerrar cada párrafo o cada texto con una síntesis. Terminar donde termina
  la idea, no donde "debería" terminar un ensayo.
- Evitar vocabulario inflado por defecto (ver listas en las referencias) salvo
  que sea el término técnico correcto para el contexto.
- Evitar encadenar conectores de transición como muletilla ("además,", "por otro
  lado,", "furthermore,") al inicio de frase seguido. Uno cada tanto es normal;
  uno por párrafo es plantilla.
- El em dash como aclaración retórica ("X — que es Y — hace Z") es un patrón muy
  marcado en inglés generado. Si aparece, casi siempre se puede reemplazar con
  una coma, un punto, o reestructurar la frase.
- Los subtítulos en forma de pregunta ("¿Cómo funciona esto?") son un tic de
  contenido "optimizado para IA", no de escritura natural — evitarlos salvo que
  el formato sea literalmente un FAQ.

## Idioma: diferencias clave

Los patrones delatores no son los mismos en inglés y en español — ver el detalle
completo y las listas de frases en:

- `reference/patterns_en.md` — patrones en inglés (dashes, "Overall...", vocabulario inflado)
- `reference/patterns_es.md` — patrones en español (fórmulas contrastivas, subtítulos-pregunta, cierres tipo "guía definitiva")

Lee el archivo del idioma correspondiente cuando quieras el listado exhaustivo
de frases a evitar o ejemplos de reescritura. No hace falta cargarlos si ya
tienes claro el patrón — están ahí para consulta detallada, no como lectura
obligatoria en cada uso.

## El validador

`scripts/validate.py` es un chequeo determinístico, no un juicio de calidad.
Detecta:

- Frases delatoras exactas (lista curada por idioma).
- Densidad de conectores de transición.
- Densidad de bullets vs. prosa.
- Simetría de longitud de oraciones (varianza baja = sospechoso).
- Uso de em dash como aclaración retórica.
- Vocabulario inflado.

Uso:

```
python scripts/validate.py archivo.md --lang es
python scripts/validate.py archivo.md --lang en
python scripts/validate.py archivo.md --lang auto
echo "texto suelto para revisar" | python scripts/validate.py - --lang auto
```

El script imprime cada hallazgo con línea y contexto, y un score final
(0 = limpio, mientras más alto peor). No es una nota objetiva de "qué tan
humano" es el texto — es una lista de señales para revisar con criterio. El
script termina con exit code 1 si el score supera el umbral (por defecto 8,
configurable con `--threshold`), útil si se quiere encadenar en un pipeline.

Trátalo como un linter de estilo, no como un gate automático de calidad: un
texto puede pasar el validador y seguir sonando a IA por razones que no son
detectables por regex (argumentos genéricos, falta de especificidad, tono
demasiado seguro). Y puede fallar el validador por un uso legítimo y puntual
de una de las frases. El script ayuda a no repetir los tics más obvios; el
juicio final es tuyo.

## Feedback

Si esta skill marcó como "delator" algo que en realidad era un uso legítimo, dejó
pasar un patrón obvio de IA, o el score del validador no coincidió con tu
criterio, abre un issue en el repo del marketplace (protocolo completo en
`FEEDBACK.md` en la raíz del repo, si está presente en tu checkout):

```bash
gh issue create --repo chuchomexia/project-doc-skill \
  --title "[anti-slop] <resumen corto>" --label skill-feedback \
  --body "Qué decía la skill / qué pasó / qué hiciste en su lugar"
```

Si `gh` no está disponible o autenticado, dile al usuario que hay feedback pendiente y sugiere
abrirlo manualmente en `github.com/chuchomexia/project-doc-skill/issues/new?labels=skill-feedback`.
