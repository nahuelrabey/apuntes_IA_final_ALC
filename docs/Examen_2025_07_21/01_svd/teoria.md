# Solución del Ejercicio 1 (Examen 21 de julio de 2025 - SVD)

> **Ejercicio 1.** Sea $A$ una matriz con coeficientes reales de $n \times 2$. Sean $U$, $\Sigma$ y $V$ las matrices que dan su descomposición SVD, con $u_i$ la columna $i$-ésima de $U$, $\Sigma_{ii} = \sigma_i$ (con $\sigma_i \neq \sigma_j$ si $i \neq j$), y $v_i$ la columna $i$-ésima de $V$. Sea $\tilde{A} = \sigma_1 u_1 v_1^t$ una aproximación de rango 1 de $A$.
>
> a) Si $x \in \mathbb{R}^2$ es un vector perteneciente al círculo unitario, mostrar que el error cometido al calcular $Ax$ como $\tilde{A}x$ está acotado por $\sigma_2$.
>
> b) Sea $B = A^tA$ y $x \in \mathbb{R}^2$ elegido al azar. Mostrar que el siguiente algoritmo converge al vector $v_1$ cuando $N \to \infty$:
>
> - Para $k \in 1, \dots, N$:
>
>   - $x = Bx$
>
>   - $x = x / ||x||$
>
> c) Escriba una rutina que calcule la mejor aproximación de rango 1 de una matriz real de $n \times 2$ en el sentido de la norma 2. Toda función que involucre operaciones más complejas que el producto matricial debe ser definida explícitamente.

---

## Interpretación del enunciado

Dado que la matriz $A$ es de dimensiones $n \times 2$, su descomposición SVD $A = U \Sigma V^t$ nos indica rigurosamente, por propiedades algebraicas de dimensión, que:

- $U$ es una matriz ortogonal de $n \times n$, por ende sus vectores columna la componen como $U = [u_1, u_2, \dots, u_n]$.

- $V$ es una matriz ortogonal de $2 \times 2$, compuesta como $V = [v_1, v_2]$.

- $\Sigma$ es una matriz de $n \times 2$ (mismas dimensiones que $A$) cuyos valores singulares $\sigma_i$ se ubican en la diagonal principal ($\Sigma_{ii}$). **Todos los demás elementos son nulos ($\Sigma_{ij} = 0$ para todo $i \neq j$)**. Esta es una propiedad fundamental de la SVD. Las filas desde $n=3$ hasta la última son filas de ceros.

- La expresión $\tilde{A} = \sigma_1 u_1 v_1^t$ se denomina **aproximación de rango 1**. El **Teorema de Eckart-Young-Mirsky** establece que al truncar la SVD reteniendo los mayores valores singulares, se obtiene la mejor aproximación de rango reducido en el sentido de la norma 2 y de Frobenius. Por lo tanto, $\sigma_1 u_1 v_1^t$ es la aproximación de rango 1 óptima de $A$.

## Solución Inciso A
> a) Si $x \in \mathbb{R}^2$ es un vector perteneciente al círculo unitario, mostrar que el error cometido al calcular $Ax$ como $\tilde{A}x$ está acotado por $\sigma_2$.

Sabemos por definición de la SVD truncada que como la matriz original $A$ es de orden $n \times 2$, sólo poseerá a lo sumo 2 valores singulares no nulos. Podemos entonces descomponerla como la suma de sus componentes de rango 1:

$$
A = \sum_{i=1}^{k} \sigma_i u_i v_i^t = \sigma_1 u_1 v_1^t + \sigma_2 u_2 v_2^t
$$

??? info "Profundización: Descomposición en Sumatoria de Matrices de Rango 1"
    Para cualquier matriz general $M \in \mathbb{R}^{m \times n}$ con rango $r$, la Descomposición en Valores Singulares $M = U \Sigma V^t$ puede ser reescrita lógicamente usando multiplicación por bloques como una sumatoria exacta de $r$ matrices individuales, cada una de rango estrictamente 1:

    $$
    M = \sum_{i=1}^{r} \sigma_i u_i v_i^t
    $$

    Dado que $u_i$ y $v_i$ son vectores columna, cada término $u_i v_i^t$ (el **producto exterior** entre el $i$-ésimo vector singular izquierdo y el derecho) produce una matriz de $m \times n$ de **rango 1**, ya que todas sus columnas son múltiplos de $u_i$.

    Al ponderarla por su valor singular $\sigma_i$, la suma de estos términos de rango 1 reconstruye exactamente $M$, con los términos asociados a mayores valores singulares capturando la mayor parte de la varianza.

