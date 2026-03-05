# Solución del Ejercicio 2 (Examen 21 de julio de 2025 - Diagonalización)

> **Ejercicio 2.** Sea una matriz $A \in \mathbb{R}^{n \times n}$ con $n$ autovalores mayores a cero y distintos entre sí. Sean $\lambda_1, \dots, \lambda_n$ sus autovalores y $v_1, \dots, v_n$ los autovectores asociados. Mostrar que:
>
> a) $\{v_1, \dots, v_n\}$ forma una base de $\mathbb{R}^n$. Justificar.
>
> b) La matriz $C \in \mathbb{R}^{n \times n}$ cuyas columnas están dadas por los vectores $v_1, \dots, v_n$ es inversible y cumple con que $AC = CS$, con $S$ una matriz diagonal con $\lambda_1, \dots, \lambda_n$ en la diagonal.
>
> c) La matriz $A$ es diagonalizable.

---

## Solución Inciso A

> a) $\{v_1, \dots, v_n\}$ forma una base de $\mathbb{R}^n$. Justificar.

El teorema fundamental sobre autovectores establece que "autovectores correspondientes a autovalores distintos son linealmente independientes".

Dado que por hipótesis se nos confirma que la matriz $A$ posee $n$ autovalores estrictamente **distintos entre sí** ($\lambda_i \neq \lambda_j$ para todo $i \neq j$), este lema nos garantiza de forma deductiva que el conjunto de sus correspondientes autovectores $\{v_1, \dots, v_n\}$ constituye un conjunto de exactamente $n$ vectores **linealmente independientes**.

??? info "Demostración Teórica: Independencia Lineal por Autovalores Distintos"
    El hecho de que autovalores distintos garanticen la independencia lineal de sus autovectores asociados se demuestra por inducción fuerte.

    📌 *Para consultar paso a paso la justificación analítica y matemática detrás de este Lema de Independencia (junto con su validador masivo estocástico en Python), puedes remitirte a: [Demostración: Independencia Lineal de Autovectores](../../demostraciones/autovalores_distintos.md).*

    Fin de la demostración.

Todo conjunto de $n$ vectores linealmente independientes en un espacio de dimensión $n$ forma una base de dicho espacio. Por lo tanto, $\{v_1, \dots, v_n\}$ es una base de $\mathbb{R}^n$.

---

## Solución Inciso B

> b) La matriz $C \in \mathbb{R}^{n \times n}$ cuyas columnas están dadas por los vectores $v_1, \dots, v_n$ es inversible y cumple con que $AC = CS$, con $S$ una matriz diagonal con $\lambda_1, \dots, \lambda_n$ en la diagonal.

A partir del inciso (A), hemos concluido que los autovectores $\{v_1, \dots, v_n\}$ estructuran una base de $\mathbb{R}^n$ y por tanto son independientes. La matriz columna unificada $C$ se define en bloques como:

$$
C = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \dots & v_n \\ | & | & & | \end{pmatrix}
$$

Como sus columnas son **linealmente independientes**, su determinante es no nulo y la matriz $C$ es inversible.

??? info "Demostración Teórica: Columnas L.I. e Invertibilidad"
    Toda matriz cuyas columnas son linealmente independientes es inversible. Esto se desprende del Teorema de la Matriz Inversible (IMT).

    📌 *Para consultar el porqué de esta afirmación estructural, el desarrollo del Teorema de la Matriz Inversible (IMT) y su respectiva contraverificación estadística por fuerza bruta en Python, puedes remitirte a: [Demostración: Independencia Lineal e Invertibilidad](../../demostraciones/columnas_li_inversibles.md).*

    Fin de la demostración.

??? info "Observación Teórica: ¿Los autovectores siempre son ortogonales entre sí?"
    **No.** El resultado del inciso anterior garantiza que los autovectores son **linealmente independientes** cuando los autovalores son distintos, pero no que sean ortogonales entre sí.

    La ortogonalidad entre autovectores (es decir, que $v_i \cdot v_j = 0$) es una propiedad exclusiva de las **matrices simétricas reales**, garantizada por el *Teorema Espectral*.

    Para una matriz cuadrada $A$ general no simétrica, los autovectores forman una base de $\mathbb{R}^n$, pero en general es una **base oblicua** (independientes pero no necesariamente ortogonales).

    Fin de la observación.

A continuación debemos probar la aseveración analítica de igualdad. Evaluemos el producto en el miembro izquierdo $AC$:

$$
AC = A \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} = \begin{pmatrix} | & & | \\ Av_1 & \dots & Av_n \\ | & & | \end{pmatrix}
$$

??? abstract "Fundamento Algebraico: Multiplicación Matricial (Por Columnas)"
    Esta igualdad se desprende directamente de la **definición del producto de matrices**.

    Al multiplicar $A \in \mathbb{R}^{n \times n}$ por $C \in \mathbb{R}^{n \times p}$, se puede expresar $C$ en términos de sus columnas $[v_1, v_2, \dots, v_p]$.

    El producto $AC$ produce una matriz cuya $i$-ésima columna es $Av_i$.

    Fin del fundamento.

Por definición de autovector, $Av_i = \lambda_i v_i$, por lo que:

$$
AC = \begin{pmatrix} | & & | \\ \lambda_1 v_1 & \dots & \lambda_n v_n \\ | & & | \end{pmatrix}
$$

Evaluamos ahora el miembro derecho, el producto de $C$ por la matriz diagonal $S = \text{diag}(\lambda_1, \dots, \lambda_n)$:

$$
CS = \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix}
$$

La multiplicación por derecha de una matriz diagonal escala cada columna de $C$ por el correspondiente elemento diagonal. Por lo tanto:

$$
CS = \begin{pmatrix} | & & | \\ \lambda_1 v_1 & \dots & \lambda_n v_n \\ | & & | \end{pmatrix}
$$

Como ambos lados producen la misma matriz, queda demostrado que **$AC = CS$**.

---

## Solución Inciso C

> c) La matriz $A$ es diagonalizable.

En el inciso anterior se demostró la igualdad:

$$
AC = CS
$$

Como se estableció que $C$ es inversible, multiplicamos por $C^{-1}$ a derecha en ambos miembros:

$$
(AC)C^{-1} = (CS)C^{-1}
$$

Por asociatividad y usando que $CC^{-1} = I$:

$$
A = C S C^{-1}
$$

Por definición, **una matriz cuadrada es diagonalizable si y solo si es semejante a una matriz diagonal**.

La igualdad $A = C S C^{-1}$ verifica exactamente esta condición, con $S$ diagonal y $C$ invertible. **Por lo tanto, $A$ es diagonalizable.**

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/02_diagonalizacion/verificacion.py"
```
