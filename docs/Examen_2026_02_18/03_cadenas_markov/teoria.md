# Ejercicio 3: Cadenas de Markov y Matrices Estocásticas

> **Ejercicio 3.**
>
> **a) Sea P $\in \mathbb{R}^{n \times n}$ una matriz de Markov.**
>
> - **i)** Probar que si $P$ es diagonalizable y $-1$ no es autovalor, entonces existe el estado límite para todo estado inicial.
> - **ii)** Sean $\alpha, \beta, \gamma \in \mathbb{R}$ y $v^{(0)} = \alpha w_1 + \beta w_2 + \gamma u$ donde $w_1$ y $w_2$ son estados de equilibrio de $P$ y $u$ es un autovector de $P$ con autovalor $\lambda$ tal que $|\lambda| < 1$. Calcular el estado límite de la sucesión $v^{(k)} = P^k v^{(0)}$ en función de $\alpha, \beta, \gamma, w_1, w_2$ y u.
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

Por **hipótesis**, la matriz $P$ es diagonalizable.

??? info "Observación Teórica: Diagonalizabilidad y Bases de Autovectores"
    Que una matriz de orden $n \times n$ sea **diagonalizable** significa que posee $n$ autovectores linealmente independientes. Este conjunto de autovectores forma una base de $\mathbb{R}^n$, lo que permite expresar cualquier estado del sistema como una combinación lineal de los mismos.

    *¿Qué garantiza que una matriz sea diagonalizable?* Una condición suficiente es que sus autovalores sean distintos entre sí. Para el desarrollo formal de esta propiedad, véase [Demostración: Autovalores Distintos implican L.I.](../../demostraciones/autovalores_distintos.md).

    Fin de la observación.

??? warning "Trampa Común: ¿Diagonalizable implica autovalores únicos?"
    Una confusión metodológica frecuente es asumir que si $P$ es diagonalizable, entonces todos sus autovalores deben ser distintos, y por ende el estado estacionario con $\lambda = 1$ sería único. **Esto es falso**.
    La implicación matemática es estrictamente unidireccional: **Autovalores distintos $\implies$ Diagonalizable.**

    Una matriz puede ser diagonalizable con autovalores repetidos (como ocurre en este mismo ejercicio en el inciso B, donde $\lambda=1$ tiene multiplicidad algebraica 2). Si $\lambda=1$ se repite (ej. múltiples estados absorbentes), el estado estacionario límite no tiende a un único autovector $v_{\text{max}}$, sino a una **combinación lineal** de la base del autoespacio $E_{\lambda=1}$ (los estados de equilibrio $w_1, \dots, w_k$), y sus ponderaciones dependerán del vector de condición inicial $v^{(0)}$.

    Para ver una demostración formal matricial y computacional de esto, véase [Demostración: Diagonalizable con Autovalores Repetidos](../../demostraciones/diagonalizable_autovalores_repetidos.md).

    Fin de la advertencia.

Al ser $P$ diagonalizable, existe una base de autovectores $\{v_1, \dots, v_n\}$. Por lo tanto, cualquier estado inicial arbitrario $v^{(0)} \in \mathbb{R}^n$ se puede expresar como una combinación lineal de dicha base:

$$
v^{(0)} = c_1 v_1 + c_2 v_2 + \dots + c_n v_n
$$

La evolución del sistema tras $k$ pasos ($v^{(k)} = P^k v^{(0)}$) escala cada componente por su autovalor correspondiente a la potencia $k$:

