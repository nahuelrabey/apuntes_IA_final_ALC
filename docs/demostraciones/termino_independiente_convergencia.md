# Rol del Término Independiente $c$ en Métodos Iterativos

> **Proposición.**
> Sea el método iterativo $x^{k+1} = B\, x^k + c$. Si el método converge, el punto fijo $x^*$ satisface:
>
> $$
> x^* = (I - B)^{-1} c
> $$
>
> La condición de convergencia ($\rho(B) < 1$) es independiente de $c$.

## Interpretación del Enunciado

Al analizar el inciso **b)** del método SOR se tiene la iteración:

$$
x^{k+1} = B(\omega)\, x^k + c, \qquad c = (D + \omega L)^{-1}\,\omega b
$$

Una pregunta natural es: ¿por qué la condición $\omega \in (0,2)$ no involucra a $c$? La demostración muestra que el término independiente determina *hacia dónde* converge el método, pero no *si* converge.

---

## Demostración

### 1. El Punto Fijo

Si el método converge, existe $x^*$ tal que la sucesión se estabiliza. Tomando el límite cuando $k \to \infty$ en la recursión:

$$
x^* = B\, x^* + c
$$

Despejando $x^*$:

$$
(I - B)\, x^* = c \implies x^* = (I - B)^{-1} c
$$

Nótese que esta relación coincide exactamente con la solución del sistema $Ax = b$, lo cual garantiza que el método iterativo converge a la solución correcta (cuando converge).

### 2. Dinámica del Error

Definimos el error en el paso $k$ como $e^k = x^k - x^*$. Usando la recursión y la ecuación del punto fijo:

$$
e^{k+1} = x^{k+1} - x^* = \underbrace{(B x^k + c)}_{x^{k+1}} - \underbrace{(B x^* + c)}_{x^*} = B\, e^k
$$

El término $c$ **se cancela exactamente**. Aplicando esta relación de forma sucesiva:

$$
e^k = B^k\, e^0
$$

### 3. Condición de Convergencia

El error tiende a cero para cualquier condición inicial $e^0$ si y solo si $B^k \to \mathbf{0}$, lo cual ocurre si y solo si (ver [convergencia y radio espectral](./convergencia_radio_espectral.md)):

$$
\rho(B) < 1
$$

Esta condición depende **únicamente de $B$**, no de $c$.

---

## Conclusión

| Elemento | Rol |
|---|---|
| $B(\omega)$ | Controla **si** el método converge: se requiere $\rho(B) < 1$ |
| $c$ | Determina **a dónde** converge: el punto fijo $x^* = (I-B)^{-1}c$ |

En el contexto del método SOR, la condición $\omega \in (0, 2)$ se deriva exclusivamente del análisis de $\det(B(\omega)) = (1-\omega)^n$ y no depende de $c$.

---

## Referencias Externas

Para profundizar en la teoría de convergencia de métodos iterativos:

*   **Libro**: *Numerical Mathematics* (Quarteroni, Sacco, Saleri). **Capítulo 4, Sección 4.2: \"Convergence Results for Iterative Methods\"**. Define el punto fijo, la matriz de amplificación del error, y prueba el teorema de convergencia basado en el radio espectral.
*   **Libro**: *Numerical Linear Algebra* (Trefethen & Bau). **Lectura 25: \"Overview of Iterative Methods\"**. Introduce la idea de que la velocidad de convergencia depende de $\rho(B)$, independent of the right-hand side.
*   **Libro**: *Numerical Analysis* (Burden & Faires). **Capítulo 7, Sección 7.3: \"The Jacobi and Gauss-Seidel Iterative Techniques\"**. Demuestra explícitamente que el vector $c$ no participa en la condición de convergencia.
*   **Wiki**: [Iterative method – Fixed-point iteration](https://en.wikipedia.org/wiki/Iterative_method#Stationary_iterative_methods) — Describe la forma general $x^{k+1} = Bx^k + c$ y los criterios de convergencia.
