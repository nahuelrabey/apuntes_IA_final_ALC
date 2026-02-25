# Enunciado General: Examen 07 de Ago 2025

*(Los siguientes enunciados fueron extraídos y compilados automáticamente de las resoluciones individuales)*

---

## 01 Proyector

> **Ejercicio 1.** Sea $A = \begin{pmatrix} -1 & 1 & 0 & 1 \\ 1 & -1 & -1 & -2 \\ 1 & -1 & 0 & -1 \\ 1 & -1 & 1 & 0 \end{pmatrix}$ y $f: \mathbb{R}^4 \to \mathbb{R}^4$ definida por $f(x) = Ax$.
>
> **a)** Definir un proyector $p:\mathbb{R}^4 \to \mathbb{R}^4$ tal que $Im(p) = Im(f)$ y $Nu(p) = Nu(f)$.
>
> **b)** Decidir si $p$ es un proyector ortogonal. ¿Es $p$ idéntico a $f$?
>
> **c)** Hallar una base $B$ tal que la matriz de $p$ en $B$ sea diagonal.


---

## 02 Markov

> **Ejercicio 2.**
> 
> a) Sea $P \in \mathbb{R}^{n \times n}$ la matriz de un proceso de Markov en el que hay $k$ estados $i_1, i_2, \ldots, i_k$ tales que la probabilidad de pasar de $i_j$ a $i_{j+1}$ para $j = 1, \ldots, k-1$ y de $i_k$ a $i_1$ es 1. Probar que existe un $\lambda \in \mathbb{C}$ autovalor de $P$ tal que $\lambda \neq 1$, pero $|\lambda| = 1$.
> 
> b) Considerar el proceso descripto por el grafo, donde las probabilidades de transición desde cada nodo se reparten en partes iguales entre todas las ramas salientes. Hallar un estado de equilibrio. ¿Es único? ¿Se alcanza este equilibrio desde cualquier estado inicial?


---

## 03 Cuadrados Minimos

> **Ejercicio 3.** Dada $A \in \mathbb{R}^{m \times n}$ de rango $n$ y $b \in \mathbb{R}^m$ con $m > n$ se quiere resolver el problema de cuadrados mínimos: hallar $x \in \mathbb{R}^n$ que minimice $\|Ax - b\|_2$. Probar que $x = A^\dagger b$, donde $A^\dagger$ es la pseudo-inversa de $A$. Indicar por qué esto sirve para resolver el problema en la práctica.


---

## 04 Numero Condicion

> **Ejercicio 4.** Sea $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ k^2 & 0 & k^2 \end{pmatrix}$, para $k \in \mathbb{N}, k > 1$.
> 
> **a)** Probar que $Cond_\infty(A) \ge k^2$ y que $Cond_2(A) \ge ck^2$ para alguna constante $c$.
>
> **b)** Explicar qué consecuencias tendría un valor de $k$ alto a la hora de resolver un sistema de la forma $Ax = b$. ¿Depende esto de $b$?
>
> **c)** Un mecanismo para mejorar la calidad de las soluciones obtenidas al resolver un sistema es multiplicarlo por un *precondicionador*: se toma una matriz $C$ y se resuelve el sistema $(CA)x = Cb$. Por supuesto, no es obvio cómo elegir $C$ en cada caso. Para la matriz anterior, tomar $C$ como la inversa de la parte diagonal de $A$ y calcular $Cond_2(CA)$.


---

## 05 Descomposicion Lu

> **Ejercicio 5.** Sea $A = \begin{pmatrix} 1 & 1 & -1 & 1 \\ 1 & 0 & 1 & -1 \\ -1 & -1 & 0 & 1 \\ 0 & 1 & -2 & 2 \end{pmatrix}$.
> 
> **a)** Decidir si $A$ admite descomposición $LU$. En tal caso, hallarla. En caso contrario, dar una permutación $P$ de modo que $PA$ tenga descomposición $LU$.
>
> **b)** Implementar una función de Python que reciba una matriz cuadrada e intente realizar la descomposición $LU$ de $A$ sin pivoteo. Si la matriz no admite descomposición $LU$, las matrices resultantes deben ser `None`.


---

