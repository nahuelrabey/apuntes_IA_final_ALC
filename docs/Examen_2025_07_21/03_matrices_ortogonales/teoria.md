# Solución del Ejercicio 3 (Examen 21 de julio de 2025 - Matrices Singulares y Espectros)

> **Ejercicio 3.** Sea $A \in \mathbb{R}^{n \times n}$ una matriz tal que $A^t = A = A^{-1}$.
>
> a) ¿Cuánto vale el determinante de $A$? ¿Es $A$ diagonalizable?
> 
> b) ¿Cuáles son sus posibles autovalores?
>
> c) Calcular la matriz $\Sigma$ de la factorización SVD de $A$. Justificar.
>
> d) Calcular los autovalores de la siguiente matriz:
>
> $$B = \begin{pmatrix} 5/10 & -5/10 & -1/10 & -7/10 \\ -5/10 & 5/10 & -1/10 & -7/10 \\ -1/10 & -1/10 & 98/100 & -14/100 \\ -7/10 & -7/10 & -14/100 & 2/100 \end{pmatrix}$$
>
> *Sugerencia: usar los items anteriores.*

---

## Solución Inciso A

> a) ¿Cuánto vale el determinante de $A$? ¿Es $A$ diagonalizable?


El enigma postula que la matriz es idéntica tanto a su transpuesta ($A^t = A$, por ende es **Simétrica**) como a su recíproca inversa ($A = A^{-1}$, ergo es **Involutiva**). De la yuxtaposición de estas dos igualdades se extrae que $A^t = A^{-1}$, lo que por definición de álgebra lineal consagra a $A$ adicionalmente como una matriz **Ortogonal**.

Para averiguar el determinante, partimos de la definición que nos fue dada al unificar la simetría con la inversa:

$$A \cdot A = A \cdot A^{-1}$$

$$A^2 = I$$

Buscamos aplicar el operador determinante a ambos lados de la ecuación, recordando la propiedad multiplicativa del determinante $|A \cdot B| = |A| \cdot |B|$:

??? info "Demostración Teórica: La Regla Multiplicativa del Determinante"
    ¿De dónde surge que la multiplicidad algorítmica subyacente de la función módulo respeta en total lealtad al producto de los agrupamientos? Su rigor matemático nace de las Matrices Elementales. Toda matriz regular inversible es descomponible en un tren finito de elementales ($A = E_1\dots E_k$), los cuales individualmente traccionan al determinante separándolo en pedazos lógicos.
    
    📌 *Para consultar minuciosamente paso por paso este desarme matricial que demuestra por qué $\det(AB) = \det(A)\det(B)$ (anexado junto al validador por inducción Monte Carlo estocástica dictaminado por la metodología de estudio), remitirse aquí: [Demostración: Regla Multiplicativa del Determinante](../../demostraciones/determinante_producto.md).*

$$|A^2| = |I|$$

$$|A|^2 = 1$$

Al despejar algebraicamente, obtenemos las dos posibles raíces reales del determinante:

$$|A| = \pm 1$$

Por lo tanto, **el determinante de la matriz estructurada $A$ puede valer $1$ o $-1$**. 

Acerca de si la matriz es diagonalizable, la respuesta viene dada inmediatamente por el **Teorema Espectral**. Dicho colosal teorema dictamina que "Toda matriz real y simétrica es diagonalizable ortogonalmente dentro de los números reales". Como nuestra matriz satisface fehacientemente la condición de ser real y simétrica ($A = A^t$), **es innegablemente diagonalizable**.

??? info "Demostración Teórica: Teorema Espectral"
    ¿De dónde surgen algebraicamente las garantías insalvables de que ninguna matriz simétrica escapa jamás al terreno imaginario de Raíces Complejas, y que sus correspondientes bases multidimensionales describen ángulos perpetuos y exactos de 90° entre sí? Todo se reduce a manipulaciones hermíticas de la pre-multiplicación y del conjugado transpuesto.
    
    📌 *Revisar riguroso desarrollo paso a paso del porqué $\lambda = \overline{\lambda}$ junto con el porqué de la ortogonalidad $v_i \cdot v_j = 0$ sumado a su estrés computacional randomizado por Python, aquí: [Demostración: Teorema Espectral](../../demostraciones/teorema_espectral.md).*

---

## Solución Inciso B

> b) ¿Cuáles son sus posibles autovalores?


Si $A$ es diagonalizable, asume autovalores $\lambda_i$ y autovectores asociados $v_i \neq 0$ que obedecen la transformación originaria:

$$A v_i = \lambda_i v_i$$

Para desentrañar el espectro posible (los valores escalares que puede asir $\lambda$), podemos pre-multiplicar libremente por $A$ de ambos lados de la igualdad de autovectores:

$$A (A v_i) = A (\lambda_i v_i)$$

Dada la linealidad matricial, se absorbe el factor en escalares externos:

$$A^2 v_i = \lambda_i (A v_i)$$

Reemplazando la recursión original $A v_i$:

$$A^2 v_i = \lambda_i (\lambda_i v_i) = \lambda_i^2 v_i$$

No obstante, en el inciso A determinamos por las imposiciones del propio ejercicio que $A^2 = I$. Reemplazando temporalmente al operador izquierdo:

