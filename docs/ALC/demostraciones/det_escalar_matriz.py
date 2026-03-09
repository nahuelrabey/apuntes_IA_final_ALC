"""
Verificación empírica: det(kA) = k^n · det(A)

Se generan matrices A aleatorias de distintos tamaños y se prueba la identidad
para múltiples valores del escalar k.
"""

import numpy as np

rng = np.random.default_rng(seed=7)

SIZES = [1, 2, 3, 4, 5, 8, 10]
ESCALARES = [0, 0.5, 1, -1, 2, -3, 0.1, -0.25]
N_TESTS = 200

fallos = 0

for _ in range(N_TESTS):
    n = rng.choice(SIZES)
    A = rng.uniform(-10, 10, size=(n, n))

    for k in ESCALARES:
        det_kA = np.linalg.det(k * A)
        det_formula = (k ** n) * np.linalg.det(A)

        if not np.isclose(det_kA, det_formula, rtol=1e-9, atol=1e-11):
            fallos += 1
            print(f"[FALLO] n={n}, k={k}")
            print(f"  det(kA)   : {det_kA:.8e}")
            print(f"  k^n·det(A): {det_formula:.8e}")

total = N_TESTS * len(ESCALARES)
print(f"\nResultado: {total - fallos}/{total} casos correctos.")

if fallos == 0:
    print("✓ Verificación exitosa: det(kA) = k^n · det(A) en todos los casos.")
else:
    print(f"✗ {fallos} fallos detectados.")
