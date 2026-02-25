# Ejercicio 1: Proyectores y Subespacios

> **Ejercicio 1.** Sea $A = \begin{pmatrix} -1 & 1 & 0 & 1 \\ 1 & -1 & -1 & -2 \\ 1 & -1 & 0 & -1 \\ 1 & -1 & 1 & 0 \end{pmatrix}$ y $f: \mathbb{R}^4 \to \mathbb{R}^4$ definida por $f(x) = Ax$.
>
> **a)** Definir un proyector $p:\mathbb{R}^4 \to \mathbb{R}^4$ tal que $Im(p) = Im(f)$ y $Nu(p) = Nu(f)$.
>
> **b)** Decidir si $p$ es un proyector ortogonal. ¿Es $p$ idéntico a $f$?
>
> **c)** Hallar una base $B$ tal que la matriz de $p$ en $B$ sea diagonal.

## Interpretación del Enunciado

Se nos da una matriz $A \in \mathbb{R}^{4 \times 4}$ que define una transformación lineal $f(x) = Ax$. El ejercicio pide en tres incisos construir un proyector $p$ adaptado a los subespacios fundamentales de $f$, deducir sus propiedades métricas (si es ortogonal) e identificar cuándo coincide con $f$, para finalmente diagonalizarlo.

---

> a) Definir un proyector $p:\mathbb{R}^4 \to \mathbb{R}^4$ tal que $Im(p) = Im(f)$ y $Nu(p) = Nu(f)$.

## Solución del Inciso (a)

Para construir dicho proyector $p$, necesitamos conocer explícitamente bases para la imagen ($Im(f)$) y el núcleo ($Nu(f)$) de nuestra transformación lineal.

Comenzamos escalonando la matriz $A$ para hallar su forma reducida por filas y determinar los pivotes:

$$
A \sim \begin{pmatrix} 1 & -1 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

De las columnas pivotales (primera y tercera), deducimos una base $B_{Im}$ para la imagen $Im(f) = Col(A)$:

??? info "Observación Teórica: Independencia Lineal"
    Esto lo podemos hacer porque la primer y tercer columnas de la escalonada contienen a los pivotes (escalones principales no nulos), lo que garantiza algebraicamente que las columnas originales interrelacionadas en la matriz $A$ inicial son Linealmente Independientes (LI). 
    
    **(La demostración analítica de este teorema se encuentra documentada en [Independencia Lineal de las Columnas Pivotales](../../demostraciones/independencia_pivotes.md)).**

$$
B_{Im} = \left\{ \begin{pmatrix} -1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 0 \\ 1 \end{pmatrix} \right\}
$$

De las variables libres ($x_2$ y $x_4$), derivamos las ecuaciones del núcleo $Nu(f)$.

??? info "Observación Teórica: ¿Cómo derivamos estas ecuaciones rref?"
    Las ecuaciones surgen de traducir directamente las filas no nulas de la matriz escalonada reducida por filas (la forma RREF obtenida arriba) de vuelta a un sistema homogéneo ($Ax = 0$).

    - La **primera fila** $(1, -1, 0, -1)$ representa la ecuación: $1 \cdot x_1 + (-1) \cdot x_2 + 0 \cdot x_3 + (-1) \cdot x_4 = 0 \implies x_1 - x_2 - x_4 = 0$.
    
    - La **segunda fila** $(0, 0, 1, 1)$ representa la ecuación: $0 \cdot x_1 + 0 \cdot x_2 + 1 \cdot x_3 + 1 \cdot x_4 = 0 \implies x_3 + x_4 = 0$.

Expresado paramétricamente de acuerdo a las variables libres, despejamos con $x_1 = x_2 + x_4$ y $x_3 = -x_4$. Por lo que obtenemos una base $B_{Nu}$:

$$
B_{Nu} = \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \\ 1 \end{pmatrix} \right\}
$$

Para que la transformación $p$ sea un proyector definido de esta forma, y dado que queremos proyectar sobre $Im(f)$ a lo largo de $Nu(f)$, debe cumplirse que $\mathbb{R}^4 = Im(f) \oplus Nu(f)$ (suma directa). Verificamos que la unión de las bases forma un conjunto linealmente independiente evaluando el determinante de la matriz ensamblada $B = [B_{Im} \mid B_{Nu}]$:

$$
\det(B) = \det \begin{pmatrix} -1 & 0 & 1 & 1 \\ 1 & -1 & 1 & 0 \\ 1 & 0 & 0 & -1 \\ 1 & 1 & 0 & 1 \end{pmatrix} = 3 \neq 0
$$

