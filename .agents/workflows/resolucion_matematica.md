---
description: Metodología general para resolver enunciados matemáticos (Exámenes y Demostraciones)
---

# Metodología de Resolución de Enunciados Matemáticos

Este flujo de trabajo (workflow) funciona como una plantilla operativa estricta que la IA debe adoptar cada vez que se le encomiende resolver, verificar o documentar problemas de Álgebra Lineal Computacional, demostraciones matemáticas o exámenes en este proyecto. 

El mismo nace de los aprendizajes analíticos plasmados en `docs/index.md`, las convenciones documentales de `AGENTS.md` y las profundizaciones numéricas compiladas en `docs/lecciones_aprendidas.md`.

## 1) Estructura de las Carpetas (Exámenes y Demostraciones)

Cuando se inicie el desarrollo de un nuevo ejercicio, un examen completo o una validación transversal, el contenido deberá organizarse respetando la siguiente jerarquía impuesta:

- **Carpetas de Exámenes (`docs/Examen_YYYY_MM_DD/`)**:
  - Cada examen se agrupará en una carpeta matriz nombrada por su fecha.
  - El examen se divide estrictamente en ejercicios. Cada ejercicio debe tener su propia subcarpeta numerada correspondientemente y con título representativo (ej. `01_semejanza_matrices`, `02_descomposicion_svd`).
  - Dentro de la carpeta del ejercicio, la explicación analítica siempre residirá en un archivo llamado **`teoria.md`**, y su verificación algorítmica en un script Python emparejado (ej. `verificacion.py`).

- **Carpeta de Demostraciones (`docs/demostraciones/`)**:
  - Toda demostración general, inducción de un teorema o principio fundacional que sirva de apoyo transversal a múltiples ejercicios (ej. "Método de la Potencia Clásico") no debe anclarse a un examen específico, sino documentarse aquí.
  - Al igual que los exámenes, constan de su archivo markdown analítico (`01_metodo_potencia.md`) y su validador computacional hermano en formato Python (`01_metodo_potencia.py`).
  - **Uso Crítico**: Desde los apuntes formales (`teoria.md`), debes enlazar hacia estos archivos maestros cada vez que te asientes en una fórmula cubierta por ellos.

## 2) Resolución Teórica (Fase Pura)

A la hora de redactar el cuerpo matemático de `teoria.md` o cualquier otro archivo análogo de deducción, respeta firmemente la siguiente rúbrica de redacción y formato:

- **Estructura Indispensable**: 
  1. Comienza el archivo citando **textualmente el enunciado completo** dentro de un bloque quote (`> ...`).
  2. Subdivide el texto bajo los encabezados lógicos obligatorios: "Interpretación del Enunciado" (identificación táctica) y "Solución del Ejercicio" (desarrollo analítico).
  3. Si existen múltiples incisos (a, b, c), retoma y copia una vez más cada micro-enunciado en bloque quote bajo su respectivo sub-encabezado H2/H3 puntual.

- **Desarrollo Matemático**:
  - Las variables matemáticas y derivaciones formales se deben explayar de modo deductivo (paso a paso), sin obviar el "puente lógico" entre axiomas. 
  - Las ecuaciones de peso deben separarse en bloque (usando `$$...$$` con una **línea vacía adicional** obligatoria por encima, por debajo y entre bloques consecutivos para asegurar el correcto renderizado en `MkDocs` y `MathJax`).
  - **Listas y viñetas**: Asegúrate siempre de dejar un salto de línea en blanco antes y entre medio de los ítems de cualquier enumerado para evitar condensación del hipertexto al compilar.
  - **Diagramas**: Las representaciones visuales, como grafos de transición, deben hacerse utilizando sintaxis de **Mermaid** (` ```mermaid ... ``` `).

- **Manejo de Notas Adicionales y Complejidad Oculta**:
  - El razonamiento base debe fluir limpio. Cualquier justificación profunda, análisis del porqué de una técnica matemática subyacente o extensión histórica deberá quedar "escondida" en un bloque sintáctico colapsable usando **admonitions interactivos** de MkDocs: `??? info "Observación Teórica: [Título]"`.

## 3) Verificación con Python (La Fase Pragmática de Traducción)

La afirmación teórica final sólo adquiere validez incuestionable en este proyecto si supera el *"Sandbox computacional"*: la verificación empírica probabilística. Al confeccionar cada script validador (`.py`):

- **Abstracción al Caos (Randomization Testing)**:
  - Todo teorema matricial abstracto deberá someterse a rigor utilizando simulaciones estocásticas de matrices masivas en `NumPy` (`np.random.randn`, construcciones desde SVD). El orden de las filas no debe perturbar propiedades núcleo; inyéctale permutaciones al azar para asilar algoritmos de posibles matrices simétricas engañosas conformadas artificialmente.

- **Verificación Simbólica (SymPy)**:
  - Siempre que sea posible y el problema involucre derivaciones algebraicas, polinomios o matrices pequeñas con valores exactos (ej. fracciones), se deberá prioridad la **verificación simbólica con `SymPy`**. Esto permite confirmar que el polinomio característico, los autovalores o las identidades algebraicas coinciden con el desarrollo manual sin ruidos de punto flotante.

- **Comprobación Booleana por Flotantes**:
  - En hardware e informática científica real, problemas de desbordamiento, truncamiento y redondeo de punto flotante desautorizan las validaciones rígidas por doble igual (`==`).
  - Toda validación como "la traza se mantiene", o "las normas SVD son las mismas", **debe testearse tolerando márgenes residuales computacionales** (ej. $1e^{-8}$ a $1e^{-10}$) utilizando comandos laxos y robustos como `np.allclose()` o tolerancias estadísticas explícitas.

- **Inclusión Periférica y Legibilidad**:
  - El código de verificación generado no se suelta suelto sin mención; se debe acoplar visual e inequívocamente al final del `teoria.md` de su par, usualmente inyectándose a través de snipplets sintácticos (`--8<-- "Ruta/Relativa/al/verificador.py"`).
  - Recuerda incorporar conclusiones en el código frente a ineficiencias matemáticas del mundo real (ej. documentar si variables *in-place* benefician a Gauss-Seidel al ahorrarse el clonado de caché comparado a Jacobi matricial plano).

> **Aprobación Definitiva (Framework Integrado)**: Un ejercicio de ALC solo se cataloga como superado cuando cuenta con deducción matemática deductiva (Fase 1) en markdown, ha sido traducido a un script pseudo-aleatorio confiable resistiéndose a floats tolerantes (Fase 2 + 3), y finalmente ruteado correctamente en el índice del sitio documentado.
