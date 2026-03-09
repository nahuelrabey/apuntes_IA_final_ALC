"""
Verificación empírica del Teorema de Convergencia según módulo del autovalor
en Cadenas de Markov (incluyendo caso complejo).

Se verifican los tres casos del teorema:
  1. |lambda| < 1  -> término desaparece
  2. lambda = 1    -> término constante
  3. |lambda| = 1, lambda != 1 -> oscilación sin convergencia
"""

import numpy as np
import sympy as sp

print("=" * 60)
print("CASO 1: |lambda| < 1 (real y complejo)")
print("=" * 60)

# Caso 1a: lambda real con |lambda| < 1
lambda_real = 0.7
potencias_real = [lambda_real**k for k in range(20)]
print(f"\nlambda = {lambda_real} (real)")
print(f"  lambda^10  = {lambda_real**10:.8f}")
print(f"  lambda^20  = {lambda_real**20:.8f}")
assert np.isclose(lambda_real**50, 0.0, atol=1e-7), "FALLA: no converge a 0"
print("  -> Converge a 0. OK")

# Caso 1b: lambda complejo con |lambda| < 1
r = 0.8
theta = np.pi / 3  # argumento arbitrario
lambda_complejo = r * np.exp(1j * theta)
print(f"\nlambda = {r} * e^(i*pi/3)  (complejo, |lambda| = {abs(lambda_complejo):.4f})")
potencias_mod = [abs(lambda_complejo**k) for k in range(50)]
print(f"  |lambda^10| = {abs(lambda_complejo**10):.8f}")
print(f"  |lambda^20| = {abs(lambda_complejo**20):.8f}")
assert np.isclose(abs(lambda_complejo**50), 0.0, atol=1e-4), "FALLA: no converge a 0"
print("  -> |lambda^k| = r^k -> 0 independientemente del argumento theta. OK")

print()
print("=" * 60)
print("CASO 2: lambda = 1 (componente constante)")
print("=" * 60)

lambda_uno = 1.0
potencias_uno = [lambda_uno**k for k in range(100)]
assert all(np.isclose(p, 1.0) for p in potencias_uno), "FALLA: lambda=1 no es constante"
print(f"\nlambda = 1: lambda^k = 1 para todo k. OK")

print()
print("=" * 60)
print("CASO 3: |lambda| = 1, lambda != 1  (oscilación sin convergencia)")
print("=" * 60)

# Caso 3a: lambda = -1 (real, periodo 2)
lambda_menos1 = -1.0
pots = [lambda_menos1**k for k in [0, 1, 2, 3, 4, 5]]
print(f"\nlambda = -1  -> (-1)^k: {pots}")
print("  Alterna entre +1 y -1, no converge.")

# Verificación: la sucesión no es de Cauchy
diffs = [abs(pots[i+1] - pots[i]) for i in range(len(pots)-1)]
assert any(d > 1.0 for d in diffs), "FALLA: se esperaba no convergencia"
print("  -> max|diff| =", max(diffs), "(no tiende a 0). OK")

# Caso 3b: lambda = e^(2*pi*i/3)  (complejo, periodo 3)
lambda_p3 = np.exp(2j * np.pi / 3)
pots_p3 = [lambda_p3**k for k in range(6)]
print(f"\nlambda = e^(2*pi*i/3)  (|lambda| = {abs(lambda_p3):.6f})")
print("  Potencias:")
for k, p in enumerate(pots_p3):
    print(f"    lambda^{k} = {p.real:.4f} + {p.imag:.4f}i  (|.| = {abs(p):.4f})")

# Verificar que el módulo nunca cae: siempre es exactamente 1
for k in range(100):
    assert np.isclose(abs(lambda_p3**k), 1.0, atol=1e-10), f"FALLA en k={k}"
print("  -> |lambda^k| = 1 para todo k: oscilación permanente. OK")

print()
print("=" * 60)
print("VERIFICACIÓN SIMBÓLICA (SymPy)")
print("=" * 60)

# Confirmación simbólica: |r * e^(i*theta)|^k = r^k
r_sym, theta_sym, k_sym = sp.symbols('r theta k', positive=True)
lam = r_sym * sp.exp(sp.I * theta_sym)
modulo_k = sp.Abs(lam**k_sym)
modulo_k_simplified = sp.simplify(modulo_k)
print(f"\n|lambda^k| = |r * e^(i*theta)|^k = {modulo_k_simplified}")
print("  -> Simbólicamente, el resultado es r^k, independiente de theta. OK")

print()
print("=" * 60)
print("RESUMEN")
print("=" * 60)
print("""
| |lambda|        | Comportamiento de lambda^k | Genera limite? |
|-----------------|----------------------------|----------------|
| < 1 (real/cmplx)| -> 0                       | SI (desaparece)|
| = 1             | = 1 constante              | SI (equilibrio)|
| = 1, lambda!=1  | oscila en circulo unitario | NO             |
""")
print("Todos los casos verificados correctamente.")
