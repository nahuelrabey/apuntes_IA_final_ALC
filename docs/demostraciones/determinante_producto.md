# Demostración: Regla Multiplicativa del Determinante

## Interpretación del Enunciado

> Demostrar analítica y matricialmente que dadas dos matrices cuadradas de rango idéntico ($A, B \in \mathbb{R}^{n \times n}$), el operador módulo o determinante obedece de manera estricta la regla del isomorfismo multiplicativo: $|AB| = |A| |B|$ (o equivalentemente, $\det(AB) = \det(A)\det(B)$).

El determinante es, funcionalmente, un escalar que rige e indica en cuánto se "escala" o "estira" el volumen de un hipercubo fundamental de $n$-dimensiones, luego de aplicarle encima la transformación proyectada por la matriz.

Esta deconstrucción no es trivial. El producto de dos matrices cuadradas re-mezcla aditivamente filas contra columnas en arreglos complejos, donde no salta a simple vista por qué la sumatoria de sus productos cruzados puede escindirse puramente en la multiplicación de los escalares independientes de cada matriz original. Construiremos el argumento en dos sub-casos fundacionales.

---

## Solución Analítica

Desarmémoslo evaluando los dos caminos o rutas existenciales de nuestras matrices originarias:

### Caso 1: La Matriz $A$ es Singular (No Inversible)

Si una matriz como $A$ es singular, esto implica algebraicamente que su determinante sufre de un colapso en al menos una de sus trazas y se anula ($|A| = 0$). Geométricamente, toda la inmensa transformación matricial "aplastó" subitamente a todo el hiper-espacio en una dimensión estructural más chica (e.g. comprimiendo una caja cúbica en volumen $0$).

Al conformar operativamente el producto acoplado $AB$, si $A$ proyecta toda la resultante limitadamente sobre un espacio asfíctico de menor rango matricial, **el producto general $AB$ es ineludiblemente una matriz singular y suelta como resultante volumen 0:**

$$
\det(AB) = 0
$$

Al sustituir nuestro eslabón fallado $\det(A) = 0$ con esta conclusión inexorable:

$$
\det(AB) = \det(A)\det(B) = 0 \cdot \det(B) = 0
$$

Por ley contundente de absorción, si cualquiera en la cadena se deforma en cero, la equivalencia de igualar el cero de un bando con el cero del otro **resiste de manera trivial**.

### Caso 2: La Matriz $A$ es No-Singular (Inversible)

El caso grueso es indudablemente cuando ninguna sufre compresión al nulo. Si $A$ es una matriz regular su determinante detenta materialidad y la desvincula del cero ($\det(A) \neq 0$).
La teoría base postula que cualquier matriz con rango cuadrado firme puede deconstruirse (o factorizarse algorítmicamente) en algo llamado *Matrices Elementales* (matrices crudas y simples de tipo fila que operan la Identidad como permutar filas, o re-escalarlas).

Podemos re-escribir a la inmensa matriz $A$ como la mera multiplicación escalonada de $k$ pequeñas matrices elementales:

$$
A = E_1 E_2 \cdots E_k
$$

Procedemos a evaluar el bloque total de nuestro problema re-inyectando nuestra factorización desarmada en vez de $A$:

$$
\det(AB) = \det((E_1 E_2 \cdots E_k) B)
$$

Por el postulado básico indiscutible que decreta que las matrices elementales, al ser operadores primarios sobre filas, **escalan multiplicativamente al volumen general**, podemos sacar en manada para afuera su rastro:

$$
\det((E_1 E_2 \cdots E_k) B) = \det(E_1) \det(E_2) \cdots \det(E_k) \det(B)
$$

Ahora, hagamos una introspección agrupando todos los factores escalares de la propia $A$ entre paréntesis ciegos, retrocediendo su factorización artificial hacia la identidad nominal de $A$:

$$
\left( \det(E_1) \det(E_2) \cdots \det(E_k) \right) \cdot \det(B) = \det(E_1 E_2 \cdots E_k) \cdot \det(B)
$$

Como la cadena de factorizaciones internas restituye universalmente a la pieza original $A = E_1 E_2 \cdots E_k$:

$$
= \det(A) \cdot \det(B)
$$

### Conclusión

Demostramos empírica y contundentemente cómo:

1. Si un operador es singular y aplasta su rango a cero absoluto, la absorción propaga el nulo certificando el postulado lógicamente.
2. Como cualquier armatoste inversible no-singular se puede deconstruir atómicamente al formato puro y maleable de Matrices Elementales...
3. Y estas elementales portan la ley primigenia de escalar con multiplicidad separada.

El corolario formal impone sin concesiones que **el determinante del producto es siempre el producto subyacente de sus determinantes**:

$$
\det(AB) = \det(A)\det(B)
$$

Q.E.D.

---

## Referencias para Validación

Para constrastar este pilar matricial base y repasar el uso implacable de Matrices Elementales para extraerlo hacia afuera, se sugiere acudir a:

* [Wikipedia: Determinant (Multiplicativity and matrix groups)](https://en.wikipedia.org/wiki/Determinant#Multiplicativity_and_matrix_groups): Marco enciclopédico de la propiedad fundamental del determinante, con demostración análoga utilizando factorizaciones.
* [MIT 18.06 OpenCourseWare - Clase 18 (Properties of Determinants) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=3roPTXhUKzE): Minuto 32:00, donde se destila la demostración conceptual como "La Propiedad número 9", exponiendo ininteligiblemente cómo $\det(AB) = \det(A)\det(B)$.

---

## Verificación Empírica Computacional

La certeza dogmática de este corolario frente a los complejos productos matriciales de fila vs. columna, se verifica estocásticamente armando un verificador automático en Python (`03_determinante_producto.py`), exponiendo multiplicidad de rangos numéricos al azar para ver si el módulo tolera o fracasa su equivalencia.

```python
--8<-- "demostraciones/determinante_producto.py"
```
