# Ejercicio 2: Condicionamiento y Matrices de Kronecker

> **Ejercicio 2.**
> 
> **a)** Probar que si $A \in \mathbb{R}^{n \times n}$ es una matriz inversible y $\| \cdot \|$ es una norma matricial inducida, la condición de A verifica que, para toda $B$ singular:
>
> $$ \frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|} $$
>
> **b)** Para cada $n \in \mathbb{N}$ se define la matriz $A_n \in \mathbb{R}^{n \times n}$ cuyos coeficientes están dados por 
>
>$$a_{ij} = \frac{1}{n} + \frac{1}{n^2} \delta_{ij}, 1 \leq i, j \leq n$$
>
>donde $\delta_{ij}$ denota el delta de Kronecker.
> 
> - **i)** Probar que $\text{cond}_\infty(A_n) \geq g(n)$ para alguna función $g(n) \sim n^2$.
> - **ii)** Probar que $\text{cond}_2(A_n) \to \infty$ cuando $n \to \infty$.

## Interpretación del Enunciado

??? info "Observación Teórica: Norma Matricial Inducida"
    Una **norma matricial inducida** (u operatoria) es aquella que se deriva directamente de una norma vectorial $\|\cdot\|$ preexistente. Se define como el máximo factor de amplificación que la matriz $A$ puede aplicar a cualquier vector $x$ no nulo:
    
    $$ \|A\| = \max_{x \neq 0} \frac{\|Ax\|}{\|x\|} = \max_{\|x\|=1} \|Ax\| $$
    
    Estas normas son fundamentales en el análisis de error porque garantizan por definición la propiedad de **consistencia**: $\|Ax\| \leq \|A\| \cdot \|x\|$. Ejemplos clásicos son la norma 1 (máxima suma por columnas), la norma $\infty$ (máxima suma por filas) y la norma 2 (el autovalor máximo de $A^T A$).

El ejercicio analiza el condicionamiento de una matriz y su relación con la distancia a la singularidad. En la primera parte, se demuestra que el recíproco del número de condición de una matriz inversible $A$ representa una cota inferior para la distancia relativa de $A$ a cualquier matriz singular $B$.

En la segunda parte, se analiza la matriz de Kronecker $A_n$, cuya estructura depende de $n$. Se busca demostrar que su número de condición crece con $n$ (en normas $\infty$ y $2$), lo que indica que el sistema se vuelve numéricamente inestable para valores grandes de $n$.

---

## Solución del Ejercicio

### Inciso A: Distancia a la Singularidad

> **a)** Probar que si $A \in \mathbb{R}^{n \times n}$ es una matriz inversible y $\| \cdot \|$ es una norma matricial inducida, la condición de A verifica que, para toda $B$ singular: $\frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|}$

Sea $B$ una matriz singular. Existe un vector $x \neq 0$ tal que $Bx = 0$.

??? info "Observación Teórica: ¿Por qué existe un $x \neq 0$ tal que $Bx = 0$?"
    Esta propiedad define a las **matrices singulares** y es válida para todas ellas por definición. Si una matriz $B \in \mathbb{R}^{n \times n}$ es singular:
    
    1. **Determinante Nulo**: $\det(B) = 0$.
    2. **Dependencia Lineal**: Sus columnas son linealmente dependientes. Esto significa que existe una combinación lineal de sus columnas $\{b_1, \dots, b_n\}$ con coeficientes no todos nulos ($x_i$) que da como resultado el vector cero: $\sum x_i b_i = 0$.
    3. **Núcleo No Trivial**: Por la definición de producto matriz-vector, $\sum x_i b_i$ es idéntico a $Bx$. Por lo tanto, existe un vector $x = (x_1, \dots, x_n)^T \neq \mathbf{0}$ tal que $Bx = \mathbf{0}$.
    
    Geométricamente, una matriz singular "colapsa" al menos una dimensión del espacio, enviando todos los puntos de esa dirección al origen ($\mathbf{0}$).

Podemos escribir $Ax$ como:

$$
Ax = Ax - Bx = (A - B)x
$$

Como $A$ es inversible, existe $A^{-1}$. Multiplicamos por $A^{-1}$:

$$
x = A^{-1}(A - B)x
$$

Aplicando normas (usando la [submultiplicatividad de normas inducidas](../../demostraciones/submultiplicatividad_norma_inducida.md), i.e. $\|Mv\| \leq \|M\| \cdot \|v\|$, dos veces):