Dado que se nos informa que $\tilde{A} = \sigma_1 u_1 v_1^t$ es la aproximación de mayor rango, podemos definir el error vectorial de efectuar dicha predicción como $e = A x - \tilde{A} x$.

Reemplazando los términos, el residuo es exactamente la componente descartada de la matriz SVD:

$$
e = (A - \tilde{A}) x = (\sigma_2 u_2 v_2^t) x
$$

Nos piden probar que la norma de este error se encuentra acotada por $\sigma_2$. Aplicamos la norma euclidiana o Norma-2 ($|| \cdot ||_2$) en ambos lados:

$$
||e||_2 = ||\sigma_2 u_2 v_2^t x||_2
$$

Como un escalar positivo puede extraerse de la norma:

??? info "Observación Teórica: ¿Por qué $\sigma_2$ es un escalar puramente positivo?"
    Por definición de la SVD, todos los valores singulares $\sigma_i$ son reales **no negativos ($\sigma_i \geq 0$)**, ya que se obtienen como la raíz cuadrada de los autovalores de $A^tA$.

    La matriz $A^tA$ es simétrica semidefinida positiva, por lo que sus autovalores satisfacen $\lambda_i \geq 0$, garantizando que los valores singulares sean reales y no negativos.

    Dado que el enunciado establece $\sigma_i \neq \sigma_j$ y los valores singulares se ordenan descendentemente, se tiene **$\sigma_2 > 0$**.

    Por ser $\sigma_2$ un escalar positivo, puede extraerse de la norma: $|\sigma_2| = \sigma_2$ y $||\sigma_2 u|| = \sigma_2 ||u||$.

    $$
    ||e||_2 = \sigma_2 ||u_2 (v_2^t x)||_2
    $$

El término entre paréntesis $(v_2^t x)$ resulta en un número escalar del producto interno vectorial. Lo podemos extraer en valor absoluto:

$$
||e||_2 = \sigma_2 |v_2^t x| \cdot ||u_2||_2
$$

Dado que $U$ y $V$ tienen columnas ortonormales, el vector $u_2$ satisface $||u_2||_2 = 1$:

$$
||e||_2 = \sigma_2 |v_2^t x|
$$

Para el producto interno $|v_2^t x|$ restante, se tiene $||x||_2 = 1$ (por pertenecer al círculo unitario) y $||v_2||_2 = 1$ (columna ortonormal de $V$). Aplicando la desigualdad de Cauchy-Schwarz:

$$
|v_2^t x| \leq ||v_2||_2 \cdot ||x||_2 = 1 \cdot 1 = 1
$$

Por lo tanto:

$$
||e||_2 \leq \sigma_2 \cdot 1 = \sigma_2
$$

Queda así demostrado que el error cometido en la aproximación $\|A x - \tilde{A} x\|_2$ siempre estará acotado por arriba por la magnitud del segundo valor singular descartado, $\sigma_2$.

---

## Solución Inciso B
> b) Sea $B = A^tA$ y $x \in \mathbb{R}^2$ elegido al azar. Mostrar que el siguiente algoritmo converge al vector $v_1$ cuando $N \to \infty$:
>
> - Para $k \in 1, \dots, N$:
>
>   - $x = Bx$
>
>   - $x = x / ||x||$

Si $A = U \Sigma V^t$, podemos sustituirlo en lo provisto por la letra del ejercicio $B = A^t A$:

$$
B = (U \Sigma V^t)^t (U \Sigma V^t) = V \Sigma^t U^t U \Sigma V^t
$$

Por la ortogonalidad de $U$, se tiene $U^t U = I$:

$$
B = V \Sigma^t \Sigma V^t
$$

La matriz $\Sigma^t \Sigma$ es diagonal cuadrada con entradas $\sigma_i^2$. Los autovalores de $B$ (de dimensiones $2 \times 2$) son:

$$
\lambda_1 = \sigma_1^2
$$

$$
\lambda_2 = \sigma_2^2
$$

Los autovectores de $B$ son precisamente las columnas de la matriz $V$, denotados como $v_1$ y $v_2$.

