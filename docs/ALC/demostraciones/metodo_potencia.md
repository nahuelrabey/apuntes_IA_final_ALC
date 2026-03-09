# Demostración: Normalización iterativa en el Método de la Potencia

## Interpretación del Enunciado

El **Método de la Potencia** normalizado divide por la norma del vector obtenido en cada paso iterativo. A través del principio de inducción, podemos comprobar que este proceso equivale a un cambio de escala.

El objetivo es demostrar matemáticamente que en el Método de la Potencia, re-normalizar el vector resultante a magnitud 1 en cada iteración $k$ es matemáticamente equivalente a aplicar la matriz $B$ elevada a la potencia $k$ directamente sobre el vector inicial $x^{(0)}$ y normalizar el resultado de dicha operación final.

Es decir, se debe probar que:

$$
x^{(k)} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}

$$
## Solución Analítica (Demostración por Inducción)

Definimos la relación de recurrencia del Método de la Potencia normalizado. Se comienza con un vector inicial $x^{(0)}$ tal que $||x^{(0)}|| = 1$. En cada paso $k \ge 1$ se ejecuta:

$$
x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||}

$$
Se procederá a probar que para todo $k \ge 1$, la proposición $P(k)$ sobre el vector iterativo es verdadera:

$$
P(k): \quad x^{(k)} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}

$$
### 1. Caso Base ($k = 1$)

Evaluamos la proposición en su iteración $k=1$ sustituyendo directamente en la fórmula recursiva analítica:

$$
x^{(1)} = \frac{B x^{(0)}}{||B x^{(0)}||}

$$
Este resultado coincide con la proposición evaluada en $k=1$, ya que $B^1 = B$. Por lo tanto, el caso base es válido.

### 2. Paso Inductivo

Asumimos como **Hipótesis Inductiva (H.I.)** que la proposición es válida para el paso algebraico anterior, la iteración $k-1$:

$$
x^{(k-1)} = \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||}

$$
A partir de esta igualdad estructurada algorítmicamente, debemos demostrar que la proposición subyacente se satisface también para el paso $k$.

Iniciamos partiendo de la forma rigurosa de la definición iterativa computacional del caso general $k$:

$$
x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||}

$$
Sustituimos la variable temporal iterativa $x^{(k-1)}$ empleando la aserción integral de nuestra Hipótesis Inductiva:

$$
x^{(k)} = \frac{B \left( \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||} \right)}{\left\| B \left( \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||} \right) \right\|}

$$
Es oportuno mencionar que la norma observada en el denominador en el paso analizado, correspondiente formalmente a $c = ||B^{k-1} x^{(0)}||$, representa algorítmicamente un escalar estricto (número real mayor a 0, puesto que se descartan de plano los resultados del vector nulo en el proceso iterativo).

Por las propiedades de linealidad escalable que gobiernan la operatoria de las matrices algebraicas y de cualquier norma física, en conjunción para un escalar $c > 0$ y un vector físico libre $v$, pueden procesarse resultando:

- $B\left(\frac{1}{c}v\right) = \frac{1}{c} Bv$
- $\left\| \frac{1}{c} v \right\| = \left|\frac{1}{c}\right| \|v\| = \frac{1}{c} \|v\|$

Procedemos a extraer el factor numérico expresado como multiplicador recíproco $\frac{1}{||B^{k-1} x^{(0)}||}$, extrayéndolo en paralelo de la matriz $B$ que se halla como factor unitario en el numerador tanto como de los barrotes de la norma que constituyen al denominador de la superposición matricial:

$$
x^{(k)} = \frac{ \frac{1}{||B^{k-1} x^{(0)}||} \cdot B (B^{k-1} x^{(0)}) }{ \frac{1}{||B^{k-1} x^{(0)}||} \cdot \| B (B^{k-1} x^{(0)}) \| }

$$
Dado que este factor numérico es estrictamente un número real distinto de cero, su redundancia fraccional ocasiona su auto-cancelación simultánea en el cociente:

$$
x^{(k)} = \frac{ B (B^{k-1} x^{(0)}) }{ \| B (B^{k-1} x^{(0)}) \| }

$$
Al aplicar las características elementales y directas sobre arreglos factoriales algebraicos tales que matricialmente se cumple siempre ($B \cdot B^{k-1} = B^k$), llegamos a nuestra formulación requerida:

$$
x^{(k)} = \frac{ B^k x^{(0)} }{ || B^k x^{(0)} || }

$$
### Conclusión

Por el Principio de Inducción, se estipula que la fórmula iterada para la normalización en todo nivel se corresponde con el re-escalado equivalente post-multiplicación y resulta válido para cualquier constante evaluada correspondiente a número de iteraciones computacionales $k \ge 1$.

---

## Verificación Empírica Computacional

La identidad axiomática es ensayada utilizando la simulación numérica basada en Python (`01_metodo_potencia.py`), para evaluar empíricamente comparando sus valores devueltos en cálculos sobre matrices flotantes sin presentar inconvenientes algorítmicos.

---

## Referencias para Validación

Para profundizar y contar con respaldo académico de los conceptos utilizados en esta demostración (como el Teorema Espectral y el Método de la Potencia Clásico), se recomienda consultar:

* [Wikipedia: Power iteration (Método de la Potencia)](https://en.wikipedia.org/wiki/Power_iteration): Descripción del algoritmo, y fundamentación de las variables y métricas evaluadas analizadas.
* [MIT 18.06 OpenCourseWare - Clase 22 (Diagonalization and Powers of A) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=13r9QY6cmjc): Demostración en la que ahonda cómo una matriz generatriz elevada a la potencia $k$ proyecta consistentemente sobre la base de sus autovectores.
* [MIT 18.06 OpenCourseWare - Clase 29 (Singular Value Decomposition) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=mBcLRGuAFUk): Justificación esencial de la aplicabilidad directa de autovalores de matrices semidefinidas (evaluación formal en la que $B = A^tA$).
