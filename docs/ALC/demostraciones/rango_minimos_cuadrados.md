# Demostración: Rango Completo y Unicidad en Mínimos Cuadrados

## Interpretación del Enunciado

Sea $M \in \mathbb{R}^{m \times n}$ la matriz de diseño de un sistema de mínimos cuadrados. La solución de mínimos cuadrados $\hat{\theta}$ es **única** si y solo si $M$ tiene **rango columna completo**, es decir, $\text{Rango}(M) = n$.

Este resultado establece la cantidad mínima de observaciones necesarias y las condiciones sobre los datos para que el ajuste por mínimos cuadrados produzca una solución única.

---

## Demostración

### Paso 1: Las ecuaciones normales

El problema de mínimos cuadrados consiste en minimizar $\|M\vec{\theta} - \vec{Z}\|_2^2$. La condición necesaria y suficiente de mínimo es que el residuo sea ortogonal a $Col(M)$:

$$
M^T(M\hat{\theta} - \vec{Z}) = \vec{0}

$$
Reorganizando:

$$
(M^T M)\,\hat{\theta} = M^T \vec{Z}

$$
Este es el sistema de **ecuaciones normales**, de dimensiones $n \times n$.

### Paso 2: Unicidad ↔ Invertibilidad de $M^TM$

La solución $\hat{\theta}$ es única si y solo si el sistema de ecuaciones normales tiene solución única. Por el Teorema de Rouché-Frobenius, esto ocurre cuando $M^TM$ es invertible, permitiendo despejar:

$$
\hat{\theta} = (M^T M)^{-1} M^T \vec{Z}

$$
### Paso 3: Invertibilidad de $M^TM$ ↔ Rango completo de $M$

Demostraremos que $M^TM$ es invertible si y solo si $\text{Rango}(M) = n$.

**($\Rightarrow$) Si $\text{Rango}(M) < n$:** Existe $\vec{v} \neq \vec{0}$ tal que $M\vec{v} = \vec{0}$ (hay vectores no nulos en el núcleo de $M$). Entonces:

$$
M^TM\vec{v} = M^T(M\vec{v}) = M^T\vec{0} = \vec{0}

$$
Por lo tanto $\vec{v} \in Nu(M^TM)$ con $\vec{v} \neq \vec{0}$, lo que implica que $M^TM$ **no es invertible**.

**($\Leftarrow$) Si $\text{Rango}(M) = n$:** Sea $\vec{v}$ tal que $M^TM\vec{v} = \vec{0}$. Premultiplicamos por $\vec{v}^T$:

$$
\vec{v}^T M^T M \vec{v} = 0 \quad \Rightarrow \quad \|M\vec{v}\|_2^2 = 0 \quad \Rightarrow \quad M\vec{v} = \vec{0}

$$
Como $\text{Rango}(M) = n$, el único vector en $Nu(M)$ es $\vec{0}$, por lo que $\vec{v} = \vec{0}$.

Entonces $Nu(M^TM) = \{\vec{0}\}$, lo que implica que $M^TM$ **es invertible**. ∎

### Paso 4: Mínima cantidad de puntos

Para que $M \in \mathbb{R}^{m \times n}$ tenga rango $n$, es necesario que $m \geq n$:

- Si $m < n$: la matriz tiene más columnas que filas, por lo que $\text{Rango}(M) \leq m < n$. No puede tener rango columna completo.

- Si $m \geq n$ **y** las columnas son linealmente independientes: $\text{Rango}(M) = n$ y la solución es única.

Por lo tanto, se necesitan **al menos $n$ puntos** (observaciones), donde $n$ es el número de parámetros del modelo.

---

## Verificación Empírica Computacional

```python
"""
Verificación empírica: Rango completo de M y unicidad de la solución en mínimos cuadrados.

Comprueba que:
  1. Si Rango(M) = n, entonces M^TM es invertible y la solución de MC es única.
  2. Si Rango(M) < n, entonces M^TM es singular y hay infinitas soluciones.
"""

import numpy as np

np.random.seed(0)


def verificar_rango_completo():
    """M con rango completo → M^TM invertible → solución única."""
    m, n = 10, 3
    M = np.random.randn(m, n)  # rango 3 con prob. 1

    MtM = M.T @ M
    det = np.linalg.det(MtM)

    assert np.linalg.matrix_rank(M) == n, "M no tiene rango completo"
    assert abs(det) > 1e-10, f"M^TM debería ser invertible (det={det:.4f})"

    # Solución de MC
    theta_real = np.random.randn(n)
    Z = M @ theta_real + np.random.randn(m) * 0.01  # datos con ruido leve
    theta_hat = np.linalg.solve(MtM, M.T @ Z)

    assert np.allclose(theta_hat, theta_real, atol=0.1), "Solución incorrecta"
    print(f"[OK] Rango completo: Rango(M)={n}, det(M^TM)={det:.4f} → solución única")


def verificar_rango_deficiente():
    """M con rango < n → M^TM singular → infinitas soluciones."""
    m, n = 10, 3
    # Construimos M con columnas dependientes (col 3 = col 1 + col 2)
    M_base = np.random.randn(m, 2)
    M = np.hstack([M_base, M_base[:, [0]] + M_base[:, [1]]])

    MtM = M.T @ M
    det = np.linalg.det(MtM)
    rango = np.linalg.matrix_rank(M)

    assert rango < n, f"Se esperaba rango deficiente, got {rango}"
    assert abs(det) < 1e-8, f"M^TM debería ser singular (det={det:.2e})"
    print(f"[OK] Rango deficiente: Rango(M)={rango} < n={n}, det(M^TM)={det:.2e} ≈ 0 → infinitas soluciones")


def verificar_minimo_puntos():
    """Con m < n puntos, el rango nunca puede ser n."""
    n = 4
    for m in range(1, n):
        M = np.random.randn(m, n)
        rango = np.linalg.matrix_rank(M)
        assert rango <= m < n, f"Falla para m={m}"
    print(f"[OK] Con m < n={n} puntos, Rango(M) ≤ m < n siempre → solución no única")


if __name__ == "__main__":
    verificar_rango_completo()
    verificar_rango_deficiente()
    verificar_minimo_puntos()
    print("\nTodos los casos de rango y unicidad en mínimos cuadrados verificados correctamente.")

```
---

## Bibliografía y Recursos Educativos

### 📖 Libros de Texto

*   **Libro**: [*Introduction to Linear Algebra*](https://math.mit.edu/~gs/linearalgebra/) (Gilbert Strang, 5ta ed., 2016). **Capítulo 4, Sección 4.2**. Presenta las ecuaciones normales y la condición de rango completo para la unicidad de la solución de mínimos cuadrados.
*   **Libro**: [*Álgebra Lineal y sus Aplicaciones*](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006185) (David C. Lay, 5ta ed., 2016). **Capítulo 6, Sección 6.5**. Trata la solución de mínimos cuadrados y la invertibilidad de $A^TA$ bajo rango completo.

### 🌐 Recursos Web

*   **Web**: [Least squares — Normal equations](https://en.wikipedia.org/wiki/Ordinary_least_squares#Matrix/vector_formulation) - *Wikipedia (EN)*. Derivación de las ecuaciones normales y condición de unicidad en la sección de formulación matricial.
