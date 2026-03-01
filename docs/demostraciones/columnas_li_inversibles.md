# Demostración: Independencia Lineal e Invertibilidad

## Interpretación del Enunciado

> ¿Una matriz cuadrada $A$, bajo el supuesto fundamental de que posee todas sus columnas conformando un conjunto cerrado de **vectores linealmente independientes**, gozará *siempre* de la propiedad unívoca de ser **inversible**?

La respuesta a esta conjetura no sólo es afirmativa a nivel teórico, sino que representa el núcleo central para entender a priori el comportamiento holístico de una transformación lineal sin necesidad real de observar sus entrañas. Si entendemos a las columnas como "ejes" direccionales en el espacio base, la preexistencia de la misma cantidad de ejes independientes que las dimensiones del cuerpo real garantiza un mapeo no destructivo.

---

## Solución Analítica

Desarrollaremos la demostración del **Teorema de la Matriz Inversible (IMT)** conectando la dependencia lineal escalar con la suryectividad (rango) a través de una deducción formal progresiva.

Abordamos una matriz cuadrada arbitraria $A \in \mathbb{R}^{n \times n}$, que se encuentra constituida matemáticamente por una serie concatenada horizontal de $n$ vectores columna, los cuales denotaremos analíticamente como $\{a_1, a_2, \dots, a_n\}$.

$$
A = \begin{bmatrix} | & | & & | \\ a_1 & a_2 & \dots & a_n \\ | & | & & | \end{bmatrix}
$$

### Fase 1: Análisis del Espacio Nulo (Kernel)

Como dicta la consigna originaria, los precursores o vectores columna $\{a_1, \dots, a_n\}$ son un postulado de elementos **estrictamente Linealmente Independientes**.

En el universo del álgebra lineal, la definición universal estipula férreamente que si un conjunto es linealmente independiente (L.I.), la única manera causal por la cual una combinación escalar paralela de esos vectores logrará igualar y devolver el vector nulo ($\mathbf{0}$), es forzosamente a través de la solución trivial donde los escalares valen nulo matemáticamente.

$$
x_1 a_1 + x_2 a_2 + \dots + x_n a_n = \mathbf{0} \quad \implies \quad x_1 = x_2 = \dots = x_n = 0
$$

Por definición básica del producto de una Matriz por un Vector, sabemos que **multiplicar una matriz $A$ por un vector $\mathbf{x}$ es exactamente lo mismo que armar una combinación lineal usando las columnas de $A$**, donde los escalares multiplicadores son justamente los elementos individuales de ese vector $\mathbf{x}$.

Llevando este concepto a nuestro caso particular de estar igualado al vector nulo, la ecuación del sistema homogéneo ($A \mathbf{x} = \mathbf{0}$) queda planteada como:

$$
(Eq. 1) \quad A \cdot \mathbf{x} = \mathbf{0}
$$

Dada la premisa anterior de vectores independientes y su estricta obediencia de colapsar la sumatoria en ceros, probamos innegablemente que su solución subyacente obliga a que $\mathbf{x} = (0, 0, \dots, 0)^T = \mathbf{0}$.

Que la solución única en todo su hiperespacio dimensional real sea ineludiblemente trivial, certifica entonces geométricamente que el **Núcleo de la transformación** (*Kernel o Null Space*, $\text{Nul}(A)$) se encuentra totalmente desierto, contenido únicamente por el propio origen:

$$
\text{Nul}(A) = \{\mathbf{0}\}
$$

Que el kernel se haya comprobado nulo implica la preexistencia de un mapeo estrictamente inyectivo (uno a uno). Al ser $A$ una inyección perfecta, dos vectores nunca colapsarán sobre un mismo punto homónimo destructivo tras la linealidad.

### Fase 2: Aplicación del Teorema del Rango

El segundo paso de eslabonamiento dogmático de nuestro silogismo consiste en apoyarnos en la fortaleza del **Teorema del Rango-Nulidad** (*Rank-Nullity Theorem*). La ley cardinal vinculante entre subespacios dictamina que para cualquier matriz de $n$ columnas su relación inter-espacial dimensional ha de ser balanceada:

$$
\dim(\text{Col}(A)) + \dim(\text{Nul}(A)) = n
$$

*(Donde $\text{Col}(A)$ es el subespacio columna que denota hacia cúantas dimensiones estamos estirando el mapeo, y el nulidad atañe las colapsadas).*

