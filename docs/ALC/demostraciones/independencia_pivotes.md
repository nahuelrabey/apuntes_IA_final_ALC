# Indepedencia Lineal de las Columnas Pivotales

## Teorema
Dada una matriz $A \in \mathbb{R}^{m \times n}$ y su forma escalonada reducida por filas $R \in \mathbb{R}^{m \times n}$. Si un conjunto de columnas en $R$ son linealmente independientes, entonces las columnas correspondientes en la matriz original $A$ también son linealmente independientes y forman una base para el subespacio columna de $A$ ($Col(A)$).

## Interpretación del Enunciado
El algoritmo de eliminación de Gauss-Jordan transforma una matriz $A$ en su forma escalonada reducida $R$ mediante operaciones elementales de fila. El teorema establece que la relación de dependencia (o independencia) lineal entre las columnas se mantiene invariante bajo estas operaciones. Como las columnas que contienen los *pivotes* (primer elemento no nulo de cada fila) en $R$ forman la base canónica estándar $e_1, e_2, \ldots, e_k$, son independientes; esto garantiza que sus columnas correspondientes en $A$ formen la base del Espacio Columna.

### Demostración
La transformación de $A$ a $R$ puede expresarse como la multiplicación por la izquierda de una matriz invertible $E$ (el producto de todas las matrices elementales de las operaciones de fila):

$$
E A = R

$$
Supongamos que tomamos un subconjunto de columnas pivotales de $R$, que denotamos como la submatriz $R_p$, y las correspondientes columnas de $A$, que denotamos como $A_p$. La relación se mantiene:

$$
E A_p = R_p

$$
Ahora, planteamos la ecuación de combinación lineal igualada a cero para probar la independencia lineal de las columnas originales $A_p$. Sea $x$ un vector de coeficientes:

$$
A_p x = \vec{0}

$$
Multiplicando ambos lados a la izquierda por la matriz invertible $E$:

$$
E (A_p x) = E \vec{0}

$$
$$
(E A_p) x = \vec{0}

$$
Dado que $E A_p = R_p$:

$$
R_p x = \vec{0}

$$
Por definición del escalonado reducido, las columnas pivotales $R_p$ son columnas de la matriz identidad (poseen un único $1$ en la posición del pivote y $0$ en el resto). Por lo tanto, las columnas de $R_p$ son **linealmente independientes**.
Si las columnas de $R_p$ son linealmente independientes, la única solución al sistema homogéneo $R_p x = \vec{0}$ es la solución trivial $x = \vec{0}$.

Dado que $E$ es invertible, la nulidad del producto implica la nulidad del argumento, por lo que la única solución original a $A_p x = \vec{0}$ debe ser también $x = \vec{0}$.

Esto demuestra exhaustivamente que las columnas $A_p$ originales son **Linealmente Independientes**, y dado que el resto de las columnas no-pivotales pueden construirse como combinación de estas, $A_p$ forma una base minimal generadora de todo el Espacio Columna ($Col(A)$).

### Fuente de Referencia

> **Álgebra Lineal y sus Aplicaciones** (4ta Edición), de *David C. Lay*. Capítulo 4.3 (Conjuntos Linealmente Independientes y Bases), Teorema 6: "Las columnas pivote de una matriz $A$ forman una base para $Col(A)$".

---

```python
import numpy as np

def rref(mat):
    """
    Función de utilidad para encontrar la matriz y las columnas pivotales RREF de forma rudimentaria y analógica, dado que numpy nativo carece de RREF expuesto.
    """
    M = np.array(mat, dtype=float)
    m, n = M.shape
    pivots = []
    
    lead = 0
    for r in range(m):
        if lead >= n:
            return M, pivots
        i = r
        while M[i, lead] == 0:
            i += 1
            if i == m:
                i = r
                lead += 1
                if n == lead:
                    return M, pivots
                    
        # Permutar filas
        M[[i, r]] = M[[r, i]]
        
        # Despejar el pivote
        lv = M[r, lead]
        M[r] = M[r] / lv
        
        # Despejar el resto de la columna
        for i in range(m):
            if i != r:
                lv = M[i, lead]
                M[i] = M[i] - lv * M[r]
                
        pivots.append(lead)
        lead += 1
        
    return M, pivots

def run_verification():
    print("Iniciando verificación computacional de la Invarianza de Independencia Lineal por Escalado...")

    np.random.seed(42)
    # Probando con una matriz "Gorda" (m < n) aleatoria, rango completo de filas seguro.
    m, n = 3, 5
    A = np.random.randn(m, n)
    
    # Hacer una columna obviamente dependiente para forzar variables libres
    A[:, 3] = A[:, 0] * 2.5 - A[:, 1] * 1.5

    R, pivot_indices = rref(A)

    print("\n1) Transformación Escalonada Reducida por Filas:")
    print("Matriz A:")
    print(np.round(A, 2))
    print("\nMatriz RREF R:")
    print(np.round(R, 2))
    print("\nÍndices de Columnas Pivotales:", pivot_indices)

    print("\n2) Extrayendo sub-matrices correspondientes a los pivotes (A_p y R_p):")
    A_p = A[:, pivot_indices]
    R_p = R[:, pivot_indices]
    
    print("Columnas de A original (A_p):")
    print(np.round(A_p, 2))
    print("\nColumnas del RREF (R_p):")
    print(np.round(R_p, 2))

    # Comprobación estricta de Independencia Lineal
    # Para la matriz original A_p, el cálculo del rango debe coincidir exáctamente con su longitud de columnas
    rank_Ap = np.linalg.matrix_rank(A_p)
    print(f"\nRango calculado algorítmicamente de A_p: {rank_Ap} (Esperado: {len(pivot_indices)})")
    
    assert rank_Ap == len(pivot_indices), "Fallo empírico: Las columnas extraídas de la matriz original demostraron tener pérdida de Rango, y por consiguiente NO son Linealmente Independientes."

    print("\n[OK] Verificación completada con éxito. Las columnas que empaquetan los recuadros de pivote en el RREF transmutan algorítmicamente y fielmente una base abstracta puramente lineal e independiente del subespacio original.")

if __name__ == '__main__':
    run_verification()

```
