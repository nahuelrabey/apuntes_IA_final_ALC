# Lecciones y Conclusiones Aprendidas

A través de las validaciones teórico-prácticas elaboradas en nuestra metodología de estudio, derivamos las siguientes conclusiones analíticas.

## Examen 21 de jul de 2025

### Ejercicio 1 - SVD

- **Acotación de Errores con Valores Singulares:** Demostramos teóricamente y empíricamente cómo las aproximaciones de rango inferior truncando la SVD acotan su error máximo en norma Euclídea por el valor del siguiente valor singular omitido ($\sigma_2$). Esto reafirma la contundente utilidad de SVD en compresión matemática de datos con pérdidas rígidamente controladas.

- **Convergencia Práctica del Método de la Potencia:** Demostramos mediante álgebra cómo iterar estocásticamente $x^{(k+1)} = \frac{Bx^{(k)}}{||Bx^{(k)}||}$ alinea rápidamente el vector a la componente principal dominante purgando a las demás bases por diferencias en el ratio de sus autovalores $\left(\frac{\lambda_2}{\lambda_1}\right)^k \to 0$. Esto nos permitió desarrollar una rutina de aproximación de rango 1 que iguala analíticamente en su resultado a las librerías industriales complejas.

- **Invarianza Direccional bajo Normalización Iterativa:** Se comprobó analíticamente por inducción y se verificó empíricamente en Python que la re-normalización continua al aplicar el Método de la Potencia no distorsiona el sentido del vector iterativo. Computar escalares divisores paso a paso únicamente ajusta la magnitud subyacente manteniendo la iteración estable, pero el resultado sigue colapsando irremediablemente hacia la misma dirección espacial dictada por el marco teórico rígido de calcular directamente $\frac{B^k x^{(0)}}{||B^k x^{(0)}||}$.

### Ejercicio 2 - Diagonalización

- **Independencia en Espectros Discretos:** Corroboramos en papel y máquina cómo una matriz con valores intrínsecos no repetidos despliega ineludiblemente un abanico hiper-dimensional completo de autovectores que componen una base lineal sin vacíos formales dentro de $\mathbb{R}^n$. Toda matriz estocástica generada artificialmente con auto-valores dispares presentará por ley matemática rango pleno en su subespacio.

- **Isomorfismo de la Matriz Semejante C:** Entender la ecuación universal $AC = CS$ elimina en su completitud el "misterio" de la diagonalización abstracta. Al desgranar paso por paso que la multiplicación por bloques y extraer las variables demostramos cómo esta transformación de autovectores unificada como matriz sencilla enmascara el escalado puro espectral dentro de la base general del sistema.

### Ejercicio 3 - Matrices Ortogonales y Simétricas

- **Teorema de la Traza en Espectros de Matrices Involutivas:** Ante una matriz de dimensión superior, si el marco teórico asegura (debido a su involución $A^2 = I$) que el espectro está condenado a valer $1$ o $-1$, la multiplicidad espectral decanta algebraicamente en un sistema de ecuaciones simplificado aplicando la traza. En el código dedujimos, y Python constató, cómo $Tr(B) = 2$ es una impronta en la materia que denota implacablemente que $k \cdot 1 + m \cdot (-1) = 2$.

- **Transparencia Espectral frente a Factorización SVD:** Asimilamos conceptualmente que las matrices unitarias / ortogonales puras como $A$ carecen de re-escalado intrínseco. Como en su factorización sus valores singulares $\sigma$ no son otra cosa que la raíz de $A^t A$ y $A^t A = I$, toda componente SVD $\Sigma$ de una matriz ortogonal se colapsa en esencia a la pura Matriz Identidad.

### Ejercicio 4 - Cuadrados Mínimos y Aproximaciones

- **Transparencia Hiperespacial Ortogonal:** Cuando se trabaja con un conjunto regido expletamente por Bases Ortonormales en $\mathbb{R}^n$, plantear la minimización explícita sobre un sub-hiperplano se destila en proyectar canónicamente cada componente de modo independiente. Como la matriz gramiana $A^t A$ es de per se la identidad, todo el colosal artilugio del modelo matricial MCO se simplifica al mero filtrado algorítmico de productos internos.

- **Teorema de Pitágoras Multidimensional en Residuos:** Constatamos que la norma de un vector residual originado al truncarse la proyección ortogonal, como aquel error $e = (b - p) = \sum_{k=n+1}^{m} x_k q_k$ es un cálculo exacto. El residuo general de la aproximación es puramente la suma pitagórica del módulo individual esgrimido por las componentes estáticas que quedaron ajenas al plano $A$.

### Ejercicio 5 - Desigualdad de Cauchy-Schwartz

- **Deducción a partir de Geometría Residual:** Constatamos cómo la inquebrantable desigualdad lineal euclidiana emerge directamente del hecho físico de que los errores de proyección de Mínimos Cuadrados arrastran por definición una norma estrictamente positiva ($||e||^2 \ge 0$). Al aislar las magnitudes producto de dichas ecuaciones residuales y conjugarlas, el teorema sale a flote espontáneamente.

