# Solución del Ejercicio 4 (Examen 21 de julio de 2025 - Bases Ortonormales y Cuadrados Mínimos)

> **Ejercicio 4.** Sea $\{q_1, q_2, q_3, q_4, q_5\}$ una base ortonormal de $\mathbb{R}^5$, $A$ una matriz de $5 \times 3$ con columnas $q_1, q_2, q_3$ y el vector $b = q_1 + 2q_2 + 3q_3 + 4q_4 + 5q_5$.
>
> a) Mostrar que el sistema $Ax = b$ no tiene solución. Plantear las ecuaciones normales y hallar la solución $\hat{x}$ de cuadrados mínimos para dicho sistema.
>
> b) Calcular el error cometido en la aproximación.
>
> c) Mostrar que $A^\dagger = A^t$, siendo $A^\dagger$ la pseudoinversa de $A$.

---

## Solución Inciso A

Definimos a la matriz $A$ por sus propios vectores columna ortonormales:

$$
A = \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix}
$$

Cualquier vector $v$ que pertenezca a la imagen de $A$ (es decir, $v \in Col(A)$), debe expresarse íntegramente como una combinación lineal estricta de sus tres columnas componentes $\{q_1, q_2, q_3\}$.

$$
A x = x_1 q_1 + x_2 q_2 + x_3 q_3
$$

Sin embargo, el vector independiente suministrado ($b$) fue definido a partir de la base ortonormal completa del espacio:

$$
b = 1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5
$$

Dado que por naturaleza los cinco vectores componen una base espacial, son lógicamente **linealmente independientes**. Nos resulta materialmente imposible generar las proyecciones relativas a $q_4$ y $q_5$ valiéndonos pura y exclusivamente de los tres primeros vectores generadores. Todo aporte al subespacio nulo del vector $b$ es ajeno a $Col(A)$.

**En conclusión, $b \notin Col(A)$, hecho que decreta instantáneamente que el sistema $A x = b$ es intrínsecamente incompatible y carece de solución matemática.**

Para solventar esta carencia, la ortodoxia analítica exige hallar el punto hiperespacial que minice el grado de residuo $||Ax - b||$. A este designio le llamamos construir la Ecuación Normal de Mínimos Cuadrados:

$$
A^t A \hat{x} = A^t b
$$

Inspeccionemos cautelosamente de qué consta en sí el núcleo multiplicativo $\bold{A^t A}$. Reuniendo los vectores columnas transpuestos, encontramos la Matriz Gramiana:

$$
A^t A = \begin{pmatrix} - & q_1^t & - \\ - & q_2^t & - \\ - & q_3^t & - \end{pmatrix} \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix} = \begin{pmatrix} q_1^t q_1 & q_1^t q_2 & q_1^t q_3 \\ q_2^t q_1 & q_2^t q_2 & q_2^t q_3 \\ q_3^t q_1 & q_3^t q_2 & q_3^t q_3 \end{pmatrix}
$$

No obstante, la premisa enmarca formalmente que el conjunto engloba una **Base Ortonormal**. Dicho vocablo asume que el producto interior decantado arroja uno entre vectores homólogos y cero frente a proyecciones ortogonales de índices mixtos ($q_i^t q_j = \delta_{ij}$). Como corolario irremediable, la diagonal queda plagada de unos, y la anti-diagonal se limpia gravitando en nulos:

$$
A^t A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3
$$

Donde $I_3$ es la matriz Identidad en $\mathbb{R}^{3 \times 3}$.

Abordemos ahora la operación restante en el extremo de resultados del modelo, desarticulando el vector $b$:

$$
A^t b = \begin{pmatrix} - & q_1^t & - \\ - & q_2^t & - \\ - & q_3^t & - \end{pmatrix} (1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5)
$$

Al distribuir los multiplicadores punto de cada fila, la cualidad de las componentes ortogonales vuelve a operar. Cada vector asimila únicamente aquél escalar co-paralelo de su misma especie y anula irrefutablemente frente al producto escalar toda correlación con elementos dispares (como $q_4$ y $q_5$).

