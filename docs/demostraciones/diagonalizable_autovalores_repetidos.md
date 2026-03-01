# Demostración: Matriz Diagonalizable con Autovalores Repetidos

> **Enunciado a Demostrar:**
> Es falso afirmar que toda matriz diagonalizable requiere autovalores estrictamente distintos. Demostrar, mediante un contraejemplo analítico y su validación empírica, que una matriz estocástica (de Markov) puede ser diagonalizable teniendo autovalores repetidos (en particular, $\lambda=1$ con multiplicidad algebraica $> 1$).

## Interpretación del Enunciado

La confusión metodológica frecuente es asumir que la implicación "Autovalores distintos $\implies$ Diagonalizable" funciona de forma bidireccional.
Para desmentirlo matemáticamente, es suficiente con encontrar una matriz $P$ que posea autovalores repetidos (raíces múltiples en su polinomio característico), pero que a la vez disponga de una base completa de autovectores (sus dimensiones de autoespacios coinciden con sus multiplicidades algebraicas).

## Solución del Ejercicio

### Construcción del Contraejemplo

Consideremos la matriz iterativa $P \in \mathbb{R}^{3 \times 3}$, la cual modela una Cadena de Markov. El estado 1 es absorbente y los estados 2 y 3 transicionan alternadamente entre sí equiprobablemente:

$$
P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0.5 & 0.5 \\ 0 & 0.5 & 0.5 \end{pmatrix}
$$

### Cálculo de Autovalores y Autoespacios

Calculamos el espectro de $P$. Como la matriz está estructurada en bloques principales, podemos aislar los autovalores de la diagonal:
- Del escalar superior: $\lambda_1 = 1$
- Del bloque inferior $\begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{pmatrix}$: $\lambda_2 = 1$ y $\lambda_3 = 0$.

El autovalor $\lambda=1$ posee multiplicidad algebraica igual a 2.

Para testear si la matriz es diagonalizable, debemos analizar la dimensión del autoespacio $E_{\lambda=1}$ frente a la multiplicidad de su raíz. Resolviendo $(P-I)v = 0$:

$$
\begin{pmatrix} 0 & 0 & 0 \\ 0 & -0.5 & 0.5 \\ 0 & 0.5 & -0.5 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \implies v_2 = v_3
$$

Cualquier vector del nulo toma la forma $(v_1, v_2, v_2)^T$. Esto nos permite parametrizar y obtener dos autovectores generadores linealmente independientes para $E_{\lambda=1}$:

$$
w_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad \text{y} \quad w_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
$$

Como la dimensión del autoespacio (multiplicidad geométrica) para $\lambda=1$ es 2 (idéntica a su multiplicidad algebraica), y $\lambda=0$ provee su propio autovector base, la matriz goza de un set de 3 autovectores L.I. (rango completo en $\mathbb{R}^3$).
La **matriz es diagonalizable** iterativamente y permite una descomposición en bloques $P = VDV^{-1}$, invalidando que las raíces múltiples le prohíban la diagonalización.

## Verificación Empírica Computacional (NumPy)

En consonancia matemática para contrarrestar flotantes, inyectamos en un sandbox estandarizado el contraejemplo en cuestión:

```python
--8<-- "demostraciones/contraejemplo_diagonalizable.py"
```
