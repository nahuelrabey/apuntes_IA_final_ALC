# Demostración: $\det(D + \omega L) = \det(D) = \prod_{i=1}^{n} a_{ii}$

Esta identidad se utiliza como paso intermedio en la demostración de que $\det(B(\omega)) = (1-\omega)^n$ para el método SOR. Ver [contexto completo](../Examen_2026_02_18/01_metodo_sor/teoria.md#inciso-b-determinante-de-iteracion-y-condicion-de-rango-cota).

---

## Enunciado

Sea $A = L + D + U \in \mathbb{R}^{n \times n}$ con $a_{ii} \neq 0$ para todo $i$, y $\omega \neq 0$. Entonces:

$$
\det(D + \omega L) = \det(D) = \prod_{i=1}^{n} a_{ii}
$$

---

## Demostración

### Paso 1: Estructura de $D + \omega L$

Por definición de la descomposición:

- $D$ es diagonal: $D_{ij} = a_{ii}$ si $i = j$, y $0$ en otro caso.

- $L$ es triangular inferior **estricta**: $L_{ij} = a_{ij}$ si $i > j$, y $0$ en otro caso. En particular, $L_{ii} = 0$ para todo $i$.

La suma $D + \omega L$ tiene entonces la siguiente estructura por entradas:

$$
(D + \omega L)_{ij} = \begin{cases} a_{ii} & \text{si } i = j \\ \omega \, a_{ij} & \text{si } i > j \\ 0 & \text{si } i < j \end{cases}
$$

Por lo tanto, $D + \omega L$ es una **matriz triangular inferior** con diagonal $a_{11}, a_{22}, \ldots, a_{nn}$.

### Paso 2: Determinante de una matriz triangular

El determinante de cualquier matriz triangular (superior o inferior) es igual al producto de sus entradas diagonales:

$$
\det(T) = \prod_{i=1}^{n} T_{ii}
$$

??? info "Justificación: expansión de Leibniz en matrices triangulares"
    El determinante se define por la fórmula de Leibniz:

$$
    \det(T) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} T_{i,\sigma(i)}
$$

    Para una matriz triangular inferior, $T_{ij} = 0$ siempre que $j > i$. El único término no nulo en la suma corresponde a la permutación identidad $\sigma = \text{id}$, ya que cualquier otra permutación $\sigma$ contiene al menos un índice $\sigma(i) > i$ para algún $i$, forzando un factor cero en el producto.

    Por lo tanto:

$$
    \det(T) = \text{sgn}(\text{id}) \prod_{i=1}^{n} T_{ii} = \prod_{i=1}^{n} T_{ii}
$$

### Paso 3: Aplicación a $D + \omega L$

Dado que $D + \omega L$ es triangular inferior con diagonal $a_{ii}$, aplicando el resultado anterior:

$$
\det(D + \omega L) = \prod_{i=1}^{n} (D + \omega L)_{ii} = \prod_{i=1}^{n} a_{ii}
$$

Y dado que $D$ también es triangular con los mismos elementos en la diagonal:

$$
\det(D) = \prod_{i=1}^{n} a_{ii}
$$

Por lo tanto:

$$
\det(D + \omega L) = \det(D) = \prod_{i=1}^{n} a_{ii} \qquad \blacksquare
$$

---

## Intuición Geométrica

La multiplicación por $\omega L$ agrega entradas por debajo de la diagonal, pero no modifica la diagonal. El determinante de una matriz triangular solo depende de su diagonal, por lo que las entradas subdiagonales (cualquiera sea $\omega$) no tienen efecto en el determinante.
