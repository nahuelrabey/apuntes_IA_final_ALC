# Solución del Ejercicio 4 (Examen 21 de julio de 2025 - Bases Ortonormales y Cuadrados Mínimos)

<Enunciado titulo="Ejercicio 4.">

Sea $\{q_1, q_2, q_3, q_4, q_5\}$ una base ortonormal de $\mathbb{R}^5$, $A$ una matriz de $5 \times 3$ con columnas $q_1, q_2, q_3$ y el vector $b = q_1 + 2q_2 + 3q_3 + 4q_4 + 5q_5$.

a) Mostrar que el sistema $Ax = b$ no tiene solución. Plantear las ecuaciones normales y hallar la solución $\hat{x}$ de cuadrados mínimos para dicho sistema.

b) Calcular el error cometido en la aproximación.

c) Mostrar que $A^\dagger = A^t$, siendo $A^\dagger$ la pseudoinversa de $A$.

</Enunciado>


---

## Solución Inciso A

Definimos a la matriz $A$ por sus propios vectores columna ortonormales:

$$
A = \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix}

$$
Cualquier vector $v \in Col(A)$ se expresa como combinación lineal de las columnas de $A$: $\{q_1, q_2, q_3\}$.

$$
A x = x_1 q_1 + x_2 q_2 + x_3 q_3

$$
Sin embargo, el vector independiente suministrado ($b$) fue definido a partir de la base ortonormal completa del espacio:

$$
b = 1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5

$$
Como los cinco vectores forman una base, son **linealmente independientes**: las componentes en $q_4$ y $q_5$ no pueden generarse a partir de $\{q_1, q_2, q_3\}$. Por lo tanto $b \notin Col(A)$, y **el sistema $Ax = b$ no tiene solución**.

Se busca entonces el vector $\hat{x}$ que minimice el residuo $||Ax - b||$. Esto conduce a la ecuación normal:

$$
A^t A \hat{x} = A^t b

$$
Calculamos $A^t A$ (la matriz de Gram):

$$
A^t A = \begin{pmatrix} - & q_1^t & - \\ - & q_2^t & - \\ - & q_3^t & - \end{pmatrix} \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix} = \begin{pmatrix} q_1^t q_1 & q_1^t q_2 & q_1^t q_3 \\ q_2^t q_1 & q_2^t q_2 & q_2^t q_3 \\ q_3^t q_1 & q_3^t q_2 & q_3^t q_3 \end{pmatrix}

$$
Como $\{q_1, q_2, q_3, q_4, q_5\}$ es una **base ortonormal**, se tiene $q_i^t q_j = \delta_{ij}$. Por lo tanto:

<Info titulo="Observación Teórica: ¿Por qué vale $q_i^t q_j = \delta_{ij}$?">

El término $q_i^t q_j$ es el **producto interno** entre los vectores $q_i$ y $q_j$. El resultado $\delta_{ij}$ (delta de Kronecker) unifica dos propiedades que define una base ortonormal:

- **Norma unitaria**: cada vector tiene longitud 1, por lo que $q_i^t q_i = \|q_i\|_2^2 = 1$.
- **Ortogonalidad**: vectores distintos son perpendiculares, por lo que $q_i^t q_j = 0$ para $i \neq j$.

En forma compacta:

</Info>

$$
    \delta_{ij} = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}

$$
    Fin de la observación.

$$
A^t A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3

$$
Donde $I_3$ es la matriz Identidad en $\mathbb{R}^{3 \times 3}$.

Calculamos ahora $A^t b$:

$$
A^t b = \begin{pmatrix} - & q_1^t & - \\ - & q_2^t & - \\ - & q_3^t & - \end{pmatrix} (1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5)

$$
Por ortonormalidad, cada fila de $A^t$ extrae únicamente el coeficiente del vector correspondiente. Los términos en $q_4$ y $q_5$ se anulan. El resultado es:

$$
A^t b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}

$$
Sustituyendo en la ecuación normal:

$$
I_3 \hat{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}

$$
Por lo tanto:
**$\hat{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$**

---

## Solución Inciso B

La proyección ortogonal $p$ obtenida por la solución $\hat{x}$ es:

$$
p = A \hat{x} = \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 1 q_1 + 2 q_2 + 3 q_3

$$
El vector de error es:

$$
e = b - p

$$
$$
e = (1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5) - (1 q_1 + 2 q_2 + 3 q_3)

$$
Cancelando los términos comunes:

$$
e = 4 q_4 + 5 q_5

$$
Como $q_4$ y $q_5$ son ortogonales, por el teorema de Pitágoras:

$$
||e||_2^2 = (4 ||q_4||_2)^2 + (5 ||q_5||_2)^2

$$
<Info titulo="Observación Teórica: ¿Cómo aplica el teorema de Pitágoras aquí?">

El teorema de Pitágoras se generaliza a espacios con producto interno: si $u \perp v$, entonces $\|u + v\|_2^2 = \|u\|_2^2 + \|v\|_2^2$.

**Paso 1: Distribuir la transpuesta**

La transpuesta es lineal, por lo que:

</Info>

$$
    (u + v)^t = u^t + v^t

$$
    **Paso 2: Reescribir la norma al cuadrado**

$$
    \|u + v\|_2^2 = (u + v)^t(u + v) = (u^t + v^t)(u + v)

$$
    **Paso 3: Distribuir como un binomio**

$$
    = u^t u + u^t v + v^t u + v^t v

$$
    **Paso 4: Identificar cada término**

    - $u^t u = \|u\|_2^2$
    - $v^t v = \|v\|_2^2$
    - $u^t v = v^t u = \langle u, v \rangle = 0$ (por ortogonalidad de $q_4$ y $q_5$)

    Por lo tanto: $\|u + v\|_2^2 = \|u\|_2^2 + \|v\|_2^2$.

    Aplicando esto a $e = 4q_4 + 5q_5$, con $u = 4q_4$ y $v = 5q_5$:

$$
    \|e\|_2^2 = \|4q_4\|_2^2 + \|5q_5\|_2^2 = (4\|q_4\|_2)^2 + (5\|q_5\|_2)^2

$$
    Fin de la observación.

Como $||q_i||_2 = 1$ para todo $i$:

$$
||e||_2^2 = 16 (1)^2 + 25 (1)^2 = 41

$$
$$
||e||_2 = \sqrt{41}

$$
El error de la aproximación por mínimos cuadrados es $\sqrt{41}$.

---

## Solución Inciso C

La pseudoinversa de Moore-Penrose, denotada $A^\dagger$, generaliza la inversa a matrices no cuadradas o singulares.

Si $A$ tiene **rango columna completo** (sus columnas son linealmente independientes), la pseudoinversa izquierda se define como:

$$
A^\dagger = (A^t A)^{-1} A^t

$$
Las columnas de $A$ son linealmente independientes (son parte de una base ortonormal), por lo que $A$ tiene rango columna completo. Del inciso A se tiene que:

$$
A^t A = I_3

$$
Sustituyendo:

$$
A^\dagger = (I)^{-1} A^t

$$
$$
A^\dagger = I \cdot A^t = A^t

$$
Por lo tanto, **$A^\dagger = A^t$**, lo que se cumple porque las columnas de $A$ forman una base ortonormal.

---

## Verificación Computacional en Python

```python
{/* --8<-- "Examen_2025_07_21/04_cuadrados_minimos/verificacion.py" */}
```
