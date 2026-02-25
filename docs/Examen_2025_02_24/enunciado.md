# Enunciado General: Examen 24 de Feb 2025

*(Los siguientes enunciados fueron extraídos y compilados automáticamente de las resoluciones individuales)*

---

## 01 Semejanza Matrices

> **Ejercicio 1**
>
> Se dice que $A \in \mathbb{K}^{n \times n}$ es semejante a $B \in \mathbb{K}^{n \times n}$ si existe una matriz invertible $S \in \mathbb{K}^{n \times n}$ tal que:
>
> $$SA(S^{-1}) = B$$
>
> 1. Demostrar que la relación de semejanza es una relación de equivalencia.
>
> 2. Demostrar que si $A$ es semejante a $B$, entonces:
>
>    $$\text{Tr}(A) = \text{Tr}(B)$$
>
>    **Sugerencia:** Utilizar la propiedad $\text{Tr}(EC) = \text{Tr}(CE)$ para matrices $C$ y $E$.
>
> 3. Probar que si $A$ es diagonalizable (es decir, $A$ es semejante a una matriz diagonal $D$) y los valores propios de $A$ son 0 y 1, entonces:
>
>    $$A^2 = A$$


---

## 02 Descomposicion Svd

> **Ejercicio 2**
>
> 1. Calcular la descomposición en valores singulares (SVD) de la matriz:
>
>    $$A = \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix}$$
>
> 2. Probar que $PA$ y $AP$ tienen los mismos valores singulares que $A$, donde $P$ es una matriz de permutación. Además, calcular $||PA||_2$ y $\kappa_2(PA)$.


---

## 03 Metodos Iterativos

> **Ejercicio 3**
>
> Dada la matriz:
>
> $$A = \begin{pmatrix} 1 & c & 0 \\ 0 & 1 & c \\ 0 & c & 1 \end{pmatrix}$$
>
> 1. Determinar para qué valores de $c$ convergen los métodos de Jacobi y Gauss-Seidel.
> 2. Comparar la velocidad de convergencia de ambos métodos.
> 3. Plantear las iteraciones correspondientes para cada método.


---

## 04 Minimos Cuadrados

> **Ejercicio 4**
>
> Dada la función:
>
> $$z = a y^b e^{cx+2}$$
>
> 1. Plantear las ecuaciones de mínimos cuadrados para estimar los parámetros $a$, $b$ y $c$.
> 2. Proponer puntos de datos para que la solución sea única.
> 3. Determinar la mínima cantidad de puntos necesarios para que la solución sea única.


---

