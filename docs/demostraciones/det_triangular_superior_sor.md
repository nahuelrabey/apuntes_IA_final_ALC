# Demostración: Determinante de una Triangular Superior con Escalar en la Diagonal

## Interpretación del Enunciado

> Dada la descomposición $A = L + D + U$ con $a_{ii} \neq 0$, demostrar que la matriz $((1-\omega)D - \omega U)$ es una **matriz triangular superior** cuya diagonal principal es $(1-\omega)a_{ii}$, y que en consecuencia su determinante satisface:
>
> $$\det\big((1-\omega)D - \omega U\big) = (1-\omega)^n \cdot \det(D)$$

Esta propiedad es un paso clave en la demostración de que $\det(B(\omega)) = (1-\omega)^n$ en el **Método SOR**, ya que permite factorizar el escalar $(1-\omega)$ fuera del determinante de manera controlada, aprovechando la estructura triangular de la matriz y la propiedad de multilinealidad del determinante.

---

## Solución Analítica

### Paso 1: Verificar la Estructura Triangular Superior

Recordemos la anatomía de cada bloque en la descomposición $A = L + D + U$:

- $D$ es **diagonal**: $d_{ij} = a_{ii}$ si $i = j$, y $0$ si $i \neq j$.

- $U$ es **estrictamente triangular superior**: $u_{ij} = a_{ij}$ si $i < j$, y $0$ si $i \geq j$.

- $L$ es **estrictamente triangular inferior**: $l_{ij} = a_{ij}$ si $i > j$, y $0$ si $i \leq j$.

Construyamos el bloque en cuestión entrada a entrada. Para los índices $i, j$:

$$\big[(1-\omega)D - \omega U\big]_{ij} = (1-\omega) d_{ij} - \omega\, u_{ij}$$

Analicemos los tres casos posibles:

- **Si $i > j$ (entrada estrictamente por debajo de la diagonal):** $d_{ij} = 0$ y $u_{ij} = 0$, por lo que la entrada es $0$.

- **Si $i = j$ (entrada diagonal):** $d_{ij} = a_{ii}$ y $u_{ij} = 0$, por lo que la entrada es $(1-\omega)a_{ii}$.

- **Si $i < j$ (entrada estrictamente por encima de la diagonal):** $d_{ij} = 0$ y $u_{ij} = a_{ij}$, por lo que la entrada es $-\omega\, a_{ij}$.

En síntesis, la matriz tiene todos los coeficientes por **debajo de la diagonal iguales a cero**. Esto es precisamente la definición de **matriz triangular superior**.

### Paso 2: Determinar la Diagonal Principal

Del análisis anterior, los elementos diagonales de $(1-\omega)D - \omega U$ son:

$$\big[(1-\omega)D - \omega U\big]_{ii} = (1-\omega)\, a_{ii}$$

### Paso 3: Calcular el Determinante

El determinante de **toda matriz triangular** (superior o inferior) se calcula simplemente como el **producto de los elementos de su diagonal principal**. Esto se desprende directamente de la expansión por cofactores, ya que todos los menores que involucran entradas bajo (o sobre) la diagonal se anulan en cascada.

Aplicando esta propiedad a nuestra matriz triangular superior:

$$\det\big((1-\omega)D - \omega U\big) = \prod_{i=1}^{n} (1-\omega)\, a_{ii}$$

Dado que el escalar $(1-\omega)$ aparece como factor multiplicativo en **cada uno de los $n$ términos** del producto:

$$\prod_{i=1}^{n} (1-\omega)\, a_{ii} = (1-\omega)^n \prod_{i=1}^{n} a_{ii}$$

Y reconociendo que $\displaystyle\prod_{i=1}^{n} a_{ii} = \det(D)$ (por ser $D$ diagonal):

$$\boxed{\det\big((1-\omega)D - \omega U\big) = (1-\omega)^n \cdot \det(D)}$$

Q.E.D.

??? info "Observación: ¿Por qué el determinante de una triangular es el producto de su diagonal?"
    Sea $T$ una matriz triangular superior de orden $n$. Su determinante se define recursivamente mediante la expansión de Laplace por la primera columna. Como todos los elementos $t_{i1}$ para $i > 1$ son cero, el único término no nulo en la expansión es el que involucra la entrada diagonal $t_{11}$:

    $$\det(T) = t_{11} \cdot \det(T_{11})$$

    donde $T_{11}$ es la submatriz de orden $(n-1)$ obtenida borrando la primera fila y columna, que sigue siendo triangular superior. Aplicando inducción sobre $n$, el resultado general es:

    $$\det(T) = \prod_{i=1}^{n} t_{ii}$$

---

## Verificación Empírica Computacional

La fórmula se testea numéricamente en Python para múltiples valores de $\omega$ y matrices $A$ aleatorias, verificando la identidad contra el cálculo directo con `np.linalg.det`:

```python
--8<-- "demostraciones/det_triangular_superior_sor.py"
```