$$
\|x\| = \|A^{-1}(A - B)x\| \leq \|A^{-1}\| \|(A - B)x\| \leq \|A^{-1}\| \|A - B\| \|x\|
$$

Dado que $x \neq 0$, tenemos $\|x\| > 0$, por lo que podemos dividir por $\|x\|$:

$$
1 \leq \|A^{-1}\| \|A - B\|
$$

Recordando que $\text{cond}(A) = \|A\| \|A^{-1}\|$, sustituimos $\|A^{-1}\| = \frac{\text{cond}(A)}{\|A\|}$:

$$
1 \leq \frac{\text{cond}(A)}{\|A\|} \|A - B\|
$$

Reordenando los términos obtenemos:

$$
\frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|}
$$

Queda demostrada la propiedad para cualquier norma inducida.

---

### Inciso B: Condicionamiento de la Matriz $A_n$

La matriz $A_n \in \mathbb{R}^{n \times n}$ se define como:

$$a_{ij} = \frac{1}{n} + \frac{1}{n^2} \delta_{ij}$$

Esta matriz puede expresarse como:

$$
A_n = \frac{1}{n} E + \frac{1}{n^2} I_n
$$

donde $E$ es la matriz de unos y $I_n$ la identidad.

#### B-1. Cota inferior para $\text{cond}_\infty(A_n)$

> **i)** Probar que $\text{cond}_\infty(A_n) \geq g(n)$ para una función $g(n) \sim n^2$.

Calculamos la norma infinito de $A_n$. Cada fila tiene $n$ entradas: $(n-1)$ entradas fuera de la diagonal con valor $\frac{1}{n}$, y una entrada diagonal con valor $\frac{1}{n} + \frac{1}{n^2}$. La suma por fila es:

$$
\|A_n\|_\infty = \max_i \sum_j |a_{ij}| = (n-1)\frac{1}{n} + \left(\frac{1}{n} + \frac{1}{n^2}\right) = 1 + \frac{1}{n^2}
$$

Utilizamos la cota del inciso A. Elegimos la matriz singular $B = \frac{1}{n} E$:

$$
A_n - B = \frac{1}{n^2} I_n \implies \|A_n - B\|_\infty = \frac{1}{n^2}
$$

Sustituimos en la fórmula:

$$
\frac{1}{\text{cond}_\infty(A_n)} \leq \frac{1/n^2}{1 + 1/n^2} = \frac{1}{n^2 + 1}
$$

Invirtiendo la inecuación:

$$
\text{cond}_\infty(A_n) \geq n^2 + 1
$$

Por lo tanto, $\text{cond}_\infty(A_n)$ crece por lo menos como $n^2$.

#### B-2. Límite de $\text{cond}_2(A_n)$

> **ii)** Probar que $\text{cond}_2(A_n) \to \infty$ cuando $n \to \infty$.

Para una matriz simétrica, $\text{cond}_2(A_n) = \frac{|\lambda_{\max}|}{|\lambda_{\min}|}$. Determinamos los autovalores de $A_n$:

1. Si $v = \mathbf{1} = (1, \dots, 1)^T$:

    $$
    A_n \mathbf{1} = \frac{1}{n^2} \mathbf{1} + \frac{1}{n} (n \mathbf{1}) = \left( \frac{1}{n^2} + 1 \right) \mathbf{1}
    $$

    $\implies \lambda_1 = 1 + \frac{1}{n^2}$.

2. Si $v \perp \mathbf{1}$ (hay $n-1$ tales vectores). Como $Ev = 0$ por ortogonalidad:

    $$
    A_n v = \frac{1}{n^2} v + \frac{1}{n} \cdot 0 = \frac{1}{n^2} v
    $$

    $\implies \lambda_i = \frac{1}{n^2}$ para $i = 2, \dots, n$.

El número de condición es:

$$
\text{cond}_2(A_n) = \frac{1 + 1/n^2}{1/n^2} = n^2 + 1
$$

Al tender $n$ a infinito:

$$
\lim_{n \to \infty} \text{cond}_2(A_n) = \lim_{n \to \infty} (n^2 + 1) = \infty
$$

El sistema se vuelve mal condicionado al aumentar $n$.

---

## Verificación Computacional

El script siguiente verifica numéricamente los resultados del inciso B para valores crecientes de $n$, confirmando que $\text{cond}_\infty(A_n) \geq n^2 + 1$ y que $\text{cond}_2(A_n) = n^2 + 1$:

```python
--8<-- "docs/Examen_2026_02_18/02_condicionamiento/verificacion.py"
```
