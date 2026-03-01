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
  Las ecuaciones de peso deben separarse en bloque. **Es obligatorio** dejar una línea vacía por encima, por debajo y entre bloques de ecuaciones consecutivos para asegurar el correcto renderizado en MkDocs/MathJax.
- **Listas y Viñetas**:
  Asegúrate siempre de dejar un salto de línea en blanco antes y entre medio de los ítems de cualquier enumerado para evitar condensación del hipertexto al compilar.
- **Diagramas (Mermaid)**:
  Las representaciones visuales (arquitecturas, grafos de transición Markov, etc.) deben hacerse utilizando sintaxis de Mermaid (` ```mermaid ... ``` `).

## 3. Manejo de Notas Adicionales y Complejidad Oculta

- El razonamiento principal debe fluir de forma limpia y directa.
- Cualquier justificación profunda, análisis del porqué de una técnica matemática subyacente, demostraciones periféricas o historia, deberá quedar "escondida" en un bloque sintáctico colapsable usando los **admonitions interactivos** de MkDocs.
- Sintaxis obligatoria del bloque colapsable: `??? info "Título Breve"` (o `??? question`, `??? warning` según corresponda).

## 4. Validación Automatizada Estricta

Para garantizar que estas normas se cumplan de manera sistemática y que el renderizado no se contamine con aglomeraciones de texto, se deben ejecutar obligatoriamente **dos scripts de verificación y corrección tras cada sesión de redacción o modificación de los archivos Markdown**.

```bash
# 1. Ejecutar el auto-fixer para reparar/aislar bloques matemáticos adheridos
python scripts/fix_math_blocks.py

# 2. Correr el linter verificador para certificar listas y reglas de formato subyacentes
python scripts/verificador_formato_markdown.py
```

- **Este paso doble es obligatorio.** El corrector intentará despegar los bloques de ecuaciones que posean sintaxis aglomerada. 
- Luego, el *linter* reportará las advertencias residuales en consola indicando la línea del conflicto. La IA debe iterar y solucionar la falta de espaciado señalada antes de poder dar la tarea por absolutamente concluida.
