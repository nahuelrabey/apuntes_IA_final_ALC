# Ejercicio 2: Factorización QR y SVD

> **Ejercicio 2.** Sea $\{q_1, q_2, q_3, q_4, q_5\}$ una base ortonormal de $\mathbb{R}^5$, $A$ una
> matriz de $5 \times 3$ tal que
>
> $$
> A = \left(\, q_1 \;\middle|\; q_1 + q_2 \;\middle|\; q_2 + q_3 \,\right)
> $$
>
> **(a)** De una factorización $QR$ de la matriz $A$.
>
> **(b)** De una descomposición en valores singulares de la matriz $A$.
>
> **(c)** Calcule $\|A\|_2$. Indique una cota inferior para $\|A\|_\infty$.

---

## Interpretación del Enunciado

<!-- Las columnas de A se expresan como combinaciones lineales de la base ortonormal (q_i).
     Esto sugiere escribir A = Q_hat * R donde Q_hat tiene columnas ortonormales extraídas
     de la base, y R refleja los coeficientes de combinación. -->

---

## Solución del Ejercicio

### Inciso A — Factorización QR

> **(a)** De una factorización $QR$ de la matriz $A$.

<!-- Expresar cada columna de A como combinación de q_i ortogonales.
     La estructura triangular de los coeficientes da directamente R. -->

### Inciso B — Descomposición SVD

> **(b)** De una descomposición en valores singulares de la matriz $A$.

<!-- Calcular A^T A, sus autovalores (σ_i^2) y autovectores (V).
     Los vectores singulares izquierdos U_i = A v_i / σ_i. -->

### Inciso C — Normas

> **(c)** Calcule $\|A\|_2$. Indique una cota inferior para $\|A\|_\infty$.

<!-- ||A||_2 = σ_max (mayor valor singular).
     Cota inferior para ||A||_∞: usar submultiplicatividad o norma de alguna fila de A. -->

---

Ver implementación en [`verificacion.py`](verificacion.py).

--8<-- "Examen_2026_02_25/02_qr_svd/verificacion.py"
