# Equivalencia de Normas Matriciales: $\|A\|_2$ y $\|A\|_\infty$

> **Demostración.** Sea $A \in \mathbb{R}^{n \times n}$. Demostrar las siguientes desigualdades que relacionan la norma matricial inducida $\ell_2$ (norma espectral) con la norma matricial inducida $\ell_\infty$ (máxima suma por filas):
>
> $$
> \frac{1}{\sqrt{n}}\|A\|_\infty \leq \|A\|_2 \leq \sqrt{n}\|A\|_\infty
> $$

## Interpretación del Enunciado

Las normas matriciales inducidas heredan propriedades de las normas vectoriales subyacentes. Dado que las normas vectoriales en $\mathbb{R}^n$ son equivalentes, sus normas inducidas también lo son. Esta demostración establece los factores de escala necesarios para acotar la norma espectral (difícil de calcular, ligada a autovalores) mediante la norma infinito (trivial de calcular por sumas de filas).

---

## Solución Analítica

Recordemos que para una norma matricial inducida por una norma vectorial $\|\cdot\|_p$, se define:
$\|A\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$.

### 1. Demostración de $\|A\|_2 \leq \sqrt{n}\|A\|_\infty$

Por definición de norma inducida $\ell_2$:

$$
\|A\|_2 = \max_{x \neq 0} \frac{\|Ax\|_2}{\|x\|_2}
$$

Utilizando las equivalencias de normas vectoriales ya demostradas ($\|v\|_2 \leq \sqrt{n}\|v\|_\infty$ y $\|v\|_\infty \leq \|v\|_2$):

$$
\|Ax\|_2 \leq \sqrt{n}\|Ax\|_\infty
$$
$$
\|x\|_2 \geq \|x\|_\infty \implies \frac{1}{\|x\|_2} \leq \frac{1}{\|x\|_\infty}
$$

Combinando ambas desigualdades:

$$
\frac{\|Ax\|_2}{\|x\|_2} \leq \frac{\sqrt{n}\|Ax\|_\infty}{\|x\|_\infty}
$$

Al tomar el máximo sobre $x \neq 0$:

$$
\max_{x \neq 0} \frac{\|Ax\|_2}{\|x\|_2} \leq \sqrt{n} \cdot \max_{x \neq 0} \frac{\|Ax\|_\infty}{\|x\|_\infty}
$$
$$
\|A\|_2 \leq \sqrt{n}\|A\|_\infty
$$

### 2. Demostración de $\frac{1}{\sqrt{n}}\|A\|_\infty \leq \|A\|_2$

Nuevamente usamos las equivalencias vectoriales: $\|v\|_\infty \leq \|v\|_2$ y $\|v\|_2 \leq \sqrt{n}\|v\|_\infty \implies \|v\|_\infty \geq \frac{1}{\sqrt{n}}\|v\|_2$.

$$
\|Ax\|_\infty \leq \|Ax\|_2
$$

$$
\|x\|_\infty \geq \frac{1}{\sqrt{n}}\|x\|_2 \implies \frac{1}{\|x\|_\infty} \leq \frac{\sqrt{n}}{\|x\|_2}
$$

Multiplicando:

$$
\frac{\|Ax\|_\infty}{\|x\|_\infty} \leq \frac{\|Ax\|_2 \cdot \sqrt{n}}{\|x\|_2}
$$

Tomando el máximo sobre $x$:

$$
\|A\|_\infty \leq \sqrt{n}\|A\|_2 \implies \frac{1}{\sqrt{n}}\|A\|_\infty \leq \|A\|_2
$$

Combinando ambos resultados:

$$
\frac{1}{\sqrt{n}}\|A\|_\infty \leq \|A\|_2 \leq \sqrt{n}\|A\|_\infty
$$

---

--8<-- "docs/demostraciones/verificacion_normas_matriciales_2_inf.py"
