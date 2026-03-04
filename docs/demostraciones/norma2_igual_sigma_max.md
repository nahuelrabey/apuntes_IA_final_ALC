# Norma-2 de una Matriz e Igual a su Mayor Valor Singular

## Enunciado del Teorema

> Sea $M \in \mathbb{R}^{m \times n}$ una matriz con descomposición SVD $M = U \Sigma V^T$, y sea $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$ sus valores singulares. Entonces la norma matricial inducida por la norma euclídea vectorial satisface:
>
> $$
> \|M\|_2 = \sigma_{\max}(M) = \sigma_1
> $$
>

---

## Demostración

La norma matricial inducida por la norma euclídea $\|\cdot\|_2$ se define como:

$$
\|M\|_2 = \max_{x \neq 0} \frac{\|Mx\|_2}{\|x\|_2} = \max_{\|x\|_2 = 1} \|Mx\|_2
$$

### Paso 1: Reducción a $\Sigma$ usando la SVD

Sea $M = U \Sigma V^T$ la descomposición SVD de $M$, donde $U$ y $V$ son matrices ortogonales ($U^T U = I$, $V^T V = I$), y $\Sigma = \text{diag}(\sigma_1, \ldots, \sigma_r, 0, \ldots, 0)$.

Como $U$ y $V^T$ son ambas ortogonales, preservan la norma euclídea: $\|Qz\|_2 = \|z\|_2$ para toda $Q$ ortogonal. Así, para cualquier $x$ con $\|x\|_2 = 1$:

$$
\|Mx\|_2 = \|U \Sigma V^T x\|_2 = \|\Sigma V^T x\|_2
$$

Además, $V^T$ mapea la esfera unitaria sobre sí misma (es una biyección isométrica), por lo que al maximizar sobre $\|x\|_2 = 1$ es equivalente a maximizar sobre $\|V^T x\|_2 = 1$. El problema se reduce entonces a:

$$
\|M\|_2 = \max_{\|x\|_2 = 1} \|\Sigma V^T x\|_2 = \max_{\|w\|_2 = 1} \|\Sigma w\|_2
$$

### Paso 3: Cota superior mediante los valores singulares

Escribiendo $y = (y_1, y_2, \ldots, y_n)^T$ con $\sum_i y_i^2 = 1$, y usando que $\Sigma$ es diagonal con entradas $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r \geq 0$:

$$
\|\Sigma y\|_2^2 = \sum_{i=1}^{r} \sigma_i^2 y_i^2 \leq \sigma_1^2 \sum_{i=1}^{r} y_i^2 \leq \sigma_1^2 \sum_{i=1}^{n} y_i^2 = \sigma_1^2
$$

Tomando raíz cuadrada: $\|\Sigma y\|_2 \leq \sigma_1$. Por lo tanto:

$$
\|M\|_2 \leq \sigma_1
$$

### Paso 4: La cota se alcanza

Tomando $y = e_1 = (1, 0, \ldots, 0)^T$ (primer vector canónico), con $\|e_1\|_2 = 1$:

$$
\|\Sigma e_1\|_2 = \|(\sigma_1, 0, \ldots, 0)^T\|_2 = \sigma_1
$$

Luego el máximo es efectivamente alcanzado, y:

$$
\|M\|_2 \geq \sigma_1
$$

### Conclusión

Combinando ambas cotas:

$$
\|M\|_2 = \sigma_1 = \sigma_{\max}(M) \qquad \blacksquare
$$

---

??? info "Intuición Geométrica"
    La SVD descompone la acción de $M$ en tres pasos: rotación/reflexión ($V^T$), escalado a lo largo de ejes ortogonales ($\Sigma$), y segunda rotación/reflexión ($U$). Las rotaciones no cambian longitudes, por lo que la máxima elongación que $M$ puede aplicar a un vector unitario es precisamente $\sigma_1$, el mayor factor de escala en $\Sigma$. El vector que alcanza ese máximo es la primera columna de $V$ (es decir, $x = v_1$).

??? info "Consecuencia: Número de Condición en Base 2"
    Una vez establecido que $\|M\|_2 = \sigma_{\max}$, la misma lógica aplicada a $M^{-1}$ (cuya SVD invierte y ordena los valores singulares) da $\|M^{-1}\|_2 = 1/\sigma_{\min}$. El número de condición resulta entonces:

$$
    \kappa_2(M) = \|M\|_2 \cdot \|M^{-1}\|_2 = \frac{\sigma_{\max}}{\sigma_{\min}}
$$

    Este cociente mide el ratio entre la máxima y mínima elongación que $M$ aplica a vectores unitarios.

---

## Verificación Computacional

```python
--8<-- "docs/demostraciones/norma2_igual_sigma_max.py"
```

---

## Referencias Externas

- [*Numerical Linear Algebra*](https://www.google.com/books/edition/Numerical_Linear_Algebra/4Mou5YpRD_kC) (Trefethen & Bau, 1997). **Lectura 4, Theorem 4.1**. Prueba que $\|A\|_2 = \sigma_{\max}(A)$ directamente desde la definición de norma inducida y la SVD.

- [Singular value — Wikipedia](https://en.wikipedia.org/wiki/Singular_value#Geometric_meaning) — *Wikipedia*. La sección "Geometric meaning" ilustra cómo los valores singulares representan los semiejes de la elipsoide imagen de la bola unitaria, haciendo evidente que el mayor es la norma-2.

- [Matrix norm — Wikipedia, §Induced norm](https://en.wikipedia.org/wiki/Matrix_norm#Induced_norm) — *Wikipedia*. Definición formal de norma matricial inducida y su relación directa con los valores singulares para la norma espectral ($p=2$).
