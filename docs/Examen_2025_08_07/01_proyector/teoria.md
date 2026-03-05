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

??? info "¿Qué es un Proyector? (Definición Conceptual)"
    En álgebra lineal, un **proyector** es una transformación lineal $p: V \to V$ que es **idempotente**, lo que significa que aplicar la transformación dos veces es lo mismo que aplicarla una sola vez: $p \circ p = p$ (o en términos de matrices, $P^2 = P$).

    Conceptualmente, un proyector "descompone" el espacio en dos partes:

    -   **La Imagen ($Im(p)$)**: Es el subespacio "hacia donde" proyectamos. Si un vector ya está aquí, el proyector lo deja idéntico.
    -   **El Núcleo ($Nu(p)$)**: Es el subespacio "a lo largo del cual" proyectamos. Todo lo que esté aquí se colapsa al vector nulo.

    Cualquier vector del espacio se puede escribir como una suma de un vector en la imagen y uno en el núcleo. El proyector simplemente "se queda" con la parte que pertenece a la imagen y "descarta" la parte del núcleo.

Comenzamos escalonando la matriz $A$ para hallar su forma reducida por filas y determinar los pivotes:

$$
A \sim \begin{pmatrix} 1 & -1 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$


??? info "¿Por qué las Columnas Pivotales?"
    Las operaciones elementales de fila aplicadas para llegar a la RREF (Escalonada Reducida) preservan las **relaciones de dependencia lineal** entre las columnas.

    Si las columnas 1 y 3 son pivotales en la RREF, significa que son linealmente independientes y que las demás columnas pueden expresarse como combinación lineal de ellas. Debido a que la estructura se mantiene, las columnas 1 y 3 de la matriz **original** $A$ también son linealmente independientes y generan el mismo espacio (la Imagen).

De las columnas pivotales (primera y tercera), deducimos una base $B_{Im}$ para la imagen $Im(f) = Col(A)$:

$$
B_{Im} = \left\{ \begin{pmatrix} -1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ -1 \\ 0 \\ 1 \end{pmatrix} \right\}
$$

De las variables libres ($x_2$ y $x_4$), derivamos las ecuaciones del núcleo $Nu(f)$.

??? info "¿Por qué las Variables Libres?"
    El Núcleo consiste en todos los vectores $x$ tales que $Ax = 0$. Al escalonar la matriz, estamos simplificando este sistema de ecuaciones sin cambiar su conjunto solución.

    Las **variables libres** representan los grados de libertad del sistema. Cada variable libre nos permite construir un vector independiente en el Núcleo (asignándole el valor 1 y 0 a las demás libres). La cantidad de variables libres coincide exactamente con la **nulidad** de la transformación (por el Teorema de la Dimensión).

??? info "Observación Teórica: ¿Cómo derivamos estas ecuaciones rref?"
    Las ecuaciones surgen de traducir directamente las filas no nulas de la matriz escalonada reducida por filas (la forma RREF obtenida arriba) de vuelta a un sistema homogéneo ($Ax = 0$).

    - La **primera fila** $(1, -1, 0, -1)$ representa la ecuación: $1 \cdot x_1 + (-1) \cdot x_2 + 0 \cdot x_3 + (-1) \cdot x_4 = 0 \implies x_1 - x_2 - x_4 = 0$.

    - La **segunda fila** $(0, 0, 1, 1)$ representa la ecuación: $0 \cdot x_1 + 0 \cdot x_2 + 1 \cdot x_3 + 1 \cdot x_4 = 0 \implies x_3 + x_4 = 0$.

Expresado paramétricamente de acuerdo a las variables libres, despejamos con $x_1 = x_2 + x_4$ y $x_3 = -x_4$. Por lo que obtenemos una base $B_{Nu}$:

$$
B_{Nu} = \left\{ \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \\ 1 \end{pmatrix} \right\}
$$

Para que la transformación $p$ sea un proyector definido de esta forma, y dado que queremos proyectar sobre $Im(f)$ a lo largo de $Nu(f)$, debe cumplirse que $\mathbb{R}^4 = Im(f) \oplus Nu(f)$ (suma directa).

??? info "¿Por qué se requiere la Suma Directa ($\oplus$)??"
    Para que este proyector $p$ sea una función bien definida para **cualquier** vector $x$, necesitamos poder descomponerlo de forma **única** como:

    $$
    x = \underbrace{s}_{s \in Im(f)} + \underbrace{n}_{n \in Nu(f)}
    $$

    Donde la acción del proyector es simplemente filtrar la componente de la imagen: $p(x) = s$.

    Para que esa descomposición exista y sea unívoca para todo el espacio, se deben cumplir dos pilares algebraicos:

    1.  **Cobertura Total**: $Im(f) + Nu(f) = \mathbb{R}^4$ (la suma de los subespacios genera todo el espacio).
    2.  **Intersección Trivial**: $Im(f) \cap Nu(f) = \{0\}$ (no hay solapamiento de información entre ellos).

    La unión de estas condiciones define la **Suma Directa**.

