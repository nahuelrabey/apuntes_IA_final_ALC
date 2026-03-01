# Demostración: Independencia Lineal de Autovectores con Autovalores Distintos

## Interpretación del Enunciado

> Demostrar formalmente el lema matricial que establece que si una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ posee autovalores estrictamente distintos entre sí ($\lambda_i \neq \lambda_j$), entonces sus autovectores correspondientes $\{v_1, v_2, \dots, v_n\}$ son un conjunto de vectores **linealmente independientes**.

La importancia vital de este teorema radica en que es la base misma de la **diagonalización**. Si una matriz de orden $n$ logra disponer de $n$ autovectores independientes, éstos formarán una Base para todo el hiperplano $\mathbb{R}^n$, posibilitando armar una matriz de permutación $P$ invertible que desemboque en un cálculo como $A = P D P^{-1}$.

Demostraremos deductivamente esta verdad apelando al Principio de Inducción Fuerte sobre el número de autovectores $k$ evaluados simultáneamente.

## Solución Analítica (Demostración por Contradicción)

La siguiente demostración está fundamentada en el libro *"Álgebra Lineal y sus Aplicaciones"* (David C. Lay), operando mediante la técnica de contradicción sobre el conjunto dependiente más pequeño posible.

**PRUEBA.** Supongamos, buscando una contradicción, que el conjunto de autovectores $\{v_1, \dots, v_r\}$ es **linealmente dependiente**.

Como cada uno de los vectores propios $v_1$ es no nulo por definición ($v_i \neq 0$), sabemos por teoremas previos de dependencia lineal que al menos uno de los vectores en el conjunto debe ser reducible a una combinación lineal de sus predecesores.

Sea entonces $p$ el índice más pequeño ("*least index*") tal que el vector $v_{p+1}$ es una combinación lineal de los vectores que lo preceden (los cuales, por la misma definición del subconjunto mínimo, asumimos linealmente independientes). Entonces, existirán obligatoriamente escalares $c_1, \dots, c_p$ tales que:

$$
(Eq. 5) \quad c_1 v_1 + \dots + c_p v_p = v_{p+1}
$$

Si multiplicamos ambos lados de la ecuación $(Eq. 5)$ por la matriz original $A$, y utilizamos el hecho fundacional de que $A v_k = \lambda_k v_k$ para cada índice $k$, obtenemos:

$$
c_1 A v_1 + \dots + c_p A v_p = A v_{p+1}
$$

$$
(Eq. 6) \quad c_1 \lambda_1 v_1 + \dots + c_p \lambda_p v_p = \lambda_{p+1} v_{p+1}
$$

En paralelo, podemos tomar nuestra $(Eq. 5)$ inmaculada y multiplicarla directamente en ambos lados por el autovalor extraído $\lambda_{p+1}$, y luego, **restar ese resultado a nuestra nueva ecuación matricial $(Eq. 6)$**. Esto nos deja:

$$
(Eq. 7) \quad c_1 (\lambda_1 - \lambda_{p+1}) v_1 + \dots + c_p (\lambda_p - \lambda_{p+1}) v_p = \mathbf{0}
$$

Dado que el subconjunto anterior $\{v_1, \dots, v_p\}$ era asertivamente nuestro núcleo linealmente independiente, estamos forzados a concluir que todos los "pesos macros" (o coeficientes) en la ecuación $(Eq. 7)$ deben ser rigurosamente un cero absoluto.

Sin embargo, sabemos imperativamente que ninguno de los factores compuestos por la diferencia $(\lambda_i - \lambda_{p+1})$ son cero, **debido a que la premisa fundamental estipula que todos los valores propios son estrictamente distintos**.

Por mera inferencia y despeje matemático, la culpa matemática de anular la ecuación recae íntegramente de que:

$$
c_i = 0 \quad \text{para } i = 1, \dots, p
$$

¡Pero si regresamos e insertamos todos estos ceros absolutos en nuestra primera e inmaculada aserción $(Eq. 5)$, la matemática dictamina catastróficamente que $v_{p+1} = \mathbf{0}$!

Esto es un exabrupto y completamente **imposible**, ya que viola la doctrina de que los vectores propios nunca pueden consistir en el vector nulo. Por ende, como hemos chocado de frente con una contradicción irrompible, nuestra suposición primigenia debe ser falsa.

El racimo $\{v_1, \dots, v_r\}$ jamás pudo haber sido linealmente dependiente desde un comienzo y, por tanto, **debe ser linealmente independiente**. ∎

---

## Verificación Empírica Computacional

La veracidad de este postulado inductivo abstracto fue sometida a estrés sistémico por medio del validador aleatorio programado en Python, corroborando por flotantes y en repetidos ciclos la premisa sin contradicciones.

```python
--8<-- "demostraciones/autovalores_distintos.py"
```

---

## Bibliografía y Recursos Educativos

Para comprender mejor los pasos algebraicos explicados en la demostración por inducción de este documento, a continuación se listan varios recursos externos que recorren y validan la misma secuencia lógica:

### 📖 Libros de Texto y Artículos

- **Libro: Álgebra Lineal y sus Aplicaciones (David C. Lay)**. *Capítulo 5: Valores Propios y Vectores Propios*. El autor introduce formalmente el "Teorema 2" de este capítulo (pag. 273 en la 4ta edición), el cual versa: *Si $v_1, ..., v_r$ son vectores propios que corresponden a valores propios distintos $\lambda_1, ..., \lambda_r$ de una matriz $n \times n$ $A$, entonces el conjunto $\{v_1, ..., v_r\}$ es linealmente independiente.* La demostración en el libro avanza por **contradicción** y utiliza exactamente las mismas restas analíticas presentadas en este apunte para llevar los c-escalares a cero.
- **Libro: Linear Algebra and Its Applications (Gilbert Strang)**. *Capítulo 6*. Strang también formaliza que si poseemos $n$ *eigenvalues* distintos en la matriz $A$, ineludiblemente contaremos con $n$ *eigenvectors* independientes, asegurando la propiedad de que toda matriz simétrica con espectro único puede diagonalizarse como $S \Lambda S^{-1}$.

### 🇪🇸 Videos en Español

- **[Álgebra Lineal - Autovectores. Propiedades de independencia lineal](https://www.youtube.com/watch?v=KmjpJtXbk90)** (Prof. Jesús Soto, UCAM): El video aborda la prueba de una manera sumamente clara y pausada. Muestra precisamente la misma construcción de la ecuación original $\text{Eq. 1}$, la aplicación de la matriz $A$, y la multiplicación por el $n$-ésimo autovalor para forzar la eliminación en la resta.
- **[Autovalores y Diagonalización - Multiplicidad de autovectores](https://www.youtube.com/watch?v=JalJlpAYZvw)** (OpenFING): Clase de facultad universitaria donde se demuestra rigurosamente el teorema iterando el mismo concepto matemático de asumir un subconjunto de multiplicidad $k$ L.I. y verificar el eslabón $k+1$.

### 🇺🇸 Videos en Inglés

- **[Linear Independence of Eigenvectors (Proof by Induction)](https://www.youtube.com/watch?v=Fljli8GcfEs)** (Dr. Peyam): Excelente y pedagógica explicación que arma el Caso Base ($k=1$) logrando que $c_1 = 0$, para luego saltar a lo que denomina "una inducción muy hermosa" documentando exactamente el mismo razonamiento y notación algebraica planteado en este apunte.
