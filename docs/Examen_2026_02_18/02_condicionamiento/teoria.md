# Ejercicio 2: Condicionamiento y Matrices de Kronecker

> **Ejercicio 2.**
> 
> **a)** Probar que si $A \in \mathbb{R}^{n \times n}$ es una matriz inversible y $\| \cdot \|$ es una norma matricial inducida, la condición de A verifica que, para toda $B$ singular:
>
> $$ \frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|} $$
> 
> **b)** Para cada $n \in \mathbb{N}$ se define la matriz $A_n \in \mathbb{R}^{n \times n}$ cuyos coeficientes están dados por 
>
>$$a_{ij} = \frac{1}{n} + \frac{1}{n^2} \delta_{ij}, 1 \leq i, j \leq n$$
>
>donde $\delta_{ij}$ denota el delta de Kronecker.
> 
> - **i)** Probar que $\text{cond}_\infty(A_n) \geq g(n)$ para alguna función $g(n) \sim n^2$.
> - **ii)** Probar que $\text{cond}_2(A_n) \to \infty$ cuando $n \to \infty$.

## Interpretación del Enunciado

El segundo ejercicio ataca radicalmente el concepto de la "Radiación de Condicionamiento". La Primera parte nos pide forjar el famosísimo *Teorema de la Cota de Distancia a la Singularidad*, que reza que el recíproco del Número de Condición es exactamente la distancia relativa más corta desde tu matriz inversible hacia la peor matriz no-inversible asfixiante.

La segunda fase involucra forzar teóricamente una matriz artificial generatriz (Kronecker) que se debilita a medida que su grilla $n$ crece, probando bajo el cristal de dos topologías de normas distintas (Infinita y Espectral 2) que al tender a infinito, el acondicionamiento explota, probando que el problema de resolver su Inversa resultará computacionalmente intratable e inestable a perturbaciones.

---

## Solución del Ejercicio

### Inciso A: Distancia a la Singularidad (Eckart-Young General)

> **a)** Probar que si $A \in \mathbb{R}^{n \times n}$ es una matriz inversible y $\| \cdot \|$ es una norma matricial inducida, la condición de A verifica que, para toda $B$ singular: $\frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|}$

Sabemos por hipótesis que la matriz adversaria $B$ detenta un núcleo fatal: **es puramente singular**. Esto nos autoriza a afirmar a ciencia cierta que existe al menos un vector $x \neq 0$ que al multiplicarse resulta exterminado devolviendo el origen: 
$Bx = 0$.

Forcemos astutamente a insertar a nuestra estrella $A$ en la ecuación reescribiendo el sistema como $(A - A + B)x$:

$$
(A - A + B)x = 0
$$
$$
Ax - (A - B)x = 0
$$
$$
Ax = (A - B)x
$$

Como se ha estipulado que la matriz $A$ es indiscutiblemente inversible (no-singular), posee un operador de reversa lícito universal ($A^{-1}$). Pre-multipliquemos ambos ejes dimensionales por la matriz $A^{-1}$:

$$
A^{-1}(Ax) = A^{-1} (A - B)x
$$

Recordando la ley geométrica axiomática de aniquilamiento de inversas ($A^{-1}A = I$):

$$
Ix = A^{-1}(A - B)x
$$
$$
x = A^{-1}(A - B)x
$$

En este cenit analítico introducimos la herramienta topológica pesada. Envolvemos la igualdad al calor de las leyes de la **Norma Vectorial e Inducida**.
Aplicamos las propiedades inquebrantables de sub-multiplicatividad ($\|Mx\| \leq \|M\| \|x\|$) y combinatoria de normas matriciales ($\|XY\| \leq \|X\| \|Y\|$) al bloque completo:

$$
\|x\| = \|A^{-1}(A - B)x\| \leq \|A^{-1}\| \|(A - B)x\| \leq \|A^{-1}\| \|A - B\| \|x\|
$$

Como el génesis vector garante $x$ era taxativamente **no-nulo** de acuerdo a la nulidad estricta de $B$, su métrica de distancia se encuentra viva y garantizada estrictamente positiva ($\|x\| > 0$). Esto habilita el permiso algebraico directo para dividir la inecuación a ambos flancos por su norma e independizarnos de su existencia:

$$
1 \leq \|A^{-1}\| \|A - B\|
$$

