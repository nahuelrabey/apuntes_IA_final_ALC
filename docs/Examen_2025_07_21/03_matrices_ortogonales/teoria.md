# Solución del Ejercicio 3 (Examen 21 de julio de 2025 - Matrices Singulares y Espectros)

> **Ejercicio 3.** Sea $A \in \mathbb{R}^{n \times n}$ una matriz tal que $A^t = A = A^{-1}$.
>
> a) ¿Cuánto vale el determinante de $A$? ¿Es $A$ diagonalizable?
>
> b) ¿Cuáles son sus posibles autovalores?
>
> c) Calcular la matriz $\Sigma$ de la factorización SVD de $A$. Justificar.
>
> d) Calcular los autovalores de la siguiente matriz:
>
> $$
> B = \begin{pmatrix} 5/10 & -5/10 & -1/10 & -7/10 \\ -5/10 & 5/10 & -1/10 & -7/10 \\ -1/10 & -1/10 & 98/100 & -14/100 \\ -7/10 & -7/10 & -14/100 & 2/100 \end{pmatrix}
> $$
>
> *Sugerencia: usar los items anteriores.*

---

## Solución Inciso A

> a) ¿Cuánto vale el determinante de $A$? ¿Es $A$ diagonalizable?

El enunciado establece que $A^t = A$ (es decir, $A$ es **simétrica**) y que $A = A^{-1}$ (es decir, $A$ es **involutiva**). De estas dos condiciones se obtiene que $A^t = A^{-1}$, lo que por definición implica que $A$ es también **ortogonal**.

Para averiguar el determinante, partimos de la definición que nos fue dada al unificar la simetría con la inversa:

$$
A \cdot A = A \cdot A^{-1}
$$

$$
A^2 = I
$$

Buscamos aplicar el operador determinante a ambos lados de la ecuación, recordando la propiedad multiplicativa del determinante $|A \cdot B| = |A| \cdot |B|$:

??? info "Demostración Teórica: La Regla Multiplicativa del Determinante"
    La propiedad $\det(AB) = \det(A)\det(B)$ se demuestra a partir de las matrices elementales. Toda matriz inversible se descompone en un producto finito de matrices elementales ($A = E_1\dots E_k$), y cada una contribuye multiplicativamente al determinante.

    📌 *Para consultar minuciosamente paso por paso este desarme matricial que demuestra por qué $\det(AB) = \det(A)\det(B)$ (anexado junto al validador por inducción Monte Carlo estocástica dictaminado por la metodología de estudio), remitirse aquí: [Demostración: Regla Multiplicativa del Determinante](../../demostraciones/determinante_producto.md).*

    Fin de la demostración.

    $$
|A^2| = |I|
$$

$$
|A|^2 = 1
$$

Al despejar algebraicamente, obtenemos las dos posibles raíces reales del determinante:

$$
|A| = \pm 1
$$

Por lo tanto, **el determinante de la matriz estructurada $A$ puede valer $1$ o $-1$**.

Respecto a la diagonalizabilidad, el **Teorema Espectral** establece que toda matriz real simétrica es ortogonalmente diagonalizable sobre los reales. Como $A$ satisface $A = A^t$, **$A$ es diagonalizable**.

??? info "Demostración Teórica: Teorema Espectral"
    La demostración de que las matrices simétricas tienen autovalores reales y autovectores ortogonales se basa en propiedades del conjugado transpuesto.

    📌 *Revisar riguroso desarrollo paso a paso del porqué $\lambda = \overline{\lambda}$ junto con el porqué de la ortogonalidad $v_i \cdot v_j = 0$ sumado a su estrés computacional randomizado por Python, aquí: [Demostración: Teorema Espectral](../../demostraciones/teorema_espectral.md).*

    Fin de la demostración.

---

## Solución Inciso B

> b) ¿Cuáles son sus posibles autovalores?

Si $A$ es diagonalizable, asume autovalores $\lambda_i$ y autovectores asociados $v_i \neq 0$ que obedecen la transformación originaria:

$$
A v_i = \lambda_i v_i
$$

Para determinar los posibles valores de $\lambda$, multiplicamos por $A$ en ambos lados de la ecuación de autovectores:

