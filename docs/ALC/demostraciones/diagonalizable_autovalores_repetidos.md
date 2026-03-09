# Demostración: Matriz Diagonalizable con Autovalores Repetidos

**Enunciado a Demostrar:**
Es falso afirmar que toda matriz diagonalizable requiere autovalores estrictamente distintos. Demostrar, mediante un contraejemplo analítico y su validación empírica, que una matriz estocástica (de Markov) puede ser diagonalizable teniendo autovalores repetidos (en particular, $\lambda=1$ con multiplicidad algebraica $> 1$).

## Interpretación del Enunciado

Un error común es asumir que la implicación "Autovalores distintos $\implies$ Diagonalizable" funciona en ambos sentidos.
Para refutar esta presuposición matemáticamente, es suficiente construir una matriz $P$ que posea autovalores repetidos (raíces múltiples en su polinomio característico), y que disponga de una base completa de autovectores (sus multiplicidades geométricas resultan iguales a sus multiplicidades algebraicas).

## Solución del Ejercicio

### Construcción del Contraejemplo

Consideremos la matriz iterativa $P \in \mathbb{R}^{3 \times 3}$, la cual modela una Cadena de Markov. El estado 1 es absorbente y los estados 2 y 3 transicionan alternadamente entre sí de manera equiprobable:

$$
P = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0.5 & 0.5 \\ 0 & 0.5 & 0.5 \end{pmatrix}

$$
### Cálculo de Autovalores y Autoespacios

Calculamos los autovalores de $P$. Como la matriz posee una estructura triangular en bloques, los elementos de la diagonal de cada bloque conforman sus raíces:

- Del término $(1,1)$: $\lambda_1 = 1$
- Del bloque $\begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{pmatrix}$: $\lambda_2 = 1$ y $\lambda_3 = 0$.

El autovalor $\lambda=1$ posee multiplicidad algebraica igual a 2.

Para comprobar si la matriz es diagonalizable, analizamos la dimensión del autoespacio $E_{\lambda=1}$ frente a la multiplicidad de su raíz. Resolviendo $(P-I)v = 0$:

$$
\begin{pmatrix} 0 & 0 & 0 \\ 0 & -0.5 & 0.5 \\ 0 & 0.5 & -0.5 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \implies v_2 = v_3

$$
Cualquier vector resultante toma la forma $(v_1, v_2, v_2)^T$. Parametrizando obtenemos dos autovectores generadores linealmente independientes para la base del autoespacio $E_{\lambda=1}$:

$$
w_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad \text{y} \quad w_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}

$$
Como la dimensión del autoespacio (multiplicidad geométrica) para $\lambda=1$ resulta en 2 (idéntica a su multiplicidad algebraica), y al autovalor simple $\lambda=0$ se le asigna un único autovector correspondiente, la matriz expone un conjunto integrado de 3 autovectores linealmente independientes (rango $3$ en $\mathbb{R}^3$).
Por lo tanto, la **matriz es diagonalizable** y se permite su descomposición $P = VDV^{-1}$, refutando que la múltiple multiplicidad algebraica invalide por defecto la capacidad de diagonalización en todas las matrices cuadradas.

## Verificación Empírica Computacional (NumPy)

En forma adicional comprobamos lo obtenido analíticamente con las funciones computacionales standard en la resolución espectral empleando NumPy:

```python
import numpy as np

def verificar_contraejemplo():
    print("--- Verificación de Contraejemplo: Diagonalizable sin Autovalores Distintos ---")
    print("Objetivo: Encontrar una Matriz de Markov P que sea diagonalizable,")
    print("pero que tenga autovalores repetidos (multiplicidad de lambda=1 es > 1).\n")
    
    # Construimos una matriz de Markov block-diagonal
    # Estado 1: Absorbente
    # Estado 2 y 3: Transicionan entre sí
    P = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 0.5, 0.5],
        [0.0, 0.5, 0.5]
    ])
    
    print("Matriz de Transición P:")
    print(P)
    
    # Calculamos autovalores y autovectores
    eigenvalues, eigenvectors = np.linalg.eig(P)
    
    print("\n1) Autovalores de P:")
    # Redondeamos para evitar errores de punto flotante en la visualización
    lambdas = np.round(eigenvalues, decimals=8)
    print(lambdas)
    
    # Verificamos si hay autovalores repetidos
    unique_lambdas, counts = np.unique(lambdas, return_counts=True)
    if any(counts > 1):
        repetidos = unique_lambdas[counts > 1]
        print(f"-> CONCLUSIÓN 1: La matriz NO tiene autovalores distintos. Existen multiplicidades > 1 para lambda={repetidos}.")
        
    print("\n2) Verificando Diagonalizabilidad (Dimensiones del Autoespacio):")
    # Para ser diagonalizable, la matriz de autovectores debe ser inversible (rango = n)
    rank = np.linalg.matrix_rank(eigenvectors)
    print(f"Rango de la matriz de autovectores V: {rank} (esperado para R^3: 3)")
    
    if rank == P.shape[0]:
        print("-> CONCLUSIÓN 2: La matriz posee 3 autovectores linealmente independientes.")
        print("Por lo tanto, matriz P ES DIAGONALIZABLE.")
    
    # Comprobación de P = V * D * V^-1
    try:
        V_inv = np.linalg.inv(eigenvectors)
        D = np.diag(eigenvalues)
        P_reconstruida = eigenvectors @ D @ V_inv
        
        # Validación booleana con floats tolerantes
        if np.allclose(P, P_reconstruida, atol=1e-8):
            print("\n3) Verificación Empírica: P == V * D * V^-1 es VERDADERO.")
            print("El teorema P = V D V^-1 se cumple, validando la diagonalizabilidad frente a autovalores repetidos.")
    except np.linalg.LinAlgError:
         print("Error: No se pudo invertir la matriz de autovectores.")

if __name__ == "__main__":
    verificar_contraejemplo()

```
