# Solución del Ejercicio 5 (Examen 21 de julio de 2025 - Desigualdad de Cauchy-Schwartz)

> **Ejercicio 5.** Probar la desigualdad de Cauchy-Schwartz: $|x^* y| \le ||x||_2 ||y||_2$.

---

## Solución: Demostración Matemática

La Desigualdad de Cauchy-Schwartz es uno de los teoremas angulares del análisis matemático y el álgebra lineal subyacente a los espacios con producto interno (como las geometrías de Hilbert o el espacio $\mathbb{R}^n$ / $\mathbb{C}^n$). El denoto $x^*$ asume ser la matriz Transpuesta Conjugada (Adjunta o *Hermitiana*), ratificando que el vector podría habitar el plano complejo.

Iniciaremos el recabo analítico modelando un sistema axiomático puramente axiomático de **Mínimos Cuadrados y Proyecciones Ortogonales**, entrelazando lógicamente los cimientos que construimos en el Ejercicio 4 previo de este examen.

Sabemos categóricamente por la fundamentación euclídea que: **La norma al cuadrado de cualquier vector jamás puede ser un número negativo.**

Elijamos para modelar artificialmente a un vector $e$, constituido como aquel vector residuo estricto que resulta de restarle al vector $y$ su respectiva proyección escalar matemática sobre el vector $x$:

$$e = y - \frac{x^* y}{x^* x} x$$

Bajo la doctrina del producto interno hermítico, la norma l2 al cuadrado ($||e||_2^2$) equivale irrebocablemente al producto de un vector por su propio conjugado adosado:
$$||e||_2^2 = e^* e$$

Sometemos nuestro axioma primigenio (que dictamina matemáticamente $||e||_2^2 \ge 0$) al modelo armado por sus partes internas:

$$\left(y - \frac{x^* y}{x^* x} x \right)^* \left(y - \frac{x^* y}{x^* x} x \right) \ge 0$$

Como es un sistema sobre $\mathbb{C}^n$, debemos distribuir aplicando las rígidas normas de transposiciones conjugadas. Siendo que $x^* x = ||x||_2^2 \in \mathbb{R}$ (es un escalar puramente real), y que en el marco del plano complejo es ley que todo producto alternado $(x^* y)^* = y^* x$ y $(x^* y)(y^* x) = |x^* y|^2$:

$$ \left( y^* - \frac{(x^* y)^*}{||x||_2^2} x^* \right) \left( y - \frac{x^* y}{||x||_2^2} x \right) \ge 0 $$

Multiplicamos cruzado los cuatro términos como binomios estándar:

$$y^* y - y^* \left( \frac{x^* y}{||x||_2^2} x \right) - \left( \frac{y^* x}{||x||_2^2} x^* \right) y + \left( \frac{y^* x}{||x||_2^2} x^* \right) \left( \frac{x^* y}{||x||_2^2} x \right) \ge 0$$

Simplifiquemos reconociendo a las normas incrustadas dentro del espectro analítico individual, retirando los escalares por fuera de la multiplicación y reconociendo que $y^* y = ||y||_2^2$ y $x^* x = ||x||_2^2$:

$$||y||_2^2 - \frac{(x^* y)(y^* x)}{||x||_2^2} - \frac{(y^* x)(x^* y)}{||x||_2^2} + \frac{(y^* x)(x^* y)}{||x||_2^4} ||x||_2^2 \ge 0$$

Al simplificar la redundancia modal $(y^* x)(x^* y)$ y achicar el $||x||_2^2$ del último denominador del polinomio se devela una estructura predecible:

$$||y||_2^2 - \frac{|x^* y|^2}{||x||_2^2} - \frac{|x^* y|^2}{||x||_2^2} + \frac{|x^* y|^2}{||x||_2^2} \ge 0$$

Cancelando dos de las iteraciones asintóticas contrapuestas finales:

$$||y||_2^2 - \frac{|x^* y|^2}{||x||_2^2} \ge 0$$

Despejando nuestro axioma de desigualdad para aislar la naturaleza del producto interno por fuera de sus normas base:

$$||y||_2^2 \ge \frac{|x^* y|^2}{||x||_2^2}$$

$$||y||_2^2 ||x||_2^2 \ge |x^* y|^2$$

Finalmente, dado que todas las magnitudes abarcadas son números reales positivos lícitos por naturaleza física de la medición de norma ($||\cdot|| \ge 0$), estamos habilitados a suministrar raíz cuadrada a ambos lados del espectro de inequidad destilando el objetivo central del teorema:

$$||x||_2 ||y||_2 \ge |x^* y|$$

Demostrando de forma categórica que el valor absoluto del producto interno entre dos subespacios invariantes en la topología nunca puede exceder la frontera analítica del producto aislado por sus magnitudes métricas subyacentes.

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/05_cauchy_schwartz/verificacion.py"
```