$$
A (A v_i) = A (\lambda_i v_i)
$$

Por linealidad:

$$
A^2 v_i = \lambda_i (A v_i)
$$

Reemplazando la recursión original $A v_i$:

$$
A^2 v_i = \lambda_i (\lambda_i v_i) = \lambda_i^2 v_i
$$

Del inciso A se tiene que $A^2 = I$. Sustituyendo:

$$
I v_i = \lambda_i^2 v_i
$$

$$
v_i = \lambda_i^2 v_i
$$

Como los autovectores satisfacen $v_i \neq 0$ por definición, la igualdad requiere:

$$
\lambda_i^2 = 1
$$

Por lo tanto, **los únicos autovalores posibles son $\lambda \in \{1, -1\}$**.

---

## Solución Inciso C

> c) Calcular la matriz $\Sigma$ de la factorización SVD de $A$. Justificar.

La SVD descompone $A = U \Sigma V^t$, donde la matriz diagonal $\Sigma$ contiene los **valores singulares ($\sigma_i$)** en orden descendente.

Los valores singulares $\sigma_i$ de $A$ son las raíces cuadradas de los autovalores de $A^t A$.

Calculemos internamente esta matriz a modelar:

$$
A^t A
$$

Usando las condiciones del enunciado ($A^t = A^{-1}$):

$$
A^t A = A^{-1} A = I
$$

La matriz $A^t A = I$, cuyos autovalores son todos iguales a $1$.

Los valores singulares son:

$$
\sigma_i = \sqrt{1} = 1 \quad \forall i \in (1, \dots, n)
$$

Todos los valores singulares son iguales a $1$. Por lo tanto, **$\Sigma = I$.**

---

## Solución Inciso D

> d) Calcular los autovalores de la siguiente matriz:
>
> $$
> B = \begin{pmatrix} 5/10 & -5/10 & -1/10 & -7/10 \\ -5/10 & 5/10 & -1/10 & -7/10 \\ -1/10 & -1/10 & 98/100 & -14/100 \\ -7/10 & -7/10 & -14/100 & 2/100 \end{pmatrix}
> $$
>
> *Sugerencia: usar los items anteriores.*

Nos proponen la matriz $4 \times 4$:

$$
B = \begin{pmatrix} 0.5 & -0.5 & -0.1 & -0.7 \\ -0.5 & 0.5 & -0.1 & -0.7 \\ -0.1 & -0.1 & 0.98 & -0.14 \\ -0.7 & -0.7 & -0.14 & 0.02 \end{pmatrix}
$$

La sugerencia indica usar los resultados de los incisos anteriores. Inspeccionando $B$:

- Naturalmente saltan a la vista por espejo estructural sobre la diagonal que **B es simétrica** ($B = B^t$).

- El cómputo de $B^2$ (verificable numéricamente) da **$B^2 = I$**, por lo que $B = B^{-1}$.

Por lo tanto, $B$ satisface $B^t = B = B^{-1}$. Por el inciso B, **sus únicos autovalores posibles son $1$ y $-1$**. Resta determinar las multiplicidades correspondientes.

Aplicando la propiedad de la **Traza** ($Tr(B)$), que es invariante bajo cambios de base e igual a la suma de los autovalores:

Calculando la diagonal de $B$:

$$
Tr(B) = 0.5 + 0.5 + 0.98 + 0.02 = 2
$$

Sea $k$ la cantidad de autovalores iguales a $1$ y $m$ la cantidad de autovalores iguales a $-1$. Como $\dim(B) = 4$, se plantea el sistema:

$$
\begin{cases} k + m = 4 \quad \text{(Espectro total)} \\ k(1) + m(-1) = 2 \quad \text{(Suma traza-autovalores)} \end{cases}
$$

Sumando las dos ecuaciones ($2k = 6$):

$$
k = 3
$$

$$
m = 1
$$

Por lo tanto, sin necesidad de factorizar el polinomio de grado 4, **los autovalores de $B$ son $\{1, 1, 1, -1\}$**.

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/03_matrices_ortogonales/verificacion.py"
```