??? info "Observación Teórica: ¿Por qué los autovectores de $B$ son las columnas de $V$?"
    De la ecuación anterior, $B = V (\Sigma^t \Sigma) V^t$. Definiendo $\Lambda = \Sigma^t \Sigma$:

    $$
    B = V \Lambda V^t
    $$

    Por definición de la SVD, $V$ es una matriz **ortogonal**, lo que implica $V^t = V^{-1}$. Sustituyendo:

    $$
    B = V \Lambda V^{-1}
    $$

    Esta expresión coincide con la definición de la **diagonalización** ($M = P D P^{-1}$), donde $D$ (equivalente a $\Lambda$) contiene los **autovalores** y $P$ (equivalente a $V$) es la matriz cuyas columnas son los **autovectores** correspondientes.

    Por lo tanto, las columnas de $V$ ($v_1, v_2$) son los autovectores de $B$.

Dado que $\sigma_1 > \sigma_2 > 0$, se tiene $\lambda_1 > \lambda_2 > 0$.

??? info "Observación Teórica: ¿El orden estricto $\sigma_1 > \sigma_2 > 0$ es una convención algorítmica?"
    Sí, el ordenamiento $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$ es la convención estándar adoptada por bibliotecas como NumPy y SciPy, y corresponde a la formulación canónica de la SVD.

    La SVD ordena los valores singulares de mayor a menor, de modo que $\sigma_1$ corresponde a la dirección de máxima varianza.

    El enunciado establece adicionalmente que **$\sigma_i \neq \sigma_j$** para $i \neq j$, lo que descarta la posibilidad de valores singulares repetidos.

    Combinando la convención de ordenamiento descendente con la restricción de desigualdad estricta, se obtiene **$\sigma_1 > \sigma_2 > 0$**.

El algoritmo planteado evalúa un simple bucle $k \in 1, \dots, N$ sobre la operación iterada:

$$
x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}
$$

??? info "Observación Teórica: ¿Por qué la iteración asume esta forma colapsada general?"
    En el **Método de la Potencia** normalizado, cada paso divide por la norma del vector obtenido. Se puede demostrar por inducción que esto equivale a un reescalado que no afecta la dirección:

    1. Paso 1: $x^{(1)} = \frac{B x^{(0)}}{||B x^{(0)}||}$.
    2. Paso 2: $x^{(2)} = \frac{B x^{(1)}}{||B x^{(1)}||} = \frac{B \left( \frac{B x^{(0)}}{||B x^{(0)}||} \right)}{||B \left( \frac{B x^{(0)}}{||B x^{(0)}||} \right)||}$.

    Como $c = ||B x^{(0)}||$ es un escalar real positivo, por linealidad se tiene $B(c v) = c B v$ y $||c v|| = c ||v||$, por lo que **el escalar del paso anterior se cancela en el cociente**:

    $$
x^{(2)} = \frac{\frac{1}{||B x^{(0)}||} \cdot B^2 x^{(0)}}{\frac{1}{||B x^{(0)}||} \cdot ||B^2 x^{(0)}||} = \frac{B^2 x^{(0)}}{||B^2 x^{(0)}||}
$$

    Repitiendo este argumento $k$ veces, los factores escalares intermedios se cancelan por linealidad, con lo que la dirección de $x^{(k)}$ es la misma que la de $B^k x^{(0)}$ normalizado.

    📌 *Para consultar la demostración inductiva detallada y su verificación empírica en Python, podés remitirte al [Método de la Potencia](../../demostraciones/metodo_potencia.md).*

Se nos explica que $x \in \mathbb{R}^2$ es elegido al azar, por lo que podemos representarlo en función de la base ortonormal completa del plano compuesto por $v_1$ y $v_2$:

$$
x^{(0)} = c_1 v_1 + c_2 v_2
$$

??? info "Observación Teórica: ¿Por qué $v_1$ y $v_2$ forman una Base Ortonormal completa para $\mathbb{R}^2$?"
    En la SVD, $V$ es una matriz ortogonal de $2 \times 2$. Sus columnas son mutuamente ortogonales ($v_1 \cdot v_2 = 0$) y de norma unitaria ($||v_i||_2 = 1$).

    Como $v_1$ y $v_2$ son dos vectores ortogonales en $\mathbb{R}^2$, son linealmente independientes y forman una **base ortonormal** del espacio.

    Por lo tanto, cualquier vector $x^{(0)} \in \mathbb{R}^2$ puede expresarse como combinación lineal: $x^{(0)} = c_1 v_1 + c_2 v_2$.

