# Ejercicio 4: Cuadrados Mínimos con SVD_rank (Aproximación Numérica)

> **Ejercicio 4.** Se desea aproximar un conjunto de datos experimentales mediante una combinación lineal de funciones dadas $\{f_1, \dots, f_m\}$, encontrando la función $f(x) = \sum_{i=1}^m \alpha_i f_i(x)$ que mejor aproxime los datos en el sentido de cuadrados mínimos, utilizando la descomposición en valores singulares (SVD) reducida por rango.
> 
> **Objetivo:** Determinar los coeficientes $\alpha_1, \dots, \alpha_m$ que minimizan el error cuadrático:
> $$ EC(\mathbf{\alpha}) = \sum_{j=1}^n (f(x_j) - y_j)^2 $$
> con $\mathbf{x} = (x_1, \dots, x_n)$ e $\mathbf{y} = (y_1, \dots, y_n)$ datos experimentales, con $n \ge m$.
> 
> **a)** Implementar una función en python que calcule la matriz $A \in \mathbb{R}^{n\times m}$ asociada al problema de cuadrados mínimos a partir de las funciones y de los datos. Además, asuma que existe $(U, s, V^T) = \text{SVD\_rank}(A)$. La función debe devolver $A$, $U$, $V^T$, $s$.
> 
> **b)** Implementar una función que, utilizando la descomposición del ítem anterior, calcule el vector de coeficientes $\mathbf{\alpha}$ y el correspondiente Error Cuadrático. No se permite el uso del comando algorítmico global `numpy.linalg.lstsq`. Solo se toleran operaciones atómicas (array, dot, diag, .T, @).

## Interpretación del Enunciado

El ejercicio trata sobre la aproximación de datos mediante **Cuadrados Mínimos** utilizando la Descomposición en Valores Singulares (SVD).

1. **Matriz de Diseño**: Se construye la matriz $A$ evaluando las funciones base $f_i$ en los puntos $x_j$.
2. **Sistema Sobre-determinado**: Dado que usualmente el número de datos $n$ es mayor al de funciones $m$, el sistema $A\alpha = y$ no tiene solución exacta. Se busca minimizar el error cuadrático $\|A\alpha - y\|^2$.
3. **Uso de SVD**: La solución de cuadrados mínimos se puede obtener mediante la pseudoinversa de Moore-Penrose $A^+$, calculada a partir de la SVD ($A = U \Sigma V^T$):
   $$ A^+ = V \Sigma^+ U^T $$
   donde $\Sigma^+$ contiene los recíprocos de los valores singulares no nulos.

El vector de coeficientes óptimo es:
$$ \alpha = A^+ y = V \text{diag}\left(\frac{1}{s_i}\right) U^T y $$

---

## Solución Técnica (Implementación Python)

Dado que no se permite `lstsq`, se implementa el cálculo de la matriz $A$ y la resolución del sistema utilizando únicamente operaciones de `NumPy`.

```python
--8<-- "Examen_2026_02_18/04_cuadrados_minimos_svd/verificacion.py"
```

### Cálculo del Error Cuadrático (EC)

Una vez hallados los coeficientes $\alpha$, el error cuadrático se calcula evaluando la diferencia entre las predicciones del modelo y los valores observados:

$$ \hat{y} = A \cdot \alpha $$

$$ \text{Residuos} = \hat{y} - y $$

$$ EC(\alpha) = \|\text{Residuos}\|_2^2 = (A \cdot \alpha - y)^T (A \cdot \alpha - y) $$

Este valor permite cuantificar la bondad del ajuste del modelo a los datos experimentales.
