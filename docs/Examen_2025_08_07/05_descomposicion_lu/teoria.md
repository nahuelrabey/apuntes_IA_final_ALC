# Ejercicio 5: Factorización LU Algebraica y Algorítmica

> **Ejercicio 5.** Sea $A = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 1 & 0 & 1 & -1 \\ -1 & -1 & 0 & 1 \\ 0 & 1 & -2 & 2 \end{pmatrix}$.
>
> **a)** Decidir si $A$ admite descomposición $LU$. En tal caso, hallarla. En caso contrario, dar una permutación $P$ de modo que $PA$ tenga descomposición $LU$.
>
> **b)** Implementar una función de Python que reciba una matriz cuadrada e intente realizar la descomposición $LU$ de $A$ sin pivoteo. Si la matriz no admite descomposición $LU$, las matrices resultantes deben ser `None`.

## Interpretación del Enunciado

Este problema clásico evalúa el reconocimiento de factorizaciones exactas en álgebra lineal tanto desde un aspecto manual (deducción progresiva fila por fila en el inciso a) como programático general (inciso b). Una matriz cuadrada admite una descomposición pura $A = LU$ (donde $L$ es triangular inferior unitaria y $U$ es triangular superior) sí y sólo sí no requiere pivoteos por ceros en su diagonal principal durante la eliminación de Gauss convencional a lo largo de todos sus sub-pasos procesados o matrices principales menores determinantes distintos a cero $\det(A_k) \neq 0$.

---

## Solución del Ejercicio

> a) Decidir si $A$ admite descomposición $LU$. En tal caso, hallarla. En caso contrario, dar una permutación $P$ de modo que $PA$ tenga descomposición $LU$.

Para decidir de forma analítica exacta si la $LU$ plana existe, ensayamos el "escalonamiento" progresivo Gaussiano tradicional de $A$ a un estado triangular superior $U$, memorizando los multiplicadores elementales empleados debajo de la diagonal subyacente de la matriz $L$.

Partimos de:

$$
A^{(1)} = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 1 & 0 & 1 & -1 \\ -1 & -1 & 0 & 1 \\ 0 & 1 & -2 & 2 \end{pmatrix}
$$

**Paso 1: Pivote $u_{11} = 1$ no es nulo.** Las operaciones de fila apuntadas para anular elementos bajo la columna 1 son:
- Fila 2: $F_2 \gets F_2 - (1/1) F_1 \implies L_{21} = 1 \implies A_{2,:} = (0, -1, 2, -2)$
- Fila 3: $F_3 \gets F_3 - (-1/1) F_1 \implies L_{31} = -1 \implies A_{3,:} = (0, 0, -1, 2)$
- Fila 4: $F_4 \gets F_4 - (0/1) F_1 \implies L_{41} = 0 \implies A_{4,:} = (0, 1, -2, 2)$

Matriz residual reducida:

$$
A^{(2)} = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 0 & -1 & 2 & -2 \\ 0 & 0 & -1 & 2 \\ 0 & 1 & -2 & 2 \end{pmatrix}
$$

**Paso 2: Pivote $u_{22} = -1$ no es nulo.** Las operaciones elementales bajo él proceden:
- Fila 3: $F_3 \gets F_3 - (0/-1) F_2 \implies L_{32} = 0 \implies A_{3,:} = (0, 0, -1, 2)$
- Fila 4: $F_4 \gets F_4 - (1/-1) F_2 \implies L_{42} = -1 \implies A_{4,:} = F_4 + F_2 = (0, 0, 0, 0)$

Matriz residual reducida:

$$
A^{(3)} = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 0 & -1 & 2 & -2 \\ 0 & 0 & -1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

**Paso 3: Pivote $u_{33} = -1$ no es nulo.** Procedemos contra el nivel final por consistencia algorítmica:
- Fila 4: $F_4 \gets F_4 - (0/-1) F_3 \implies L_{43} = 0 \implies A_{4,:} = (0, 0, 0, 0)$
El último término es siempre $u_{44} = A^{(4)}_{44} = 0$.

Terminamos la eliminación. Puesto que **jamás emergieron divisiones por ceros** subyacentes ni multiplicadores imposibles en los denominadores obligatorios ($A_{kk}^{(k)} \neq 0, \forall k < 4$), **sí admite descomposición $LU$ pura garantizada**, y las matrices formales obtenidas son:

$$
U = A^{(4)} = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 0 & -1 & 2 & -2 \\ 0 & 0 & -1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

$$
L = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \end{pmatrix}
$$

---

> b) Implementar una función de Python que reciba una matriz cuadrada e intente realizar la descomposición $LU$ de $A$ sin pivoteo. Si la matriz no admite descomposición $LU$, las matrices resultantes deben ser `None`.

Adjuntamos aquí la implosión algorítmica solicitada (las funciones se encuentran embebidas explícitamente y comprobadas dentro del archivo final de verificación anexado a pie de firma). El requerimiento de detectar fracasos de la $LU$ plana (pivotes cero) exige un bucle temporal iterativo tolerante a EPS flotantes sobre un bloque `try-except` o estructuras condicionadas lógicas para atar al retorno a la ausencia o "Nulidad" literal de Python general (`None, None`).

```python
import numpy as np

def descomposicion_lu_plana(A_in, tol=1e-12):
    """
    Intenta un escaleonamiento LU sin pivoteo.
    Devuelve (L, U) si es exitoso, (None, None) caso contrario.
    """
    n = A_in.shape[0]
    A = A_in.astype(float).copy()
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n):
        # 1. Comprobamos posible colapso algorítmico del pivote nulo
        if abs(A[k, k]) < tol:
            print(f"Fallo algorítmico natural: Pivote 0 detectado escalonando iteración {k}.")
            return None, None

        U[k, k:] = A[k, k:]

        # 2. Computar multiplicadores L y actualizar sub bloque bajo fila
        for i in range(k+1, n):
            L[i, k] = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - L[i, k] * U[k, k:]

    return L, U
```

--8<-- "docs/Examen_2025_08_07/05_descomposicion_lu/verificacion.py"
