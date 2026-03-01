"""
Verificación computacional - Ejercicio 2: Condicionamiento de A_n

Confirma para valores crecientes de n que:
  - cond_inf(A_n) >= n^2 + 1  (cota probada en B-1 vía distancia a la singularidad)
  - cond_2(A_n)  == n^2 + 1  (calculado exactamente en B-2)
"""

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Verificación simbólica para n pequeño (SymPy, sin errores de punto flotante)
# ---------------------------------------------------------------------------
n_sym = sp.Symbol("n", positive=True, integer=True)

for n_val in [2, 3, 4, 5]:
    n = n_val
    A = sp.Rational(1, n) * sp.ones(n, n) + sp.Rational(1, n**2) * sp.eye(n)

    eigenvalues = A.eigenvals()          # {valor: multiplicidad}
    evs = list(eigenvalues.keys())

    lam_max = max(evs, key=lambda e: sp.Abs(e))
    lam_min = min(evs, key=lambda e: sp.Abs(e))
    cond_2_sym = lam_max / lam_min

    expected = n**2 + 1
    assert cond_2_sym == expected, (
        f"n={n}: cond_2 simbólico={cond_2_sym}, esperado={expected}"
    )
    print(f"[SYMPY] n={n:2d} | λ_max={lam_max} | λ_min={lam_min} | "
          f"cond_2={cond_2_sym} | esperado={expected} ✓")

print()

# ---------------------------------------------------------------------------
# 2. Verificación numérica con NumPy para n más grandes
# ---------------------------------------------------------------------------
print(f"{'n':>5} | {'cond_inf(A_n)':>14} | {'cond_2(A_n)':>12} | "
      f"{'cota n²+1':>10} | {'cond_inf >= cota':>16} | {'cond_2 == cota':>14}")
print("-" * 80)

for n in [2, 3, 5, 10, 20, 50, 100, 200]:
    A = np.full((n, n), 1.0 / n) + np.eye(n) / n**2

    cond_inf = np.linalg.cond(A, np.inf)
    cond_2   = np.linalg.cond(A, 2)
    cota     = n**2 + 1

    ok_inf = cond_inf >= cota - 1e-8           # cota inferior: cond_inf >= n^2+1
    ok_2   = np.isclose(cond_2, cota, rtol=1e-8)  # igualdad exacta: cond_2 == n^2+1

    print(f"{n:>5} | {cond_inf:>14.4f} | {cond_2:>12.4f} | "
          f"{cota:>10} | {'✓' if ok_inf else '✗':>16} | {'✓' if ok_2 else '✗':>14}")

    assert ok_inf, f"n={n}: cond_inf={cond_inf:.4f} < cota={cota}"
    assert ok_2,   f"n={n}: cond_2={cond_2:.4f} ≠ esperado={cota}"

print()
print("Todas las verificaciones pasaron correctamente.")