Llegamos al umbral. Traemos al frente la definición fundamental de lo que modela matemáticamente el **Número de Condición**, postulado globalmente como $\text{cond}(A) = \|A\| \|A^{-1}\|$. Aislamos a favor de la Inversa dictaminando geométricamente que:
$$ \|A^{-1}\| = \frac{\text{cond}(A)}{\|A\|}$$

Sustituimos el despeje incrustándolo en la inecuación de vida que habíamos asegurado:

$$
1 \leq \left( \frac{\text{cond}(A)}{\|A\|} \right) \|A - B\|
$$

Re-agrupamos pasando cond dividiendo pasivamente el espectro, y empaquetando al resto sobre la división:

$$
\frac{1}{\text{cond}(A)} \leq \frac{\|A - B\|}{\|A\|}
$$

∎ Queda probada magistralmente la Cota Inferior a la singularidad, independientemente de qué norma natural riga al espacio vectorial.

---

### Inciso B: Metamorfosis de la Matriz Generatriz y la Asintótica del Condicionamiento

Definen la pseudo-matriz $A_n \in \mathbb{R}^{n \times n}$ como un ente donde el espacio en sus celdas se dibuja por:
$$a_{ij} = \frac{1}{n} + \frac{1}{n^2} \delta_{ij}$$

Esta es una forma lúgubre de enmascarar una matriz maravillosamente simple. 
- Cualquier celda en general recibe una cuota base estática de "$\frac{1}{n}$".
- $\delta_{ij}$ (el Delta de Kronecker), se "enciende" ($\delta = 1$) reventando el segundo término _exclusivamente_ si nos posamos sobre celdas diagonales ($i = j$). Para el resto de casilleros infértiles ($i \neq j$), $\delta=0$, abortando la contribución.

Si descomponemos geométrica y analíticamente, constatamos asombrados que la matriz $A_n$ es tan solo el fruto de sumar dos arquitecturas puras: Una matriz gorda compuesta 100% por valores repetitivos "unos", y una rala Matriz Identidad pura:

$$
A_n = \frac{1}{n} E \quad + \quad \frac{1}{n^2} I_n
$$
*(Donde la matriz matriz "E" es el bloque $n \times n$ pletórico de $\mathbf{1}$'s en toda celda).*

#### B-1. Probar cota inferior bajo Norma Infinito ($\text{cond}_\infty$) que envuelve orden cuadrático.

> **ii)** Probar que $\text{cond}_\infty(A_n) \geq g(n)$ para alguna función $g(n) \sim n^2$.

Escarbemos a qué equivale realmente sacar la Norma Infinita $\|A_n\|_\infty$. Esta norma es famosamente catalogada como **"Rayo Máximo de Suma de Fila"**. Mide qué renglón atesora estancada la mayor suma en módulos absolutos.
Al presenciar que $a_{ij}$ carece por completo de signos negativos en su diseño universal (solo divisores positivos frente a dimensiones naturales $n$), sus módulos son trivialmente directos. Además, por su simetría extrema, ¡las sumas de absolutamente todas sus filas detentan calcadas el mismo total exacto!

Revisemos una fila arbitraria cual sea:
Tiene $(n-1)$ elementos cruzados no-diagonales de valor puro $\frac{1}{n}$.
Tiene (1) elemento anaranjado diagonal valeroso coronado como $\left(\frac{1}{n} + \frac{1}{n^2}\right)$.

Sumando sus elementos sin discriminación: 
$$ \|A_n\|_\infty = \sum_{j=1}^n |a_{ij}| = (n-1) \left(\frac{1}{n}\right) + \left(\frac{1}{n} + \frac{1}{n^2}\right)$$
$$ = \frac{n-1}{n} + \frac{1}{n} + \frac{1}{n^2} = \frac{n}{n} + \frac{1}{n^2} = 1 + \frac{1}{n^2}$$

Entonces: **$\|A_n\|_\infty = 1 + 1/n^2$**.

Retomemos nuestro flamante y recién forjado milagro de cota de singularidad provisto en el Inciso A:
$$ \frac{1}{\text{cond}_\infty(A_n)} \leq \frac{\|A_n - B\|_\infty}{\|A_n\|_\infty} $$

Necesitamos invocar en nombre de la ciencia a una letal *matriz adversaria ($B$)*, la cual esté obligada a portar carácter singular.
¿Qué sucedería si le mutilamos toda la diagonal a $A_n$ y nos adueñamos simplemente del armatoste primitivo $\frac{1}{n} E$?
Postulemos a nuestra candidata $B = \frac{1}{n} E$. Esta gigantesca matriz rebalsa ser predeciblemente dependiente con la misma asfixiante monotonía global: todas sus infinitas $n$ filas albergan calcos repetitivos con valores clonados de $\frac{1}{n}$. Al no tener independencia lustral desde su rango 1, **la matriz $B$ elegida es irremediablemente singular**. Y encaja impecable.