$$I v_i = \lambda_i^2 v_i$$

$$v_i = \lambda_i^2 v_i$$

Como los autovectores no pueden ser el vector nulo por definición de su existencia subyacente ($v_i \neq 0$), la única condición axiomática para que ambas proyecciones se equiparen es que el polinomio factor extraído asuma la igualdad:

$$\lambda_i^2 = 1$$

Resolviendo, encontramos que **los únicos autovalores viables que componen el espectro de cualquier matriz con estas características son $\lambda = \{1, -1\}$**.

---

## Solución Inciso C

> c) Calcular la matriz $\Sigma$ de la factorización SVD de $A$. Justificar.


La descomposición en valores singulares (SVD) nos permite desarticular a $A$ en la multiplicación $A = U \Sigma V^t$. Por teorema, la matriz analítica diagonal $\Sigma$ resguarda en orden descendente los **valores singulares ($\sigma_i$)** estrictamente positivos de $A$.

La doctrina matemática pauta que los valores singulares $\sigma_i$ de una matriz $A$ son las raíces cuadradas de los autovalores algebraicos provenientes de la nueva matriz simétrica definida positiva $A^t A$.

Calculemos internamente esta matriz a modelar:

$$A^t A$$

Viendo las definiciones iniciales ($A^t = A = A^{-1}$), la premultiplicamos algebráicamente sabiendo que es ortogonal:

$$A^t A = A^{-1} A = I$$

Efectivamente, la matriz de correlación es la Identidad. Los autovalores $\lambda$ vinculados a la matriz unidad matricial $I$ son estática e irrevocablemente todos de monto numérico igual a $1$.

Por consiguiente, extirpando raíces para obtener los valores singulares:

$$\sigma_i = \sqrt{1} = 1 \quad \forall i \in (1, \dots, n)$$

Todos los valores rectro-singulares son igual a la unidad. Al disponerse jerárquicamente en la diagonal $\Sigma$, ésta pasará a ser una matriz rellena fundamentalmente de unos. **La matriz $\Sigma$ evaluada resulta ser idéntica analíticamente a la Matriz Identidad: $\Sigma = I$.**

---

## Solución Inciso D

> d) Calcular los autovalores de la siguiente matriz:
>
> $$B = \begin{pmatrix} 5/10 & -5/10 & -1/10 & -7/10 \\ -5/10 & 5/10 & -1/10 & -7/10 \\ -1/10 & -1/10 & 98/100 & -14/100 \\ -7/10 & -7/10 & -14/100 & 2/100 \end{pmatrix}$$
>
> *Sugerencia: usar los items anteriores.*


Nos proponen la matriz $4 \times 4$:

$$B = \begin{pmatrix} 0.5 & -0.5 & -0.1 & -0.7 \\ -0.5 & 0.5 & -0.1 & -0.7 \\ -0.1 & -0.1 & 0.98 & -0.14 \\ -0.7 & -0.7 & -0.14 & 0.02 \end{pmatrix}$$

El *hint* nos insta a usar las conclusiones deductivas asimiladas en items previos. Inspeccionemos a $B$:

- Naturalmente saltan a la vista por espejo estructural sobre la diagonal que **B es simétrica** ($B = B^t$).

- Si computarizáramos o realizásemos el esfuerzo maratónico de calcular $B^2$, notaríamos (como comprobará la computadora acto seguido) que **$B^2 = I$**, con lo que $B = B^{-1}$.

Por consiguiente, la matriz $B$ asienta empíricamente en el grupo de matrices de los incisos anteriores ($B^t = B = B^{-1}$). Según el inciso B, **sus probables y únicos autovalores son exhaustivamente $1$ o $-1$**. Nos toca descubrir la multiplicidad de ellos, es decir, determinar exactamente dentro de esos cuatro valores espaciales en $\mathbb{R}^4$ cuántos "unos" positivos y "unos" negativos subyacen.

Haciendo uso analítico implacable de la **Traza de la Matriz** ($Tr(B)$, sumatoria lineal de los índices puros diagonales), sabemos que por el Teorema de la Traza ésta no muta jamás bajo cambios de base y es perennemente idéntica a la sumatoria de sus autovalores matemáticos abstractos.

Calculando la diagonal de $B$:

$$Tr(B) = 0.5 + 0.5 + 0.98 + 0.02 = 2$$

Frente a esto, postulamos nuestro conjunto de auto-valores en incógnitas: Sea $k$ la cantidad de autovalores de monto $1$, y $m$ la cantidad de autovalores de monto $-1$. Como $\dim(B) = 4$, tenemos 4 autovalores totales y armamos el sistema 2x2:

$$ \begin{cases} k + m = 4 \quad \text{(Espectro total)} \\ k(1) + m(-1) = 2 \quad \text{(Suma traza-autovalores)} \end{cases}$$

Acumulando ambas igualdades ($2k = 6$), extirpamos lógicamente a los constituyentes:

$$k = 3$$

$$m = 1$$

Por ende, deducimos implacablemente sin factorizar grado 4, que **los cuatro autovalores exactos de la matriz B son: $\{1, 1, 1, -1\}$**.

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/03_matrices_ortogonales/verificacion.py"
```
