# Ejercicio 4: Factorización LU

> **Ejercicio 4.** Dada una matriz $A$ de $\mathbb{R}^{n \times n}$,
>
> **(a)** Detalle el procedimiento para encontrar la factorización $A = LU$ sin pivoteo, indicando
> cuándo falla. ¿El fallo del algoritmo implica la inexistencia de la factorización $LU$?
>
> **(b)** Describa condiciones conocidas para que la factorización $LU$ de $A$ exista y/o sea única.

---

## Interpretación del Enunciado

{/* El ejercicio pide distinguir entre: (1) el fallo del algoritmo de eliminación gaussiana
     sin pivoteo, y (2) la inexistencia de la factorización LU. Son conceptos distintos. */}

---

## Solución del Ejercicio

### Inciso A — Procedimiento y Fallo

> **(a)** Detalle el procedimiento para encontrar $A = LU$ sin pivoteo. ¿Cuándo falla?
> ¿El fallo implica inexistencia de LU?

{/* 1. Describir la eliminación gaussiana: en el paso k se requiere que a_{kk}^{(k)} ≠ 0
        (pivote no nulo). Si es cero, el algoritmo FALLA (división por cero).

     2. Pero esto NO implica que LU no exista: puede existir LU aunque el algoritmo sin
        pivoteo falle. Dar un contraejemplo (ej. matriz con a_{11}=0 pero LU existe). */}

### Inciso B — Condiciones de Existencia y Unicidad

> **(b)** Describa condiciones conocidas para que la factorización $LU$ exista y/o sea única.

{/* Condiciones suficientes de existencia:

     - Todas las submatrices principales de A son no singulares (menores principales ≠ 0).
     - A es estrictamente diagonal dominante.
     - A es definida positiva (simétrica).

     Unicidad: si L se normaliza con diagonal 1 (forma de Doolittle), la factorización LU
     es única cuando existe. */}

---

Ver implementación en [`verificacion.py`](verificacion.py).

```python
"""
Verificación: Ejercicio 4 — Factorización LU (Examen 25/02/2026)
"""

import numpy as np
from scipy.linalg import lu


# ---------------------------------------------------------------------------
# Función: LU sin pivoteo (implementación manual)
# ---------------------------------------------------------------------------

def lu_sin_pivoteo(A):
    """
    Calcula la factorización A = L·U mediante eliminación gaussiana sin pivoteo.
    Lanza ValueError si se encuentra un pivote nulo.

    Parámetros
    ----------
    A : np.ndarray — Matriz cuadrada n×n.

    Retorna
    -------
    L, U : np.ndarray — Factores triangular inferior (L) y superior (U).
    """
    n = A.shape[0]
    U = A.astype(float).copy()
    L = np.eye(n)

    for k in range(n - 1):
        if np.isclose(U[k, k], 0.0):
            raise ValueError(
                f"Pivote nulo en la posición ({k},{k}): el algoritmo sin pivoteo falla."
            )
        for i in range(k + 1, n):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:] -= factor * U[k, k:]

    return L, U


# ---------------------------------------------------------------------------
# Inciso (a): demostración de fallo vs. inexistencia
# ---------------------------------------------------------------------------

# Caso 1: LU existe y el algoritmo funciona
A1 = np.array([[2., 1., 1.],
               [4., 3., 3.],
               [8., 7., 9.]])
L1, U1 = lu_sin_pivoteo(A1)
print("Caso 1 — LU existe y el algoritmo sin pivoteo funciona:")
print("  A = L·U:", np.allclose(A1, L1 @ U1))
print()

# Caso 2: pivote nulo → el algoritmo falla, pero LU SÍ existe (con permutación)
# Ejemplo clásico: a_11 = 0
A2 = np.array([[0., 1.],
               [1., 0.]])

print("Caso 2 — a_{11}=0: el algoritmo sin pivoteo falla...")
try:
    L2, U2 = lu_sin_pivoteo(A2)
except ValueError as e:
    print(f"  Error capturado: {e}")

# Scipy LU con pivoteo (P·A = L·U): la factorización SÍ existe como P·A = L·U
P2, L2, U2 = lu(A2)
print("  Con pivoteo (scipy): P·A = L·U ->", np.allclose(P2 @ A2, L2 @ U2))
print("  → El fallo del algoritmo NO implica inexistencia de LU.")
print()

# ---------------------------------------------------------------------------
# Inciso (b): condición de existencia — menores principales no singulares
# ---------------------------------------------------------------------------

print("Verificación condición suficiente — menores principales:")
A3 = np.array([[4., 3.],
               [6., 3.]])

for k in range(1, A3.shape[0] + 1):
    det_k = np.linalg.det(A3[:k, :k])
    print(f"  det(A[:{k},:{k}]) = {det_k:.4f}  ({'≠0 ✓' if not np.isclose(det_k, 0) else '=0 ✗'})")

L3, U3 = lu_sin_pivoteo(A3)
print("  A = L·U:", np.allclose(A3, L3 @ U3))

```