Insuflamos esta matriz parásita en nuestra ley métrica para ver cuánta distancia hay. La resta $(A_n - B)$ extermina por fase diametral a todos los "$\frac{1}{n}$" de absolutamente todo el mapa (los bloques llenos colisionan extinguiéndose). El único residuo sobreviviente de este cataclismo de restas es la matriz rala Identidad resquicidul de la diagonal atómica original:

$$(A_n - B) = \frac{1}{n^2} I_n$$

Concebimos la norma parásita que restó aislada: ¿Cuál es el rayo fila máximo absoluto (Norma Infinito) de una Identidad destellada por $1/n^2$? Apenas tiene un único elemento valeroso solitario por fila $\left(\frac{1}{n^2}\right)$. Acertaste, su métrica será taxativamente esa misma cota.
$$\|A_n - B\|_\infty = \| \frac{1}{n^2} I_n \|_\infty = \frac{1}{n^2}$$

Sustituimos finalmente todos nuestros desentramados heroicos dentro de la inecuación del Inciso A para presenciar su cota base:

$$
\frac{1}{\text{cond}_\infty(A)} \leq \frac{\left( \frac{1}{n^2} \right)}{\left( 1 + \frac{1}{n^2} \right)}
$$

Asiendo y traccionando a nuestro objetivo principal ($\text{cond}(A)$) hacia la cima revirtiendo algebraicamente las fracciones (¡Alerta!, invertir de tajo voltea el sentido lógico del signo en la Inecuación mayor/menor $\leq \to \geq$):

$$
\text{cond}_\infty(A) \geq \frac{1 + \frac{1}{n^2}}{\frac{1}{n^2}}
$$
$$
\text{cond}_\infty(A) \geq n^2 \left(1 + \frac{1}{n^2}\right)
$$
$$
\text{cond}_\infty(A) \geq n^2 + 1
$$

∎ Como la afirmación ha parido que $\text{cond}(A)$ crece con un empuje mínimo inexpugnable de emparejamiento parabólico $(n^2 + 1)$, probamos definitivamente la hipótesis de que se adosa indefectiblemente por arriba a una función $g(n) = n^2 + 1$, donde categóricamente visumbramos que **su cota de orden creacional estocástico se alínea estricta y rígidamente al patrón $g(n) \sim \mathcal{O}(n^2)$**.

??? info "Observación Teórica: Elección Táctica de Matrices Antagónicas"
    La belleza poética envuelta en las Demostraciones de Cotas Inferiores yace enteramente en el intelecto humano al saber **"inventar y forzar"** la matriz más maliciosa imaginable para estresar el Teorema en nuestro propio provecho algorítmico computacional. En este asalto, "fabricamos" a costa propia con un rango paupérrimo ($1$), pero lo suficientemente parecida facialmente al sujeto en prueba, rindiendo la resta inmensamente provechosamente pura.

---

#### B-2. Explotación Asintótica a Infinito bajo Norma Espectral 2

> **iii)** Probar que $\text{cond}_2(A_n) \to \infty$ cuando $n \to \infty$.

Para este eslabón debemos desempolvar y mutar momentáneamente de herramienta. Abordar Condicionamiento Espectral 2 (basado en autovalores) precisa asir la relación entre el máximo y el mínimo elongamiento que sufre el hiperespacio esférico matriz ($ \kappa_2(M) = \frac{|\lambda_{\max}|}{|\lambda_{\min}|} $), en este caso siendo ella plenamente una matiz *simétrica pura*, su desmembramiento SVD clona y calca enteramente a su propia radiografía intrínseca de autovalores.

Procedamos a autopsiar la matriz $A_n$ a finística, desvelando a qué autovalores rige el universo frente a esta red Kronecker con componentes: $\frac{1}{n^2} I_n + \frac{1}{n} E$.

Si inyectamos un vector alejado de la base, el universal "repleto de unos" denotado habitualmente como $\mathbf{1} = (1, 1, \dots, 1)^T$. Observamos atónitos empíricamente qué hace el embudo estocástico $E$ contra él: cada renglón lleno agrupa $n \times 1$; la multiplicación $E \cdot \mathbf{1}$ revienta con la sumatoria global $n$ multiplicada nuevamente por el propio vector de unos $\to n \cdot \mathbf{1}$.

