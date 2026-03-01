# Demostración: Normalización iterativa en el Método de la Potencia

## Interpretación del Enunciado

> El mecanismo fundamental del **Método de la Potencia** normalizado a menudo confunde porque en cada paso iterativo se divide por la norma entera del vector obtenido, pareciendo perder el hilo del vector primigenio $x^{(0)}$. No obstante, podemos probar por inducción que esto es un simple cambio de escala unidimensional.

El objetivo es demostrar matemáticamente y por el principio de inducción que en el Método de la Potencia, re-normalizar el vector resultante a magnitud 1 en cada iteración $k$ produce la misma orientación e idéntica posición en el espacio que aplicar la matriz $B$ elevada a la potencia $k$ directamente sobre el vector inicial $x^{(0)}$ y normalizar recién el resultado final de ese "armatoste".

Es decir, se debe probar que:

$$
x^{(k)} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}
$$

## Solución Analítica (Demostración por Inducción)

Definimos la relación de recurrencia del Método de la Potencia normalizado. Se comienza con un vector inicial $x^{(0)}$ tal que $||x^{(0)}|| = 1$. En cada paso $k \ge 1$ se ejecuta:

$$
x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||}
$$

Se procederá a probar que para todo $k \ge 1$, la proposición $P(k)$ sobre el colapso del vector es verdadera:

$$
P(k): \quad x^{(k)} = \frac{B^k x^{(0)}}{||B^k x^{(0)}||}
$$

### 1. Caso Base ($k = 1$)

Primero evaluamos la aserción universal en su iteración primaria $k=1$ sustituyendo directamente en la fórmula recursiva temporal:

$$
x^{(1)} = \frac{B x^{(0)}}{||B x^{(0)}||}
$$

Lo cual coincide exactamente con la fórmula analítica cerrada propuesta evaluada en $k=1$, debido a la trivialidad algorítmica de que $B^1 = B$. Por lo tanto, el caso base se verifica como correcto.

### 2. Paso Inductivo

Asumimos como **Hipótesis Inductiva (H.I.)** que la proposición es válida y verídica para un cierto paso o iteración anterior $k-1$:

$$
x^{(k-1)} = \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||}
$$

A partir de esta verdad matemática transitoria, debemos demostrar estructuralmente que la proposición también se satisface para el paso global $k$.

Iniciamos partiendo de la forma rigurosa de la definición iterativa computacional impuesta para avanzar en $k$:

$$
x^{(k)} = \frac{B x^{(k-1)}}{||B x^{(k-1)}||}
$$

Sustituimos la variable temporal y arrastrada $x^{(k-1)}$ insertando íntegramente toda nuestra Hipótesis Inductiva previa formulada:

$$
x^{(k)} = \frac{B \left( \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||} \right)}{\left\| B \left( \frac{B^{k-1} x^{(0)}}{||B^{k-1} x^{(0)}||} \right) \right\|}
$$

Recordemos conceptualmente que la norma del denominador en el paso anterior, es decir $c = ||B^{k-1} x^{(0)}||$, es por axioma de espacios geométricos un estricto escalar (número real absoluto estrictamente mayor a 0 si $x^{(0)}$ no está arruinado nulificándose).

Por las propiedades de linealidad escalable irrefutable que gobiernan a las matrices y las normas topológicas, sabemos que para cualquier paramento escalar $c > 0$ y un vector físico libre $v$, pueden "salir fuera" comportándose así:
- $B\left(\frac{1}{c}v\right) = \frac{1}{c} Bv$
- $\left\| \frac{1}{c} v \right\| = \left|\frac{1}{c}\right| \|v\| = \frac{1}{c} \|v\|$

Procedemos ahora a extraer dicho factor numérico común e invisible de escala $\frac{1}{||B^{k-1} x^{(0)}||}$, liberándolo simultáneamente tanto del impacto de la matriz $B$ en el numerador matricial como abriendo las puertas de la magnitud topológica de la norma abstracta en el macro-denominador:

$$
x^{(k)} = \frac{ \frac{1}{||B^{k-1} x^{(0)}||} \cdot B (B^{k-1} x^{(0)}) }{ \frac{1}{||B^{k-1} x^{(0)}||} \cdot \| B (B^{k-1} x^{(0)}) \| }
$$

Dado que este factor numérico es estrictamente un número real no vacío, su existencia superpuesta en la división colapsa en la matriz aritmética cancelándose mutuamente a sí mismo:

$$
x^{(k)} = \frac{ B (B^{k-1} x^{(0)}) }{ \| B (B^{k-1} x^{(0)}) \| }
$$

Aplicando en el paso cúlmine las clásicas y contundentes propiedades de la potenciación abstracta en anillos de matrices ($B \cdot B^{k-1} = B^k$), finalmente arribamos limpios de todo artificio intermedio a:

$$
x^{(k)} = \frac{ B^k x^{(0)} }{ || B^k x^{(0)} || }
$$

### Conclusión

Por el inquebrantable Principio de Inducción Matemática, el argumento queda clausurado: se estipula que la fórmula analítica des-iterada es un axioma válido para cualquier cantidad arbitraria de bifurcaciones computacionales $k \ge 1$. El proceso iterativo de dividir por la norma escalar paso tras paso únicamente cumple con re-escalar el objeto geométrico manteniéndolo en órbita a la bola unidad, sin perturbar por un segundo la dirección o sentido de la topología fundamental esgrimida directamente por el vector $B^k x^{(0)}$.

---

## Verificación Empírica Computacional

La certeza deductiva fue sometida a estrés estocástico por medio del verificador automático estructurado en Python (`01_metodo_potencia.py`), el cual expone vectores al azar bajo ambos esquemas para validar este colapso en el silicio.

---

## Referencias para Validación

Para profundizar y contar con respaldo académico de los conceptos utilizados en esta demostración (como el Teorema Espectral y el Método de la Potencia Clásico), se recomienda consultar:

* [Wikipedia: Power iteration (Método de la Potencia)](https://en.wikipedia.org/wiki/Power_iteration): Descripción enciclopédica del algoritmo, su ritmo de convergencia y demostración analítica general.
* [MIT 18.06 OpenCourseWare - Clase 22 (Diagonalization and Powers of A) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=13r9QY6cmjc): Demostración audiovisual magistral de cómo una matriz elevada a la potencia $k$ proyecta repetidamente sobre la base de sus autovectores ponderada exponencialmente por sus autovalores.
* [MIT 18.06 OpenCourseWare - Clase 29 (Singular Value Decomposition) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=mBcLRGuAFUk): Justificación esencial del armado y propiedades espectrales de matrices semidefinidas (como $B = A^tA$).
