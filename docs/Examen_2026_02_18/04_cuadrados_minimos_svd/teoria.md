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

## Interpretación del Enunciado (El Alma del Least Squares)

Este ejercicio abandona la topología pura y adentra los pies de lleno en la lutería matemática computacional: **¿Cómo programaríamos internamente nosotros lo que hacen los paquetes estadísticos al predecir curvas?**

1. **La Matriz de Diseño (Regresores)**: Mapear el vector de entradas $x$ frente a las funciones candidatas para originar la "Matriz de Características" o *Design Matrix* ($A$).
2. **Sustitución de Inversas Falsas**: El sistema formal asintótico es sobre-determinado (hay más datos $n$ que pesos de regresión $m$). Ergo, $A\alpha = y$ no posee solución exacta en el mundo natural. Requiere que minizemos su distancia. Para esto matemáticamente forjamos las "Ecuaciones Normales" $\to A^T A \alpha = A^T y$. Su solución exige multiplicar por $(A^T A)^{-1}$, lo que se conoce universalmente como matriz Pseudoinversa $A^+$.
3. **El Inyector SVD Mágico**: En lugar de hacer multiplicaciones engorrosas y ruidosas en flotantes como $(A^TA)^{-1}A^T$, las computadoras reales descomponen a $A$ por SVD ($\to U \Sigma V^T$). Por virtudes algebraicas, la pseudoinversa de Moore-Penrose se recicla exquisita y robustamente invirtiendo solo a las piezas no nulas de la cadena y retrostajando a $U$ y $V$: 
   $$ A^+ = V \cdot \Sigma^{-1} \cdot U^T $$
   (Donde $\Sigma^{-1}$ es trivial de obtener, es simplemente una matriz diagonal repleta de los cocientes $1 / s_i$).

Entonces, el gran vector de coeficientes se logra multiplicando al vector solitario $y$ con las piezas SVD atadas:
$$ \alpha = V \cdot \text{diag}\left(\frac{1}{s}\right) \cdot U^T \cdot y $$

Pasaremos a desgranar directamente el bloque de código que satisface las restricciones tiránicas estipuladas por el examen, recondicionando todo mediante herramientas rasas `NumPy`.

---

## Solución Pragmática (Implementación Python)

Dado que no se permite `lstsq`, nos encargaremos de modelar atómicamente la seccionadora SVD. Construyéndola estrictamente como piden:

```python
--8<-- "Examen_2026_02_18/04_cuadrados_minimos_svd/verificacion.py"
```

### Anatomía del Error Cuadrático (EC)

Habiendo empaquetado los coeficientes "mágicos" ($\alpha$) provenientes de exprimir a la matriz rala descompuesta y ensamblada de su inversa ($V \Sigma^{-1} U^T$), la consigna impone proveer el control de daños, dictando al mundo real cuál es el desajuste total originado del modelo inventado en contraste con la realidad natural cruda.

Matemáticamente, evaluamos al modelo con nuestros pesos hallados alimentándole las bases operativas de muestra:
$$ \text{Predicciones}(\hat{y}) = A \cdot \alpha $$

Computamos la brecha diferencial entre predicción vs observación innegable $y$:
$$ \text{Residuos} = \hat{y} - y = (A \cdot \alpha) - y $$

Como la estadística penaliza a las brechas simétricamente sin importar signos para magnificar fallas grotescas, enjaulamos los residuos perimetrales al cuadrado:
$$ EC(\alpha) = \|\text{Residuos}\|_2^2 = (A \cdot \alpha - y)^T (A \cdot \alpha - y) $$
*(En la programación esto decanta simple y elegante en una acumulación sumatoria mediante producto escalar de sí mismo o elevando al cuadrado sus componentes vectoriales, arrojando un escalar liso y puro)*.
