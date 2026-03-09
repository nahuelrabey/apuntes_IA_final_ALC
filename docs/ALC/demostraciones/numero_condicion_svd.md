# Número de Condición en Base 2: $\kappa_2(M) = \dfrac{\sigma_{\max}}{\sigma_{\min}}$

## Enunciado del Teorema

> Sea $M \in \mathbb{R}^{n \times n}$ invertible con descomposición SVD $M = U \Sigma V^T$ y valores singulares $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n > 0$. Entonces:
>
>

$$
> \kappa_2(M) = \|M\|_2 \cdot \|M^{-1}\|_2 = \frac{\sigma_{\max}}{\sigma_{\min}}
>

$$
>

---

## Demostración

La demostración se apoya directamente en el resultado $\|M\|_2 = \sigma_{\max}(M)$ ya establecido.

### Paso 1: Definición del número de condición

El número de condición en base 2 se define como:

$$
\kappa_2(M) = \|M\|_2 \cdot \|M^{-1}\|_2

$$
Por el resultado de la [norma-2 y el mayor valor singular](norma2_igual_sigma_max.md), sabemos que:

$$
\|M\|_2 = \sigma_{\max}(M) = \sigma_1

$$
Resta calcular $\|M^{-1}\|_2$.

### Paso 2: SVD de la matriz inversa

Si $M = U \Sigma V^T$, entonces:

$$
M^{-1} = (U \Sigma V^T)^{-1} = V \Sigma^{-1} U^T

$$
Esta es una factorización del tipo $M^{-1} = \tilde{U} \tilde{\Sigma} \tilde{V}^T$ con:

- $\tilde{U} = V$ (ortogonal),
- $\tilde{V} = U$ (ortogonal),
- $\tilde{\Sigma} = \Sigma^{-1} = \text{diag}\!\left(\tfrac{1}{\sigma_1}, \tfrac{1}{\sigma_2}, \ldots, \tfrac{1}{\sigma_n}\right)$.

Esta es exactamente la SVD de $M^{-1}$: los valores singulares de $M^{-1}$ son $\tfrac{1}{\sigma_i}$.

### Paso 3: Norma-2 de la inversa

Como los valores singulares de $M^{-1}$ son $\tfrac{1}{\sigma_1} \leq \tfrac{1}{\sigma_2} \leq \cdots \leq \tfrac{1}{\sigma_n}$ (el orden se invierte al tomar recíprocos), el mayor de ellos es $\tfrac{1}{\sigma_n} = \tfrac{1}{\sigma_{\min}}$.

Aplicando nuevamente el teorema de la norma-2:

$$
\|M^{-1}\|_2 = \sigma_{\max}(M^{-1}) = \frac{1}{\sigma_{\min}(M)}

$$
### Paso 4: Producto final

Combinando los Pasos 1 y 3:

$$
\kappa_2(M) = \|M\|_2 \cdot \|M^{-1}\|_2 = \sigma_{\max} \cdot \frac{1}{\sigma_{\min}} = \frac{\sigma_{\max}}{\sigma_{\min}} \qquad \blacksquare

$$
---

??? info "Interpretación Geométrica"
    La SVD muestra que $M$ estira la bola unitaria en la dirección $v_1$ por un factor $\sigma_{\max}$ y la contrae en la dirección $v_n$ por un factor $\sigma_{\min}$. El número de condición $\kappa_2(M)$ mide exactamente el cociente entre la máxima elongación y la máxima contracción. Cuando $\kappa_2(M)$ es grande, la matriz está casi degenerada: estira fuertemente en una dirección y aplana casi a cero en otra, lo que hace numericamente inestable la resolución de sistemas lineales.

    Fin de la interpretación.

??? info "Caso no invertible: número de condición infinito"
    Si $M$ es singular, $\sigma_{\min} = 0$ y la expresión $\sigma_{\max}/\sigma_{\min}$ es infinita. Esto es consistente con la definición: una matriz singular no puede invertirse, y cualquier perturbación pequeña del lado derecho puede producir errores arbitrariamente grandes en la solución, lo que se corresponde con $\kappa_2 = \infty$.

    Fin de la observación.

??? question "¿Por qué invertir el orden de los valores singulares?"
    Si $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n > 0$, entonces tomando recíprocos se invierte el orden de las desigualdades:

$$
    \frac{1}{\sigma_1} \leq \frac{1}{\sigma_2} \leq \cdots \leq \frac{1}{\sigma_n}

$$
    por lo que

$$
    \max_i \tfrac{1}{\sigma_i} = \tfrac{1}{\sigma_n} = \tfrac{1}{\sigma_{\min}}.

$$
    Fin de la explicación.

---

## Verificación Computacional

```python
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

```
---

## Referencias Externas

- [*Numerical Linear Algebra*](https://www.google.com/books/edition/Numerical_Linear_Algebra/4Mou5YpRD_kC) (Trefethen & Bau, 1997). **Lectura 12, Theorem 12.1**. Define el número de condición en términos de la norma inducida y relaciona directamente $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$.

- [Condition number — Wikipedia, §Matrices](https://en.wikipedia.org/wiki/Condition_number#Matrices) — *Wikipedia*. Sección que formaliza la relación entre $\kappa_2$, la norma espectral y los valores singulares, con interpretación geométrica.
