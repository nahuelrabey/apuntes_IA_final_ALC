---
description: Metodología general para resolver enunciados matemáticos (Exámenes y Demostraciones)
---

# Metodología de Resolución de Enunciados Matemáticos

Este flujo de trabajo (workflow) funciona como una plantilla operativa estricta que la IA debe adoptar cada vez que se le encomiende resolver matemáticamente o verificar computacionalmente problemas de Álgebra Lineal Computacional y demostraciones.

*(Para la estructura de carpetas, ver `estructura_examenes.md`. Para formato de texto, ver `estructuracion_markdown.md`)*.

## 1) Resolución Teórica Analítica

Todo planteo matemático debe resolverse con rigor antes de recurrir a código:
- **Claridad Lógica**: Justificar cada paso conectando axiomas y propiedades conocidas.
- **Relación con Demostraciones**: Si en el desarrollo se utiliza un principio fundamental ya demostrado (ej. "Convergencia y Radio Espectral"), se debe enlazar hacia el archivo maestro correspondiente en `docs/demostraciones/`.

## 2) Verificación con Python (La Fase Pragmática de Traducción)

La afirmación teórica final sólo adquiere validez incuestionable si supera el *"Sandbox computacional"*: la verificación empírica. Al confeccionar cada script validador (`verificacion.py` o análogo):

- **Abstracción al Caos (Randomization Testing)**:
  - Todo teorema matricial abstracto deberá someterse a rigor utilizando simulaciones estocásticas de matrices masivas en `NumPy` (`np.random.randn`, construcciones desde SVD). El orden de las filas no debe perturbar propiedades núcleo; inyéctale permutaciones al azar para asilar algoritmos de posibles matrices simétricas engañosas conformadas artificialmente.

- **Verificación Simbólica (SymPy)**:
  - Siempre que sea posible y el problema involucre derivaciones algebraicas, polinomios o matrices pequeñas con valores exactos (ej. fracciones), se deberá dar prioridad a la **verificación simbólica con `SymPy`**. Esto permite confirmar determinantes, autovalores o identidades sin errores de punto flotante.

- **Comprobación Booleana por Flotantes**:
  - En informática científica real, problemas de desbordamiento, truncamiento y redondeo de punto flotante desautorizan las validaciones rígidas por doble igual (`==`).
  - Toda validación geométrica o matricial debe testearse tolerando márgenes residuales computacionales utilizando comandos como `np.allclose()` o tolerancias explícitas (ej. $1e^{-8}$).

- **Inclusión Periférica y Legibilidad**:
  - El código de verificación generado no queda suelto: se debe acoplar visual e inequívocamente al final de su documento teórico emparejado (usualmente inyectándose a través de snipplets sintácticos: `--8<-- "Ruta/Relativa/al/verificador.py"`).
  - Recuerda incorporar conclusiones en el código frente a ineficiencias matemáticas del mundo real.

> **Aprobación Definitiva**: Un ejercicio solo se cataloga como superado cuando cuenta con deducción matemática deductiva validada, traducida a un script pseudo-aleatorio confiable resistiéndose a floats tolerantes, y ruteado correctamente en la documentación.
