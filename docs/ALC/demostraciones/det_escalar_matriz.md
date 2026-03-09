# Demostración: Determinante de un Escalar por una Matriz

## Interpretación del Enunciado

Dada $A \in \mathbb{R}^{n \times n}$ y un escalar $k \in \mathbb{R}$, demostrar que:

$$
\det(kA) = k^n \cdot \det(A)
$$


Esta propiedad es la razón profunda por la que, al calcular $\det\big((1-\omega)D - \omega U\big)$ en el método SOR, el factor $(1-\omega)$ de la diagonal aparece elevado a la potencia $n$. Es también una consecuencia directa de la **multilinealidad** del determinante respecto a sus filas (o columnas).

---

## Solución Analítica

### Paso 1: Desarrollar la Matriz $kA$ Explícitamente

Multiplicar una matriz $A$ por el escalar $k$ significa multiplicar **cada una de sus entradas** por $k$:

$$
kA = \begin{pmatrix} k\,a_{11} & k\,a_{12} & \cdots & k\,a_{1n} \\ k\,a_{21} & k\,a_{22} & \cdots & k\,a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ k\,a_{n1} & k\,a_{n2} & \cdots & k\,a_{nn} \end{pmatrix}

$$
### Paso 2: Aplicar la Multilinealidad del Determinante (Fila a Fila)

El determinante es una función **multilineal respecto a las filas**: si una fila se multiplica por un escalar $k$, el determinante queda multiplicado por ese mismo $k$.

En $kA$, las $n$ filas de $A$ han sido multiplicadas simultaneamente por $k$. Aplicamos la extracción de escalares **una fila por vez**:

- Extraemos $k$ de la fila 1:

$$
\det(kA) = k \cdot \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ k\,a_{21} & \cdots & k\,a_{2n} \\ \vdots & & \vdots \\ k\,a_{n1} & \cdots & k\,a_{nn} \end{pmatrix}

$$
- Extraemos $k$ de la fila 2:

$$
= k^2 \cdot \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ a_{21} & \cdots & a_{2n} \\ \vdots & & \vdots \\ k\,a_{n1} & \cdots & k\,a_{nn} \end{pmatrix}

$$
- Continuando este proceso hasta la fila $n$, cada una aporta un factor $k$, acumulando exactamente $n$ factores:

$$
\det(kA) = k^n \cdot \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ a_{21} & \cdots & a_{2n} \\ \vdots & & \ddots & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix}

$$
### Conclusión

Una vez extraído el escalar de todas las filas, la matriz remanente es exactamente $A$:

$$
\boxed{\det(kA) = k^n \cdot \det(A)}

$$
Q.E.D.

<Info titulo="Demostración alternativa: Fórmula de Leibniz">

La **fórmula de Leibniz** define el determinante como:

</Info>

$$
\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} a_{i,\sigma(i)}

$$
    donde la suma recorre todas las permutaciones $\sigma$ del conjunto $\{1, \dots, n\}$.

    Al sustituir $kA$ en lugar de $A$, cada entrada $a_{i,\sigma(i)}$ pasa a ser $k\,a_{i,\sigma(i)}$. Como el producto $\prod_{i=1}^{n}$ contiene exactamente $n$ factores, el escalar $k$ aparece $n$ veces:

$$
\det(kA) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} k\,a_{i,\sigma(i)} = k^n \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^{n} a_{i,\sigma(i)} = k^n \cdot \det(A)

$$
    Esta vía es más directa pero requiere conocer la definición combinatoria del determinante.

    Fin de la justificación.

---

## Verificación Empírica Computacional

La identidad se testea numéricamente para múltiples matrices aleatorias y escalares, verificando por `np.isclose` contra el cálculo directo:

```python
"""
Verificación empírica: det(kA) = k^n · det(A)

Se generan matrices A aleatorias de distintos tamaños y se prueba la identidad
para múltiples valores del escalar k.
"""

import numpy as np

rng = np.random.default_rng(seed=7)

SIZES = [1, 2, 3, 4, 5, 8, 10]
ESCALARES = [0, 0.5, 1, -1, 2, -3, 0.1, -0.25]
N_TESTS = 200

fallos = 0

for _ in range(N_TESTS):
    n = rng.choice(SIZES)
    A = rng.uniform(-10, 10, size=(n, n))

    for k in ESCALARES:
        det_kA = np.linalg.det(k * A)
        det_formula = (k ** n) * np.linalg.det(A)

        if not np.isclose(det_kA, det_formula, rtol=1e-9, atol=1e-11):
            fallos += 1
            print(f"[FALLO] n={n}, k={k}")
            print(f"  det(kA)   : {det_kA:.8e}")
            print(f"  k^n·det(A): {det_formula:.8e}")

total = N_TESTS * len(ESCALARES)
print(f"\nResultado: {total - fallos}/{total} casos correctos.")

if fallos == 0:
    print("✓ Verificación exitosa: det(kA) = k^n · det(A) en todos los casos.")
else:
    print(f"✗ {fallos} fallos detectados.")

```