Basados en el colosal descubrimiento obtenido en nuestra *Fase 1* ($\dim(\text{Nul}(A)) = 0$), su reemplazo unívoco arroja la siguiente verdad indomable por despeje directo:

$$
\dim(\text{Col}(A)) + 0 = n
$$

$$
\text{Rango}(A) = n
$$

El dictamen expone en base a esto que el alcance perimetral de las combinaciones posibles ($\text{Col}(A)$), logra abarcar imperiosamente toda la totalidad de dimensiones del subconjunto destino de imagen (es un operador $\mathbb{R}^n \to \mathbb{R}^n$). Como el subespacio es coincidente y abarcativo con todo el espacio de base, demostramos irrefutablemente que **la matriz opera de manera totalmente sobreyectiva**.

### Conclusión Axiomática

Demostramos empíricamente cómo al concatenar lógicamente las ramificaciones abstractas de las columnas:

1. Al albergar exclusivamente vectores independientes, su núcleo colapsó en $\mathbf{0}$ garantizando la **Inyectividad** pura matricial.
2. Esta nulidad dictaminó, vía Teorema del Rango, un Rank $n$ de cobertura completa que certificaba que las columnas eran una base real, validando la **Sobreyectividad** paralela.

En todo campo abstracto funcional, cualquier mapa originario o transformación abstracta en $n \times n$ que garantice gozar en plenitud y en simultaneo de propiedades inyectivas como sobreyectivas, detenta geométricamente el título de *Función Biyectiva*.

Por doctrina unívoca matemática, **toda transformación lineal que sostenga de forma ininterrumpida una correlación biyectiva es lógicamente reversible en el espacio**, y el acto algebraico singular correlativo a una función que se puede deshacer es, indudablemente, que **su operadora subyacente ($A$) califique como matriz universalmente inversible**, o no-singular ($\exists A^{-1}$ y $\det(A) \neq 0$).

∎

---

## Verificación Empírica Computacional

La correspondencia teórica subyacente planteada entre el rango o independencia de un set vectorial original que compone la estructura medular (*core*) de una matriz y el consecuente nacimiento instantáneo en paralelo de su propiedad de invertibilidad, es testeada incansablemente bajo el siguiente simulador en Python.

```python
--8<-- "demostraciones/columnas_li_inversibles.py"
```

---

## Bibliografía y Recursos Educativos

Para la consolidación y anclaje mnemotécnico al respecto de este fenómeno, referirse a:

### 📖 Libros de Texto y Artículos

- **Libro: Álgebra Lineal y sus Aplicaciones (David C. Lay)**. *Capítulo 2.3: Caracterizaciones de matrices invertibles*. El autor fundamenta allí el renombrado y pilar **Teorema de la Matriz Inversible** (IMT). Dicho compendio abarca un listado inquebrantable de $12$ afirmaciones homólogas estocásticas, donde demuestra que los equivalentes $A$ es *invertible* (Afirmación A) están atados per sécular a que *La ecuación $Ax=0$ sólo admite la solución trivial* (C), y a su vez *Las columnas de $A$ operan como un conjunto L.I.* (E). Si una resiste el fallo, resiste sistemáticamente todas al ser homomórficamente análogas.

### 🌐 Sitios Web Universitarios

- **[Interactive Linear Algebra (Georgia Tech)](https://textbooks.math.gatech.edu/ila/invertible-matrix-thm.html)**: Libro de texto interactivo abierto creado por la universidad Georgia Tech. En la subsección *3.6 - The Invertible Matrix Theorem*, prueba de manera concisa y análoga a nuestro apunte cómo el hecho de que el núcleo sea $0$ (o lo que es lo mismo, independencia lineal) fuerza a que el rango de la matriz sea pleno y, por ende, goce de la propiedad de ser invertida por existir una correspondencia uno a uno (biyectiva).

### 🇺🇸 Videos en Inglés

- **[The Invertible Matrix Theorem (Dr. Trefor Bazett)](https://www.youtube.com/watch?v=kYJj06Gz0Cg)**: El Dr. Bazett explica pedagógica y geométricamente la lista gigantesca de condiciones que colisionan y significan exactamente lo mismo al momento de hablar de matrices invertibles, partiendo justamente desde el requerimiento de conformar Independencia Lineal y el Nulaje trivial del kernel.
