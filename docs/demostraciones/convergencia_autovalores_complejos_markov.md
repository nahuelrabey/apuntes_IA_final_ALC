# Convergencia del Sistema según el Módulo del Autovalor (Cadenas de Markov)

> **Teorema.**
> Sea $P \in \mathbb{R}^{n \times n}$ una matriz de Markov diagonalizable y sea $v^{(k)} = P^k v^{(0)}$ la sucesión de estados con estado inicial $v^{(0)}$ arbitrario. Expresando $v^{(0)} = \sum_{i=1}^n c_i v_i$ en la base de autovectores, la contribución del $i$-ésimo término satisface:
>
> 1. Si $|\lambda_i| < 1$, la componente $c_i \lambda_i^k v_i \to 0$ cuando $k \to \infty$.
> 2. Si $\lambda_i = 1$, la componente $c_i \lambda_i^k v_i = c_i v_i$ es constante para todo $k$.
> 3. Si $|\lambda_i| = 1$ y $\lambda_i \ne 1$, la componente oscila en el círculo unitario y **no converge**.
>
> En consecuencia, la sucesión $v^{(k)}$ converge para todo $v^{(0)}$ si y sólo si no existen autovalores con $|\lambda_i| = 1$ distintos de $1$.

## Interpretación del Enunciado

Este resultado explica por qué la hipótesis "$-1$ no es autovalor" aparece en los enunciados sobre existencia de estado límite en cadenas de Markov.
La demostración aclara además que el comportamiento del sistema ante autovalores de módulo 1 es idéntico para valores **reales** (como $\lambda = -1$) y para valores **complejos** (como $e^{2\pi i/3}$): en ambos casos la ausencia de convergencia proviene de la rotación indefinida en el círculo unitario, no de la naturaleza real o imaginaria del valor.

---

## Demostración

### 1. Representación en base de autovectores

Como $P$ es diagonalizable, existe una base de $\mathbb{R}^n$ formada por autovectores $\{v_1, \dots, v_n\}$ con autovalores asociados $\{\lambda_1, \dots, \lambda_n\}$.
Todo estado inicial $v^{(0)} \in \mathbb{R}^n$ se expresa de forma única como:

$$
v^{(0)} = c_1 v_1 + c_2 v_2 + \dots + c_n v_n
$$

Aplicando $P^k$ y usando la linealidad y la definición de autovector ($P^k v_i = \lambda_i^k v_i$):

$$
v^{(k)} = P^k v^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \dots + c_n \lambda_n^k v_n
$$

El comportamiento asintótico de $v^{(k)}$ queda reducido al análisis de cada potencia $\lambda_i^k$.

### 2. Caso $|\lambda_i| < 1$: convergencia a cero (válido en $\mathbb{C}$)

Sea $\lambda_i \in \mathbb{C}$ con $|\lambda_i| = r < 1$. Escribimos $\lambda_i = r e^{i\theta}$. Entonces:

$$
\lambda_i^k = r^k e^{ik\theta}
$$

Tomando módulo:

$$
|\lambda_i^k| = r^k \xrightarrow{k \to \infty} 0
$$

dado que $0 < r < 1$. Por lo tanto $\lambda_i^k \to 0$ en $\mathbb{C}$, **independientemente del argumento** $\theta$. La rotación $e^{ik\theta}$ tiene módulo 1 pero no impide la convergencia, ya que el factor $r^k$ domina y aplasta la amplitud.

$$
\therefore \quad c_i \lambda_i^k v_i \to 0
$$

### 3. Caso $\lambda_i = 1$: componente constante

$$
\lambda_i^k = 1^k = 1 \quad \forall k \in \mathbb{N}
$$

La componente $c_i v_i$ permanece inalterada para todo $k$. Estos son los **estados de equilibrio** (o estacionarios) de la cadena.

### 4. Caso $|\lambda_i| = 1$, $\lambda_i \ne 1$: oscilación sin convergencia

Sea $\lambda_i = e^{i\theta}$ con $\theta \ne 0$. Entonces:

$$
\lambda_i^k = e^{ik\theta}
$$

Esta expresión traza una trayectoria en el círculo unitario del plano complejo. Su módulo es siempre 1 pero su argumento $k\theta$ crece sin parar.

