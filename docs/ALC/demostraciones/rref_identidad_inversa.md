# Demostración: Pivotes, RREF y la Matriz Identidad

## Interpretación de la Afirmación

El Teorema de la Matriz Inversible (*IMT*) postula que para una matriz cuadrada $A$ de tamaño $n \times n$, las siguientes afirmaciones son equivalentes:

1. "La matriz $A$ tiene $n$ pivotes."
2. "La Forma Escalonada Reducida por Filas (RREF) de $A$ es la **matriz identidad** $I_n$."

Además, establece que esta equivalencia es la base teórica del procedimiento algebraico para calcular la matriz inversa algebraicamente.

---

## Concepto de "Pivote"

Un pivote (o *leading entry*) es el primer número distinto de cero en una fila al leer de izquierda a derecha, habiendo llevado la matriz previamente a su forma escalonada mediante operaciones elementales de fila.

El procedimiento de eliminación de Gauss-Jordan opera de la siguiente manera:

- Al evaluar la primera fila de izquierda a derecha, el primer elemento no nulo es el primer pivote.
- Mediante operaciones de fila, se generan ceros en todas las posiciones directamente por debajo del pivote en esa misma columna.
- En la fila subsiguiente, el primer elemento no nulo, que debe estar a la derecha de la columna del pivote anterior, se define como el siguiente pivote.

### Condición de "$n$ pivotes"
Para una matriz cuadrada de $n \times n$, poseer $n$ pivotes significa que cada una de las columnas y cada una de las filas posee su propio pivote principal, de tal suerte que no existen filas completamente nulas al finalizar el procedimiento de eliminación.

---

## Demostración Mutua ($1 \iff 2$)

### Parte A: Si tiene $n$ pivotes $\implies$ Su RREF es la Identidad

Dada una matriz $n \times n$ con $n$ pivotes, sabemos que existe un pivote por fila y uno por columna. Tras aplicar la eliminación, la matriz está en forma escalonada.

Recordemos las condiciones para llegar a la Forma Escalonada **Reducida** por Filas (RREF):

1. **Normalización**: Todo pivote debe tener un valor de `1` (dividiendo la fila por su valor).
2. **Pivotes aislados**: Todos los elementos por encima y por debajo del pivote en su columna deben ser reducidos matemáticamente a `0`.
3. **Escalón estricto**: Cada pivote debe ubicarse a la derecha del pivote de la fila superior.

Al aplicar estas tres condiciones a una matriz cuadrada de $n \times n$ que posee $n$ pivotes, la única conformación matricial resultante presenta los valores `1` alineados estrictamente en la diagonal principal y todos los demás elementos con valor `0`.

Esta estructura unívoca es la **Matriz Identidad ($I_n$)**. Por lo tanto, $\text{RREF}(A) = I_n$.

### Parte B: Si la RREF es la Identidad $\implies$ Tiene $n$ pivotes

Si la Forma Escalonada Reducida por Filas de una matriz $A$ es la Matriz Identidad ($I_n$), esta matriz resultante cuenta por definición con valores `1` ubicados en cada posición de su diagonal principal a lo largo de las $n$ columnas.

Las operaciones elementales de fila en el álgebra lineal garantizan la contabilidad geométrica de posiciones independientes; por tanto, los valores `1` en la RREF representan ineludiblemente $n$ pivotes presentes estructuralmente en el formato de escalonamiento final originado por la matriz primitiva $A$.

---

## El Procedimiento del Cálculo de la Inversa

El procedimiento convencional para calcular la matriz inversa requiere conformar una matriz aumentada y posicionar la Identidad del lado derecho de la ecuación general:

$$
[~A \quad \mid \quad I_n~]

$$
El algoritmo instruye aplicar operaciones elementales de fila simultáneas sobre la estructura combinada hasta que el sector izquierdo alcance la forma de la Identidad ($I_n$). El producto resultante estacionado en la mitad derecha corresponderá a la matriz inversa: $[I_n \mid A^{-1}]$.

**Fundamento Algebraico**

En Álgebra Lineal, aplicar cualquier operación elemental de fila es matemáticamente equivalente a pre-multiplicar la matriz $A$ por una matriz elemental de igual escala ($E_1, E_2, \dots$).

Someter a la matriz $A$ y llevarla hasta su escalonado de la Identidad ($I_n$), requiere una cadena progresiva de premultiplicaciones por parte de estas elementales estructurales:

$$
(\dots E_3 \cdot E_2 \cdot E_1) \cdot A = I_n

$$
Si se define el producto acumulado de estas matrices limitantes como una matriz $C$:

$$
C \cdot A = I_n

$$
Por definición matricial formal, la matriz $C$ que al pre-multiplicar a $A$ produce la Identidad, es su matriz inversa:

La formulación $C = A^{-1}$ determina la veracidad de su transformación temporal del sector derecho. Al haber iniciado esta fase artificialmente combinándola con la matriz de Identidad ($I_n$), el bloque secundario adquirió las alteraciones factoriales estipuladas por $C$:

$$
C \cdot I_n = C = A^{-1}

$$
El fundamento formal del procedimiento expone que **el algoritmo depende del hecho fundamental de que $A$ es reductible en forma $I_n$. (Por ende, tiene $n$ pivotes).**

Si durante la eliminación se obtiene un renglón nulo que dictamina la falta de un pivote, el paso a $I_n$ es algorítmicamente imposible de cumplir y la matriz correspondiente original no posee inversa estructural.

??? failure "Análisis del Fallo: ¿A qué hace referencia *'Fewer than $n$ pivots in the first $n$ columns'*?"
    Durante la aplicación de este algoritmo de cálculo, se evalúa una matriz aumentada ($[A \mid I_n]$) que adopta una estructura de **$n$ filas** y **$2n$ columnas**.

    El objetivo del proceso es posicionar un número estricto correspondientes a pivotes totales ("1" formales) en las primeras $n$ columnas a ser mapeadas hacia la variable de la Identidad.

    Si el proceso denota dependencia lineal ocasionando que una fila se anule completamente, el espacio asignado por un escalón resbalará a la derecha ubicando y reconociendo el pivote siguiente por afuera del parámetro acotado de $A$.

    El bloque matriz general izquierdo no será igualado funcionalmente a la Identidad en este escenario estricto y consecuente de falta del pivote sobre la variable correspondiente que corrobora la inexistencia de un Rango numérico pleno originario. Como $A$ no cuenta con $n$ pivotes base, no es inversible de raíz.

    Fin del análisis del fallo.
