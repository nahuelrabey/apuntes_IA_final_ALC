# Demostración: Teorema de Rouché-Frobenius

## Interpretación del Enunciado

> Dado un sistema lineal $A\vec{x} = \vec{b}$, donde $A \in \mathbb{R}^{m \times n}$ y $\vec{b} \in \mathbb{R}^m$, el sistema tiene solución si y solo si $\text{Rango}(A) = \text{Rango}(A|\vec{b})$, donde $(A|\vec{b})$ es la matriz ampliada. Además:
>
> - Si $\text{Rango}(A) = \text{Rango}(A|\vec{b}) = n$, la solución es **única**.
> - Si $\text{Rango}(A) = \text{Rango}(A|\vec{b}) < n$, existen **infinitas soluciones** (con $n - \text{Rango}(A)$ variables libres).
> - Si $\text{Rango}(A) \neq \text{Rango}(A|\vec{b})$, el sistema es **incompatible** (sin solución).

Este teorema es el criterio fundamental de compatibilidad de sistemas lineales. En el contexto de mínimos cuadrados, justifica cuántos puntos se necesitan para obtener una solución única.

---

## Demostración

### Parte 1: Condición de compatibilidad

El sistema $A\vec{x} = \vec{b}$ tiene solución si y solo si $\vec{b}$ pertenece al espacio columna de $A$, es decir, $\vec{b} \in Col(A)$.

Por definición, $Col(A)$ está generado por las columnas de $A$. Agregar $\vec{b}$ a la matriz no cambia dicho espacio si y solo si $\vec{b}$ ya está en él. Esto equivale a:

$$
\text{Rango}(A) = \text{Rango}(A|\vec{b})

$$
Si $\vec{b} \notin Col(A)$, entonces $\vec{b}$ aporta una dirección linealmente independiente al sistema, y el rango de la matriz ampliada es estrictamente mayor:

$$
\text{Rango}(A|\vec{b}) = \text{Rango}(A) + 1

$$
En ese caso el sistema es incompatible.

### Parte 2: Unicidad de la solución

Supuesto que el sistema es compatible ($\vec{b} \in Col(A)$), analicemos cuántas soluciones existen.

El conjunto de soluciones del sistema homogéneo $A\vec{x} = \vec{0}$ es el **núcleo** de $A$, denotado $Nu(A)$. Por el **Teorema de la Dimensión** (o Teorema Rango-Nulidad):

$$
\text{Rango}(A) + \dim(Nu(A)) = n

$$
donde $n$ es el número de columnas (incógnitas).

- Si $\text{Rango}(A) = n$, entonces $\dim(Nu(A)) = 0$, es decir, $Nu(A) = \{\vec{0}\}$. La única solución al sistema homogéneo es el vector nulo, por lo que la solución particular es **única**.

- Si $\text{Rango}(A) < n$, entonces $\dim(Nu(A)) = n - \text{Rango}(A) > 0$. Existen $n - \text{Rango}(A)$ variables libres y por tanto **infinitas soluciones**, de la forma:

$$
\vec{x} = \vec{x}_p + \vec{x}_h

$$
donde $\vec{x}_p$ es una solución particular y $\vec{x}_h \in Nu(A)$ es cualquier solución homogénea. ∎

---

## Aplicación en Mínimos Cuadrados

En el contexto de mínimos cuadrados con matriz de diseño $M \in \mathbb{R}^{m \times n}$, las ecuaciones normales son:

$$
(M^T M)\,\hat{\theta} = M^T Z

$$
Este es un sistema cuadrado $n \times n$. Para que tenga solución **única**, por Rouché-Frobenius se necesita:

$$
\text{Rango}(M^T M) = n

$$
Lo que equivale a que $M^T M$ sea invertible, condición que se cumple si y solo si $M$ tiene **rango columna completo** ($\text{Rango}(M) = n$).

---

## Verificación Empírica Computacional

```python
"""
Verificación empírica del Teorema de Rouché-Frobenius.

Comprueba los tres casos del teorema sobre sistemas aleatorios:
  1. Sistema compatible con solución única (Rango(A) = Rango(A|b) = n)
  2. Sistema compatible con infinitas soluciones (Rango(A) = Rango(A|b) < n)
  3. Sistema incompatible (Rango(A) < Rango(A|b))
"""

import numpy as np

np.random.seed(42)


def caso_compatible_unico():
    """Rango(A) = Rango(A|b) = n → solución única."""
    n = 4
    A = np.random.randn(n + 2, n)  # m > n, rango completo
    x_real = np.random.randn(n)
    b = A @ x_real  # b exactamente en Col(A)

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_A == rango_Ab == n, "No se cumple la condición de unicidad"
    x_sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    assert np.allclose(x_sol, x_real), "La solución no coincide con la real"
    print(f"[OK] Compatible única: Rango(A) = Rango(A|b) = {rango_A}")


def caso_compatible_infinitas():
    """Rango(A) = Rango(A|b) < n → infinitas soluciones."""
    n = 4
    # Construimos A con rango 2 duplicando columnas
    A_base = np.random.randn(n + 2, 2)
    A = np.hstack([A_base, A_base])  # columnas 1,2 = columnas 3,4 → rango 2

    coefs = np.random.randn(2)
    b = A_base @ coefs  # b ∈ Col(A)

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_A == rango_Ab < n, "No se detectó rango deficiente"
    print(f"[OK] Compatible infinitas: Rango(A) = Rango(A|b) = {rango_A} < n={n}")


def caso_incompatible():
    """Rango(A) < Rango(A|b) → sin solución."""
    n = 3
    A = np.random.randn(n, n)
    # Hacemos A de rango n-1 colapsando la última fila
    A[-1] = A[0]

    b = np.random.randn(n)
    # Con alta probabilidad b no está en Col(A) → incompatible
    b[-1] = b[0] + 1.0  # rompemos la consistencia explícitamente

    rango_A = np.linalg.matrix_rank(A)
    rango_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

    assert rango_Ab > rango_A, "Se esperaba sistema incompatible"
    print(f"[OK] Incompatible: Rango(A)={rango_A} < Rango(A|b)={rango_Ab}")


if __name__ == "__main__":
    caso_compatible_unico()
    caso_compatible_infinitas()
    caso_incompatible()
    print("\nTodos los casos del Teorema de Rouché-Frobenius verificados correctamente.")

```
---

## Bibliografía y Recursos Educativos

### 📖 Libros de Texto

*   **Libro**: [*Álgebra Lineal y sus Aplicaciones*](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006185) (David C. Lay, 5ta ed., 2016). **Capítulo 1, Sección 1.6**. Presenta el teorema de consistencia de sistemas lineales en función del rango de la matriz ampliada.
*   **Libro**: [*Introduction to Linear Algebra*](https://math.mit.edu/~gs/linearalgebra/) (Gilbert Strang, 5ta ed., 2016). **Capítulo 2**. Strang analiza la estructura de soluciones ($x_p + x_n$) y la relación entre rango, nulidad y número de soluciones.

### 🌐 Recursos Web

*   **Web**: [Teorema de Rouché–Frobenius](https://es.wikipedia.org/wiki/Teorema_de_Rouch%C3%A9-Frobenius) - *Wikipedia (ES)*. Enunciado formal con ejemplos para los tres casos de compatibilidad.
