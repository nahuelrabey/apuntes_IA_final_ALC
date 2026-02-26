"""
Verificación empírica:
    det((1-ω)D - ωU) = (1-ω)^n · det(D)

Se generan matrices A aleatorias con diagonal no nula, se extraen los bloques
D y U, y se compara el determinante calculado directamente contra la fórmula.
"""

import numpy as np

rng = np.random.default_rng(seed=42)

N_TESTS = 500
OMEGAS = [0.1, 0.5, 1.0, 1.5, 1.9, -0.5, 2.5]
SIZES = [2, 3, 5, 8]

fallos = 0

for _ in range(N_TESTS):
    n = rng.choice(SIZES)

    # Generar A con diagonal no nula (sumamos 1 para evitar ceros exactos)
    A = rng.uniform(-5, 5, size=(n, n))
    A[np.arange(n), np.arange(n)] += rng.choice([-1, 1], size=n) * (rng.uniform(0.5, 2, size=n))

    # Extraer bloques D y U
    D = np.diag(np.diag(A))
    U = np.triu(A, k=1)   # estrictamente triangular superior

    for omega in OMEGAS:
        M = (1 - omega) * D - omega * U

        det_directo = np.linalg.det(M)
        det_formula = (1 - omega) ** n * np.linalg.det(D)

        if not np.isclose(det_directo, det_formula, rtol=1e-8, atol=1e-10):
            fallos += 1
            print(f"[FALLO] n={n}, omega={omega}")
            print(f"  det directo : {det_directo:.6e}")
            print(f"  det fórmula : {det_formula:.6e}")

total_casos = N_TESTS * len(OMEGAS)
print(f"\nResultado: {total_casos - fallos}/{total_casos} casos correctos.")

if fallos == 0:
    print("✓ Verificación exitosa: det((1-ω)D − ωU) = (1-ω)^n · det(D) en todos los casos.")
else:
    print(f"✗ {fallos} fallos detectados.")
