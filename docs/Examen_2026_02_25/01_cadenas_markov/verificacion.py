"""
Verificación: Ejercicio 1 — Cadenas de Markov (Examen 25/02/2026)
"""

import numpy as np


# ---------------------------------------------------------------------------
# Inciso (d): estado_limite(P, v0, max_iter, tol)
# ---------------------------------------------------------------------------

def estado_limite(P, v0, max_iter, tol):
    """
    Busca el estado límite de la distribución inicial v0 bajo la matriz
    de transición P, iterando P^k * v0 hasta converger.

    Parámetros
    ----------
    P        : np.ndarray — Matriz de transición (n x n).
    v0       : np.ndarray — Distribución inicial (n,).
    max_iter : int        — Número máximo de iteraciones permitidas.
    tol      : float      — Tolerancia para criterio de convergencia.

    Retorna
    -------
    np.ndarray con el estado límite, o None si no converge.
    """
    v = v0.copy().astype(float)

    for k in range(max_iter):
        v_new = P @ v
        if np.linalg.norm(v_new - v, ord=1) < tol:
            print(f"Convergido en iteración {k + 1}.")
            return v_new
        v = v_new

    print(f"No se alcanzó convergencia en {max_iter} iteraciones con tol={tol}.")
    return None


# ---------------------------------------------------------------------------
# Verificación numérica (completar P una vez resuelto el inciso a)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # TODO: completar P con los valores hallados en el inciso (a)
    # P = np.array([...])

    # Distribución inicial del inciso (b)
    # v0 = np.array([1/2, 0, 1/2, 0])

    # Distribución después de 10 años (inciso b)
    # v10 = np.linalg.matrix_power(P, 10) @ v0
    # print("v_10 =", v10)

    # Estado límite iterativo (inciso d)
    # resultado = estado_limite(P, v0, max_iter=1000, tol=1e-10)
    # print("Estado límite =", resultado)

    print("Completar P con los valores del inciso (a) antes de ejecutar.")