Evaluamos la independencia lineal de la unión de las bases mediante el determinante de la matriz ensamblada $B = [B_{Im} \mid B_{Nu}]$ para certificar esto:

$$
\det(B) = \det \begin{pmatrix} -1 & 0 & 1 & 1 \\ 1 & -1 & 1 & 0 \\ 1 & 0 & 0 & -1 \\ 1 & 1 & 0 & 1 \end{pmatrix} = 3 \neq 0
$$

La intersección es trivial, la suma directa existe, y por lo tanto podemos definir $p(x)$ unívocamente dictando su acción sobre nuestra nueva base:

- $\forall v \in Im(f): p(v) = v$
- $\forall n \in Nu(f): p(n) = 0$

$$
D = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}
$$

??? info "¿Por qué esta técnica construye el proyector buscado?"
    Esta construcción se basa en el **Teorema de Descomposición por Autovalores**. Un proyector $p$ queda unívocamente determinado por su acción sobre una base que descompone al espacio en $Im(p) \oplus Nu(p)$:

    - Si $v \in Im(p) \implies p(v) = 1 \cdot v$.
    - Si $n \in Nu(p) \implies p(n) = 0 \cdot n$.

    Al armar la matriz $B = [B_{Im} \mid B_{Nu}]$ y la matriz diagonal $D$ con 1s (para la imagen) y 0s (para el núcleo), la expresión $P = B D B^{-1}$ realiza tres pasos lógicamente:

    -   **$B^{-1}$**: Cambia el vector de la base canónica a nuestra base adaptada $B$.
    -   **$D$**: Aplica la proyección (mantiene componentes de la imagen, anula componentes del núcleo).
    -   **$B$**: Devuelve el vector resultante a la base canónica.

    **(La justificación analítica de este cambio de base se encuentra documentada en [Cambio de Base: Matrices $B$ y $B^{-1}$](../../demostraciones/cambio_base.md)).**

??? check "Demostración de Idempotencia ($P^2 = P$)"
    Para certificar que $P$ es efectivamente un proyector, debemos demostrar que es **idempotente**:

    $$
    P^2 = (B D B^{-1}) (B D B^{-1}) = B D (B^{-1} B) D B^{-1} = B (D \cdot D) B^{-1} = B D^2 B^{-1}
    $$

    Como $D$ es una matriz diagonal cuyos elementos son solo $0$ o $1$, y dado que $0^2 = 0$ y $1^2 = 1$, se cumple que $D^2 = D$. Por lo tanto:

    $$
    P^2 = B D B^{-1} = P
    $$

    **Q.E.D.**

Resolviendo el producto de matrices, la matriz del proyector resulta:

$$
P = \begin{pmatrix}
0.333 & -0.333 & 0 & -0.333 \\
-1.0 & 1.0 & -1.0 & 0 \\
-0.333 & 0.333 & 0 & 0.333 \\
0.333 & -0.333 & 1.0 & 0.667
\end{pmatrix}
$$

*(Nota: Valores decimales expresados de forma compacta para legibilidad, el resultado exacto usa fracciones periódicas).*

---

> b) Decidir si $p$ es un proyector ortogonal. ¿Es $p$ idéntico a $f$?

## Solución del Inciso (b)

??? info "¿Qué es un Proyector Ortogonal?"
    Un proyector $p$ sobre un subespacio $S$ es **ortogonal** si proyecta los vectores de forma perpendicular al subespacio imagen. Geométricamente, esto significa que la dirección de proyección (el núcleo) es perpendicular a la imagen:

    $$
    Nu(p) = Im(p)^\perp
    $$

    En términos matriciales (en base canónica), un proyector es ortogonal **si y solo si su matriz asociada $P$ es simétrica** ($P = P^T$). Si el proyector es idempotente pero no simétrico, se denomina proyector **oblicuo**.

Para que un proyector $p$ sea proyectado **ortogonal** sobre un subespacio, el núcleo del proyector debe ser el complemento ortogonal de su imagen: $Nu(p) = Im(p)^\perp$. Esto se verifica analíticamente comprobando si la matriz del proyector $P$ en la base canónica es simétrica: $P = P^T$.

