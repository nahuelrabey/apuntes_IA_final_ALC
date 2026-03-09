---
description: Reglas de formato y estructura para la redacción de archivos markdown de teoría y demostración.
---

# Estructuración de Archivos Markdown (Teoría y Demostraciones)

Este flujo de trabajo define las reglas estrictas de redacción y formato que la IA debe adoptar al confeccionar archivos Markdown analíticos (usualmente llamados `teoria.md` o análogos en `docs/demostraciones/`).

## 1. Estructura Indispensable del Documento

1. **Cita del Enunciado**: 
   Comienza el archivo citando **textualmente el enunciado completo** dentro de un bloque quote (`> ...`).
2. **Subdivisiones Lógicas**:
   Subdivide el texto bajo los encabezados lógicos obligatorios: `## Interpretación del Enunciado` (identificación táctica) y `## Solución del Ejercicio` (desarrollo analítico).
3. **Múltiples Incisos**:
   Si existen múltiples incisos (a, b, c), retoma y copia una vez más cada micro-enunciado en un bloque quote bajo su respectivo sub-encabezado H3 (ej. `### Inciso A`).

## 2. Desarrollo Matemático y Formato

- **Deducción Paso a Paso**: Las variables matemáticas y derivaciones formales se deben explayar de modo deductivo, sin obviar el "puente lógico" entre axiomas.
- **Bloques de Ecuaciones (`$$...$$`)**: 
  Las ecuaciones de peso deben separarse en bloque. **ES EXTREMADAMENTE OBLIGATORIO** dejar una línea vacía por encima, por debajo y entre bloques de ecuaciones consecutivos para asegurar el correcto renderizado de Docusaurus y MDX. Si hay texto en la misma línea que `$$`, la compilación fallará.
- **Identación de Bloques LaTeX dentro de Admonitions**:
  Si un bloque `$$...$$` aparece dentro de un componente MDX (`<Nota>`, `<Advertencia>`, etc.), NO debe estar identado con espacios adicionales, pero debe mantener las líneas vacías. La sintaxis es puramente JSX y Markdown.
- **Listas y Viñetas**:
  Asegúrate siempre de dejar un salto de línea en blanco antes y entre medio de los ítems de cualquier enumerado para evitar condensación del hipertexto al compilar.
- **Diagramas (Mermaid)**:
  Las representaciones visuales (arquitecturas, grafos de transición Markov, etc.) deben hacerse utilizando sintaxis de Mermaid (` ```mermaid ... ``` `).

## 3. Manejo de Notas Adicionales, Admonitions y Código MDX

- El razonamiento principal debe fluir de forma limpia y directa.
- Cualquier justificación profunda o análisis del porqué de una técnica matemática subyacente deberá quedar en un bloque destacado usando **React Components de Docusaurus**.
- Sintaxis obligatoria para Admonitions:
  ```mdx
  <Nota titulo="Título Breve">
  Contenido de la nota detallada aquí. Puede tener bloques matemáticos sin problema.
  </Nota>
  
  <Advertencia titulo="Aviso importante">
  Texto de la advertencia.
  </Advertencia>
  ```
- **Regla Estricta MDX**: No utilices sintaxis de MkDocs (`!!! note`, `??? info`). Usa siempre `<Nota>`, `<Advertencia>`, `<Ejercicio>`, o `<Demostracion>`.
- **Regla Estricta MDX sobre Llaves e Inclusiones**: No debes dejar llaves `{}` sin escapar fuera de bloques de código o bloques matemáticos. Tampoco debes usar la sintaxis de Snippets de MkDocs (`--8<--`). Si necesitas incluir código, usa bloques ` ```python ` estándar.

Para garantizar que estas normas se cumplan de manera sistemática y que el renderizado no se contamine con aglomeraciones de texto, se deben ejecutar obligatoriamente **dos scripts de verificación y corrección tras cada sesión de redacción o modificación de los archivos Markdown**.

```bash
# 1. Ejecutar el auto-fixer para reparar/aislar bloques matemáticos adheridos
python scripts/fix_formato_markdown.py

# 2. Correr el linter verificador para certificar listas y reglas de formato subyacentes
python scripts/verificador_formato_markdown.py
```

- **Este paso doble es obligatorio.** El corrector intentará despegar los bloques de ecuaciones que posean sintaxis aglomerada. 
- Luego, el *linter* reportará las advertencias residuales en consola indicando la línea del conflicto. La IA debe iterar y solucionar la falta de espaciado señalada antes de poder dar la tarea por absolutamente concluida.
