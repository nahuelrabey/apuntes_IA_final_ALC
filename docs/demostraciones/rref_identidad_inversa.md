# Demostración: Pivotes, RREF y la Matriz Identidad

## Interpretación de la Afirmación

El recorte del Teorema de la Matriz Inversible (*IMT*) postula que para una matriz cuadrada $A$ de tamaño $n \times n$, es exactamente equivalente afirmar:

1. "La matriz $A$ tiene $n$ pivotes."
2. "La Forma Escalonada Reducida por Filas (RREF) de $A$ es la **matriz identidad** $I_n$."

Además, remata asegurando que este fenómeno es la base teórica de por qué funciona el famoso procedimiento para calcular la matriz inversa algebraicamente.

---

## ¿Qué es exactamente un "Pivote"?

Para desmitificar el nombre, pensemos en una matriz cruda llena de números, a la cual empezamos a hacerle operaciones de fila (sumas, restas, multiplicaciones por escalares) con el único objetivo de triangularla (dejar ceros abajo).

**Un pivote (o *leading entry*) no es más que el primer número distinto de cero que te encontrás al leer una fila de izquierda a derecha**, *siempre y cuando la matriz ya esté debidamente escalonada*.

Imaginá este proceso como armar escalones en una escalera:

- Te paras en la primera fila. Lees de izquierda a derecha. El primer número no nulo que tocaste, lo marcás con fibrón. **Ese es el primer pivote.**
- Para que sea una escalera válida, todos los números que vivan *exactamente abajo* de ese pivote en la misma columna, tenés la obligación matemática de aniquilarlos convirtiéndolos en cero operando las filas.
- Una vez que limpiaste la columna, bajás al segundo renglón. Volvés a leer de izquierda a derecha. El primer número que te choque (que lógicamente debió nacer más a la derecha que el anterior por la limpieza que hiciste), lo marcás. **Ese es tu segundo pivote.**
- Y así vas bajando y armando la escalera.

### ¿A qué le dicen "Tener $n$ pivotes"?
Si tu matriz es de $3 \times 3$, "tener 3 pivotes" significa poder armar una escalera perfecta de 3 escalones que bajan sostenidamente de la esquina superior izquierda a la inferior derecha. Ninguna fila colapsó enteramente en ceros, y cada columna es sostenida firmemente por su propio escalón marcado en fibrón.

Un pivote es, esenciálmente empírico, la **"espina dorsal"** que sostiene viva la información de una columna y una fila al mismo tiempo frente a las cancelaciones por Gauss.

---

## Demostración Mutua ($1 \iff 2$)

### Parte A: Si tiene $n$ pivotes $\implies$ Su RREF es la Identidad

Imaginemos una matriz cuadrada de $n$ filas por $n$ columnas. Si nos aseguran que posee **$n$ pivotes** detectados tras aplicarle el método de Eliminación Gaussiana, significa geométricamente que logramos encontrar un "escalón" o pivote principal para *cada una* de las columnas y para *cada una* de las filas. (No hubo ninguna de las columnas que dependiera de otras, ni sobraron "filas de ceros" inútiles en el fondo de la matriz).

Ahora, recordemos las reglas estrictas para llevar la matriz un paso más allá, calculando su Forma Escalonada **Reducida** por Filas (RREF):

1. **Normalización**: Todo elemento que sea pivote debe ser dividido algebraicamente hasta convertirse en un `1`.
2. **Pivotes Aislados**: Todo elemento que exista *por encima o por debajo* del pivote ocupando la misma columna, debe ser atacado reduciendo la fila hasta que pase a valer `0`.
3. **Escalera estricta**: Cada pivote debe situarse ineludiblemente una columna (como mínimo) a la derecha del pivote de la fila superior.

Si acomodamos $n$ números `1` cumpliendo religiosamente esa regla de "escalera" visual y aislamiento nulo dentro de nuestra grilla de $n \times n$, **la única disposición de legos posible** es dibujar una diagonal perfecta y solitaria que arranque arriba a la izquierda y muera empalmando abajo a la derecha, mientras que todo el resto de las celdas circundantes se funden a cero.

Esta estructura naciente y unívoca es la encarnación visual de la **Matriz Identidad ($I_n$)**.

### Parte B: Si la RREF es la Identidad $\implies$ Tiene $n$ pivotes

El camino analítico de retorno nos devuelve lo mismo de manera trivial. 
Si alguien te lanza la matriz $A$ y al reducirla terminás estacionando visualmente en una matriz Identidad ($I_n$), esta última expone claramente un valor `1` liderando cada una de las columnas (ejerciendo como sus $n$ respectivos pivotes inamovibles).

