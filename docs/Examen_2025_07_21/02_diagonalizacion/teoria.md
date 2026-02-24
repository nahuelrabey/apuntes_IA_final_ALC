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
    El porqué un "abanico" de autovalores distintos garantiza de forma obligatoria y deductiva que sus autovectores asociados no pueden colapsar formando dependencias espaciales, se demuestra axiomáticamente mediante el Principio de Inducción Fuerte Matemática.
    
    📌 *Para consultar paso a paso la justificación analítica y matemática detrás de este Lema de Independencia (junto con su validador masivo estocástico en Python), puedes remitirte a: [Demostración: Independencia Lineal de Autovectores](../../demostraciones/autovalores_distintos.md).*

Sabemos que cualquier conjunto de $n$ vectores linealmente independientes dentro de un espacio vectorial euclídeo de dimensión $n$ (como es en este caso $\mathbb{R}^n$) obligatoriamente genera dicho espacio (sirve como sistema generador) y, por consiguiente, forma inherentemente una **Base**. Queda justificado analíticamente.

---

## Solución Inciso B

> b) La matriz $C \in \mathbb{R}^{n \times n}$ cuyas columnas están dadas por los vectores $v_1, \dots, v_n$ es inversible y cumple con que $AC = CS$, con $S$ una matriz diagonal con $\lambda_1, \dots, \lambda_n$ en la diagonal.

A partir del inciso (A), hemos concluido que los autovectores $\{v_1, \dots, v_n\}$ estructuran una base de $\mathbb{R}^n$ y por tanto son independientes. La matriz columna unificada $C$ se define en bloques como:

$$C = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \dots & v_n \\ | & | & & | \end{pmatrix}$$

Como sus columnas son vectores estrictamente **linealmente independientes**, su determinante no será nulo y obligatoriamente existirá su inversa (la matriz $C$ es inversible / no singular). 

??? info "Observación Teórica: ¿Los autovectores siempre son ortogonales entre sí?"
    **No, rotundamente no.** El Lema demostrado en el inciso anterior únicamente nos proveyó las garantías algebraicas de que los autovectores son **Linealmente Independientes** por provenir de raíces características (autovalores) distintas. 
    
    Que sean linealmente independientes significa que "no son combinación lineal entre sí" y su span basta para cubrir las dimensiones del espacio, logrando por definición que el determinante de la matriz formada $C$ sea distinto de cero (inversible).
    
    Sin embargo, **la ortogonalidad (que formen ángulos perfectos de 90° o que su producto interno $v_i \cdot v_j = 0$) es una propiedad de élite reservada de manera exclusiva y rigurosa para las Matrices Simétricas Reales** (por aplicación del célebre *Teorema Espectral*). 
    
    Para una matriz cuadrada $A$ general asimétrica, sus autovectores construirán firmemente una base para $\mathbb{R}^n$, pero en la inmensa mayoría de los casos será una **base oblicua** (independientes pero **no ortogonales**).
    
    📌 *Para constatar la rigurosidad conceptual de esta distinción vital (que la ortogonalidad se forja como propiedad exclusiva del Teorema Espectral ante matrices simétricas reales), consúltese la [Clase 25 (Symmetric Matrices and Positive Definiteness) - Prof. Gilbert Strang (MIT 18.06 OpenCourseWare)](https://www.youtube.com/watch?v=13r9QY6cmjc&list=PLE7DDD91010BC51F8&index=26) o la [Wikipedia: Spectral Theorem (Symmetric matrices)](https://en.wikipedia.org/wiki/Spectral_theorem).*

A continuación debemos probar la aseveración analítica de igualdad. Evaluemos el producto en el miembro izquierdo $AC$:

$$AC = A \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} = \begin{pmatrix} | & & | \\ Av_1 & \dots & Av_n \\ | & & | \end{pmatrix}$$

Por la naturaleza teórica de un autovector asosciado a su respectivo autovalor, sustituimos que la transformación sobre ella resulta en un reescalado homótetico por el propio autovalor $Av_i = \lambda_i v_i$:

$$AC = \begin{pmatrix} | & & | \\ \lambda_1 v_1 & \dots & \lambda_n v_n \\ | & & | \end{pmatrix}$$

Por el otro flanco, evaluemos el miembro derecho mediante el producto de $C$ por la matriz diagonal espectral $S = \text{diag}(\lambda_1, \dots, \lambda_n)$:

$$CS = \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix}$$

La regla subyacente de la multiplicación por derecha de una matriz escalar diagonal afirma que cada elemento multiplicará la columna entera de su misma posición indexada. Esto resulta, irrebatiblemente, en idéntico resultado que nuestro primer paso matemático evaluado superiormente:

$$CS = \begin{pmatrix} | & & | \\ \lambda_1 v_1 & \dots & \lambda_n v_n \\ | & & | \end{pmatrix}$$

Dado que ambos caminos algebraicos convergen a la misma matriz constituida por los vectores proyectados, se decreta que **$AC = CS$**.

---

## Solución Inciso C

> c) La matriz $A$ es diagonalizable.

En el inciso estipulado previamente demostramos que subsiste la igualdad operacional:

$$AC = CS$$

En ese mismo desarrollo inicializamos nuestra justificación validando que $C$ formaba una matriz con inversa existencial $C^{-1}$. Con esta autoridad lícita, podemos optar por premultiplicar y despejar ambos extremos valíendonos por derecha de dicha inversa:

$$(AC)C^{-1} = (CS)C^{-1}$$

Asumiendo la propiedad asociativa, $CC^{-1} = I$ (siendo $I$ la Matriz Identidad) liberando a $A$:

$$A = C S C^{-1}$$

¿Qué significa algebraicamente que $A$ pueda re-enunciarse como un sistema recíproco $C S C^{-1}$?. Por la definición ontológica expuesta en el álgebra estructural matricial: **una matriz cuadrada es diagonalizable si y sólo si es semejante a una matriz diagonal**.

La igualdad demostrada verifica de manual dicha condición. Puesto que confirmamos que $A$ está formulada por una matriz de pasaje de base en tándem con la matriz diagonal de sus autovalores ($S$), **entonces la matriz A es incuestionablemente diagonalizable**, ergo sus operaciones vectoriales sobre $\mathbb{R}^n$ se reducen a proyecciones re-escalables y ortográficas en el subespacio rotado.

---

## Verificación Computacional en Python

```python
--8<-- "Examen_2025_07_21/02_diagonalizacion/verificacion.py"
```