Insuflamos la revelación computada generalizadamente y se la arrojamos a toda la entidad de nuestra pseudo matriz $A_n \cdot \mathbf{1}$:

$$ A_n \cdot \mathbf{1} = \left( \frac{1}{n^2} I_n + \frac{1}{n} E \right) \mathbf{1} = \frac{1}{n^2} I_n\mathbf{1} + \frac{1}{n} E\mathbf{1} $$
$$ = \frac{1}{n^2} \mathbf{1} + \frac{1}{n} (n \mathbf{1}) = \left(\frac{1}{n^2}\right) \mathbf{1} + 1 \cdot \mathbf{1} $$
$$ A_n \cdot \mathbf{1} = \left(1 + \frac{1}{n^2}\right) \mathbf{1} $$

Emerge frente a nuestros aturdidos ojos el corolario dictatorial: Acabamos de aislar fehacientemente a $\left(1 + \frac{1}{n^2}\right)$ como un **Autovalor Lícito Dominante** preñado originariamente del autovector base genético $\mathbf{1}$.

Mutelemos la búsqueda ahora hacia rastrear escalones recíprocos de contracción mínima en la geometría. Proveemos adentrar el campo ortogonal del vector $\mathbf{1}$. Todo vector $v$ en su ortogonal goza la particularidad letal impuesta que la sumatoria interna destructiva de todos sus sub-componentes se desangra y dictamina un ríspido $0$. Entonces, enfrentar en contracción la mole de repetitivos con algo que agrupa todo y suma nulo en red, resulta aniquilado: $E \cdot v = 0$.

Lancemos sin piedad esta daga $v$ a lo espeso de la matriz madre originaria ($A_n \cdot v$):

$$ A_n \cdot v = \left( \frac{1}{n^2} I_n + \frac{1}{n} E \right) v = \frac{1}{n^2} v + \frac{1}{n} (0) = \left( \frac{1}{n^2} \right) v $$

Vuelve a emerger colosalmente el segundo estrato: El factor micro-homotético remanente $\frac{1}{n^2}$ se proclaman orgullosamente constituirse como **el conjunto autovalor más insignificante restrictivo posible**, multiplicándose transversalmente a través de las restantes $n-1$ dimensiones espaciales ortogonales.

Teniendo capturados a nuestra fiera reina engordada máxima $\left(\lambda_{max} = 1 + \frac{1}{n^2}\right)$ y al escabullidizo ratoncito aplastado diminuto autovalor mínimo $\left(\lambda_{min} = \frac{1}{n^2}\right)$, la métrica de Condición Espectral Suprema queda atada y sellada puramente a la relación perimetral de tamaño (razón de colapso esférico por estirado elíptico base):

$$ \text{cond}_2(A_n) = \frac{|\lambda_{\max}|}{|\lambda_{\min}|} = \frac{1 + \frac{1}{n^2}}{\frac{1}{n^2}} $$

Operando la distribución fraccionada para desvelar el desnivel numérico natural:

$$ \text{cond}_2(A_n) = \left( 1 + \frac{1}{n^2} \right) \cdot n^2 = n^2 + 1 $$

Con el escenario enteramente limpio, desprovistos de bruma topológica y portando el motor de crecimiento puro algebraico empacado en $(n^2 + 1)$, empujamos el experimento calculístico al finístico tendiendo geométricamente $n \to \infty$:

$$
\lim_{n \to \infty} \text{cond}_2(A_n) = \lim_{n \to \infty} (n^2 + 1) = \infty
$$

∎ Probado y finiquitado analíticamente. Cuando se expande masivamente la red perimetral pseudo generatriz $n$, **su Condición estocástica número 2 detona hacia el irremediable Infinito**, presagiando una extrema fragilidad letal de inversión informática donde variarle infinitesimales resquicios arroja hecatombes masivas numéricas imprevisibles, volviendo fútil su despeje vía sistemas algorítmicos comunes en matrices vastas.

---

## Verificación Empírica Computacional (Radio Asintótico en Normas)

Emplearemos una verificación NumPy agresiva iterando e incrementando la dimensionalidad perimetral $N$ con la intención de someter matrices en base algorítmica y presenciar visual e implacablemente la explosivo exponencial de $n \to \infty$ sobre su condicionamiento 2, contrastando las cuotas subyacentes predichas de la matriz Kronecker singular.

```python
--8<-- "Examen_2026_02_18/02_condicionamiento/verificacion.py"
```