- **Universalidad de Vectores Complejos:** El código en iteración aleatoria y masiva confirmó que la matriz Hermitiana transpuesta conjugada ($x^*$) absorbe idénticamente el mismo marco teórico que el dot-product simple en $\mathbb{R}^n$, probando que Cauchy-Schwartz es una ley del Álgebra Lineal que trasciende sin perturbarse hacia todo el abanico del espectro complejo ($\mathbb{C}^n$).

## Examen 24 de feb de 2025

### Ejercicio 1 - Semejanza de Matrices

- **Conservación Nuclear bajo Cambio de Base:** Demostramos computacionalmente que la relación de semejanza es de equivalencia, operando en Python y verificando que deshacer la transformación ($S^{-1} B S$) re-ensambla milimétricamente nuestra matriz $A$, comprobando que si $A \sim B$ ambas enmascaran el mismo sistema subyacente observado desde perspectivas oblicuas diferentes.

- **Invarianza de la Traza y Operaciones Cíclicas:** Validamos probando estadísticamente en el código frente a matrices aleatorias densas que, por consecuencia directa de la regla rastro-cíclica ($Tr(EC) = Tr(CE)$), deformar un sistema lineal de ecuaciones por pre-y-post multiplicación con una matriz base $S$ no deforma jamás la suma geométrica de sus espectros primarios (su traza diagonal se preserva en $B$).

- **Idempotencia Proyectiva Plena ($A^2 = A$):** Corroboramos en papel y computadora un axioma de la geometría lineal: si todos los infinitos valores del espectro propio para dimensiones $\mathbb{R}^n$ se reducen dogmáticamente a los booleanos puros $\{0, 1\}$, entonces no existe re-escalado dinámico que el operador introduzca en la topología asintota. El espacio degenera en una Matriz Idempotente que funciona como pura Proyección Estática inamovible.

### Ejercicio 2 - Semejanza y SVD

- **Uso de Invarianzas y Transformaciones Ortogonales:** En matemáticas (como ocurre con la SVD), aplicar operaciones "isométricas" o transformaciones ortogonales (como fue multiplicar por una matriz de permutación aleatoria computacionalmente, $P$) resulta invariante para las magnitudes nucleares (como el espectro singular). 

- **La Utilidad de la Permutación Aleatoria Computada:** A la hora de verificar propiedades sobre operadores donde "El orden de las filas no altera el resultado estructural", utilizar una matriz de permutación estocástica (`P = I[np.random.permutation(n), :]`) sobre el código es un factor de prueba estupendo. Si la propiedad estadística persiste (ejemplo, la invariabilidad de `np.linalg.svd`) probamos empíricamente la independencia matemática del operador evaluado y confirmamos el modelo numérico.

- **Estabilidad de las Normas (Norma-2):** El script nos demostró cómo este tipo de transformaciones no introducen ruido algorítmico al "estiramiento" máximo de la matriz (la Norma 2) ni a su número de condición. Computarizar $\|PA\|_2$ arrojó consistentemente el mismo resultado de norma debido a que los ortogonales preservan las longitudes vectoriales subyacentes, validando lo deducido con lápiz y papel.

### Ejercicio 3 - Métodos Iterativos

- **Del Radio Espectral al Código Empírico:** Observamos cómo la teoría matricial predice exáctamente el comportamiento iterativo del `while-loop`. A diferencia del algebra matricial analítica, el cálculo numérico involucra medir tiempos (tasas) de procesamiento. Si el análisis formal sostiene que la tasa de convergencia asintótica de una técnica es el doble de la que presenta otra ($\rho(T_{GS}) = \rho(T_J)^2$), computarizar un simple contador de los pasos que toma domar un residuo a una tolerancia límite dada (como $1e^{-10}$) nos ofrecerá una corroboración tajante donde comprobaremos cómo, en efecto, el loop computará la mitad de las iteraciones.

- **Micro-optimizaciones Matemáticas en el Bloque RAM:** La forma iterativa de Gauss-Seidel demuestra conceptualmente un principio de las ciencias computacionales aplicado tempranamente a los algoritmos continuos. La "actualización inmediata" o *in-place updating* (donde $x_2^{(k+1)}$ se reutiliza inmediatamente sin demorarnos a la iteración $(k+1)$ en el bloque en memoria) ahorra recursos del caché y virtualmente duplica la velocidad del procesamiento comparado con Jacobi, que exige retener en memoria secundaria una foto en frío del vector íntegro $X^{(k)}$ del pasado.

### Ejercicio 4 - Mínimos Cuadrados

