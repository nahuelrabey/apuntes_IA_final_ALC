"""
Verificación: Ejercicio 2 — Factorización QR y SVD (Examen 25/02/2026)
"""

import numpy as np


# ---------------------------------------------------------------------------
# Construcción simbólica de A a partir de una base ortonormal aleatoria
# ---------------------------------------------------------------------------
# Generamos una base ortonormal {q1..q5} de R^5 mediante QR aleatorio,
# y luego construimos A = (q1 | q1+q2 | q2+q3) para validar las factorizaciones.

np.random.seed(42)
Q_full, _ = np.linalg.qr(np.random.randn(5, 5))  # base ortonormal de R^5
q1, q2, q3, q4, q5 = Q_full.T  # columnas = vectores de la base

A = np.column_stack([q1, q1 + q2, q2 + q3])
print("Matriz A (5x3):")
print(A)
print()

# ---------------------------------------------------------------------------
# Inciso (a): Factorización QR
# ---------------------------------------------------------------------------
Q, R = np.linalg.qr(A)
print("Factorización QR — Q (5x3):")
print(np.round(Q, 6))
print("Factorización QR — R (3x3):")
print(np.round(R, 6))
print("Reconstrucción A ≈ Q·R:", np.allclose(A, Q @ R))
print()

# ---------------------------------------------------------------------------
# Inciso (b): Descomposición SVD
# ---------------------------------------------------------------------------
U, s, Vt = np.linalg.svd(A, full_matrices=False)
print("Valores singulares σ:", np.round(s, 6))
print("Reconstrucción A ≈ U·Σ·Vt:", np.allclose(A, U @ np.diag(s) @ Vt))
print()

# ---------------------------------------------------------------------------
# Inciso (c): Normas
# ---------------------------------------------------------------------------
norma_2 = s[0]  # mayor valor singular = ||A||_2
norma_inf = np.max(np.sum(np.abs(A), axis=1))  # norma inf real

print(f"||A||_2  = σ_max = {norma_2:.6f}")
print(f"||A||_∞  (real)  = {norma_inf:.6f}")
print(f"Cota inferior para ||A||_∞: σ_max / sqrt(n_cols) = {norma_2 / np.sqrt(A.shape[0]):.6f}")
print(f"Verificamos: norma_2 ≤ norma_inf: {np.allclose(norma_2, norma_inf) or norma_2 <= norma_inf}")
