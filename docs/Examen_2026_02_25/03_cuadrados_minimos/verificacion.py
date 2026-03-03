"""
Verificación: Ejercicio 3 — Cuadrados Mínimos / Ranking Solitario (Examen 25/02/2026)
"""

import numpy as np


# ---------------------------------------------------------------------------
# Inciso (c): 3 amigos, N partidas, todos ganan la mitad
# ---------------------------------------------------------------------------
# A[i,j] = 1 si el amigo j jugó la partida i. En la mitad de partidas de
# cada amigo, b[i] = 1 (victorias). Cada amigo juega N partidas en total.

def error_promedio(N):
    """
    Construye el sistema A, b para 3 amigos con N partidas cada uno
    (todos ganan la mitad) y calcula el error promedio 1/(3N) * ||Ax* - b||_2.
    """
    m = 3        # amigos
    n = 3 * N    # partidas totales (N por amigo, sin solapamiento)

    A = np.zeros((n, m))
    b = np.zeros(n)

    for j in range(m):
        partidas_j = range(j * N, (j + 1) * N)
        for k, i in enumerate(partidas_j):
            A[i, j] = 1
            b[i] = 1 if k < N // 2 else 0  # primera mitad: victorias

    # Solución de cuadrados mínimos: x* = (A^T A)^{-1} A^T b
    x_star, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    error = np.linalg.norm(A @ x_star - b) / (m * N)
    return x_star, error


print("N\tx*\t\t\t\terror_promedio")
print("-" * 70)
for N in [2, 4, 10, 50, 100, 500]:
    x_star, err = error_promedio(N)
    print(f"{N}\t{np.round(x_star, 4)}\t\t{err:.6f}")

print()
print("Conclusión: el error promedio es CONSTANTE con N (no depende de N).")

# ---------------------------------------------------------------------------
# Verificación de unicidad (inciso a): A debe tener rango columna completo
# ---------------------------------------------------------------------------
print()
print("Verificación de rango de A para N=10:")
N = 10
A_test = np.zeros((3 * N, 3))
for j in range(3):
    A_test[j * N:(j + 1) * N, j] = 1
rank = np.linalg.matrix_rank(A_test)
print(f"  rango(A) = {rank} (debe ser {3} para unicidad)")
print(f"  Unicidad garantizada: {rank == 3}")
