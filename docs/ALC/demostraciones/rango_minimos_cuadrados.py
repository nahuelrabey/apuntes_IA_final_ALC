"""
Verificación empírica: Rango completo de M y unicidad de la solución en mínimos cuadrados.

Comprueba que:
  1. Si Rango(M) = n, entonces M^TM es invertible y la solución de MC es única.
  2. Si Rango(M) < n, entonces M^TM es singular y hay infinitas soluciones.
"""

import numpy as np

np.random.seed(0)


def verificar_rango_completo():
    """M con rango completo → M^TM invertible → solución única."""
    m, n = 10, 3
    M = np.random.randn(m, n)  # rango 3 con prob. 1

    MtM = M.T @ M
    det = np.linalg.det(MtM)

    assert np.linalg.matrix_rank(M) == n, "M no tiene rango completo"
    assert abs(det) > 1e-10, f"M^TM debería ser invertible (det={det:.4f})"

    # Solución de MC
    theta_real = np.random.randn(n)
    Z = M @ theta_real + np.random.randn(m) * 0.01  # datos con ruido leve
    theta_hat = np.linalg.solve(MtM, M.T @ Z)

    assert np.allclose(theta_hat, theta_real, atol=0.1), "Solución incorrecta"
    print(f"[OK] Rango completo: Rango(M)={n}, det(M^TM)={det:.4f} → solución única")


def verificar_rango_deficiente():
    """M con rango < n → M^TM singular → infinitas soluciones."""
    m, n = 10, 3
    # Construimos M con columnas dependientes (col 3 = col 1 + col 2)
    M_base = np.random.randn(m, 2)
    M = np.hstack([M_base, M_base[:, [0]] + M_base[:, [1]]])

    MtM = M.T @ M
    det = np.linalg.det(MtM)
    rango = np.linalg.matrix_rank(M)

    assert rango < n, f"Se esperaba rango deficiente, got {rango}"
    assert abs(det) < 1e-8, f"M^TM debería ser singular (det={det:.2e})"
    print(f"[OK] Rango deficiente: Rango(M)={rango} < n={n}, det(M^TM)={det:.2e} ≈ 0 → infinitas soluciones")


def verificar_minimo_puntos():
    """Con m < n puntos, el rango nunca puede ser n."""
    n = 4
    for m in range(1, n):
        M = np.random.randn(m, n)
        rango = np.linalg.matrix_rank(M)
        assert rango <= m < n, f"Falla para m={m}"
    print(f"[OK] Con m < n={n} puntos, Rango(M) ≤ m < n siempre → solución no única")


if __name__ == "__main__":
    verificar_rango_completo()
    verificar_rango_deficiente()
    verificar_minimo_puntos()
    print("\nTodos los casos de rango y unicidad en mínimos cuadrados verificados correctamente.")
