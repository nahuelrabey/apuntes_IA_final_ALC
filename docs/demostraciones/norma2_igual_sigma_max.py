"""
Verificación: la norma-2 inducida de una matriz es su mayor valor singular.

Metodología:
- Prueba estocástica sobre matrices aleatorias de distintos tamaños.
- Compara np.linalg.norm(M, 2) contra np.linalg.svd(M, compute_uv=False)[0].
- Valida con tolerancia numérica via np.isclose.
"""

import numpy as np

rng = np.random.default_rng(seed=42)

SHAPES = [(3, 3), (5, 5), (4, 7), (10, 3), (20, 20)]
N_TRIALS = 200

all_passed = True

for shape in SHAPES:
    m, n = shape
    passed = 0

    for _ in range(N_TRIALS):
        M = rng.standard_normal((m, n))

        # Norma-2 inducida (norma espectral) via numpy
        norm2 = np.linalg.norm(M, ord=2)

        # Mayor valor singular
        sigma_max = np.linalg.svd(M, compute_uv=False)[0]

        if np.isclose(norm2, sigma_max, atol=1e-10):
            passed += 1

    ok = passed == N_TRIALS
    all_passed = all_passed and ok
    status = "✓ OK" if ok else f"✗ FALLÓ ({N_TRIALS - passed}/{N_TRIALS} casos)"
    print(f"Forma {str(shape):>8}  →  {passed}/{N_TRIALS} pruebas  {status}")

print()

# Verificación simbólica con un ejemplo concreto del ejercicio
print("── Caso concreto (Ejercicio 2, Examen 2025-02-24) ──")
A = np.array([[0, -1, 0],
              [2,  0, 0],
              [0,  0, -3]], dtype=float)

norm_A = np.linalg.norm(A, ord=2)
svd_A  = np.linalg.svd(A, compute_uv=False)

print(f"  Valores singulares de A : {svd_A}")
print(f"  ‖A‖₂ via numpy          : {norm_A:.10f}")
print(f"  σ_max(A)                : {svd_A[0]:.10f}")
print(f"  ¿Coinciden?             : {np.isclose(norm_A, svd_A[0])}")

print()
if all_passed:
    print("✓ Todas las pruebas aleatorias pasaron: ‖M‖₂ = σ_max(M).")
else:
    print("✗ Algunas pruebas fallaron.")
