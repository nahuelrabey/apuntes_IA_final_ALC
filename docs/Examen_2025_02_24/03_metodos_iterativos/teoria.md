# Solución del Ejercicio 3

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

Dada la matriz del sistema:

Podemos descomponer la matriz en su diagonal ($D$), su parte estrictamente inferior ($L$) y su parte estrictamente superior ($U$), de tal forma que $A = D + L + U$:

- $D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I$

- $L = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & c & 0 \end{pmatrix}$

- $U = \begin{pmatrix} 0 & c & 0 \\ 0 & 0 & c \\ 0 & 0 & 0 \end{pmatrix}$

---

## 1. Valores de $c$ para los cuales convergen Jacobi y Gauss-Seidel

Ambos métodos iterativos convergen para cualquier valor inicial si y solo si el **radio espectral** de sus matrices de iteración (denotado $\rho$, que es el máximo valor absoluto de sus autovalores) es estrictamente menor a 1 ($\rho < 1$).

### Método de Jacobi

La matriz de iteración de Jacobi está dada por:

$$T_J = -D^{-1}(L + U) = -I (L + U) = \begin{pmatrix} 0 & -c & 0 \\ 0 & 0 & -c \\ 0 & -c & 0 \end{pmatrix}$$

Calculamos sus autovalores encontrando el núcleo del polinomio característico $\det(T_J - \lambda I) = 0$:

$$ \begin{vmatrix} -\lambda & -c & 0 \\ 0 & -\lambda & -c \\ 0 & -c & -\lambda \end{vmatrix} = 0 $$

Desarrollando el determinante evaluando por la primera columna:

$$ -\lambda \begin{vmatrix} -\lambda & -c \\ -c & -\lambda \end{vmatrix} = -\lambda (\lambda^2 - c^2) = 0 $$

Las raíces son: $\lambda_1 = 0$, $\lambda_2 = c$, $\lambda_3 = -c$.

El radio espectral es $\rho(T_J) = \max(|0|, |c|, |-c|) = |c|$.

Por lo tanto, el método de **Jacobi converge si y solo si $|c| < 1$**.

### Método de Gauss-Seidel

La matriz de iteración de Gauss-Seidel está dada por:

$$T_{GS} = -(D + L)^{-1} U$$

Primero, calculamos $(D + L)^{-1}$:

$$D + L = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & c & 1 \end{pmatrix} \implies (D + L)^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -c & 1 \end{pmatrix}$$

Ahora hallamos $T_{GS}$:

$$T_{GS} = -\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -c & 1 \end{pmatrix} \begin{pmatrix} 0 & c & 0 \\ 0 & 0 & c \\ 0 & 0 & 0 \end{pmatrix} = - \begin{pmatrix} 0 & c & 0 \\ 0 & 0 & c \\ 0 & 0 & -c^2 \end{pmatrix} = \begin{pmatrix} 0 & -c & 0 \\ 0 & 0 & -c \\ 0 & 0 & c^2 \end{pmatrix}$$

Al ser una matriz triangular superior, sus autovalores se desprenden directamente de la diagonal principal:

$\lambda_1 = 0$, $\lambda_2 = 0$, $\lambda_3 = c^2$.

El radio espectral es $\rho(T_{GS}) = \max(|0|, |0|, |c^2|) = c^2$.

Por lo tanto, el método de **Gauss-Seidel converge si y solo si $c^2 < 1$, lo cual ocurre puramente si $|c| < 1$**.

Ambos métodos convergen en el mismo intervalo: $c \in (-1, 1)$.

---

## 2. Comparar la velocidad de convergencia

La tasa asintótica de convergencia se define computacionalmente como $R(T) = -\ln(\rho(T))$. 

A mayor tasa de convergencia teórica ($R$), se requieren en la práctica menos iteraciones para converger con la computadora.

- Para Jacobi: $R(T_J) = -\ln(|c|)$

- Para Gauss-Seidel: $R(T_{GS}) = -\ln(c^2) = -2\ln(|c|) = 2 R(T_J)$

La relación concluyente es que la tasa de convergencia de Gauss-Seidel es exactamente el doble. Por lo tanto, el método de **Gauss-Seidel converge el doble de rápido** que el método de Jacobi. Esperamos que Gauss-Seidel demore analíticamente la mitad de iteraciones computacionales en confluir para cualquier valor de $|c| < 1$.

---

## 3. Plantear las iteraciones correspondientes para cada método

Para el sistema general $A \vec{x} = \vec{b}$, es decir:

$$
\begin{cases} 
x_1 + c x_2 = b_1 \\ 
x_2 + c x_3 = b_2 \\ 
c x_2 + x_3 = b_3 
\end{cases}
$$

### Forma iterativa de Jacobi:

El método actualiza todas las variables en la iteración $(k+1)$ en base exclusiva de los valores previos de la iteración $(k)$:

$$x_1^{(k+1)} = b_1 - c \cdot x_2^{(k)}$$

$$x_2^{(k+1)} = b_2 - c \cdot x_3^{(k)}$$

$$x_3^{(k+1)} = b_3 - c \cdot x_2^{(k)}$$

### Forma iterativa de Gauss-Seidel:

Este método utiliza los escalares más actualizados que encuentra (es decir, usa variables del estrato $k+1$ tan pronto como hayan sido calculadas en cascada natural).

$$x_1^{(k+1)} = b_1 - c \cdot x_2^{(k)}$$

$$x_2^{(k+1)} = b_2 - c \cdot x_3^{(k)}$$

$$x_3^{(k+1)} = b_3 - c \cdot x_2^{(k+1)}$$

*(Nótese que en esta última línea usa formalmente $x_2^{(k+1)}$, que ya fue computado en el paso anterior).*

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_02_24/03_metodos_iterativos/verificacion.py"
```