En consecuencia obtenemos algebraicamente el vector unicamente compuesto por los escalares base rescatados:

$$
A^t b = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
$$

Retornando a nuestra Ecuación Normal primigenia y volcando allí nuestras deducciones operacionales:

$$
I_3 \hat{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
$$

Revelando la estocástica pura:
**$\hat{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$**

---

## Solución Inciso B

Calcularemos matemáticamente la pureza de la respuesta hallada evaluando el vector margen de error originado en la desestimación. Formulemos a la Proyección Ortonormal $p$ arrojada por nuestro sistema aproximado en mínimos recuadros:

$$
p = A \hat{x} = \begin{pmatrix} | & | & | \\ q_1 & q_2 & q_3 \\ | & | & | \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 1 q_1 + 2 q_2 + 3 q_3
$$

Se define unánimemente el vector de error $e$ intercediendo el objetivo deseado frente al punto más próximo lícito validable en subespacio ($p$):

$$
e = b - p
$$

$$
e = (1 q_1 + 2 q_2 + 3 q_3 + 4 q_4 + 5 q_5) - (1 q_1 + 2 q_2 + 3 q_3)
$$

Extrayendo denominadores comunes y suprimiendo términos afines:

$$
e = 4 q_4 + 5 q_5
$$

Someteremos a evaluación de norma Euclidiana (distancia-2 computacional) ($|| \cdot ||_2$) para constatar el Error Cuadrático Final total. Aplicando el axioma de Pitágoras debido a que nuestra base es un abanico pre-ortogonal (donde el cateto vector 4 no posee injerencias angulares con el cateto vector 5):

$$
||e||_2^2 = (4 ||q_4||_2)^2 + (5 ||q_5||_2)^2
$$

Dado su condición normativa que restringe el largo a uno ($||q||=1$ para todo subespacio interviniente):

$$
||e||_2^2 = 16 (1)^2 + 25 (1)^2 = 41
$$

$$
||e||_2 = \sqrt{41}
$$

El error cometido en la regresión matemática más plausible asume rigurosamente la suma pitagórica del módulo residual de todo tensor independiente al subespacio de recabo ($\sqrt{41}$).

---

## Solución Inciso C

La Pseudoinversa explícita de Moore-Penrose, universalmente representada por el símbolo transfigurado de una daga formal algebraico o comúnmente una cuña supra-marcada ($A^\dagger$), generaliza matricialmente toda función inversa en el contexto que aglomera tensores asimétricos no cuadrados para poder invertirlos en espacios de características lineales dependientes.

Para constatar si encuadramos, se sabe por norma general que si el conjunto matriz en columnas asume en su integridad **rango pleno de sus componentes columna** (que sus columnas $q_1, q_2, q_3$ son linealmente independientes en todo aspecto), la pseudoinversa de limitación izquierda subyace definida por la formalidad computacional:

$$
A^\dagger = (A^t A)^{-1} A^t
$$

A diferencia del espectro, nuestra matriz de diseño $A$ sí posee sus vectores base definidos y ratificados en este postulado al ser la base ortonormal madre (donde todo generador ostentado no asume interdependencia). Nos avala a aplicar la Ley Fundamental de la izquierda, invocando el álgebra probada rigurosamente en el comienzo del Inciso A, en donde expusimos en un cuadro gramiano axiomático que la multiplicación pre-transpuesta desencadenaba el orden en Identidad Absoluta:

$$
A^t A = I_3
$$

Retornando al modelo teórico:

$$
A^\dagger = (I)^{-1} A^t
$$

$$
A^\dagger = I \cdot A^t = A^t
$$

Hemos demostrado incuestionablemente que por la idiosincrasia formal de ostentar matrices constituidas como subespacios con bases de características modulares ortonormales puros, **su inversa ideal minimizadora se contrae por isomorfismo lógicamente analítico a su propia Matriz Traspuesta ($A^\dagger = A^t$)**.

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/04_cuadrados_minimos/verificacion.py"
```