Sabiendo que las operaciones elementales de fila en el álgebra preservan históricamente tanto la cantidad vital como la posición esquelética de los pivotes, ratificamos obligatoriamente que la matriz original $A$ que parió a esta Identidad espiada debía esconder y detentar internamente un total de $n$ pivotes en su mapa.

---

## El Secreto del Algoritmo de la Inversa

La última oración del teorema en cuestión (*"This happens exactly when the procedure in Section 3.5 to compute the inverse succeeds"*) enmascara una epifanía genial sobre el trasfondo de cómo solemos calcular inversas "a mano" en la universidad.

Cuando se nos instruye buscar una inversa, nos obligan a armar una súper-matriz espejada sumando la Identidad artificialmente del lado derecho:

$$[~A \quad \mid \quad I_n~]$$

La mecánica obliga a machacar la mitad izquierda con operaciones elementales por fila hasta transformarla milagrosamente en un bloque ralo $I_n$. Finalmente, se nos asegura ciegas que lo que sobreviva mutilado del lado derecho representará ineludiblemente la matriz inversa, logrando el eslabón: $[I_n \mid A^{-1}]$.

**¿Por qué funciona esta artilugio mágicamente?**

Todo movimiento de ficha que hagas sobre los renglones (multiplicar por constante, o sumar una fila combinada con otra), para el Álgebra Lineal representa fielmente estar "pre-multiplicando" a gran escala tu matriz original $A$ por una matriz unitaria chiquita llamada **Matriz Elemental** ($E_1, E_2, \dots$).

Por lo tanto, al ensañarte hasta llevar a la matriz $A$ al piso escalonado de la Identidad ($I_n$), lo que algebraicamente acaeció entretelones  fue una multiplicatoria en cadena progresiva:

$$(\dots E_3 \cdot E_2 \cdot E_1) \cdot A = I_n$$

Empaquemos imaginariamente a toda esa lluvia densa de operaciones en un único bloque estelar matriz bautizado "C":

$$C \cdot A = I_n$$

¡Un santiamén! Una matriz ($C$) que atacando por flanco derecho a $A$ rinde devolviendo una unitaria Identidad es la acepción más pura y dura del Álgebra Vectorial para dictaminar la identidad de una **Matriz Inversa**.

Es decir que el compendio envasado de operaciones elementales empleadas conformaba exactamente la receta para $A^{-1}$. Y como a la mitad de la derecha de nuestra hoja de calco le adosamos inicialmente $I_n$ y le inyectamos a fuego el mismo paquete homólogo $C$, esta padeció la transfiguración final:

$$C \cdot I_n = C = A^{-1}$$

Acabamos de confirmar que, incuestionablemente, **todo este truco algorítmico depende la vida en que la matriz matriz $A$ original tenga el esqueleto de $n$ pivotes suficientes que propicien mutarla a una $I_n$.** 

En cuanto un renglón se nos extingue a cero (falta de pivotes), el eslabón colapsa, no hay Identidad posible, la caja algorítmica se rompe y procedemos a rotular a esa matriz como irremediablemente Incompleta (o fallida de **no ser inversible**).

??? failure "Análisis del Fallo: ¿A qué hace referencia *'Fewer than $n$ pivots in the first $n$ columns'*?"
    Durante la aplicación de este algoritmo de cálculo, nosotros arrancamos fusionando visualmente la matriz $A$ (tamaño $n \times n$) que pretendemos invertir a la izquierda, pegada a la matriz $I_n$ (tamaño $n \times n$) a la derecha. Obtenemos una nueva "súper-matriz" ampliada ($[A \mid I_n]$) que ahora goza del doble de largo: consta de **$n$ filas** pero **$2n$ columnas**.

    Durante el algoritmo de triangulación, nuestra meta ciega es generar un pivote "1" en cada una de las primeras $n$ columnas para poder despejar una Identidad en la mitad izquierda.
    
    Si en algún momento el proceso arroja un renglón nulo (o sea, las filas chocan por depender linealmente entre sí), ese pivote que debió nacer en el sector de la matriz original $A$ se perderá y "resbalará" hacia la derecha (hacia el sector aportado por $I_n$). 
    
    La frase matemática es estricta: *"Menos de $n$ pivotes están contenidos en las primeras $n$ columnas (la parte no extendida de la matriz)"*. Esto es exactamente así porque al perder un escalón a la izquierda por dependencia lineal, nuestro algoritmo **sólo logró ubicar menos de $n$ pivotes útiles del lado correspondiente a $A$**. 
    
    Como no se lograron agrupar los estelares $n$ pivotes sobre las primeras $n$ columnas, el bloque izquierdo ($A$) no llegó a volverse la Identidad, probando concluyentemente que el rango de $A$ es incompleto ("tiene variables libres") y confirmando que $A$ no posee Inversa.