Para que la sucesión $e^{ik\theta}$ converja, sería necesario que $e^{ik\theta} \to L$ para algún $L \in \mathbb{C}$ con $|L| = 1$, lo cual exigiría $e^{i(k+1)\theta} - e^{ik\theta} \to 0$, es decir $e^{ik\theta}(e^{i\theta} - 1) \to 0$. Pero $|e^{ik\theta}| = 1$ para todo $k$, de modo que esto sólo ocurre si $e^{i\theta} = 1$, contradiciendo $\theta \ne 0$.

$$
\therefore \quad c_i \lambda_i^k v_i \text{ no converge si } c_i \ne 0.
$$

??? info "Periodicidad: casos concretos en cadenas de Markov"
    Las cadenas de Markov **periódicas** de período $p$ presentan exactamente este fenómeno. Sus autovalores de módulo 1 son las $p$-ésimas raíces de la unidad:

$$
    \lambda_k = e^{2\pi i k / p}, \quad k = 0, 1, \dots, p-1
$$

    - **Período 2**: $\lambda \in \{1, -1\}$. El caso $\lambda = -1$ es el único real; su potencia $(-1)^k$ alterna entre $+1$ y $-1$.
    - **Período 3**: $\lambda \in \{1, e^{2\pi i/3}, e^{4\pi i/3}\}$. Los dos últimos son complejos conjugados no reales.
    - **Período $p$ general**: los $p-1$ autovalores distintos de $1$ producen estados que "rotan" entre $p$ configuraciones sin estabilizarse nunca.

### 5. Conclusión

$$
\lim_{k \to \infty} v^{(k)} = \sum_{\lambda_i = 1} c_i v_i
$$

siempre que no existan autovalores con $|\lambda_i| = 1$ y $\lambda_i \ne 1$.
Si existieran tales autovalores y su coeficiente $c_i \ne 0$ en la expansión de $v^{(0)}$, el límite no existiría.

---

## Referencias Externas

*   **Libro**: [*Linear Algebra and Its Applications*](https://www.amazon.com/Linear-Algebra-Its-Applications-5th/dp/032198238X) (David C. Lay, 5ª ed.). **Capítulo 4, Sección 4.9: "Applications to Markov Chains"** y **Capítulo 5, Sección 5.5: "Complex Eigenvalues"**. La sección 4.9 establece las condiciones de convergencia de $P^k$ bajo autovalores de módulo menor a 1; la sección 5.5 formaliza el comportamiento de $\lambda^k$ para $\lambda \in \mathbb{C}$.

*   **Libro**: [*Introduction to Linear Algebra*](https://math.mit.edu/~gs/linearalgebra/) (Gilbert Strang, 5ª ed.). **Capítulo 10: "Applications of Linear Algebra" — Sección sobre Markov Matrices**. Strang ilustra gráficamente por qué el autovalor $\lambda = 1$ es el responsable del estado límite, y cómo los demás autovalores de la cadena determinan la velocidad de convergencia.

*   **Libro**: [*Matrix Analysis*](https://www.cambridge.org/core/books/matrix-analysis/A6A6E6FF55D2E25F91A9E0E15DAE3CC3) (R. A. Horn & C. R. Johnson). **Capítulo 5, Sección 5.6: "Spectral Radius"** y **Sección 8.3: "Stochastic Matrices"**. Contiene la demostración completa de que el radio espectral de una matriz estocástica es exactamente 1 y caracteriza los autovalores de módulo 1.

*   **Web**: [Markov chain — Convergence and stationary distribution](https://en.wikipedia.org/wiki/Markov_chain#Convergence_speed_and_mixing_time) - *Wikipedia (English)*. Sección "Convergence speed and mixing time": explica el rol de la brecha espectral (distancia entre $\lambda_1 = 1$ y el segundo autovalor de mayor módulo) para determinar la velocidad de convergencia de la cadena.

---

## Verificación Empírica Computacional

Se utilizan `NumPy` y `SymPy` para verificar los tres casos del teorema: decaimiento geométrico para $|\lambda| < 1$ (incluyendo complejos), constancia para $\lambda = 1$, y oscilación persistente para $|\lambda| = 1$, $\lambda \ne 1$.

```python
--8<-- "demostraciones/convergencia_autovalores_complejos_markov.py"
```
