# Radio Espectral de una Matriz de Markov

> **Teorema.**
> Sea $P \in \mathbb{R}^{n \times n}$ una matriz estocástica por columnas (es decir, $p_{ij} \ge 0$ para todo $i,j$ y $\sum_{i=1}^n p_{ij} = 1$ para todo $j$). Entonces, su radio espectral es exactamente 1:
>
> $$ \rho(P) = 1 $$

## Interpretación del Enunciado

En el estudio de las **Cadenas de Markov**, la matriz de transición $P$ dicta cómo evoluciona la probabilidad de los estados de un sistema. El hecho de que el radio espectral sea siempre igual a 1 es fundamental porque garantiza que las probabilidades no crezcan indefinidamente ni se desvanezcan a cero; esto permite la existencia de al menos un **estado de equilibrio estacionario**.

---

## Demostración

La demostración se divide en dos partes: probar que $\lambda = 1$ es siempre un autovalor de $P$, y probar que ningún autovalor puede tener un módulo estrictamente mayor a 1.

### 1. $\lambda = 1$ es autovalor de $P$

Por definición, las columnas de una matriz de Markov suman 1. Podemos expresar esta propiedad usando el vector constante de unos $e = (1, 1, \dots, 1)^T$. 

Multiplicar $e^T$ por $P$ equivale a sumar las filas de cada columna. Como cada columna suma 1, el vector resultante es invariante:

$$ e^T P = (1, 1, \dots, 1) P = \left( \sum_{i=1}^n p_{i1}, \sum_{i=1}^n p_{i2}, \dots, \sum_{i=1}^n p_{in} \right) = (1, 1, \dots, 1) = e^T $$

Tomando la traspuesta en ambos lados:

$$ (e^T P)^T = (e^T)^T \implies P^T e = e = 1 \cdot e $$

Esto demuestra que **$e$ es un autovector de $P^T$ asociado al autovalor $\lambda = 1$**. 

Dado que una matriz $P$ y su traspuesta $P^T$ comparten exactamente el mismo polinomio característico y, por ende, los mismos autovalores (ver [Determinante de la Traspuesta](./determinante_producto.md)), concluimos que **$\lambda = 1$ es autovalor de $P$**.

### 2. Ningún autovalor excede 1 en módulo ($|\lambda| \le 1$)

Sea $\lambda$ cualquier autovalor de $P$ y sea $v = (v_1, v_2, \dots, v_n)^T$ su autovector asociado ($v \neq 0$). Dado que los autovalores y autovectores pueden ser complejos, consideramos sus módulos.

La ecuación de autovalores es $P v = \lambda v$. Para la $i$-ésima componente:

$$ \lambda v_i = \sum_{j=1}^n p_{ij} v_j $$

Tomando módulo a ambos lados y aplicando la desigualdad triangular ($|a+b| \le |a|+|b|$):

$$ |\lambda| |v_i| = \left| \sum_{j=1}^n p_{ij} v_j \right| \le \sum_{j=1}^n |p_{ij} v_j| = \sum_{j=1}^n p_{ij} |v_j| $$
*(Nota: $p_{ij} \ge 0$, por lo que $|p_{ij}| = p_{ij}$).*

Sea $k$ el índice de la componente de $v$ con el módulo máximo: $|v_k| = \max_j |v_j|$. 
Sustituimos todos los $|v_j|$ de la sumatoria por el valor máximo $|v_k|$, lo cual como mucho agrandará la suma:

$$ |\lambda| |v_i| \le \sum_{j=1}^n p_{ij} |v_k| = |v_k| \sum_{j=1}^n p_{ij} $$

Esta desigualdad vale para *cualquier* fila $i$. Evaluémosla en particular para la misma fila $k$ donde el autovector alcanza su máximo:

$$ |\lambda| |v_k| \le |v_k| \sum_{j=1}^n p_{kj} $$

Aquí hay un detalle crucial: $P$ es estocástica **por columnas**, no por filas, por lo que la suma $\sum_{j=1}^n p_{kj}$ (que es la suma de la fila $k$) no es necesariamente 1. 

Para sortear esto con absoluta elegancia sin invocar normas matriciales, recordemos la demostración de la Parte 1: si aplicamos el mismo análisis anterior a $P^T$ en lugar de $P$ (quienes comparten espectro), la ecuación $P^T u = \lambda u$ para la componente máxima $k$ de $u$ dicta:

$$ |\lambda| |u_k| \le |u_k| \sum_{j=1}^n (P^T)_{kj} = |u_k| \underbrace{\sum_{j=1}^n p_{jk}}_{= 1} = |u_k| \cdot 1 $$

Como $u$ es autovector, $u \neq 0 \implies |u_k| > 0$. Podemos dividir ambos lados por $|u_k|$:

$$ |\lambda| \le 1 $$

### 3. Conclusión

Puesto que todo autovalor de $P$ (y $P^T$) obedece $|\lambda| \le 1$ y probamos explícitamente la existencia del autovalor $\lambda = 1$, el autovalor de máximo módulo es exactamente 1. Por definición de radio espectral:

$$ \rho(P) = \max \{ |\lambda| : \lambda \in \sigma(P) \} = 1 $$

---

## Referencias Externas

*   **Libro**: *Linear Algebra and Its Applications* (David C. Lay). **Capítulo 4, Sección 4.9: "Applications to Markov Chains"**. Demuestra estructuralmente por qué una matriz estocástica siempre admite el estado estacionario $\lambda=1$.
*   **Libro**: *Matrix Computations* (Golub & Van Loan). **Capítulo 7, Sección 7.1**. Extiende la demostración usando el Teorema de Gershgorin para acotar el espectro matricial dentro de discos unitarios basándose en las normas de transición.
*   **Web**: [Markov Matrices and Eigenvectors](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/video-lectures/) - *MIT OpenCourseWare (Gilbert Strang, Lecture 24)*. Expone en video la deducción canónica visual del vector de unos para $P^T$.

---

## Verificación Empírica Computacional

Aplicamos el testeo mediante simulación de matrices de Markov aleatorias (normalizando columnas generadas aleatoriamente por la distribución uniforme) calculando sus autovalores empíricos mediante `numpy.linalg.eig`.

```python
--8<-- "demostraciones/radio_espectral_markov.py"
```
