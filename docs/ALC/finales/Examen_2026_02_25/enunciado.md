# Enunciado General: Examen 25 de Feb 2026

*(Álgebra Lineal Computacional — Examen Final)*

---

## Contenido Teórico Obligatorio

El presente examen evalúa la comprensión y aplicación práctica de los siguientes teoremas y métodos,
cuyas demostraciones formales pueden ser consultadas en la base de conocimiento:

- **Cadenas de Markov**: Matrices estocásticas, estado de equilibrio, distribución límite $P^\infty$.
    - [Demostración: Radio Espectral en Markov (ρ=1)](../../demostraciones/radio_espectral_markov.md)

- **Factorización QR**: Relación entre bases ortonormales y la descomposición QR de una matriz.

- **Descomposición SVD**: Valores singulares, norma espectral y relación con factorizaciones ortogonales.

- **Cuadrados Mínimos**: Condición de unicidad de la solución de $Ax = b$, interpretación estadística.
    - [Demostración: Independencia de Columnas Pivotales](../../demostraciones/independencia_pivotes.md)

- **Factorización LU**: Procedimiento de eliminación gaussiana sin pivoteo, condiciones de existencia y unicidad.

---

## 01 Cadenas de Markov

> **Ejercicio 1.** El movimiento anual entre 4 ciudades está regido por el siguiente diagrama de
> transición. Se sabe que $v = (0, 0, \frac{1}{2}, \frac{1}{2})^t$ es un estado de equilibrio.
>
> **(a)** Hallar la matriz de transición **P**.
>
> **(b)** Determinar la distribución de población después de 10 años,
> si la distribución inicial es $v_0 = (\frac{1}{2}, 0, \frac{1}{2}, 0)^t$.
>
> **(c)** ¿Existe $P^\infty$? Si existe, calcularla.
>
> **(d)** Implemente `estado_limite(P, v0, max_iter, tol)` en Python, que busca el estado
> límite de la distribución inicial `v0`. En caso de no hallarlo con tolerancia `tol`,
> o de realizar más de `max_iter` iteraciones, la función debe retornar `None`
> con el mensaje correspondiente.

---

## 02 Factorización QR y SVD

> **Ejercicio 2.** Sea $\{q_1, q_2, q_3, q_4, q_5\}$ una base ortonormal de $\mathbb{R}^5$, $A$ una
> matriz de $5 \times 3$ tal que
>
> $$
> A = \left(\, q_1 \;\middle|\; q_1 + q_2 \;\middle|\; q_2 + q_3 \,\right)
> $$
>
> **(a)** De una factorización $QR$ de la matriz $A$.
>
> **(b)** De una descomposición en valores singulares de la matriz $A$.
>
> **(c)** Calcule $\|A\|_2$. Indique una cota inferior para $\|A\|_\infty$.

---

## 03 Cuadrados Mínimos

> **Ejercicio 3.** Para ver quién es el mejor en el solitario, un grupo de $m$ amigos organiza $n$
> partidas del juego. Anotan el resultado en la forma $(A|b)$, con $A$ una matriz de $n \times m$,
> que tiene un 1 en la posición $i,j$ si el amigo $j$ jugó en la partida $i$ (y 0 si no); y $b$ un
> vector de longitud $n$ que tiene un 1 en la posición $i$ si la partida fue victoriosa y 0 si no.
> Para establecer un ranking buscan un vector de puntajes $x$ tal que $Ax = b$.
>
> **(a)** ¿Qué condición se debe cumplir para que el puntaje $x$ esté definido unívocamente para
> todos los amigos?
>
> **(b)** Muestre que el puntaje $x_j$ del amigo $j$ es igual a la fracción de victorias que obtuvo.
>
> **(c)** Para el caso en el que tres amigos juegan $N$ partidas, y todos ganan la mitad de ellas,
> calcule el error promedio por partida $\frac{1}{3N}\|Ax - b\|_2$. ¿Aumenta o disminuye con el
> número de partidas?

---

## 04 Factorización LU

> **Ejercicio 4.** Dada una matriz $A$ de $\mathbb{R}^{n \times n}$,
>
> **(a)** Detalle el procedimiento para encontrar la factorización $A = LU$ sin pivoteo, indicando
> cuándo falla. ¿El fallo del algoritmo implica la inexistencia de la factorización $LU$?
>
> **(b)** Describa condiciones conocidas para que la factorización $LU$ de $A$ exista y/o sea única.

---
