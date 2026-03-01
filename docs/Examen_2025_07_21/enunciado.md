# Enunciado General: Examen 21 de Jul 2025

*(Los siguientes enunciados fueron extraídos y compilados automáticamente de las resoluciones individuales)*

---

## Contenido Teórico Obligatorio

El presente examen evalúa la comprensión y aplicación práctica de los siguientes teoremas y métodos, cuyas demostraciones formales pueden ser consultadas en la base de conocimiento:

*   **Descomposición en Valores Singulares (SVD)**: Aproximaciones de rango 1 y método de iteración matricial para singularidad principal.
    *   [Demostración: Método de la Potencia (Punto b)](../demostraciones/metodo_potencia.md)
*   **Diagonalización**: Bases de autovectores y descomposición $AC = CS$.
    *   [Demostración: Autovalores Distintos implican Autovectores L.I.](../demostraciones/autovalores_distintos.md)
*   **Matrices Ortogonales y Simétricas**: Determinantes de reflexión/rotación y Teorema Espectral real.
    *   [Demostración: Teorema Espectral Real](../demostraciones/teorema_espectral.md)
*   **Cuadrados Mínimos**: Bases ortonormales, matrices $Q$ e Inversas Generalizadas (Pseudoinversas $A^\dagger$).
*   **Espacios con Producto Interno**: Acotación de proyecciones a través de ángulos vectoriales.

---

## 01 Svd

> **Ejercicio 1.** Sea $A$ una matriz con coeficientes reales de $n \times 2$. Sean $U$, $\Sigma$ y $V$ las matrices que dan su descomposición SVD, con $u_i$ la columna $i$-ésima de $U$, $\Sigma_{ii} = \sigma_i$ (con $\sigma_i \neq \sigma_j$ si $i \neq j$), y $v_i$ la columna $i$-ésima de $V$. Sea $\tilde{A} = \sigma_1 u_1 v_1^t$ una aproximación de rango 1 de $A$.
>
> a) Si $x \in \mathbb{R}^2$ es un vector perteneciente al círculo unitario, mostrar que el error cometido al calcular $Ax$ como $\tilde{A}x$ está acotado por $\sigma_2$.
>
> b) Sea $B = A^tA$ y $x \in \mathbb{R}^2$ elegido al azar. Mostrar que el siguiente algoritmo converge al vector $v_1$ cuando $N \to \infty$:
>
> - Para $k \in 1, \dots, N$:
>
>   - $x = Bx$
>
>   - $x = x / ||x||$
>
> c) Escriba una rutina que calcule la mejor aproximación de rango 1 de una matriz real de $n \times 2$ en el sentido de la norma 2. Toda función que involucre operaciones más complejas que el producto matricial debe ser definida explícitamente.

---

## 02 Diagonalizacion

> **Ejercicio 2.** Sea una matriz $A \in \mathbb{R}^{n \times n}$ con $n$ autovalores mayores a cero y distintos entre sí. Sean $\lambda_1, \dots, \lambda_n$ sus autovalores y $v_1, \dots, v_n$ los autovectores asociados. Mostrar que:
>
> a) $\{v_1, \dots, v_n\}$ forma una base de $\mathbb{R}^n$. Justificar.
>
> b) La matriz $C \in \mathbb{R}^{n \times n}$ cuyas columnas están dadas por los vectores $v_1, \dots, v_n$ es inversible y cumple con que $AC = CS$, con $S$ una matriz diagonal con $\lambda_1, \dots, \lambda_n$ en la diagonal.
>
> c) La matriz $A$ es diagonalizable.

---

## 03 Matrices Ortogonales

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
> $$
> B = \begin{pmatrix} 5/10 & -5/10 & -1/10 & -7/10 \\ -5/10 & 5/10 & -1/10 & -7/10 \\ -1/10 & -1/10 & 98/100 & -14/100 \\ -7/10 & -7/10 & -14/100 & 2/100 \end{pmatrix}
> $$
>
> *Sugerencia: usar los items anteriores.*

---

## 04 Cuadrados Minimos

> **Ejercicio 4.** Sea $\{q_1, q_2, q_3, q_4, q_5\}$ una base ortonormal de $\mathbb{R}^5$, $A$ una matriz de $5 \times 3$ con columnas $q_1, q_2, q_3$ y el vector $b = q_1 + 2q_2 + 3q_3 + 4q_4 + 5q_5$.
>
> a) Mostrar que el sistema $Ax = b$ no tiene solución. Plantear las ecuaciones normales y hallar la solución $\hat{x}$ de cuadrados mínimos para dicho sistema.
>
> b) Calcular el error cometido en la aproximación.
>
> c) Mostrar que $A^\dagger = A^t$, siendo $A^\dagger$ la pseudoinversa de $A$.

---

## 05 Cauchy Schwartz

> **Ejercicio 5.** Probar la desigualdad de Cauchy-Schwartz: $|x^* y| \le ||x||_2 ||y||_2$.

---