**(La demostración formal de por qué la simetría implica ortogonalidad se encuentra en [Simetría y Ortogonalidad de Proyectores](../../demostraciones/proyector_simetria_ortogonalidad.md)).**

Observando la matriz $P$ obtenida en el inciso a), claramente $P \neq P^T$ (por ejemplo, $P_{1,2} = -0.333 \neq P_{2,1} = -1.0$). Por lo tanto, **$p$ no es un proyector ortogonal**; es un proyector oblicuo.

De manera alternativa, podíamos verificarlo tomando vectores de ambas bases calculadas y haciendo el producto interno. Si tomamos $v_1 \in Im(f)$ y $n_1 \in Nu(f)$:

$$
\langle v_1, n_1 \rangle = (-1)(1) + (1)(1) + (1)(0) + (1)(0) = 0
$$

Sin embargo, basta probar con otro par:

$$
\langle v_2, n_1 \rangle = (0)(1) + (-1)(1) + (0)(0) + (1)(0) = -1 \neq 0
$$

Esto demuestra que $Nu(f)$ no es perpendicular a $Im(f)$.

??? info "¿Por qué un solo producto no nulo invalida la ortogonalidad?"
    Para que dos subespacios sean perpendiculares ($S \perp W$), **todos** los vectores de $S$ deben ser ortogonales a **todos** los vectores de $W$.

    Si encontramos aunque sea un par de vectores (uno de cada subespacio) cuyo producto interno sea distinto de cero, hemos hallado un **contraejemplo** que rompe la condición de perpendicularidad global. En este caso, aunque $\langle v_1, n_1 \rangle = 0$, el hecho de que $\langle v_2, n_1 \rangle = -1$ es suficiente para asegurar que los subespacios no están a 90 grados entre sí.

¿Es $p$ idéntico a $f$?
Para que $p(x) = f(x) \;\forall x$, debería ocurrir que la matriz $P$ sea idéntica a $A$. A simple vista de las matrices, vemos que $P \neq A$. Otra forma de verlo es analizando la restricción sobre la imagen: si $p \equiv f$, deberíamos tener $f(v) = v$ para todo $v \in Im(f)$.
Evaluamos la transformación $f$ en $v_1$:

$$
f(v_1) = A v_1 = \begin{pmatrix} 3 \\ -5 \\ -3 \\ -1 \end{pmatrix} \neq v_1
$$

??? info "¿Por qué esta desigualdad demuestra que $p \neq f$?"
    El razonamiento es una **demostración por contradicción**:

    1.  **Propiedad del Proyector**: Por definición, un proyector $p$ actúa como la identidad sobre su imagen. Es decir, si $v \in Im(p)$, entonces $p(v) = v$.
    2.  **Igualdad de Imágenes**: Nosotros definimos $p$ tal que $Im(p) = Im(f)$. Por lo tanto, para cualquier vector $v \in Im(f)$, se debe cumplir que $p(v) = v$.
    3.  **Hipótesis**: Si $f$ fuera idéntico a $p$ ($f \equiv p$), entonces $f$ debería cumplir la misma propiedad: $f(v) = v$ para todo vector en su imagen.

    Al comprobar que para el vector $v_1$, la transformación $f(v_1)$ devuelve algo distinto a $v_1$, demostramos que $f$ **no es la identidad en su propia imagen**. Como un proyector *debe* ser la identidad en su imagen, entonces $f$ no puede ser ese proyector.

Con esto, demostramos que **$p$ no es idéntico a $f$**. $A$ no actuaba operativamente como la identidad en su propio subespacio imagen.

---

> c) Hallar una base $B$ tal que la matriz de $p$ en $B$ sea diagonal.

## Solución del Inciso (c)

??? info "¿Qué significa que la matriz sea diagonal en una base $B$?"
    En álgebra lineal, decir que una matriz es diagonal en una base determinada significa que todos los vectores de esa base son **autovectores** de la transformación.

    Para un proyector $p$, esto es especialmente sencillo ya que solo existen dos autovalores posibles:

    - **$\lambda = 1$**: Para cualquier vector que pertenezca a la Imagen ($Im(p)$).
    - **$\lambda = 0$**: Para cualquier vector que pertenezca al Núcleo ($Nu(p)$).

    Por lo tanto, "hallar una base $B$ tal que la matriz sea diagonal" consiste simplemente en ensamblar una base del espacio total utilizando vectores de la imagen y vectores del núcleo. Decimos entonces que la matriz del proyector $P$ es **semejante** a la matriz diagonal $D$ ($P = BDB^{-1}$), lo que significa que ambas representan la misma transformación pero expresadas en sistemas de coordenadas distintos.

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
