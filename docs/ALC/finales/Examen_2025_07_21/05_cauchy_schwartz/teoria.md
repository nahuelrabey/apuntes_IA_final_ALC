# Solución del Ejercicio 5 (Examen 21 de julio de 2025 - Desigualdad de Cauchy-Schwartz)

<Enunciado titulo="Ejercicio 5.">

Probar la desigualdad de Cauchy-Schwartz: $|x^* y| \le ||x||_2 ||y||_2$.

</Enunciado>


---

## Solución: Demostración Matemática

La desigualdad de Cauchy-Schwarz es válida en todo espacio con producto interno (como $\mathbb{R}^n$ o $\mathbb{C}^n$). La notación $x^*$ denota la transpuesta conjugada (adjunta o hermitiana), que permite extender el resultado al caso complejo.

La demostración utiliza el enfoque de mínimos cuadrados y proyecciones ortogonales, relacionado con el Ejercicio 4.

Se utiliza la propiedad fundamental: **la norma al cuadrado de cualquier vector es no negativa.**

Se define el vector residuo $e$ como la diferencia entre $y$ y su proyección sobre $x$:

$$
e = y - \frac{x^* y}{x^* x} x

$$
Por definición del producto interno hermítico:

$$
||e||_2^2 = e^* e

$$
Aplicando la condición $||e||_2^2 \ge 0$:

$$
\left(y - \frac{x^* y}{x^* x} x \right)^* \left(y - \frac{x^* y}{x^* x} x \right) \ge 0

$$
Distribuyendo la adjunta sobre el producto, y usando que $x^* x = ||x||_2^2 \in \mathbb{R}$, $(x^* y)^* = y^* x$, y $(x^* y)(y^* x) = |x^* y|^2$:

$$
\left( y^* - \frac{(x^* y)^*}{||x||_2^2} x^* \right) \left( y - \frac{x^* y}{||x||_2^2} x \right) \ge 0

$$
Expandiendo el producto:

$$
y^* y - y^* \left( \frac{x^* y}{||x||_2^2} x \right) - \left( \frac{y^* x}{||x||_2^2} x^* \right) y + \left( \frac{y^* x}{||x||_2^2} x^* \right) \left( \frac{x^* y}{||x||_2^2} x \right) \ge 0

$$
Usando que $y^* y = ||y||_2^2$ y $x^* x = ||x||_2^2$, y extrayendo los escalares:

$$
||y||_2^2 - \frac{(x^* y)(y^* x)}{||x||_2^2} - \frac{(y^* x)(x^* y)}{||x||_2^2} + \frac{(y^* x)(x^* y)}{||x||_2^4} ||x||_2^2 \ge 0

$$
Simplificando $(y^* x)(x^* y) = |x^* y|^2$ y cancelando $||x||_2^2$ en el último término:

$$
||y||_2^2 - \frac{|x^* y|^2}{||x||_2^2} - \frac{|x^* y|^2}{||x||_2^2} + \frac{|x^* y|^2}{||x||_2^2} \ge 0

$$
Cancelando dos términos iguales de signo contrario:

$$
||y||_2^2 - \frac{|x^* y|^2}{||x||_2^2} \ge 0

$$
Despejando $|x^* y|^2$:

$$
||y||_2^2 \ge \frac{|x^* y|^2}{||x||_2^2}

$$
$$
||y||_2^2 ||x||_2^2 \ge |x^* y|^2

$$
Como las normas son no negativas, se puede tomar raíz cuadrada en ambos lados:

$$
||x||_2 ||y||_2 \ge |x^* y|

$$
Queda demostrado que el valor absoluto del producto interno no puede superar el producto de las normas.

---

## Verificación Computacional en Python

```python
{/* --8<-- "Examen_2025_07_21/05_cauchy_schwartz/verificacion.py" */}
```