La intersección es trivial, la suma directa existe, y por lo tanto podemos definir $p(x)$ unívocamente dictando su acción sobre nuestra nueva base:

- $\forall v \in Im(f): p(v) = v$
- $\forall n \in Nu(f): p(n) = 0$

Así, definimos $p$ explícitamente a través de su matriz asociada $P$ en la base canónica como $P = B D B^{-1}$, siendo $D$ la matriz diagonal con los autovalores asignados:

$$
D = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

Resolviendo el producto de matrices, la matriz del proyector resulta:

$$
P = \begin{pmatrix}
-1.33 & 1.33 & 0 & -2.33 \\
0.66 & 0.33 & 0 & 1.66 \\
0.33 & -0.33 & 1 & 0.66 \\
0.33 & -0.33 & 0 & 1.66
\end{pmatrix}
$$

*(Nota: Valores decimales expresados de forma compacta para legibilidad, el resultado exacto usa fracciones periódicas).*

---

> b) Decidir si $p$ es un proyector ortogonal. ¿Es $p$ idéntico a $f$?

## Solución del Inciso (b)

Para que un proyector $p$ sea proyectado **ortogonal** sobre un subespacio, el núcleo del proyector debe ser el complemento ortogonal de su imagen: $Nu(p) = Im(p)^\perp$. Esto se verifica analíticamente comprobando si la matriz del proyector $P$ en la base canónica es simétrica: $P = P^T$.

Observando la matriz $P$ obtenida en el inciso a), claramente $P \neq P^T$ (por ejemplo, $P_{1,2} = 1.33 \neq P_{2,1} = 0.66$). Por lo tanto, **$p$ no es un proyector ortogonal**; es un proyector oblicuo.

De manera alternativa, podíamos verificarlo tomando vectores de ambas bases calculadas y haciendo el producto interno. Si tomamos $v_1 \in Im(f)$ y $n_1 \in Nu(f)$:

$$
\langle v_1, n_1 \rangle = (-1)(1) + (1)(1) + (1)(0) + (1)(0) = 0
$$

Sin embargo, basta probar con otro par:

$$
\langle v_2, n_1 \rangle = (0)(1) + (-1)(1) + (0)(0) + (1)(0) = -1 \neq 0
$$

Esto demuestra que $Nu(f)$ no es perpendicular a $Im(f)$.

¿Es $p$ idéntico a $f$?
Para que $p(x) = f(x) \;\forall x$, debería ocurrir que la matriz $P$ sea idéntica a $A$. A simple vista de las matrices, vemos que $P \neq A$. Otra forma de verlo es analizando la restricción sobre la imagen: si $p \equiv f$, deberíamos tener $f(v) = v$ para todo $v \in Im(f)$.
Evaluamos la transformación $f$ en $v_1$:

$$
f(v_1) = A v_1 = \begin{pmatrix} 3 \\ -5 \\ -3 \\ -1 \end{pmatrix} \neq v_1
$$

Con esto, demostramos que **$p$ no es idéntico a $f$**. $A$ no actuaba operativamente como la identidad en su propio subespacio imagen.

---

> c) Hallar una base $B$ tal que la matriz de $p$ en $B$ sea diagonal.

## Solución del Inciso (c)

Esta respuesta la construimos inherentemente en la resolución del inciso a). Todo proyector $p$ cuyas restricciones son la suma directa iterativa de su propia imagen y núcleo ($Im \oplus Nu = \mathbb{R}^n$) es naturalmente diagonalizable, teniendo como autovalores a 1 (con multiplicidad algebraica igual a la dimensión de su imagen) y a 0 (con multiplicidad idéntica a la nulidad).

La matriz diagonal $D_{p}$ la obtenemos usando una matriz de paso $B$ cuyas columnas sean las bases combinadas en orden de los autovalores:

$$
B_{diag} = \left\{ \underbrace{\begin{pmatrix} -1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 0 \\ 1 \end{pmatrix}}_{\text{Autovalor } \lambda=1}, \underbrace{\begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \\ 1 \end{pmatrix}}_{\text{Autovalor } \lambda=0} \right\}
$$

Con respecto a esta base $B_{diag}$, la matriz de $p$ es, en efecto, la matriz diagonal construida anteriormente:

$$
[P]_B = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

---

--8<-- "docs/Examen_2025_08_07/01_proyector/verificacion.py"
