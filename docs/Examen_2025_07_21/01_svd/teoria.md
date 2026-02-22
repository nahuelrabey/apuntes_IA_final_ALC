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

- $V$ es una matriz ortogonal de $2 \times 2$, ergo se compone acotadamente como $V = [v_1, v_2]$.

- $\Sigma$ es una matriz de $n \times 2$ (mismas dimensiones que $A$) que alberga a los valores singulares $\sigma_i$ estrictamente a lo largo de su "diagonal principal" (donde el índice de fila coincide con el de columna, $\Sigma_{ii}$). **En consecuencia, todos los demás elementos que no pertenecen a esta diagonal son estrictamente nulos ($\Sigma_{ij} = 0$ para todo $i \neq j$)**. Esta es una propiedad basal inquebrantable de la SVD. A la hora de iterar, notamos que todas las filas contenidas entre $n=3$ hasta la última ($n$) serán filas llenas enteramente de ceros.

- La expresión $\tilde{A} = \sigma_1 u_1 v_1^t$ se denomina **aproximación de rango 1**. El **Teorema de Eckart-Young-Mirsky** ([fuente matemática](https://es.wikipedia.org/wiki/Teorema_de_Eckart-Young-Mirsky)) en álgebra lineal demuestra infaliblemente que al truncar la SVD reteniendo únicamente el o los mayores valores singulares, se obtiene la matriz "más cercana" posible a la original minimizando el margen de error, en el sentido de la Norma Rectangular Espectral (Norma-2) y de Frobenius. Por ende, la conjunción de los mayores vectores singulares $\sigma_1 u_1 v_1^t$ conforma la proyección hiper-dimensional estricta de mayor asertividad para explicar la matriz general reduciéndola a un solo espectro principal (un solo vector-base).

## Solución Inciso A

Sabemos por definición de la SVD truncada que como la matriz original $A$ es de orden $n \times 2$, sólo poseerá a lo sumo 2 valores singulares no nulos. Podemos entonces descomponerla como la suma de sus componentes de rango 1:

$$A = \sum_{i=1}^{k} \sigma_i u_i v_i^t = \sigma_1 u_1 v_1^t + \sigma_2 u_2 v_2^t$$

Dado que se nos informa que $\tilde{A} = \sigma_1 u_1 v_1^t$ es la aproximación de mayor rango, podemos definir el error vectorial de efectuar dicha predicción como $e = A x - \tilde{A} x$.

Reemplazando los términos, el residuo es exactamente la componente descartada de la matriz SVD:

$$e = (A - \tilde{A}) x = (\sigma_2 u_2 v_2^t) x$$

Nos piden probar que la norma de este error se encuentra acotada por $\sigma_2$. Aplicamos la norma euclidiana o Norma-2 ($|| \cdot ||_2$) en ambos lados:

$$||e||_2 = ||\sigma_2 u_2 v_2^t x||_2$$

Como un escalar positivo puede extraerse de la norma:

$$||e||_2 = \sigma_2 ||u_2 (v_2^t x)||_2$$

El término entre paréntesis $(v_2^t x)$ resulta en un número escalar del producto interno vectorial. Lo podemos extraer en valor absoluto:

$$||e||_2 = \sigma_2 |v_2^t x| \cdot ||u_2||_2$$

Dado que las matrices de la SVD componen isometrías ortogonales perfectas, $U$ y $V$ se componen de vectores columna ortonormales unitarios. Es una certeza, por ende, que el vector singular de la izquierda $u_2$ posee norma estricta igual a 1 ($||u_2||_2 = 1$):

$$||e||_2 = \sigma_2 |v_2^t x|$$

Al observar minuciosamente la parte restante correspondiente al producto interno $|v_2^t x|$, descubrimos que ambos vectores provienen del disco estandarizado: sabemos que $x \in \mathbb{R}^2$ con $||x||_2 = 1$ (nos dicen que pertenece al "círculo unitario") y paralelamente $v_2$ siempre es un vector ortonormal de $V$, por lo cual $||v_2||_2 = 1$.

Recurriendo a la célebre inecuación de Cauchy-Schwarz:

$$|v_2^t x| \leq ||v_2||_2 \cdot ||x||_2 = 1 \cdot 1 = 1$$

Consumiendo nuestra afirmación, arribamos a que:

$$||e||_2 \leq \sigma_2 \cdot 1 = \sigma_2$$

Queda así demostrado que el error cometido en la aproximación $\|A x - \tilde{A} x\|_2$ siempre estará acotado por arriba por la magnitud del segundo valor singular descartado, $\sigma_2$.

---

## Solución Inciso B

Si $A = U \Sigma V^t$, podemos sustituirlo en lo provisto por la letra del ejercicio $B = A^t A$:

$$B = (U \Sigma V^t)^t (U \Sigma V^t) = V \Sigma^t U^t U \Sigma V^t$$

Dada la ortogonalidad de la matriz $U$, sabemos que su autotranspuesta obedece $U^t U = I$. Aplicando este axioma simplificador:

$$B = V \Sigma^t \Sigma V^t$$

Dado que la matriz pre-multiplicada $\Sigma^t \Sigma$ conforma invariablemente una matriz diagonal cuadrada en la que surgen iterativamente los valores singulares originales elevados al cuadrado ($\Sigma_{ii}^2 = \sigma_i^2$), entonces los autovalores formales de $B$ (que recordemos es de $2 \times 2$), llamados convencionalmente $\lambda_1$ y $\lambda_2$, son por añadidura:

$$\lambda_1 = \sigma_1^2$$

$$\lambda_2 = \sigma_2^2$$

Los autovectores de $B$ son precisamente las columnas de la matriz $V$, denotados como $v_1$ y $v_2$.

En base a esto, y conociendo que los valores singulares de SVD exigen que $\sigma_i \neq \sigma_j$ y vienen típicamente ordenados descendiendo $\sigma_1 > \sigma_2 > 0$, deducimos que $\lambda_1 > \lambda_2 \geq 0$.

El algoritmo planteado evalúa un simple bucle $k \in 1, \dots, N$ sobre la operación iterada:

$$x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}$$

Se nos explica que $x \in \mathbb{R}^2$ es elegido al azar, por lo que podemos representarlo en función de la base ortonormal completa del plano compuesto por $v_1$ y $v_2$:

$$x^{(0)} = c_1 v_1 + c_2 v_2$$

Aplicando el álgebra del operador iterativo con iteraciones tendientes a $\infty$:

$$B^k x^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2$$

Factorizando para independizarnos del exponente del autovalor dominante:

$$B^k x^{(0)} = \lambda_1^k \left( c_1 v_1 + c_2 \left( \frac{\lambda_2}{\lambda_1} \right)^k v_2 \right)$$

Dado que denotamos ex-ante que $\lambda_1 > \lambda_2$, la fracción es decididamente un número en el recuadro menor a la unidad $( \frac{\lambda_2}{\lambda_1} < 1 )$. Por propiedad de los límites asintóticos exponenciales:

$$\lim_{k \to \infty} \left( \frac{\lambda_2}{\lambda_1} \right)^k = 0$$

Al aproximarse velozmente todo el segundo término aditivo al valor cero, obtenemos con precisión que la iteración de nuestro vector de partida se alineará siendo puramente colineal con el primer autovector:

$$B^k x^{(0)} \approx \left( \lambda_1^k \cdot c_1 \right) v_1$$

Evidentemente si nuestro vector estocástico nació sin componente principal ($c_1 = 0$, ortogonalidad perfecta elegida para nuestra semilla inicial), el proceso fallará al converger a $v_2$. Tal salvedad, en algoritmos estocásticos que operan en floats (cuyos conjuntos de medida afirman que extraer el exacto plano euclidiano en flotantes ortogonales tiene teóricamente "probabilidad cero"), carece de sustento para descalificar la iteración.

Como para rematar cada ciclo el vector se normaliza contra sí mismo $x = \frac{x}{||x||}$, todo componente escalar global $\lambda$ decae por divisiones intrínsecas, dejando con exclusividad un vector de tamaño 1 alineado a la dirección principal:

$$\lim_{N \to \infty} x^{(N)} = \pm v_1$$

Evidenciando la validez asintótica teórica de lo que universalmente nombramos "Método de la Potencia".

---

## Solución Inciso C: Rutina en Python

A continuación, la rutina desarrollada sin emplear funciones de grado superlativo como factorizaciones directas en la librería algorítmica. Para hallar el valor singular predominante nos basamos en el cociente de Rayleigh, aplicando producto punto clásico entre la iteración convergiendo de las potencias.

```python
--8<-- "Examen_2025_07_21/01_svd/verificacion.py"
```
