# Ejercicio 3: Cadenas de Markov y Matrices Estocásticas

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

## Interpretación del Enunciado

El ejercicio analiza el comportamiento asintótico de las **Cadenas de Markov**. 
En la parte teórica, se estudian las condiciones para la existencia de un estado límite y el cálculo de dicho límite en función de los estados de equilibrio iniciales.
En la parte práctica, se modela la dinámica poblacional de animales entre cuatro hábitats mediante una matriz de transición estocástica, analizando sus autovalores, autoespacios y la evolución a largo plazo.

---

## Solución del Ejercicio

### Inciso A: Estados de Equilibrio y Límites Asintóticos

#### Demostración A-1: Existencia de Estado Límite

> **a-i)** Probar que si $P$ es diagonalizable y $-1$ no es autovalor, entonces existe el estado límite para todo estado inicial.

Por las propiedades de las matrices de Markov, el radio espectral de $P$ es $\rho(P) = 1$ (ver [demostración rigurosa](../../demostraciones/radio_espectral_markov.md)). Esto implica que para todo autovalor $\lambda_i$, se cumple $|\lambda_i| \le 1$.

Al ser $P$ diagonalizable, existe una base de autovectores $\{v_1, \dots, v_n\}$. Cualquier estado inicial $v_0$ se puede expresar como:
$$
v_0 = c_1 v_1 + c_2 v_2 + \dots + c_n v_n
$$

La evolución del sistema tras $k$ pasos es $v_k = P^k v_0$:
$$
v_k = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \dots + c_n \lambda_n^k v_n
$$

Analizamos el comportamiento de $\lambda_i^k$ cuando $k \to \infty$:
1. Si $|\lambda_i| < 1$, entonces $\lambda_i^k \to 0$.
2. Si $\lambda_i = 1$, entonces $\lambda_i^k = 1$ para todo $k$.
3. Si $\lambda_i = -1$, el término $(-1)^k$ oscilaría. Sin embargo, por hipótesis, $-1$ no es autovalor de $P$.

Dado que no hay autovalores de módulo 1 distintos de 1 (y $-1$ está excluido), todos los términos con $|\lambda_i| < 1$ desaparecen en el límite, y los términos con $\lambda_i = 1$ permanecen constantes. Por lo tanto, el límite existe para cualquier $v_0$.

#### Demostración A-2: Cálculo del Límite

> **a-ii)** Sean $\alpha, \beta, \gamma \in \mathbb{R}$ y $v_0 = \alpha w_1 + \beta w_2 + \gamma u$ donde $w_1$ y $w_2$ son estados de equilibrio de $P$ y $u$ es un autovector con $|\lambda| < 1$. Calcular el límite de $v_k$.

Sabemos que:
- $w_1, w_2$ son estados de equilibrio $\implies P w_1 = w_1$ y $P w_2 = w_2$ (autovalor $\lambda = 1$).
- $u$ es autovector con autovalor $\lambda$ tal que $|\lambda| < 1$.

Aplicamos $P^k$ a $v_0$:
$$
v_k = P^k (\alpha w_1 + \beta w_2 + \gamma u) = \alpha P^k w_1 + \beta P^k w_2 + \gamma P^k u
$$
$$
v_k = \alpha (1)^k w_1 + \beta (1)^k w_2 + \gamma \lambda^k u
$$

Tomando el límite $k \to \infty$:
$$
\lim_{k \to \infty} v_k = \alpha w_1 + \beta w_2 + \gamma (0) u = \alpha w_1 + \beta w_2
$$

---

### Inciso B: Dinámica Poblacional

#### Matriz de Transición y Autoespacios

Definimos los hábitats en el orden: Bosque (B), Selva (S), Estepa (E), Río (R). A partir de las reglas dadas, construimos la matriz $P$:

- B: 0.5 a B, 0.5 a S.
- S: 0.5 a S, 0.5 a B.
- E: 1.0 a E (estado absorbente).
- R: 0.7 a R, 0.3 a E.

$$
P = \begin{pmatrix} 
0.5 & 0.5 & 0 & 0 \\
0.5 & 0.5 & 0 & 0 \\
0 & 0 & 1 & 0.3 \\
0 & 0 & 0 & 0.7 
\end{pmatrix}
$$

Los autovalores se obtienen de los bloques diagonales:
- Del bloque $\begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{pmatrix}$: $\lambda = 1, 0$.
- Del bloque $\begin{pmatrix} 1 & 0.3 \\ 0 & 0.7 \end{pmatrix}$: $\lambda = 1, 0.7$.

Espectro de $P$: $\lambda \in \{1, 1, 0, 0.7\}$.

**Autoespacio $E_{\lambda=1}$ (equilibrio):**
Resolvemos $(P-I)v = 0$:
$\begin{pmatrix} -0.5 & 0.5 & 0 & 0 \\ 0.5 & -0.5 & 0 & 0 \\ 0 & 0 & 0 & 0.3 \\ 0 & 0 & 0 & -0.3 \end{pmatrix} \begin{pmatrix} b \\ s \\ e \\ r \end{pmatrix} = 0 \implies b=s, r=0, e \text{ libre}.$
Base: $\{(1, 1, 0, 0)^T, (0, 0, 1, 0)^T\}$. Dimensión 2.

**Autoespacio $E_{\lambda=0}$:**
Resolvemos $Pv = 0$:
$b=-s, e=0, r=0$.
Base: $\{(1, -1, 0, 0)^T\}$. Dimensión 1.

**Diagonalizabilidad:**
$\lambda=1$ tiene multiplicidad algebraica 2 y geométrica 2. Los otros autovalores son simples. La suma de dimensiones de los autoespacios es 4, igual al orden de la matriz. $P$ es diagonalizable.

#### Evolución a Largo Plazo

Estado inicial: $v_0 = (300, 100, 200, 0)^T$.

1. El subsistema B-S es cerrado y regular. La población total de 400 se distribuirá uniformemente por simetría: $b_\infty = 200, s_\infty = 200$.
2. El Río empieza con 0 animales, por lo que no aporta flujo a la Estepa. La Estepa es absorbente y mantiene sus 200 iniciales: $e_\infty = 200, r_\infty = 0$.

El estado límite es $v_\infty = (200, 200, 200, 0)^T$.

---

## Verificación Empírica Computacional (NumPy)

Se utiliza `NumPy` para instanciar la matriz $P$, calcular sus autovalores y simular la evolución del sistema a largo plazo.

```python
--8<-- "Examen_2026_02_18/03_cadenas_markov/verificacion.py"
```
