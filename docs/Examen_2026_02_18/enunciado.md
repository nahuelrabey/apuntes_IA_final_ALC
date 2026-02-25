# Enunciado General: Examen 18 de Feb 2026

*(Los siguientes enunciados fueron extraídos y compilados automáticamente de las resoluciones individuales)*

---

## 01 Metodo Sor

> **Ejercicio 1.** Dada $A \in \mathbb{R}^{n \times n}$ con $a_{ii} \neq 0$, $1 \leq i \leq n$. $A = L + D + U$.
> 
> **a)** Demostrar que el sistema $Ax = b$ es equivalente al sistema $(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b$, cualquiera sea $\omega \neq 0$.
> 
> **b)** Considere el método iterativo $x^{k+1} = B(\omega)x^k + c$ con $B(\omega) = (D + \omega L)^{-1} ((1 - \omega)D - \omega U)$. Probar que $\det(B(\omega)) = (1 - \omega)^n$ y concluir que si el método converge $\implies \omega \in (0, 2)$.
> 
> **c)** Sea $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$. Analizar que sucede con el método definido en b) para los casos $\omega = \frac{1}{2}$ y $\omega = \frac{3}{2}$.


---

## 02 Condicionamiento

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


---

## 03 Cadenas Markov

> **Ejercicio 3.**
>
> **a) Sea P $\in \mathbb{R}^{n \times n}$ una matriz de Markov.**
>
> - **i)** Probar que si $P$ es diagonalizable y $-1$ no es autovalor, entonces existe el estado límite para todo estado inicial.
> - **ii)** Sean $\alpha, \beta, \gamma \in \mathbb{R}$ y $v_0 = \alpha w_1 + \beta w_2 + \gamma u$ donde $w_1$ y $w_2$ son estados de equilibrio de $P$ y $u$ es un autovector de $P$ con autovalor $\lambda$ tal que $|\lambda| < 1$. Calcular el estado límite de la sucesión $v_k = P^k v_0$ en función de $\alpha, \beta, \gamma, w_1, w_2$ y u.
>
> **b)** Cuatro hábitats: Bosque (B), Selva (S), Estepa (E) y Río (R) están habitados por un grupo de animales. El movimiento anual entre estos hábitats está gobernado por las siguientes reglas:
>
> - Entre el Bosque (B) y la Selva (S), cada año hay una probabilidad de 0.5 de permanecer en el mismo hábitat y 0.5 de moverse al otro.
> - Si un animal se encuentra en la Estepa (E), al año siguiente permanecerá allí.
> - En el Río (R), cada año un animal permanece en R con probabilidad 0.7, o se traslada a la Estepa (E) con probabilidad 0.3.
> 
> - **i)** Escribir la matriz de transición P correspondiente (orden de hábitats: B, S, E, R), calcular sus autovalores y el autoespacio de vectores de equilibrio y los asociados a $\lambda = 0$. ¿Qué dimensión tiene cada uno de estos autoespacios? ¿Es diagonalizable la matriz P? Justificar.
> - **ii)** Inicialmente, la población de animales es la siguiente: 300 en el Bosque, 100 en la Selva, 200 en la Estepa y 0 en el Río. Calcular cómo evolucionará la población a largo plazo.


---

## 04 Cuadrados Minimos Svd

> **Ejercicio 4.** Se desea aproximar un conjunto de datos experimentales mediante una combinación lineal de funciones dadas $\{f_1, \dots, f_m\}$, encontrando la función $f(x) = \sum_{i=1}^m \alpha_i f_i(x)$ que mejor aproxime los datos en el sentido de cuadrados mínimos, utilizando la descomposición en valores singulares (SVD) reducida por rango.
> 
> **Objetivo:** Determinar los coeficientes $\alpha_1, \dots, \alpha_m$ que minimizan el error cuadrático:
> $$ EC(\mathbf{\alpha}) = \sum_{j=1}^n (f(x_j) - y_j)^2 $$
> con $\mathbf{x} = (x_1, \dots, x_n)$ e $\mathbf{y} = (y_1, \dots, y_n)$ datos experimentales, con $n \ge m$.
> 
> **a)** Implementar una función en python que calcule la matriz $A \in \mathbb{R}^{n\times m}$ asociada al problema de cuadrados mínimos a partir de las funciones y de los datos. Además, asuma que existe $(U, s, V^T) = \text{SVD\_rank}(A)$. La función debe devolver $A$, $U$, $V^T$, $s$.
> 
> **b)** Implementar una función que, utilizando la descomposición del ítem anterior, calcule el vector de coeficientes $\mathbf{\alpha}$ y el correspondiente Error Cuadrático. No se permite el uso del comando algorítmico global `numpy.linalg.lstsq`. Solo se toleran operaciones atómicas (array, dot, diag, .T, @).


---

