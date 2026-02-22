# Demostración: Independencia Lineal de Autovectores con Autovalores Distintos

## Interpretación del Enunciado

> Demostrar formalmente el lema matricial que establece que si una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ posee autovalores estrictamente distintos entre sí ($\lambda_i \neq \lambda_j$), entonces sus autovectores correspondientes $\{v_1, v_2, \dots, v_n\}$ son un conjunto de vectores **linealmente independientes**.

La importancia vital de este teorema radica en que es la base misma de la **diagonalización**. Si una matriz de orden $n$ logra disponer de $n$ autovectores independientes, éstos formarán una Base para todo el hiperplano $\mathbb{R}^n$, posibilitando armar una matriz de permutación $P$ invertible que desemboque en un cálculo como $A = P D P^{-1}$.

Demostraremos deductivamente esta verdad apelando al Principio de Inducción Fuerte sobre el número de autovectores $k$ evaluados simultáneamente.

## Solución Analítica (Demostración por Inducción)

Sea el conjunto base de autovectores no nulos $\{v_1, v_2, \dots, v_k\}$ vinculados individual y correlativamente a los autovalores distintos $\{\lambda_1, \lambda_2, \dots, \lambda_k\}$.
Plantearemos probar que la única combinación lineal que logra satisfacer la ecuación de suma nula es la trivial (es decir, donde todos los coeficientes escalares de la combinación valen rigurosamente cero).

Planteamos la hipótesis inductiva sobre un subconjunto de tamaño $k$:

$$P(k): \quad \text{El conjunto } \{v_1, v_2, \dots, v_k\} \text{ es linealmente independiente.}$$

### 1. Caso Base ($k = 1$)

Si consideramos un único vector extraído $v_1$, evaluamos la obligatoria definición de independencia lineal aislando una constante escalar multiplicadora:

$$c_1 v_1 = 0$$

Por la definición dogmática de autovector, sabemos ineludiblemente que **el vector propio nunca puede ser el vector nulo** ($v_1 \neq 0$). Si un escalar multiplicado por algo no nulo da como resultado $0$, el producto cero implica categóricamente que dicho escalar absorbió el vacío: 

$$c_1 = 0$$

Por ende, aislar a un solo autovector garantiza trivialmente que un conjunto unitario de vectores propios resulte **linealmente independiente**. El caso base $P(1)$ es totalmente verídico y se cumple.

### 2. Paso Inductivo

Procedemos a asumir explícitamente a modo de **Hipótesis Inductiva Fuerte (H.I.)** que la proposición inicial es cierta para una serie de estadios previos ordenados hasta $k \ge 1$. Es decir, suponemos probada la independencia de un conjunto de tamaño $k$:
Si se nos plantea $c_1 v_1 + c_2 v_2 + \dots + c_k v_k = 0$, la única explicación material es que obligatoriamente $c_1 = c_2 = \dots = c_k = 0$.

Bajo este pilar fundamental de fe transitoria en nuestra demostración, **debemos forzosamente demostrar que la proposición prevalece verídica para el paso adyacente extendido $k + 1$**.

Establecemos la ecuación de ligadura lineal original equiparada a $0$ pero incorporando al "invitado especial", el eslabón temporal evaluado $v_{k+1}$:

$$(Eq. 1) \quad c_1 v_1 + c_2 v_2 + \dots + c_k v_k + c_{k+1} v_{k+1} = 0$$

Como primer maniobra táctica, aplicamos linealmente el operador matricial original $A$ pre-multiplicando universalmente a ambos miembros de la ecuación ($A \cdot 0 = 0$):

$$A(c_1 v_1 + c_2 v_2 + \dots + c_k v_k + c_{k+1} v_{k+1}) = 0$$

Expandiendo por rigidez distributiva y sacando a los escalares $c_i$ fuera de la mira del operador:

$$c_1 A v_1 + c_2 A v_2 + \dots + c_k A v_k + c_{k+1} A v_{k+1} = 0$$

Como cada $v_i$ constituye un autovector leal del sistema pre-acordado, el re-escalamiento establece su definición formal de sustitución axiomática ($A v_i = \lambda_i v_i$):

$$(Eq. 2) \quad c_1 \lambda_1 v_1 + c_2 \lambda_2 v_2 + \dots + c_k \lambda_k v_k + c_{k+1} \lambda_{k+1} v_{k+1} = 0$$

Ahora poseemos dos visiones de la misma hipótesis de ligadura nula extendida. El truco analítico sublime es **multiplicar toda nuestra $(Eq. 1)$ virginal por el último valor del espectro singular $\lambda_{k+1}$**, para propiciar una cancelación masiva tras restarlas.

Multiplicando algebraicamente a $(Eq. 1)$ por el escalar $\lambda_{k+1}$:

$$(Eq. 3) \quad c_1 \lambda_{k+1} v_1 + c_2 \lambda_{k+1} v_2 + \dots + c_k \lambda_{k+1} v_k + c_{k+1} \lambda_{k+1} v_{k+1} = 0$$

