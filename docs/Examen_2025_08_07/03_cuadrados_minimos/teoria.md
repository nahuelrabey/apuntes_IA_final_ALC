# Ejercicio 3: Cuadrados Mínimos y Pseudoinversa

> **Ejercicio 3.** Dada $A \in \mathbb{R}^{m \times n}$ de rango $n$ y $b \in \mathbb{R}^m$ con $m > n$ se quiere resolver el problema de cuadrados mínimos: hallar $x \in \mathbb{R}^n$ que minimice $\|Ax - b\|_2$. Probar que $x = A^\dagger b$, donde $A^\dagger$ es la pseudo-inversa de $A$. Indicar por qué esto sirve para resolver el problema en la práctica.

## Interpretación del Enunciado

Se nos presenta un sistema lineal sobredeterminado $Ax = b$ de ecuaciones (más ecuaciones $m$ que incógnitas $n$), donde la matriz $A$ posee "rango columna completo" ($rg(A) = n$). Al carecer de solución exacta asintóticamente, buscamos minimizar el residuo $r = b - Ax$ bajo la norma Euclidiana 2. Se pide constatar analíticamente que la formulación de cuadrados mínimos ordinarios se simplifica a la aplicación directa de la matriz seudoinversa $A^\dagger$ de Moore-Penrose, y discutir su preeminencia en el campo computacional.

---

## Solución del Ejercicio

El planteo clásico para minimizar la distancia residual cuadrática $E(x) = \|Ax - b\|_2^2$ se deduce a través de proyecciones ortogonales sobre el subespacio columna de $A$ o derivadas analíticas del gradiente respecto de $x$. Ambas vertientes coinciden en la formulación de las **ecuaciones normales del sistema**:

$$
A^T A x_{cm} = A^T b
$$

Dado que $A \in \mathbb{R}^{m \times n}$ ostenta un rango columna completo ($rg(A) = n$), garantizamos que las columnas de $A$ son todas linealmente independientes. Como corolario del álgebra lineal, si $A$ tiene columnas LI, su matriz de Gramian $A^T A \in \mathbb{R}^{n \times n}$ es definida positiva, de rango completo, y biyectiva, por lo tanto, es **estrictamente inversible**.

Multiplicando a la izquierda por su inversa $(A^T A)^{-1}$, despejamos el vector iterativo final $x_{cm}$:

$$
x_{cm} = (A^T A)^{-1} A^T b
$$

Por definición analítica formal, cuando una matriz $A$ rectangular es alta ("skinny", $m > n$) y posee rango completo a nivel columnas, su **inversa generalizada a izquierda por el lado de los mínimos cuadrados** (también llamada Pseudoinversa de Moore-Penrose) asume la expresión explícita:

$$
A^\dagger = (A^T A)^{-1} A^T
$$

Notamos de inmediato la equivalencia exacta de los términos. Si unimos ambas afirmaciones previas asociando los bloques de matrices:

$$
x_{cm} = [(A^T A)^{-1} A^T] \cdot b = A^\dagger b
$$

La demostración teórica ha dictaminado con éxito la igualdad formal solicitada.

??? info "Observación Teórica: ¿Qué pasaría si el rango no fuese completo?"
    Si $rg(A) < n$ (sistema deficiente), $A^T A$ deja de ser biyectiva porque su determinante colapsa a cero. En ese caso, la resolución analítica pasa por la Descomposición SVD completa truncada, que engendra naturalmente a la forma generalizada de $A^\dagger$ con la matriz $D^\dagger$ de recíprocos espectrales. La solución de pseudoinversa nos devolverá siempre "el $x_{cm}$ más corto" ($\|x\|_2$ min).

### Importancia y Traslación a la Práctica Computacional

¿Por qué resulta útil esta formulación compacta $x = A^\dagger b$ en la ingeniería numérica?

1. **Abstracción Analítica**: Transforma un problema de optimización derivado (minimizar un residuo geométrico) en la simple operatoria lineal estática de un objeto algorítmico precalculable abstracto ($A^\dagger$). Sirve para el entrenamiento supervisado en Machine Learning (Regresión Ridge pura) donde la "función encajadora" se sintetiza al evaluar iterativamente diferentes vectores target $b$ multiplicándolos de golpe contra una única $A^\dagger$ cacheada estáticamente.
2. **Estabilidad a través de SVD y Factorizaciones**: A la hora de calcular $A^\dagger$, el hardware no comete el "crimen matricial" de ensamblar malvadamente $A^T A$ (lo cual elevaría el número de condición de manera catastrófica $\kappa(A^T A) = \kappa(A)^2$, estallando el error de coma flotante). En la práctica subyacente de BLAS/LAPACK o NumPy, la construcción de la pseudo-inversa aprovecha rotaciones QR factorizadas o SVD puras para acoplar la pseudo-inversa limitando el truncamiento. Así, la abstracción garantiza resguardos matemáticos que las ecuaciones planas originales ignoran.

---

--8<-- "docs/Examen_2025_08_07/03_cuadrados_minimos/verificacion.py"
