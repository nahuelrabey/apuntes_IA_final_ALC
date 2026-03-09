# Cambio de Base: Matrices $B$ y $B^{-1}$

> **Demostración.** Dada una base $B = \{v_1, v_2, \dots, v_n\}$ de un espacio vectorial $V$, demostrar que la matriz $B$ (cuyas columnas son los vectores de la base) transforma coordenadas en base $B$ a la base canónica, y que su inversa $B^{-1}$ realiza la transformación opuesta.

## Interpretación del Enunciado

El objetivo es formalizar la relación entre un vector $x$ expresado en la base canónica y sus coordenadas $[x]_B$ respecto a una base arbitraria $B$. Esta distinción es fundamental para entender operaciones como la diagonalización o la construcción de proyectores oblicuos, donde "filtramos" componentes en direcciones específicas.

---

## Solución Analítica

### 1. La Matriz de Paso $B$ (de Base $B$ a Canónica)

Sea un vector $x \in V$. Por definición de base, $x$ se puede escribir de forma única como una combinación lineal de los vectores de $B$:

$$
x = c_1 v_1 + c_2 v_2 + \dots + c_n v_n
$$

Donde los escalares $c_i$ son las coordenadas de $x$ en la base $B$, denotadas como:

$$
[x]_B = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}
$$

Si disponemos los vectores $v_i$ como columnas de una matriz $B = [v_1 | v_2 | \dots | v_n]$, la combinación lineal anterior se traduce exactamente en el producto matriz-vector:

$$
x = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \dots & v_n \\ | & | & & | \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} = B [x]_B
$$

Por lo tanto, **la matriz $B$ toma un vector de coordenadas $[x]_B$ y devuelve el vector $x$ en la base canónica**.

### 2. La Matriz Inversa $B^{-1}$ (de Canónica a Base $B$)

Puesto que los vectores $\{v_1, \dots, v_n\}$ forman una base, son linealmente independientes. Esto garantiza que la matriz $B$ es cuadrada y de rango completo, por lo tanto, es **invertible**.

Si multiplicamos a izquierda por $B^{-1}$ en la ecuación anterior:

$$
B^{-1} x = B^{-1} (B [x]_B)
$$

$$
B^{-1} x = (B^{-1} B) [x]_B
$$

$$
B^{-1} x = I [x]_B = [x]_B
$$

Esto demuestra que **la matriz $B^{-1}$ toma un vector en la base canónica y devuelve sus coordenadas en la base $B$**.

??? info "Conclusión Táctica"
    En la construcción de un proyector $P = B D B^{-1}$, el orden de aplicación (de derecha a izquierda) es:

    1.  **$B^{-1}$**: Lleva el vector al "espacio de la base $B$".
    2.  **$D$**: Opera sobre sus componentes (proyecta).
    3.  **$B$**: Devuelve el resultado al sistema de coordenadas estándar (canónico).

    Fin de la conclusión.

---

--8<-- "docs/demostraciones/verificacion_cambio_base.py"