$$
v^{(k)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \dots + c_n \lambda_n^k v_n
$$

Analizamos el comportamiento de $\lambda_i^k$ cuando $k \to \infty$:

1. Si $|\lambda_i| < 1$, entonces $\lambda_i^k \to 0$.

2. Si $\lambda_i = 1$, entonces $\lambda_i^k = 1$ para todo $k$.

3. Si $|\lambda_i| = 1$ y $\lambda_i \ne 1$, el término $\lambda_i^k$ oscila en el círculo unitario sin converger. Esto incluye el caso real $\lambda_i = -1$ (excluido por hipótesis) y cualquier autovalor complejo $\lambda_i = e^{i\theta}$ con $\theta \ne 0$ (no cubierto por la hipótesis).

??? info "Validez para autovalores complejos"
    El caso 1 es válido tanto para autovalores reales como complejos. Si $\lambda_i = r e^{i\theta} \in \mathbb{C}$ con $r = |\lambda_i| < 1$, entonces:

    $$
    |\lambda_i^k| = |\lambda_i|^k = r^k \xrightarrow{k \to \infty} 0
    $$

    independientemente del argumento $\theta$. Por lo tanto $\lambda_i^k \to 0$ en $\mathbb{C}$.

    El caso 3 también admite autovalores complejos: cualquier $\lambda$ con $|\lambda| = 1$ y $\lambda \ne 1$ (por ejemplo $e^{2\pi i/3}$ en una cadena de período 3) produce una sucesión $\lambda^k$ que recorre el círculo unitario sin converger. La hipótesis de que $-1$ no es autovalor cubre el único caso real problemático; en el contexto de este ejercicio (donde $P \in \mathbb{R}^{n\times n}$ y se pide probar la existencia del límite bajo esa hipótesis), es suficiente ser precisos con la condición real pedida.

    Fin de la nota.

Para que el límite exista, se requiere que **no haya ningún autovalor con $|\lambda_i| = 1$ distinto de $1$**: ni reales ni complejos. La hipótesis del enunciado garantiza la ausencia del caso real $\lambda_i = -1$. Si además no existen autovalores complejos de módulo 1 (lo cual ocurre en el inciso B y en cualquier cadena aperiodica), todos los términos con $|\lambda_i| < 1$ desaparecen en el límite y los términos con $\lambda_i = 1$ permanecen constantes. Por lo tanto, el límite existe para cualquier $v^{(0)}$.

#### Demostración A-2: Cálculo del Límite

> **a-ii)** Sean $\alpha, \beta, \gamma \in \mathbb{R}$ y $v^{(0)} = \alpha w_1 + \beta w_2 + \gamma u$ donde $w_1$ y $w_2$ son estados de equilibrio de $P$ y $u$ es un autovector con $|\lambda| < 1$. Calcular el límite de $v^{(k)}$.

??? info "Múltiples Estados de Equilibrio"
    El enunciado nos indica explícitamente que existen **dos** estados de equilibrio distintos, $w_1$ y $w_2$.
    ¿Qué significa esto algebraicamente? Significa que ambos satisfacen la ecuación $P w_i = 1 \cdot w_i$, es decir, ambos pertenecen al autoespacio asociado al autovalor $\lambda = 1$.
    Para que existan dos autovectores linealmente independientes asociados a $\lambda = 1$, la dimensión de $E_{\lambda=1}$ (multiplicidad geométrica) debe ser al menos 2, lo que implica que el autovalor $\lambda = 1$ no es único (su multiplicidad algebraica es $\ge 2$).

    ¿Qué significa esto desde el punto de vista de la cadena de Markov? Ocurre cuando la cadena es **reducible** y presenta múltiples "componentes conexas aisladas" o "estados absorbentes" (como veremos luego en el inciso B con la matriz $4 \times 4$).

    Fin de la observación.

Sabemos que:

- $w_1, w_2$ son estados de equilibrio $\implies P w_1 = w_1$ y $P w_2 = w_2$ (autovalor $\lambda = 1$).
- $u$ es autovector con autovalor $\lambda$ tal que $|\lambda| < 1$.

Aplicamos $P^k$ a $v^{(0)}$:

$$
v^{(k)} = P^k (\alpha w_1 + \beta w_2 + \gamma u) = \alpha P^k w_1 + \beta P^k w_2 + \gamma P^k u
$$

$$
v^{(k)} = \alpha (1)^k w_1 + \beta (1)^k w_2 + \gamma \lambda^k u
$$

Tomando el límite $k \to \infty$:

$$
\lim_{k \to \infty} v^{(k)} = \alpha w_1 + \beta w_2 + \gamma (0) u = \alpha w_1 + \beta w_2
$$

---

### Inciso B: Dinámica Poblacional

> **b)** Cuatro hábitats: Bosque (B), Selva (S), Estepa (E) y Río (R) están habitados por un grupo de animales. El movimiento anual entre estos hábitats está gobernado por las siguientes reglas:
>
> - Entre el Bosque (B) y la Selva (S), cada año hay una probabilidad de 0.5 de permanecer en el mismo hábitat y 0.5 de moverse al otro.
> - Si un animal se encuentra en la Estepa (E), al año siguiente permanecerá allí.
> - En el Río (R), cada año un animal permanece en R con probabilidad 0.7, o se traslada a la Estepa (E) con probabilidad 0.3.
>
> - **i)** Escribir la matriz de transición P correspondiente (orden de hábitats: B, S, E, R), calcular sus autovalores y el autoespacio de vectores de equilibrio y los asociados a $\lambda = 0$. ¿Qué dimensión tiene cada uno de estos autoespacios? ¿Es diagonalizable la matriz P? Justificar.
> - **ii)** Inicialmente, la población de animales es la siguiente: 300 en el Bosque, 100 en la Selva, 200 en la Estepa y 0 en el Río. Calcular cómo evolucionará la población a largo plazo.

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

