# Solución del Ejercicio 2

> **Ejercicio 2**
>
> 1. Calcular la descomposición en valores singulares (SVD) de la matriz:
>
>    $$A = \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix}$$
>
> 2. Probar que $PA$ y $AP$ tienen los mismos valores singulares que $A$, donde $P$ es una matriz de permutación. Además, calcular $||PA||_2$ y $\kappa_2(PA)$.

---

## 1. Calcular la descomposición en valores singulares (SVD) de la matriz $A$
> 1. Calcular la descomposición en valores singulares (SVD) de la matriz:
>    $$A = \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix}$$


Dada la matriz:

$$A = \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix}$$

Sabemos que la descomposición en valores singulares se estructura como $A = U \Sigma V^T$.

Donde $\Sigma$ contiene los valores singulares (en la diagonal) que son las raíces cuadradas de los autovalores de $A^T A$.

Calculamos $A^T A$:

$$A^T A = \begin{pmatrix} 0 & 2 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix} \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix} = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix}$$

Dado que $A^T A$ es una matriz diagonal, sus autovalores son directamente los elementos de su diagonal:

- $\lambda_1 = 9 \implies \sigma_1 = 3$

- $\lambda_2 = 4 \implies \sigma_2 = 2$

- $\lambda_3 = 1 \implies \sigma_3 = 1$

Por ende, nuestra matriz de valores singulares ordenados en forma decreciente es:

$$\Sigma = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

Ahora, hallamos los autovectores ortonormales de $A^T A$ asociados a estos autovalores para construir $V$:

- Para $\lambda_1 = 9$, el vector propio asociado a la tercera columna resulta ser $v_1 = (0, 0, 1)^T$.

- Para $\lambda_2 = 4$, el vector propio asociado a la primera columna resulta ser $v_2 = (1, 0, 0)^T$.

- Para $\lambda_3 = 1$, el vector propio asociado a la segunda columna resulta ser $v_3 = (0, 1, 0)^T$.

Concatenando dichos autovectores formamos $V$, y por lo tanto $V^T$:

$$V = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix} \implies V^T = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$

Para hallar $U = (\vec{u}_1, \vec{u}_2, \vec{u}_3)$, utilizamos la relación $u_i = \frac{1}{\sigma_i} A v_i$:

- $u_1 = \frac{1}{3} \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 0 \\ 0 \\ -3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}$

- $u_2 = \frac{1}{2} \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$

- $u_3 = \frac{1}{1} \begin{pmatrix} 0 & -1 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & -3 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}$

Reemplazando en $U$:

$$U = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{pmatrix}$$

La Descomposición completa es finalmente:

$$A = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 1 & 0 \\ -1 & 0 & 0 \end{pmatrix} \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$$

---

## 2. Probar que $PA$ y $AP$ tienen los mismos valores singulares que $A$
> 2. Probar que $PA$ y $AP$ tienen los mismos valores singulares que $A$, donde $P$ es una matriz de permutación. Además, calcular $||PA||_2$ y $\kappa_2(PA)$.


Una matriz de permutación $P$ es siempre una matriz ortogonal; es decir, altera el orden de filas o columnas, pero respeta la isometría:

$$P^T P = P P^T = I$$

**A. Para $PA$:**

Los valores singulares de $PA$ son las raíces cuadradas de los autovalores de la matriz simétrica $(PA)^T (PA)$.

Sustituyendo y desarrollando:

$$(PA)^T (PA) = A^T P^T P A$$

Como $P^T P = I$, esto simplifica a:

$$A^T I A = A^T A$$

Dado que obtenemos exactamente el mismo núcleo subyacente $A^T A$, la matriz $PA$ tiene estrictamente el mismo espectro de autovalores para dicha expresión, y por tanto, idénticos valores singulares que $A$.

**B. Para $AP$:**

Buscamos los autovalores de $(AP)^T (AP)$:

$$(AP)^T (AP) = P^T A^T A P$$

Esta expresión equivale a que $(AP)^T (AP)$ y $A^T A$ son matrices **semejantes** (aquí interviene lo demostrado en el Ejercicio 1), ya que $P^T = P^{-1}$.

Recordemos además, que las matrices semejantes preservan idénticos autovalores. 

Por consiguiente, los valores singulares producidos por $P^T A^T A P$ serán los mismos que los de $A^T A$, dejando en evidencia que $AP$ posee iguales valores singulares a $A$.

---

**C. Calcular $\|PA\|_2$ y $\kappa_2(PA)$**

Sabemos por sus propiedades fundamentales que:

- La norma-2 de una matriz es igual a su mayor valor singular: $\|M\|_2 = \sigma_{\max}$

- El número de condición en base 2 equivale a la proporción de elongamiento límite: $\kappa_2(M) = \frac{\sigma_{\max}}{\sigma_{\min}}$

Al haber probado instantes atrás que multiplicar por una permutación no afecta los valores singulares en absoluto, usamos el espectro ya calculado $\sigma \in \{3, 2, 1\}$:

$$\|PA\|_2 = \sigma_{\max}(PA) = \sigma_{\max}(A) = 3$$

$$\kappa_2(PA) = \frac{\sigma_{\max}(PA)}{\sigma_{\min}(PA)} = \frac{3}{1} = 3$$

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_02_24/02_descomposicion_svd/verificacion.py"
```
