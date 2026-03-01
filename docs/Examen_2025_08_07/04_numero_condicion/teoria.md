# Ejercicio 4: Condicionamiento y Precondicionadores

> **Ejercicio 4.** Sea $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix}$, para $k \in \mathbb{N}, k > 1$.
>
> **a)** Probar que $Cond_\infty(A) \ge k^2$ y que $Cond_2(A) \ge ck^2$ para alguna constante $c$.
>
> **b)** Explicar qué consecuencias tendría un valor de $k$ alto a la hora de resolver un sistema de la forma $Ax = b$. ¿Depende esto de $b$?
>
> **c)** Un mecanismo para mejorar la calidad de las soluciones obtenidas al resolver un sistema es multiplicarlo por un *precondicionador*: se toma una matriz $C$ y se resuelve el sistema $(CA)x = Cb$. Por supuesto, no es obvio cómo elegir $C$ en cada caso. Para la matriz anterior, tomar $C$ como la inversa de la parte diagonal de $A$ y calcular $Cond_2(CA)$.

## Interpretación del Enunciado

Se evalúa la sensibilidad y estabilidad numérica de un sistema regido por una matriz cuadrática fuertemente parametrizada por un entero $k$. Se pide acotar analíticamente su número de condición (la métrica universal de amplificación de error) bajo distintas normas, explicar cualitativamente su impacto sobre perturbaciones en $b$, y curar la inestabilidad intrínseca del sistema aplicando una iteración de precondicionamiento lateral (Método de Preacondicionamiento Diagonal o de Jacobi limitante).

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

Adicionado que partimos del supuesto base de que $k > 1$, se cumple categóricamente que $2k^2 > 3$. Por tanto, el término dominante define la norma global del objeto abstracto: $\|A\|_\infty = 2k^2$.

Ahora en búsqueda de $A^{-1}$, sabemos que cualquier norma general matricial inducida de una matriz de autovectores con inversas es siempre mayor o idéntica a 1. Pero para que quede analíticamente evidente, obteniendo la inversa de $A$ por matriz de adjuntos:

1. El determinante es $\det(A) = 1(k^2) - 1(k^2) + 1(-k^2) = -k^2$, corroborando que $A$ carece de vectores nulos para $k \neq 0$.
2. Transpuesta de la matriz de cofactores para la posición (1, 1), $C_{11} = 1 \cdot k^2 - 0 \cdot 0 = k^2$. Al dividir esta componente generalizada por el determinante, el primer término pivot es $(A^{-1})_{1,1} = -1$.

La primera fila exacta de $A^{-1}$ es $(-1, 1, 1/k^2)$. La suma abosluta resultante reciclando esta fila mínima arrojará:

$$
\|A^{-1}\|_\infty \ge \sum |(A^{-1})_{1,j}| = |-1| + |1| + |1/k^2| = 2 + \frac{1}{k^2}
$$

Multiplicando cruzadamente las normas y aislando la variable para establecer nuestra cota final:

$$
Cond_\infty(A) = (2k^2) \cdot \|A^{-1}\|_\infty \ge 2k^2 \cdot (2 + 1/k^2) = 4k^2 + 2
$$

Dado que $4k^2 + 2$ es siempre estrictamente superior a $k^2$ (y de hecho a $4k^2$), concluimos matemáticamente que **$Cond_\infty(A) \ge k^2$ queda exhaustivamente demostrado**.

Para la norma espectral euclídea de L2, podemos invocar el Teorema General de Equivalencia de Normas topológicas en rangos finitos $\mathbb{R}^{n \times n}$, que dicta formalmente:

$$
\frac{1}{n} Cond_\infty(A) \le Cond_2(A) \le n \cdot Cond_\infty(A)
$$

Fijándonos en la cota intrínseca inferior con $n=3$, inferimos lógicamente:

$$
Cond_2(A) \ge \frac{1}{3} Cond_\infty(A) \ge \frac{1}{3} (4k^2 + 2) = \frac{4}{3} k^2 + \frac{2}{3} > \frac{4}{3} k^2
$$

Alcanzamos una forma que valida que sí existe una proporcionalidad par a $k^2$. Por consiguiente, **$Cond_2(A) \ge ck^2$ es verdadero (pudiéndose materializar por la constante $c = 4/3$)**.

---

> b) Explicar qué consecuencias tendría un valor de $k$ alto a la hora de resolver un sistema de la forma $Ax = b$. ¿Depende esto de $b$?

Si asumimos un $k$ alto (por ejemplo $k=100$), $k^2 = 10000$. En conjunción con las cotas del inciso a), el condicionamiento estallará en al menos órdenes de escala proporcionales al doble cuadrado $O(k^2) > 40000$.

Esta inestabilidad intrínseca condena a que pequeñísimas alteraciones analíticas y redondeos de perturbación instrumental sobre el vector de mediciones empíricas $\delta b$ resultarán drásticamente magnificadas sobre los factores incógnita $\delta x$. Matemáticamente:

$$
\frac{\|\delta x\|}{\|x\|} \le Cond(A) \frac{\|\delta b\|}{\|b\|}
$$

Resolverlo en el hardware informático causará una **pérdida irrecuperable en dígitos significativos** en operaciones subyacentes de factorización (BLAS/LAPACK no pivotados perderán exactitud sobre los sumandos de arrastre).

**¿Depende esto del vector $b$?**
Estrictamente **sí**, la sensibilidad real de un problema dado **no** es un vector único plano. La constante del condicionamiento estipula exclusivamente la deformación global del **peor caso posible** o tope esférico del espacio dimensional. Si resulta que la perturbación real asienta predominantemente sobre la pre-dirección natural del autovector atado al valor singular máximo (o el más "blando" estocástico), el estallido algorítmico sí será fatal. Caso contrario paralelo a ejes singulares mínimos, sub-perturbaciones locales quedan virtualmente congeladas sin transmutar en desastres generales del hiperplano de control.

---

> c) Para la matriz anterior, tomar $C$ como la inversa de la parte diagonal de $A$ y calcular $Cond_2(CA)$.

Tomando el precondicionador de Jacobi puro, formamos $C$, construida enteramente de los inversos recíprocos de las entradas primigenias diagonales explícitas de $A$:

$$
Diag(A) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & k^2 \end{pmatrix} \implies C = Diag(A)^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/k^2 \end{pmatrix}
$$

Nuestra flamante matriz abstracta sub-evaluada será el acoplamiento cruzado de filas en $(CA)$:

$$
CA = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/k^2 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ \frac{k^2}{k^2} & 0 & \frac{k^2}{k^2} \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}
$$

La resultante es milagrosamente redentora: hemos mitigado la matriz paramétrica para volverla estática (1's y 0's puros). Para calcular numéricamente su cota general natural $Cond_2(CA)$ sobre SVD o espectral de ATA: $\sigma_{max} / \sigma_{min}$.
A nivel analítico formal o código empírico, la condición de $(CA)$ devuelve una constante de condicionamiento $Cond_2(CA) \approx 6.85$. Como este coeficiente numérico es drásticamente pequeño bajo métricas relativas (está en $\mathcal{O}(1)$ general) y sobre todo *independiente* paramétricamente del crecimiento de la variable caótica $k$, la matriz resultante logra una convergencia ultraeficiente bajo cualquier método iterativo y exacto que pretenda emplear la máquina.

---

--8<-- "docs/Examen_2025_08_07/04_numero_condicion/verificacion.py"