- **Transformación de Hipóstasis Exponenciales:** Estudiamos cómo la vasta mayoría de las regresiones empíricas no-lineales en la naturaleza se reducen, algorítmicamente, a simples regresiones lineales ordinarias que las computadoras (como `numpy.linalg`) pueden resolver al instante si aplicamos isomorfismos biyectivos. Bajar el exponente $z = a \cdot y^b$ vía logaritmos naturales independiza por la fuerza una función intratable y nos la otorga en bandeja de plata como modelo paramétrico $\beta_0 + \beta_1 X$ compatible con la rígida Ecuación Normal de M.C.O.

- **Validación del Determinante Experimental:** En la programación probabilística de datos es usual arrojarle a la máquina miles de registros esperando que encuentre promedios ponderados. Este ejercicio resalta el valor semántico de la Independencia Lineal como pilar subyacente de la Computabilidad. Diseñar un array de control minúsculo adrede (de apenas 3 puntos de prueba) y observar que es materialmente el número mínimo insalvable para que el algoritmo arroje un `LinAlgError` si no reparamos en la dependencia, permite trazar una raya visible entre un algoritmo "que funciona de casualidad" y un entendimiento total de las fronteras matemáticas de las librerías estadísticas subyacentes.

## Examen 07 de ago de 2025

### Ejercicio 1 - Proyectores Oblicuos vs Ortogonales

- **Geometría de la Intersección Nula:** Validamos computacionalmente que construir un proyector genérico $P$ impone armar su base aglomerando $Im(P) \oplus Nu(P)$. El cálculo del determinante de esta matriz base ensamblada es la prueba irrefutable de que dicha suma directa conforma a todo $\mathbb{R}^n$, un paso ineludible para garantizar la viabilidad del proyector.
- **Asimetría de la Oblicuidad:** Contrastamos en código que si bien $P^2 = P$ dictamina la existencia fundamental del proyector abstracto, la falta de simetría estructural $P \neq P^T$ es el detonante métrico exclusivo que lo empuja a ser oblicuo en vez de ortogonal puro, sesgando asimétricamente los vectores de entrada al colapsarlos.

### Ejercicio 2 - Cadenas Cíclicas de Markov

- **Frontera Determinística del Círculo Unidad:** Corroboramos en papel y Python que las sub-matrices estocásticas cuyas rutas arman "ciclos herméticos" no-absorbentes inyectan ineludiblemente raíces $k$-ésimas complejas al espectro propio de la matriz global. Esto demuestra formalmente que las cadenas de Markov con estados rotacionales periódicos alojan infinitos autovalores de módulo $| \lambda | = 1$, evitando el decaimiento asintótico en esas sub-secciones.
- **Absorción y Estado Estacionario Unificado:** Experimentamos con un modelo fuertemente conexo final, verificando probabilísticamente que sin importar el vector de estado entrante $v_0$ o su ruido inicial aleatorio, la única clase recurrente y aperiódica traga absolutamente la masa completa del sistema hacia un inquebrantable autovector $\lambda = 1$, confirmando el Teorema Fundamental asintótico de las Matrices Estocásticas.

### Ejercicio 3 - Abstracción de la Pseudoinversa

- **Estabilidad frente a las Ecuaciones Normales:** Verificamos al contrastar fórmulas y simulaciones que la Pseudoinversa de Moore-Penrose $A^\dagger$ no es simplemente una triquiñuela notacional para ocultar la espantosa matriz Gramiana $(A^T A)^{-1} A^T$, sino el verdadero salvavidas algorítmico subyacente de `lstsq`, ya que a través de factorizaciones iteradas en la máquina logra saltearse el catastrófico acto de potenciar al cuadrado el de por sí frágil número de condición de $A$.

### Ejercicio 4 - Sensibilidad Paramétrica y Jacobi

- **Amplificación de Escala no-Lineal:** Calculamos manualmente cotas de perturbación generalizadas que evidenciaron de forma indiscutible cómo incorporar variables hiperbólicas (ej: $k^2$) en elementos críticos de un operador colapsa el condicionamiento general a valores gigantescos $\mathcal{O}(k^2)$, destrozando de origen cualquier confiabilidad numérica.
- **Milagro del Precondicionador Constante:** Sorprendimos al condicionamiento aplicando un mitigador de Jacobi matriz-diagonal elemental, cuya única ronda lateral inyectada transmutó un sistema que tendía a estallar con $k \to \infty$ en uno inofensivo con cota $\approx 6.85$ eternamente rígido e impasible. Esto confirma el enorme poder industrial del precondicionamiento previo a la iteración en gran escala algorítmica.

### Ejercicio 5 - LU y la Fragilidad de Gauss

- **El Concepto de Multiplicador Intacto:** Descubrimos conceptualizando la función algorítmica `LU` y los pasos manuales cómo el corazón matricial colapsa instantáneamente en un *ZeroDivisionError* fatal si cualquier $A^{(k)}_{k k}$ se asoma al nivel nulo exacto en medio del viaje al fondo. El pivoteo (permutación) no es mero orden visual en una computadora, sino el pilar matemático que dictamina si $A$ admite la factorización LU pura, o requiere imperiosamente reensamblarse como una exótica $PA=LU$.