Aplicando el álgebra del operador iterativo con iteraciones tendientes a $\infty$:

$$
B^k x^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2
$$

??? info "Observación Teórica: ¿Cómo opera $B^k$ iterativamente sobre la base de autovectores?"
    Al aplicar $B$ reiteradamente sobre el vector inicial se obtiene la operación $B^k x^{(0)}$.

    Por definición del problema de autovalores, $B v_i = \lambda_i v_i$, es decir, la matriz actúa como un escalar sobre cada autovector.

    Aplicando esto $k$ veces: $B^k v_i = \lambda_i^k v_i$.

    Sustituyendo en esta expresión nuestro vector original partido en componentes del plano:

    $$
    B^k x^{(0)} = B^k (c_1 v_1 + c_2 v_2)
    $$

    Distribuyendo por linealidad:

    $$
    B^k x^{(0)} = c_1 (B^k v_1) + c_2 (B^k v_2)
    $$

    Sustituyendo el efecto de $B^k$ sobre cada autovector:

    $$
    B^k x^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2
    $$

Factorizando $\lambda_1^k$:

$$
B^k x^{(0)} = \lambda_1^k \left( c_1 v_1 + c_2 \left( \frac{\lambda_2}{\lambda_1} \right)^k v_2 \right)
$$

Como $\lambda_1 > \lambda_2$, se tiene $\frac{\lambda_2}{\lambda_1} < 1$, y por tanto:

$$
\lim_{k \to \infty} \left( \frac{\lambda_2}{\lambda_1} \right)^k = 0
$$

Cuando el segundo término tiende a cero, la iteración converge en dirección a $v_1$:

$$
B^k x^{(0)} \approx \left( \lambda_1^k \cdot c_1 \right) v_1
$$

Si $c_1 = 0$ (el vector inicial es ortogonal a $v_1$), el proceso converge a $v_2$ en lugar de $v_1$.

??? info "Observación Teórica: ¿Qué ocurre matemáticamente si $c_1 = 0$? ¿El vector se vuelve nulo?"
    La factorización por $\lambda_1^k$ es válida solo cuando $c_1 \neq 0$. Si $c_1 = 0$, se debe analizar la suma original directamente:

    $$
    B^k x^{(0)} = 0 \cdot \lambda_1^k v_1 + c_2 \lambda_2^k v_2 = c_2 \lambda_2^k v_2
    $$

    Dado que en el Método de la Potencia el paso es normalizar forzosamente $x^{(k)} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}$, no importa cuán microscópico se torne el escalar $\lambda_2^k \to 0$ con el avance del tiempo, al estar en el numerador y denominador sometido bajo norma **éste se cancela intrínsecamente**:

    $$
    x^{(k)} = \frac{c_2 \lambda_2^k v_2}{||c_2 \lambda_2^k v_2||} = \frac{c_2 \lambda_2^k}{|c_2| \lambda_2^k} \cdot \frac{v_2}{||v_2||} = \text{sgn}(c_2) v_2
    $$

    Por lo tanto, el algoritmo no tiende al origen $(0,0)$: la normalización en cada iteración preserva la norma unitaria, y el vector converge a $\pm v_2$.

En la práctica, para vectores iniciales generados aleatoriamente en aritmética de punto flotante, la probabilidad de que $c_1 = 0$ exactamente es nula, por lo que el algoritmo converge a $v_1$ con probabilidad 1.

Como en cada iteración el vector se normaliza ($x = \frac{x}{||x||}$), el factor escalar $\lambda_1^k$ se cancela, dejando únicamente la dirección principal:

$$
\lim_{N \to \infty} x^{(N)} = \pm v_1
$$

Esto es la base del **Método de la Potencia**.

---

## Solución Inciso C: Rutina en Python
> c) Escriba una rutina que calcule la mejor aproximación de rango 1 de una matriz real de $n \times 2$ en el sentido de la norma 2. Toda función que involucre operaciones más complejas que el producto matricial debe ser definida explícitamente.

A continuación se presenta la rutina, sin emplear funciones de factorización directa de la biblioteca estándar. Para obtener el valor singular dominante se utiliza el cociente de Rayleigh a partir de las iteraciones del Método de la Potencia.

```python
--8<-- "Examen_2025_07_21/01_svd/verificacion.py"
```
