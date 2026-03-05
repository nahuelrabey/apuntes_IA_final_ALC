# Ejercicio 4: Condicionamiento y Precondicionadores

> **Ejercicio 4.** Sea $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix}$, para $k \in \mathbb{N}, k > 1$.
>
> **a)** Probar que $Cond_\infty(A) \ge k^2$ y que $Cond_2(A) \ge ck^2$ para alguna constante $c$.
>
> **b)** Explicar qué consecuencias tendría un valor de $k$ alto a la hora de resolver un sistema de la forma $Ax = b$. ¿Depende esto de $b$?
>
> **c)** Un mecanismo para mejorar la calidad de las soluciones obtenidas al resolver un sistema es multiplicarlo por un *precondicionador*: se toma una matriz $C$ y se resuelve el sistema $(CA)x = Cb$. Por supuesto, no es obvio cómo elegir $C$ en cada caso. Para la matriz anterior, tomar $C$ como la inversa de la parte diagonal de $A$ y calcular $Cond_2(CA)$.

## Interpretación del Enunciado

Se evalúa la sensibilidad numérica de un sistema lineal cuya matriz $A$ depende paramétricamente de un entero $k$. Se pide acotar el número de condición bajo distintas normas, analizar el impacto de un condicionamiento elevado sobre la solución, y aplicar un precondicionador diagonal para reducirlo.

---

## Solución del Ejercicio

> a) Probar que $Cond_\infty(A) \ge k^2$ y que $Cond_2(A) \ge ck^2$ para alguna constante $c$.

Dada nuestra matriz paramétrica $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix}$, procedemos primero a calcular su número de condición bajo la norma general infinito.

El número de condición de $A$ depende formalmente de la norma:

$$
Con d(A) = \|A\| \cdot \|A^{-1}\|
$$

Recordemos que la norma matricial infinito ($\|A\|_\infty$) es la máxima suma absoluta de los constituyentes de cada fila:

- $\|A\|_\infty = \max \{ 1+1+1, \: 1+1+0, \: |k^2|+0+|k^2| \}$
- $\|A\|_\infty = \max \{ 3, \: 2, \: 2k^2 \}$

Como $k > 1$, se tiene $2k^2 > 3$. Por lo tanto, el término dominante es la tercera fila y $\|A\|_\infty = 2k^2$.

Para obtener una cota de $\|A^{-1}\|_\infty$, se calcula $A^{-1}$ usando la matriz de cofactores:

1. El determinante es $\det(A) = 1(k^2) - 1(k^2) + 1(-k^2) = -k^2$, corroborando que $A$ carece de vectores nulos para $k \neq 0$.

2. Transpuesta de la matriz de cofactores para la posición (1, 1), $C_{11} = 1 \cdot k^2 - 0 \cdot 0 = k^2$. Al dividir esta componente generalizada por el determinante, el primer término pivot es $(A^{-1})_{1,1} = -1$.

??? info "Cálculo del Determinante (Regla de Laplace)"
    El cálculo se realiza mediante el desarrollo por cofactores (o Regla de Laplace) aplicado a la **primera fila** de la matriz $A$:

    $$
    A = \begin{pmatrix} \mathbf{1} & \mathbf{1} & \mathbf{1} \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix}
    $$

    Desglosando el desarrollo por la fila 1:

    -   Para $a_{11}=1$: $\det \begin{pmatrix} 1 & 0 \\ 0 & k^2 \end{pmatrix} = (k^2 - 0) = k^2$.
    -   Para $a_{12}=1$: $\det \begin{pmatrix} 1 & 0 \\ k^2 & k^2 \end{pmatrix} = (k^2 - 0) = k^2$. Por posición impar se resta: $-1(k^2)$.
    -   Para $a_{13}=1$: $\det \begin{pmatrix} 1 & 1 \\ k^2 & 0 \end{pmatrix} = (0 - k^2) = -k^2$.

    $$
    \det(A) = 1(k^2) - 1(k^2) + 1(-k^2) = -k^2
    $$

    Fin de la explicación.

La primera fila exacta de $A^{-1}$ es $(-1, 1, 1/k^2)$. La suma abosluta resultante reciclando esta fila mínima arrojará:

$$
\|A^{-1}\|_\infty \ge \sum |(A^{-1})_{1,j}| = |-1| + |1| + |1/k^2| = 2 + \frac{1}{k^2}
$$

Multiplicando ambas normas se obtiene la cota del número de condición:

$$
Cond_\infty(A) = (2k^2) \cdot \|A^{-1}\|_\infty \ge 2k^2 \cdot (2 + 1/k^2) = 4k^2 + 2
$$

Como $4k^2 + 2 > k^2$ para todo $k > 1$, se concluye que $Cond_\infty(A) \ge k^2$. $\square$

Para la norma-2, se aplica la equivalencia entre normas matriciales en $\mathbb{R}^{n \times n}$:

$$
\frac{1}{n} Cond_\infty(A) \le Cond_2(A) \le n \cdot Cond_\infty(A)
$$

Tomando la cota inferior con $n=3$:

$$
Cond_2(A) \ge \frac{1}{3} Cond_\infty(A) \ge \frac{1}{3} (4k^2 + 2) = \frac{4}{3} k^2 + \frac{2}{3} > \frac{4}{3} k^2
$$

Se cumple $Cond_2(A) \ge ck^2$ con $c = 4/3$. $\square$

---

> b) Explicar qué consecuencias tendría un valor de $k$ alto a la hora de resolver un sistema de la forma $Ax = b$. ¿Depende esto de $b$?

Para $k$ grande (por ejemplo $k=100$), $k^2 = 10000$, y el número de condición crece al menos como $O(k^2)$, lo que da valores superiores a $40000$.

Un condicionamiento elevado implica que pequeñas perturbaciones en $b$ pueden generar errores relativos grandes en $x$, según la cota:

$$
\frac{\|\delta x\|}{\|x\|} \le Cond(A) \frac{\|\delta b\|}{\|b\|}
$$

En la práctica, esto se traduce en pérdida de dígitos significativos al resolver el sistema numéricamente.

**¿Depende esto del vector $b$?**
**Sí**, pero solo en el sentido del peor caso. El número de condición acota el error relativo máximo posible sobre todas las perturbaciones $\delta b$. Si la perturbación real tiene una dirección alineada con el vector singular asociado al valor singular máximo, el error en $x$ será del orden de $Cond(A) \cdot \|\delta b\| / \|b\|$. Si la perturbación recae sobre direcciones de valores singulares pequeños, el error efectivo puede ser mucho menor.

---

> c) Para la matriz anterior, tomar $C$ como la inversa de la parte diagonal de $A$ y calcular $Cond_2(CA)$.

El precondicionador diagonal de Jacobi se define como la inversa de la matriz diagonal de $A$:

$$
Diag(A) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & k^2 \end{pmatrix} \implies C = Diag(A)^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/k^2 \end{pmatrix}
$$

La matriz precondicionada $CA$ resulta:

$$
CA = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/k^2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ \frac{k^2}{k^2} & 0 & \frac{k^2}{k^2} \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}
$$

El precondicionamiento elimina la dependencia en $k$: la matriz resultante solo contiene entradas $0$ y $1$, con número de condición $Cond_2(CA) \approx 6.85$ (constante, independiente de $k$). Esto indica que el sistema precondicionado está bien condicionado para cualquier valor de $k$.

---

--8<-- "docs/Examen_2025_08_07/04_numero_condicion/verificacion.py"