??? info "Propiedad Algebraica de Matrices por Bloques"
    Este "truco" proviene de una propiedad fundamental del Álgebra Lineal. Si una matriz $P$ puede particionarse en bloques tal que los sub-bloques fuera de la diagonal principal son nulos (formando una matriz **bloque-diagonal** o incluso bloque-triangular), el determinante de la matriz global es el producto de los determinantes de sus bloques en diagonal.

    Por lo tanto, al plantear la ecuación del polinomio característico $p_P(\lambda) = \det(P - \lambda I)$:

    $$
    \det \begin{pmatrix} A - \lambda I_A & \mathbf{0} \\ \mathbf{0} & B - \lambda I_B \end{pmatrix} = \det(A - \lambda I_A) \cdot \det(B - \lambda I_B) = 0
    $$

    Esto demuestra algebraicamente que el polinomio característico global de $P$ se factoriza exactamente como el producto de los polinomios de sus submatrices. En consecuencia, las raíces totales del sistema son simplemente la unión de los autovalores individuales de cada bloque, evadiendo calcular y factorear un polinomio de grado 4 a fuerza bruta.

    Fin de la nota técnica.

Espectro de $P$: $\lambda \in \{1, 1, 0, 0.7\}$.

**Autoespacio $E_{\lambda=1}$ (equilibrio):**
Resolvemos $(P-I)v = 0$:

$$
\begin{pmatrix} -0.5 & 0.5 & 0 & 0 \\ 0.5 & -0.5 & 0 & 0 \\ 0 & 0 & 0 & 0.3 \\ 0 & 0 & 0 & -0.3 \end{pmatrix} \begin{pmatrix} b \\ s \\ e \\ r \end{pmatrix} = 0 \implies b=s, r=0, e \text{ libre}.
$$

Base: $\{(1, 1, 0, 0)^T, (0, 0, 1, 0)^T\}$. Dimensión 2.

**Autoespacio $E_{\lambda=0}$:**
Resolvemos $Pv = 0$:
$b=-s, e=0, r=0$.
Base: $\{(1, -1, 0, 0)^T\}$. Dimensión 1.

??? info "Multiplicidad Algebraica vs Geométrica"
    Estas dimensiones determinan si existe una base completa para diagonalizar una matriz:

    - **Multiplicidad Algebraica (M.A.):** Es la cantidad de veces que se repite un determinado autovalor (raíz) dentro del polinomio característico de la matriz. En nuestro caso, $\lambda=1$ es una raíz doble, por lo que su $M.A.=2$.
    - **Multiplicidad Geométrica (M.G.):** Es la dimensión "real" del autoespacio (el número máximo de autovectores L.I.) asociado a dicho autovalor. Se calcula como $\dim(E_\lambda) = n - \text{rg}(P-\lambda I)$.

    Por teorema, siempre se cumple que **$1 \le M.G. \le M.A.$**
    Para que una matriz sea **diagonalizable**, la multiplicidad geométrica de **todos** sus autovalores debe coincidir exactamente con su multiplicidad algebraica ($M.G. = M.A.$).

    Fin de la observación.

**Diagonalizabilidad:**
$\lambda=1$ tiene multiplicidad algebraica 2 y geométrica 2. Los otros autovalores son simples. La suma de dimensiones de los autoespacios es 4, igual al orden de la matriz. $P$ es diagonalizable.

*(Para comprender por qué esta suma define la existenciabillidad de la diagonalización, ver la [Demostración del Criterio de Diagonalizabilidad por Bases de Autoespacios](../../demostraciones/criterio_diagonalizabilidad.md)).*

#### Evolución a Largo Plazo

Estado inicial: $v^{(0)} = (300, 100, 200, 0)^T$.

1. El subsistema B-S es cerrado y regular. La población total de 400 se distribuirá uniformemente por simetría: $b^{(\infty)} = 200, s^{(\infty)} = 200$.
2. El Río empieza con 0 animales, por lo que no aporta flujo a la Estepa. La Estepa es absorbente y mantiene sus 200 iniciales: $e^{(\infty)} = 200, r^{(\infty)} = 0$.

El estado límite es $v^{(\infty)} = (200, 200, 200, 0)^T$.

---

## Verificación Empírica Computacional (NumPy)

Se utiliza `NumPy` para instanciar la matriz $P$, calcular sus autovalores y simular la evolución del sistema a largo plazo.

```python
--8<-- "Examen_2026_02_18/03_cadenas_markov/verificacion.py"
```
