# Transcripción — origen de la idea de PROJECT.md

Fragmento de entrevista (video, transcripción parcial provista por el usuario) que originó el concepto de un archivo único, exhaustivo, "fuente de la verdad" del proyecto — llamado `soul.md` en la conversación original.

> What's great is that for every single meeting that we had about the Zen, we recorded every single one and I dumped the transcripts into a soul.md file specifically for that project. And I wanted to treat that soul.md file as the source of truth and exhaustive glossary of this project. I wanted this file to have as much context as possibly possible so that it can feed all the future decisions that we need to make regarding this project.
>
> [...] Instead, just record everything and just dump it all in a soul.md file and then use that as the basis for everywhere that you want to go afterwards.
>
> Exactly. I really think that's the future. And we also wrote a manifesto for ourselves when we were working on this project. And of course, we dumped that manifesto into the soul.md. As much context that we can give the agent, the better.
>
> [...] It is nothing more than a simple MD file and it has all the context and you can also break down MD files. You can create a hierarchy of the different MD files that you want. If you want to have like a design MD file specifically for your design and how to address design you can have a separate MD for your manifesto. [...] You can dump it all in one single file. I haven't really seen one method being better than the other, but that's why we're all experimenting and figuring out if there's a better way. Overall, I think capturing as much information as possible and share that information with your agent is the best way to build software moving forward.

## Qué tomamos de esto

- La idea central: un archivo que acumula **todo** el contexto crudo del proyecto (reuniones, decisiones, manifiestos, notas) sin curar de entrada — el humano vuelca, no resume.
- La idea de jerarquía: ese archivo puede partirse en archivos especializados (diseño, producto, etc.) cuando crece.

## Qué adaptamos, no copiamos

- El video no resuelve cómo evitar que el archivo se vuelva ilegible con el tiempo. Nuestra adaptación (ver [03-project-md-especificacion.md](../03-project-md-especificacion.md)) agrega un workflow de **estructuración por el agente, sin pérdida de contenido**, que el material original no cubre.
- No copiamos la idea de "un archivo sirve igual que varios" tal cual — decidimos explícitamente la jerarquía PROJECT.md → PRODUCT.md/DESIGN.md/ENGINEER.md porque coincide mejor con cómo ya trabajamos (ver conversación de diseño).
