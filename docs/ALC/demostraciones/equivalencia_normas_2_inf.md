# Equivalencia de Normas: $\ell_2$ y $\ell_\infty$

> **Demostración.** Sea $x \in \mathbb{R}^n$. Demostrar las siguientes desigualdades que relacionan la norma euclídea ($\|x\|_2$) con la norma del máximo ($\|x\|_\infty$):
>
> $$
> \|x\|_\infty \leq \|x\|_2 \leq \sqrt{n}\|x\|_\infty
> $$

## Interpretación del Enunciado

En espacios de dimensión finita, todas las normas son equivalentes en el sentido de que "miden" lo mismo salvo constantes multiplicativas. Esta demostración técnica establece los límites de cuánto puede diferir la longitud de un vector si cambiamos nuestro criterio de medición de la mayor componente (norma infinito) a la distancia pitagórica (norma dos).

---

## Solución Analítica

Sea $x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$.

### 1. Demostración de $\|x\|_\infty \leq \|x\|_2$

Recordemos las definiciones:
-   $\|x\|_\infty = \max_{1 \leq i \leq n} |x_i|$
-   $\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$

Sea $|x_k|$ la componente de mayor magnitud, es decir, $|x_k| = \|x\|_\infty$.
Como todos los términos $x_i^2$ son no negativos, se cumple:

$$
x_k^2 \leq \sum_{i=1}^n x_i^2
$$

Aplicando la raíz cuadrada (que es una función monótona creciente en $[0, \infty)$):

$$
\sqrt{x_k^2} \leq \sqrt{\sum_{i=1}^n x_i^2}
$$
$$
|x_k| \leq \|x\|_2
$$
$$
\|x\|_\infty \leq \|x\|_2
$$

### 2. Demostración de $\|x\|_2 \leq \sqrt{n}\|x\|_\infty$

Partimos nuevamente de la definición de la norma $\ell_2$. Sabemos que para cada componente $|x_i| \leq \|x\|_\infty$, y por lo tanto $x_i^2 \leq \|x\|_\infty^2$.
Sumando sobre todas las componentes:

$$
\sum_{i=1}^n x_i^2 \leq \sum_{i=1}^n \|x\|_\infty^2
$$

Como el término $\|x\|_\infty^2$ es constante respecto al índice $i$:

$$
\sum_{i=1}^n x_i^2 \leq n \cdot \|x\|_\infty^2
$$

Aplicando la raíz cuadrada en ambos lados:

$$
\sqrt{\sum_{i=1}^n x_i^2} \leq \sqrt{n \cdot \|x\|_\infty^2}
$$
$$
\|x\|_2 \leq \sqrt{n} \cdot \|x\|_\infty
$$

Combinando ambos resultados, queda demostrada la cadena de desigualdades:

$$
\|x\|_\infty \leq \|x\|_2 \leq \sqrt{n}\|x\|_\infty
$$

---

--8<-- "docs/demostraciones/verificacion_normas_2_inf.py"
