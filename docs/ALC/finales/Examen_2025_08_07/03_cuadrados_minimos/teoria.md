# Ejercicio 3: Cuadrados Mínimos y Pseudoinversa

<Enunciado titulo="Ejercicio 3.">

Dada $A \in \mathbb{R}^{m \times n}$ de rango $n$ y $b \in \mathbb{R}^m$ con $m > n$ se quiere resolver el problema de cuadrados mínimos: hallar $x \in \mathbb{R}^n$ que minimice $\|Ax - b\|_2$. Probar que $x = A^\dagger b$, donde $A^\dagger$ es la pseudo-inversa de $A$. Indicar por qué esto sirve para resolver el problema en la práctica.

</Enunciado>


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

    Si $rg(A) < n$ (sistema deficiente), $A^T A$ deja de ser biyectiva porque su determinante colapsa a cero. En ese caso, la resolución analítica pasa por la Descomposición SVD completa truncada, que engendra naturalmente a la forma generalizada de $A^\dagger$ con la matriz $D^\dagger$ de recíprocos espectrales. La solución de pseudoinversa nos devolverá siempre "el $x_{cm}$ más corto" ($\|x\|_2$ min).

    Fin de la observación.

### Importancia y Traslación a la Práctica Computacional

¿Por qué resulta útil esta formulación compacta $x = A^\dagger b$ en la ingeniería numérica?

1. **Abstracción Analítica**: Transforma un problema de optimización derivado (minimizar un residuo geométrico) en la simple operatoria lineal estática de un objeto algorítmico precalculable abstracto ($A^\dagger$). Sirve para el entrenamiento supervisado en Machine Learning (Regresión Ridge pura) donde la "función encajadora" se sintetiza al evaluar iterativamente diferentes vectores target $b$ multiplicándolos de golpe contra una única $A^\dagger$ cacheada estáticamente.
2. **Estabilidad a través de SVD y Factorizaciones**: A la hora de calcular $A^\dagger$, el hardware no comete el "crimen matricial" de ensamblar malvadamente $A^T A$ (lo cual elevaría el número de condición de manera catastrófica $\kappa(A^T A) = \kappa(A)^2$, estallando el error de coma flotante). En la práctica subyacente de BLAS/LAPACK o NumPy, la construcción de la pseudo-inversa aprovecha rotaciones QR factorizadas o SVD puras para acoplar la pseudo-inversa limitando el truncamiento. Así, la abstracción garantiza resguardos matemáticos que las ecuaciones planas originales ignoran.

---

```python
import numpy as np

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 3...")
    
    # 1. Abstracción al caos: M y N aleatorios (m > n) con rango completo casi seguro.
    np.random.seed(101)
    m, n = 8, 4
    
    # Matriz A aleatoria asimétrica "skinny"
    A = np.random.randn(m, n) * 10 
    # Validar que Rango Columna Completo se mantiene en la simulación estocástica
    rank = np.linalg.matrix_rank(A)
    assert rank == n, f"Fallo en instanciación: El rango (r={rank}) no es completo (n={n})."

    # Vector extendido ruidoso b
    b = np.random.randn(m) * 15

    print("\n1) Resolviendo por Ecuaciones Normales explícitas (Solución Algebraica):")
    # x = (A^T A)^-1 A^T b
    AtA = A.T @ A
    AtA_inv = np.linalg.inv(AtA)
    x_eq_normales = AtA_inv @ A.T @ b
    print("Resultado x_cm (Ec. Normales):")
    print(np.round(x_eq_normales, 5))

    print("\n2) Resolviendo por minimización algorítmica robusta de Mínimos Cuadrados:")
    # np.linalg.lstsq min( ||Ax - b||_2 ) internamente vía SVD o QR robusto.
    x_lstsq, residuals, _, _ = np.linalg.lstsq(A, b, rcond=None)
    print("Resultado x_cm (np.linalg.lstsq):")
    print(np.round(x_lstsq, 5))

    print("\n3) Resolviendo por cálculo puro de Pseudo-inversa (Pinza Computacional Teorizada):")
    # np.linalg.pinv genera la inversa de Moore-Penrose (A^dagger)
    A_pinv = np.linalg.pinv(A)
    x_pinv = A_pinv @ b
    print("Resultado x_cm (A_pseudo * b):")
    print(np.round(x_pinv, 5))

    # Comparación de Tolerancias Flotantes para la Aprobación Definitiva
    assert np.allclose(x_eq_normales, x_lstsq, rtol=1e-5), "Fallo: x_eq_normales difiere de x_lstsq."
    assert np.allclose(x_lstsq, x_pinv, rtol=1e-5), "Fallo: La pseudo-inversa no converge al minimizador de norma 2."
    
    print("\n[OK] Verificación completada con éxito. La pseudo-inversa equivale analíticamente a los cuadrados mínimos para bases de rango completo, resistiéndose a desbordes de coma flotante.")

if __name__ == '__main__':
    run_verification()

```
