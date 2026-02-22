# Indepedencia Lineal de las Columnas Pivotales

## Teorema
Dada una matriz $A \in \mathbb{R}^{m \times n}$ y su forma escalonada reducida por filas $R \in \mathbb{R}^{m \times n}$. Si un conjunto de columnas en $R$ son linealmente independientes, entonces las columnas correspondientes en la matriz original $A$ también son linealmente independientes y forman una base para el subespacio columna de $A$ ($Col(A)$).

## Interpretación del Enunciado
El algoritmo de eliminación de Gauss-Jordan transforma una matriz $A$ en su forma escalonada reducida $R$ mediante operaciones elementales de fila. El teorema establece que la relación de dependencia (o independencia) lineal entre las columnas se mantiene invariante bajo estas operaciones. Como las columnas que contienen los *pivotes* (primer elemento no nulo de cada fila) en $R$ forman obviamente la base canónica estándar $e_1, e_2, \ldots, e_k$, y son trivialmente independientes; esto fuerza matemáticamente a que sus columnas análogas en $A$ sean la base del Espacio Columna.

### Demostración
La transformación de $A$ a $R$ puede expresarse como la multiplicación por la izquierda de una matriz invertible $E$ (el producto de todas las matrices elementales de las operaciones de fila):

$$ E A = R $$

Supongamos que tomamos un subconjunto de columnas pivotales de $R$, que denotamos como la submatriz $R_p$, y las correspondientes columnas de $A$, que denotamos como $A_p$. La relación se mantiene:

$$ E A_p = R_p $$

Ahora, planteamos la ecuación de combinación lineal igualada a cero para probar la independencia lineal de las columnas originales $A_p$. Sea $x$ un vector de coeficientes:

$$ A_p x = \vec{0} $$

Multiplicando ambos lados a la izquierda por la matriz invertible $E$:

$$ E (A_p x) = E \vec{0} $$

$$ (E A_p) x = \vec{0} $$

Dado que $E A_p = R_p$:

$$ R_p x = \vec{0} $$

Por definición del escalonado reducido, las columnas pivotales $R_p$ son columnas de la matriz identidad (poseen un único $1$ en la posición del pivote y $0$ en el resto). Por lo tanto, las columnas de $R_p$ son, por inspección directa, **linealmente independientes**.
Si las columnas de $R_p$ son linealmente independientes, la única solución al sistema homogéneo $R_p x = \vec{0}$ es la solución trivial $x = \vec{0}$.

Dado que los pasos matriciales son biyectivos invertibles (porque $E$ es invertible, la nulidad se conserva bidireccionalmente), la única solución original a $A_p x = \vec{0}$ debe ser también $x = \vec{0}$.

Por definición, esto demuestra rigurosamente que las columnas $A_p$ originales son **Linealmente Independientes**, y dado que el resto de las columnas no-pivotales pueden construirse como combinación de estas, $A_p$ forma una base minimal generadora de todo el Espacio Columna ($Col(A)$).

### Fuente de Referencia

> **Álgebra Lineal y sus Aplicaciones** (4ta Edición), de *David C. Lay*. Capítulo 4.3 (Conjuntos Linealmente Independientes y Bases), Teorema 6: "Las columnas pivote de una matriz $A$ forman una base para $Col(A)$".

---

--8<-- "docs/demostraciones/05_independencia_pivotes.py"
