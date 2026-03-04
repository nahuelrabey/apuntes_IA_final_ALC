"""
Verificación: κ₂(M) = σ_max / σ_min para matrices invertibles.

Metodología:
- Prueba estocástica sobre matrices aleatorias cuadradas.
- Compara np.linalg.cond(M, 2) (κ₂ via numpy) contra σ_max/σ_min calculado manualmente.
- Valida con np.isclose para tolerancia numérica.
- Verifica también que ‖M⁻¹‖₂ = 1/σ_min.
"""

import numpy as np

rng = np.random.default_rng(seed=7)

SIZES = [3, 5, 7, 10, 20]
N_TRIALS = 200

all_passed = True

for n in SIZES:
    passed_kappa = 0
    passed_inv   = 0

    for _ in range(N_TRIALS):
        # Construir una matriz invertible via SVD para garantizar σ_min > 0
        U, _ = np.linalg.qr(rng.standard_normal((n, n)))
        V, _ = np.linalg.qr(rng.standard_normal((n, n)))
        # Valores singulares positivos en [0.1, 10]
        sigma = rng.uniform(0.1, 10.0, size=n)
        Sigma = np.diag(np.sort(sigma)[::-1])   # ordenados en forma decreciente

        M = U @ Sigma @ V.T

        svd_vals = np.linalg.svd(M, compute_uv=False)  # σ₁ ≥ σ₂ ≥ ... ≥ σ_n
        sigma_max = svd_vals[0]
        sigma_min = svd_vals[-1]

        # κ₂ via numpy vs fórmula σ_max/σ_min
        kappa_numpy   = np.linalg.cond(M, 2)
        kappa_formula = sigma_max / sigma_min

        if np.isclose(kappa_numpy, kappa_formula, rtol=1e-8):
            passed_kappa += 1

        # ‖M⁻¹‖₂ vs 1/σ_min
        norm_inv_numpy   = np.linalg.norm(np.linalg.inv(M), ord=2)
        norm_inv_formula = 1.0 / sigma_min

        if np.isclose(norm_inv_numpy, norm_inv_formula, rtol=1e-8):
            passed_inv += 1

    ok = (passed_kappa == N_TRIALS) and (passed_inv == N_TRIALS)
    all_passed = all_passed and ok
    status = "✓ OK" if ok else "✗ FALLÓ"
    print(f"n={n:>2}  κ₂: {passed_kappa}/{N_TRIALS}  "
          f"‖M⁻¹‖₂: {passed_inv}/{N_TRIALS}  {status}")

print()

# Caso concreto: matriz A del Ejercicio 2, Examen 2025-02-24
print("── Caso concreto (Ejercicio 2, Examen 2025-02-24) ──")
A = np.array([[0, -1, 0],
              [2,  0, 0],
              [0,  0, -3]], dtype=float)

svd_A     = np.linalg.svd(A, compute_uv=False)
kappa_A   = np.linalg.cond(A, 2)
formula_A = svd_A[0] / svd_A[-1]

print(f"  Valores singulares σ  : {svd_A}")
print(f"  κ₂(A) via numpy       : {kappa_A:.10f}")
print(f"  σ_max/σ_min           : {formula_A:.10f}")
print(f"  ¿Coinciden?           : {np.isclose(kappa_A, formula_A)}")

print()
if all_passed:
    print("✓ Todas las pruebas pasaron: κ₂(M) = σ_max(M) / σ_min(M).")
else:
    print("✗ Algunas pruebas fallaron.")
