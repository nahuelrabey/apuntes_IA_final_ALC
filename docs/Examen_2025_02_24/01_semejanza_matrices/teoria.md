# Solución del Ejercicio 1

> **Ejercicio 1**
>
> Se dice que $A \in \mathbb{K}^{n \times n}$ es semejante a $B \in \mathbb{K}^{n \times n}$ si existe una matriz invertible $S \in \mathbb{K}^{n \times n}$ tal que:
>
> $$
> SA(S^{-1}) = B
> $$
>
> 1. Demostrar que la relación de semejanza es una relación de equivalencia.
>
> 2. Demostrar que si $A$ es semejante a $B$, entonces:
>
> $$
> \text{Tr}(A) = \text{Tr}(B)
> $$
>
> **Sugerencia:** Utilizar la propiedad $\text{Tr}(EC) = \text{Tr}(CE)$ para matrices $C$ y $E$.
>
> 3. Probar que si $A$ es diagonalizable (es decir, $A$ es semejante a una matriz diagonal $D$) y los valores propios de $A$ son 0 y 1, entonces:
>
> $$
> A^2 = A
> $$
>

---

## 1. Demostrar que la relación de semejanza es una relación de equivalencia.
> 1. Demostrar que la relación de semejanza es una relación de equivalencia.

Para que una relación binaria sea de equivalencia, esta debe cumplir tres propiedades fundamentales: reflexividad, simetría y transitividad.

**A. Reflexividad ($A \sim A$):**

Evaluamos si toda matriz cuadrada $A$ es semejante a sí misma.

Consideremos la matriz identidad $I \in \mathbb{K}^{n \times n}$. Ya que $I$ es invertible y su propia inversa es $I$ ($I^{-1} = I$), tenemos:

$$
I A I^{-1} = I A I = A
$$

Como existe al menos una matriz invertible ($I$) que satisface la igualdad, $A \sim A$ siempre se cumple.

**B. Simetría (Si $A \sim B$, entonces $B \sim A$):**

Partimos de la hipótesis de que $A \sim B$. Por definición, existe una matriz invertible $S$ tal que:

$$
S A S^{-1} = B
$$

Si multiplicamos esta ecuación por la izquierda por $S^{-1}$ y por la derecha por $S$, obtenemos:

$$
S^{-1} (S A S^{-1}) S = S^{-1} B S
$$

Aplicando la propiedad asociativa y sabiendo que $S^{-1}S = I$:

$$
(S^{-1} S) A (S^{-1} S) = S^{-1} B S
$$

$$
I A I = S^{-1} B S \implies A = S^{-1} B S
$$

Definamos una nueva matriz $T = S^{-1}$. Dado que $S$ es invertible, su inversa $S^{-1}$ también lo es (y su inversa es $(S^{-1})^{-1} = S$). Reemplazando $S^{-1}$ por $T$ y $S$ por $T^{-1}$, la expresión nos queda:

$$
T B T^{-1} = A
$$

Esto significa que $B$ es semejante a $A$, probando la simetría.

**C. Transitividad (Si $A \sim B$ y $B \sim C$, entonces $A \sim C$):**

De nuestras hipótesis se concluye que existen matrices invertibles $S$ y $P$ tales que:

1) $S A S^{-1} = B$

2) $P B P^{-1} = C$

Sustituyendo el valor de $B$ de la primera ecuación en la segunda, resulta:

$$
P (S A S^{-1}) P^{-1} = C
$$

Rearrupando por asociatividad:

$$
(P S) A (S^{-1} P^{-1}) = C
$$

Sabemos por las propiedades de matrices invertibles que $(P S)^{-1} = S^{-1} P^{-1}$. Reemplazando este término:

$$
(P S) A (P S)^{-1} = C
$$

Si llamamos $U = P S$, resultando en otra matriz que sabemos que es invertible porque el producto de dos invertibles lo es:

$$
U A U^{-1} = C
$$

Esto certifica por definición que $A \sim C$, probando la transitividad.

Al cumplirse las tres condiciones, **la semejanza de matrices es efectivamente una relación de equivalencia**.

---

## 2. Demostrar que si $A$ es semejante a $B$, entonces $\text{Tr}(A) = \text{Tr}(B)$.
> 2. Demostrar que si $A$ es semejante a $B$, entonces:
>
> $$
> \text{Tr}(A) = \text{Tr}(B)
> $$
>
>    **Sugerencia:** Utilizar la propiedad $\text{Tr}(EC) = \text{Tr}(CE)$ para matrices $C$ y $E$.

Si $A \sim B$, deducimos por definición que:

$$
B = S A S^{-1}
$$

Calculamos la traza en ambos lados:

$$
\text{Tr}(B) = \text{Tr}(S A S^{-1})
$$

Aprovechando la sugerencia, usamos la propiedad cíclica de la traza: $\text{Tr}(E C) = \text{Tr}(C E)$.

Sea $E = S$ y $C = (A S^{-1})$. Sustituyendo en la propiedad de la traza:

$$
\text{Tr}(S (A S^{-1})) = \text{Tr}((A S^{-1}) S)
$$

Reescribiendo aprovechando la asociatividad dentro de la traza:

$$
\text{Tr}((A S^{-1}) S) = \text{Tr}(A (S^{-1} S))
$$

Como $S^{-1} S = I$, tenemos:

$$
\text{Tr}(A I) = \text{Tr}(A)
$$

Por lo tanto, concluimos que:

$$
\text{Tr}(B) = \text{Tr}(A)
$$

---

## 3. Probar que si $A$ es diagonalizable con valores propios 0 y 1, entonces $A^2 = A$.
> 3. Probar que si $A$ es diagonalizable (es decir, $A$ es semejante a una matriz diagonal $D$) y los valores propios de $A$ son 0 y 1, entonces:
>
> $$
> A^2 = A
> $$
>

Si $A$ es diagonalizable, entonces es semejante a una matriz diagonal $D$. Por definición existe una matriz invertible $P$ tal que:

$$
A = P^{-1} D P
$$

*(Nota: podemos invertir los roles de $P$ y su inversa definiendo $S = P^{-1}$, con lo cual la forma $S D S^{-1} = A$ y $P A P^{-1} = D$ son homólogas a la definición del enunciado).*

En cualquier matriz diagonal $D$, los elementos de su diagonal principal están formados precisamente por los valores propios de $A$. Dado que nos aseguran que los valores propios son **0 y 1**, el contenido de $D$ solamente posee este par de dígitos.

Cuando multiplicamos una matriz diagonal consigo misma (es decir, $D^2$), los elementos resultantes de su diagonal principal están simplemente elevados al cuadrado.

Como $0^2 = 0$ y $1^2 = 1$, los valores no se ven afectados y podemos asegurar categóricamente que:

$$
D^2 = D
$$

Vamos a la expresión para $A^2$:

$$
A^2 = A \cdot A = (P^{-1} D P) (P^{-1} D P)
$$

Aplicamos asociatividad para multiplicar primero las matrices interiores:

$$
A^2 = P^{-1} D (P P^{-1}) D P
$$

Sustituyendo $P P^{-1}$ por la Identidad $I$:

$$
A^2 = P^{-1} D I D P
$$

$$
A^2 = P^{-1} D^2 P
$$

Dado la particularidad de nuestra matriz donde $D^2 = D$, sustituimos y obtenemos:

$$
A^2 = P^{-1} D P
$$

Como esto es la definición exacta de nuestra matriz original $A$, queda probado que:

$$
A^2 = A
$$

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_02_24/01_semejanza_matrices/verificacion.py"
```
