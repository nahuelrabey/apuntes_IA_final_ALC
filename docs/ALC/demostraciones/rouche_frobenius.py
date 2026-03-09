"""
Verificación empírica del Teorema de Rouché-Frobenius.

Comprueba los tres casos del teorema sobre sistemas aleatorios:
  1. Sistema compatible con solución única (Rango(A) = Rango(A|b) = n)
  2. Sistema compatible con infinitas soluciones (Rango(A) = Rango(A|b) < n)
  3. Sistema incompatible (Rango(A) < Rango(A|b))
"""

import numpy as np

np.random.seed(42)


def caso_compatible_unico():
    """Rango(A) = Rango(A|b) = n → solución única."""
    n = 4
    A = np.random.randn(n + 2, n)  # m > n, rango completo
    x_real = np.random.randn(n)
    b = A @ x_real  # b exactamente en Col(A)

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_A == rango_Ab == n, "No se cumple la condición de unicidad"
    x_sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    assert np.allclose(x_sol, x_real), "La solución no coincide con la real"
    print(f"[OK] Compatible única: Rango(A) = Rango(A|b) = {rango_A}")


def caso_compatible_infinitas():
    """Rango(A) = Rango(A|b) < n → infinitas soluciones."""
    n = 4
    # Construimos A con rango 2 duplicando columnas
    A_base = np.random.randn(n + 2, 2)
    A = np.hstack([A_base, A_base])  # columnas 1,2 = columnas 3,4 → rango 2

    coefs = np.random.randn(2)
    b = A_base @ coefs  # b ∈ Col(A)

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_A == rango_Ab < n, "No se detectó rango deficiente"
    print(f"[OK] Compatible infinitas: Rango(A) = Rango(A|b) = {rango_A} < n={n}")


def caso_incompatible():
    """Rango(A) < Rango(A|b) → sin solución."""
    n = 3
    A = np.random.randn(n, n)
    # Hacemos A de rango n-1 colapsando la última fila
    A[-1] = A[0]

    b = np.random.randn(n)
    # Con alta probabilidad b no está en Col(A) → incompatible
    b[-1] = b[0] + 1.0  # rompemos la consistencia explícitamente

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_Ab > rango_A, "Se esperaba sistema incompatible"
    print(f"[OK] Incompatible: Rango(A)={rango_A} < Rango(A|b)={rango_Ab}")


if __name__ == "__main__":
    caso_compatible_unico()
    caso_compatible_infinitas()
    caso_incompatible()
    print("\nTodos los casos del Teorema de Rouché-Frobenius verificados correctamente.")