Efectuamos sin vacilar la sustracción total de ambos polinomios matriciales $(Eq. 2) - (Eq. 3)$. 
Al observar el último eslabón, notamos simetría total de los coeficientes ($c_{k+1} \lambda_{k+1} v_{k+1} - c_{k+1} \lambda_{k+1} v_{k+1}$), por lo que **se anula y desvanece por completo el autovector extendido $v_{k+1}$**, despejando el panorama y envasando en factor común el resto de los coeficientes:

$$c_1 (\lambda_1 - \lambda_{k+1}) v_1 + c_2 (\lambda_2 - \lambda_{k+1}) v_2 + \dots + c_k (\lambda_k - \lambda_{k+1}) v_k = 0$$

¡Observemos esta magna ecuación consolidada! Toda esta aserción abstracta no es otra cosa matemática transvestida que una "Combinación Lineal pura con coeficientes raros" estipulada estrictamente para el subset que va desde $v_1$ hasta $v_k$.
Hagamos un parate semántico en dos leyes inquebrantables de esta fase argumental:

1. **Por consigna rectora del enunciado del Examen**: Todos los autovalores $\lambda$ provistos son rigurosamente **distintos**. Ello certifica que el término factorizado transversal en cada paréntesis $(\lambda_i - \lambda_{k+1})$ nunca, bajo ningún marco causal alternativo o aleatorio, podrá adoptar ni coincidir con un valor numérico cero.
2. **Por nuestra Hipótesis Inductiva Fuerte asumida**: Hemos aceptado y dado fe en el inicio de la deconstrucción que el set $\{v_1, \dots, v_k\}$ conformaba indudablemente aglomerando en masa un recinto Linealmente Independiente de $\mathbb{R}^n$.

Dado que es un conjunto L.I., la ÚNICA manera comprobable para que su sumatoria cruzada desate y devuelva un flagrante cero es que **todos y absolutamente todos los macro-coeficientes integrados atados por izquierda a esos vectores sean equivalentes a cero simultáneamente**. Es decir:

$$c_1 (\lambda_1 - \lambda_{k+1}) = 0$$
$$c_2 (\lambda_2 - \lambda_{k+1}) = 0$$
$$\dots$$
$$c_k (\lambda_k - \lambda_{k+1}) = 0$$

Como ya validamos arriba (Punto 1) que el paréntesis diferencial de las lambdas se prohíbe asimismo anularse por estar acatando la directriz de ser valores intrínsecos diferentes ($\lambda_i \neq \lambda_{k+1}$), las matemáticas empujan unívocamente a que los peones $c$ han de ser rigurosamente todos nulos en esta trágica balanza:

$$c_1 = c_2 = \dots = c_k = 0$$

Al sustituir y acribillar al vacío estos sub-coeficientes en el lecho original extendido virginal $(Eq. 1)$, casi todo el bloque estructural se volatiliza, dejándonos únicamente al sobreviviente $k+1$ de pie en su trinchera:

$$c_{k+1} v_{k+1} = 0$$

Rescatando el razonamiento primigenio que desatamos durante el eslabón embrionario en el "Caso Base" ($k=1$), como sabemos a fe cierta que el vector característico nunca puede adoptar un núcleo nulo o degenerado ($v_{k+1} \neq 0$), la lógica fuerza a una última resolución irreversible:

$$c_{k+1} = 0$$

### Conclusión

Demostramos empíricamente por la técnica de Inducción Fuerte Matemática cómo:
1. Empezando porque un autovector solo e independiente es un set L.I.
2. Construir eslabones asumiendo que un set $k$ resiste linealmente independiente y apilando un vector heterogéneo más $k+1$ genera un efecto de sustracción cruzada.
3. El cual empuja matemáticamente y sin artificios probabilísticos a que tanto todas su constantes base $(c_1 \dots c_k)$ como su constante anexa extra injertada $(c_{k+1})$ sean arrinconadas y anuladas forzosamente en cero absoluto.

Nuestra combinación original $c_1 v_1 + \dots + c_{k+1} v_{k+1} = 0$ claudicó determinando que todos sus componentes $c_i = 0$ individual e inquebrantablemente al mismo tiempo. El corolario universal decreta entonces que la aserción de la Independencia Lineal es perpetuamente abarcativa y general para todo subset de dimension paramétrica arbitraria.

Ergo, **los autovectores asociados a autovalores rigurosamente distintos componen formaciones ineludiblemente linealmente independientes**.

Q.E.D.

---

## Verificación Empírica Computacional

La veracidad de este postulado inductivo abstracto fue sometida a estrés sistémico por medio del validador aleatorio programado en Python, corroborando por flotantes y en repetidos ciclos la premisa sin contradicciones.

```python
--8<-- "demostraciones/02_autovalores_distintos.py"
```
