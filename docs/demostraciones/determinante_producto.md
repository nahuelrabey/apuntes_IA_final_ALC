# Demostración: Regla Multiplicativa del Determinante

## Interpretación del Enunciado

> Demostrar analíticamente que dadas dos matrices cuadradas del mismo orden ($A, B \in \mathbb{R}^{n \times n}$), sus determinantes cumplen la propiedad multiplicativa: $|AB| = |A| |B|$ (o equivalentemente, $\det(AB) = \det(A)\det(B)$).

El determinante es un escalar que indica el factor de cambio de volumen que experimenta el hipercubo fundamental de $n$-dimensiones debido a la transformación proyectada por la matriz.

El producto de dos matrices cuadradas reconfigura las filas y columnas. La demostración de por qué el determinante del producto se factoriza como el producto de los determinantes puede dividirse analizando matrices singulares y no singulares.

---

## Solución Analítica

Procederemos evaluando las dos condiciones posibles de las matrices base:

### Caso 1: La Matriz $A$ es Singular (No Inversible)

Si $A$ es singular, esto implica algebraicamente que su determinante se anula ($\det(A) = 0$). Geométricamente, la transformación descrita por $A$ mapea el hiperespacio base a un subespacio de menor dimensión, reduciendo su volumen a $0$.

Al realizar el producto matricial $AB$, dado que el operador $A$ se aplica resultando en una reducción dimensional inferior al rango completo $n$, **el producto completo $AB$ resulta en una matriz singular:**

$$
\det(AB) = 0
$$

Sustituyendo el valor $\det(A) = 0$ en la ecuación multiplicativa propuesta:

$$
\det(AB) = \det(A)\det(B) = 0 \cdot \det(B) = 0
$$

Por propiedad del producto por cero, si una matriz es singular, la igualdad se mantiene válida.

### Caso 2: La Matriz $A$ es No-Singular (Inversible)

Si $A$ es una matriz regular su determinante es distinto de cero ($\det(A) \neq 0$).
Se sabe por teoría de matrices que cualquier matriz de rango completo puede descomponerse como el producto algorítmico de **Matrices Elementales** (operaciones unitarias de fila como permutación o multiplicación escalar).

Reemplazando la matriz $A$ por su descomposición en $k$ matrices elementales:

$$
A = E_1 E_2 \cdots E_k
$$

Evaluamos el determinante del producto sustituyendo a $A$:

$$
\det(AB) = \det((E_1 E_2 \cdots E_k) B)
$$

Debido a que las matrices elementales corresponden a operaciones primarias de fila, éstas **multiplican escalarmente el determinante de la matriz subsiguiente**, por lo que se pueden factorizar fuera de la operación:

$$
\det((E_1 E_2 \cdots E_k) B) = \det(E_1) \det(E_2) \cdots \det(E_k) \det(B)
$$

Agrupamos los factores escalares asociados a $A$ e invertimos el proceso de factorización elemental de regreso al determinante de la matriz resultante $A$:

$$
\left( \det(E_1) \det(E_2) \cdots \det(E_k) \right) \cdot \det(B) = \det(E_1 E_2 \cdots E_k) \cdot \det(B)
$$

Como la multiplicación del conjunto de matrices elementales equivale a la original $A = E_1 E_2 \cdots E_k$:

$$
= \det(A) \cdot \det(B)
$$

### Conclusión

Repasando lo elaborado en ambos procedimientos:

1. Si un operador es singular de manera que su rango es deficiente, $\det(AB)=0$ y  $0 \cdot \det(B) = 0$.
2. Toda matriz inversible se factoriza en un producto de Matrices Elementales.
3. Las matrices elementales preservan la propiedad multiplicativa del determinante en cascada.

En consecuencia, se comprueba que **el determinante del producto es siempre el producto subyacente de sus determinantes**:

$$
\det(AB) = \det(A)\det(B)
$$

Q.E.D.

---

## Referencias para Validación

Para repasar el uso de matrices elementales asociado al cálculo y propiedades de los determinantes:

* [Wikipedia: Determinant (Multiplicativity and matrix groups)](https://en.wikipedia.org/wiki/Determinant#Multiplicativity_and_matrix_groups): Marco analítico de la multiplicatividad del determinante.
* [MIT 18.06 OpenCourseWare - Clase 18 (Properties of Determinants) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=3roPTXhUKzE): Minuto 32:00, explica la demostración de la factorización como "La Propiedad número 9", exponiendo cómo el producto cumple $\det(AB) = \det(A)\det(B)$.

---

## Verificación Empírica Computacional

La correspondencia es numéricamente testeada generando matrices aleatorias con base en Python (`03_determinante_producto.py`), validando su tolerancia de error al punto flotante.

```python
--8<-- "demostraciones/determinante_producto.py"
```
