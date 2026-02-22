Use "uv" for python commands

### Normas de Formato en Markdown
- Al escribir archivos Markdown, siempre deja una **línea en blanco adicional (un salto de línea vacío)** entre cada párrafo y alrededor de los bloques de ecuaciones matemáticas (`$$...$$`). Esto garantiza que los motores de renderizado como MkDocs interpreten correctamente los párrafos separados y puedan renderizar MathJax de forma óptima.

### Estructura de Archivos "teoria"
- Al crear o modificar un archivo `teoria.md` (o similar que explique la resolución teórica de un ejercicio), **asegúrate siempre de incluir el enunciado completo del problema al principio del documento**, antes de comenzar con el desarrollo de la solución.

- Deben haber por lo menos dos encabezados: "Interpretación del Enunciado" y "Solución del Ejercicio" (este puede hacerse en varios incisos).

- **Incisos de ejercicios:** Si la resolución de un problema está dividida estructuralmente en varios incisos (por ejemplo: "a)", "1.", etc.), **asegúrate de re-copiar textualmente el enunciado específico de ese sub-inciso bajo el subtítulo H2 correspondiente**, en formato blockquote (`> ...`). De este modo, el lector no necesitará retroceder ni hacer scroll-up continuo para refrescar qué pedía el apartado que se está resolviendo.

### Listas Desordenadas (Unordered Lists)
- Para que las viñetas y listas se rendericen de forma apropiada en MkDocs sin fusionarse con párrafos adjuntos, **siempre deja un salto de línea (espacio) antes de comenzar cualquier lista `(- )`**. Adicionalmente, inserta **un salto de línea en blanco entre cada uno de los ítems de la lista**.

### Observaciones y Notas (Admonitions)
- Toda observación complementaria, nota teórica o profundización que se desee incluir en los apuntes, debe estar contenida **SIEMPRE dentro de un bloque desplegable (collapsible)** para no saturar visualmente el flujo principal de lectura. En MkDocs, esto se construye obligatoriamente empezando el bloque con `??? info "Título de la Observación"` seguido de un salto de línea y el contenido indentado con 4 espacios ininterrumpidamente. No utilices los alert blocks expandidos (`!!!`) para estos casos.