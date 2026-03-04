# Número de Condición en Base 2: $\kappa_2(M) = \dfrac{\sigma_{\max}}{\sigma_{\min}}$

## Enunciado del Teorema

> Sea $M \in \mathbb{R}^{n \times n}$ invertible con descomposición SVD $M = U \Sigma V^T$ y valores singulares $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n > 0$. Entonces:
>
> $$
> \kappa_2(M) = \|M\|_2 \cdot \|M^{-1}\|_2 = \frac{\sigma_{\max}}{\sigma_{\min}}
> $$
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

??? info "Caso no invertible: número de condición infinito"
    Si $M$ es singular, $\sigma_{\min} = 0$ y la expresión $\sigma_{\max}/\sigma_{\min}$ es infinita. Esto es consistente con la definición: una matriz singular no puede invertirse, y cualquier perturbación pequeña del lado derecho puede producir errores arbitrariamente grandes en la solución, lo que se corresponde con $\kappa_2 = \infty$.

??? question "¿Por qué invertir el orden de los valores singulares?"
    Si $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n > 0$, entonces tomando recíprocos se invierte el orden de las desigualdades:

    $$
    \frac{1}{\sigma_1} \leq \frac{1}{\sigma_2} \leq \cdots \leq \frac{1}{\sigma_n}
    $$

    por lo que $\max_i \tfrac{1}{\sigma_i} = \tfrac{1}{\sigma_n} = \tfrac{1}{\sigma_{\min}}$.

---

## Verificación Computacional

```python
--8<-- "docs/demostraciones/numero_condicion_svd.py"
```

---

## Referencias Externas

- [*Numerical Linear Algebra*](https://www.google.com/books/edition/Numerical_Linear_Algebra/4Mou5YpRD_kC) (Trefethen & Bau, 1997). **Lectura 12, Theorem 12.1**. Define el número de condición en términos de la norma inducida y relaciona directamente $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$.

- [Condition number — Wikipedia, §Matrices](https://en.wikipedia.org/wiki/Condition_number#Matrices) — *Wikipedia*. Sección que formaliza la relación entre $\kappa_2$, la norma espectral y los valores singulares, con interpretación geométrica.
