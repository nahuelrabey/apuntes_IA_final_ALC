"""
Verificación de la submultiplicatividad de normas matriciales inducidas.

Confirma que ||Mv|| <= ||M|| * ||v|| para:
- Normas inducidas 1, 2 e inf.
- Matrices y vectores aleatorios de distinto tamaño.
"""

import numpy as np

np.random.seed(42)
SIZES = [3, 5, 10, 50]
NORMS = [1, 2, np.inf]
NORM_NAMES = {1: "1", 2: "2", np.inf: "inf"}
TRIALS = 1_000


def matrix_induced_norm(M: np.ndarray, p) -> float:
    """Norma matricial inducida por la norma vectorial p."""
    if p == 1:
        return np.max(np.sum(np.abs(M), axis=0))   # máxima suma por columna
    elif p == np.inf:
        return np.max(np.sum(np.abs(M), axis=1))   # máxima suma por fila
    elif p == 2:
        return np.linalg.norm(M, ord=2)             # mayor valor singular


print("=" * 65)
print("  Verificación: ||Mv|| <= ||M|| * ||v||  para normas inducidas")
print("=" * 65)

all_passed = True

for n in SIZES:
    for p in NORMS:
        violations = 0
        max_ratio = 0.0

        for _ in range(TRIALS):
            M = np.random.randn(n, n)
            v = np.random.randn(n)

            lhs = np.linalg.norm(M @ v, ord=p)
            rhs = matrix_induced_norm(M, p) * np.linalg.norm(v, ord=p)

            # Permitir un margen numérico muy pequeño por punto flotante
            if lhs > rhs + 1e-10:
                violations += 1

            if np.linalg.norm(v, ord=p) > 1e-14:
                max_ratio = max(max_ratio, lhs / rhs)

        status = "✓ PASS" if violations == 0 else f"✗ FAIL ({violations} violaciones)"
        print(
            f"  n={n:3d} | norma-{NORM_NAMES[p]:>3s} | {status} | "
            f"max(||Mv|| / (||M|| ||v||)) = {max_ratio:.6f}"
        )
        if violations > 0:
            all_passed = False

print("=" * 65)
print(f"\n  Resultado global: {'TODAS LAS PRUEBAS PASARON ✓' if all_passed else 'EXISTEN FALLAS ✗'}")
print(
    "\n  Nota: max_ratio <= 1.0 en todos los casos confirma que la cota\n"
    "  es ajustada y válida, sin excederse nunca (salvo ruido numérico)."
)
