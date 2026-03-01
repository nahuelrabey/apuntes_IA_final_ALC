# Módulo de Autovalores Complejos en Polinomios Cuadráticos

> **Propiedad de las Raíces Complejas.**
> Dado un polinomio cuadrático con coeficientes reales $P(\lambda) = \lambda^2 + b\lambda + c$, si el discriminante $\Delta = b^2 - 4c$ es negativo, las raíces $\lambda_1, \lambda_2$ son complejas conjugadas y su módulo es exactamente:
>
> $$
> |\lambda| = \sqrt{c}
> $$
>

## Interpretación del Enunciado

En el análisis del método SOR para matrices de $2 \times 2$, es común obtener una ecuación característica cuadrática. Si el método es estable pero oscilatorio (raíces complejas), el radio espectral $\rho(B)$ —que es el módulo de estas raíces— se puede determinar directamente a partir del término independiente del polinomio sin necesidad de calcular las raíces explícitamente.

---

## Solución Analítica

### 1. Relaciones de Vieta

Para cualquier polinomio de la forma $\lambda^2 + b\lambda + c = 0$ con raíces $\lambda_1$ y $\lambda_2$, se cumplen las relaciones de Vieta:

1.  **Suma de raíces**: $\lambda_1 + \lambda_2 = -b$
2.  **Producto de raíces**: $\lambda_1 \cdot \lambda_2 = c$

### 2. Caso de Raíces Complejas Conjugadas

Si los coeficientes $b$ y $c$ son reales y el discriminante es negativo ($b^2 - 4c < 0$), las raíces deben ser de la forma:

$$
\lambda_1 = \alpha + \beta i \quad \text{y} \quad \lambda_2 = \alpha - \beta i = \bar{\lambda}_1
$$

Sustituyendo en la relación del producto (Vieta):

$$
\lambda_1 \cdot \bar{\lambda}_1 = c
$$

Por definición de módulo de un número complejo ($z \cdot \bar{z} = |z|^2$):

$$
|\lambda_1|^2 = c \implies |\lambda_1| = \sqrt{c}
$$

Dado que $\lambda_2$ es el conjugado, su módulo es idéntico: $|\lambda_2| = |\lambda_1| = \sqrt{c}$.

### 3. Aplicación al Caso SOR ($\omega = 1/2$)

La ecuación obtenida para la matriz de iteración fue:

$$
\lambda^2 - \frac{7}{8}\lambda + \frac{1}{4} = 0
$$

Aquí identificamos $b = -7/8$ y $c = 1/4$.

1.  **Verificación del discriminante**:

$$
\Delta = \left(-\frac{7}{8}\right)^2 - 4 \cdot \frac{1}{4} = \frac{49}{64} - 1 = -\frac{15}{64} < 0
$$

    Confirmamos que las raíces son complejas conjugadas.

2.  **Cálculo del módulo**:

$$
|\lambda| = \sqrt{c} = \sqrt{\frac{1}{4}} = 0.5
$$

Por lo tanto, el radio espectral es $\rho(B) = 0.5$, lo cual garantiza la convergencia del método ($0.5 < 1$).

---

## Referencias Externas

Para profundizar en las relaciones entre raíces y coeficientes (Fórmulas de Vieta) y las propiedades de autovalores complejos:

*   **Libro**: *Linear Algebra and Its Applications* (David C. Lay). **Capítulo 5, Sección 5.5: "Complex Eigenvalues"**. En esta sección se aborda explícitamente cómo la matriz de transformación actúa sobre vectores propios complejos y se formaliza la relación entre el determinante y el módulo al cuadrado de los autovalores ($|\lambda| = \sqrt{\det(A)} = \sqrt{a^2+b^2}$).
*   **Libro**: *Introduction to Linear Algebra* (Gilbert Strang). **Capítulo 9: "Complex Vectors and Matrices"** (en ediciones anteriores puede figurar en la sección de Autovalores como "Complex Matrices"). Analiza detalladamente la aparición de autovalores conjugados en matrices reales.
*   **Libro**: *Numerical Mathematics* (Quarteroni, Sacco, Saleri). **Capítulo 4, Sección 4.3**: "Iterative Methods for solving Linear Systems". Incluye el análisis del parámetro de relajación $\omega$ del método SOR y su teorema de convergencia ligado al radio espectral.
*   **Wiki**: [Vieta's formulas](https://en.wikipedia.org/wiki/Vieta%27s_formulas) - Propiedades generales de las raíces de polinomios.

---

## Verificación Empírica Computacional

Se utiliza `SymPy` para calcular las raíces exactas y su módulo, confirmando la validez de la propiedad $\sqrt{c}$.

```python
--8<-- "demostraciones/modulo_autovalores_complejos.py"
```
