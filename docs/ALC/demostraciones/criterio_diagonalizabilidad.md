# Demostración: Criterio de Diagonalizabilidad por Bases de Autoespacios

**Teorema a Demostrar:**
Una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ es diagonalizable si y solo si la suma de las multiplicidades geométricas de todos sus autovalores es estrictamente igual a $n$ (el orden de la matriz), lo cual implica que para cada autovalor $\lambda_i$, su multiplicidad algebraica coincide con su multiplicidad geométrica.

## Interpretación del Enunciado

Para que una matriz $A$ pueda descomponerse algebraicamente a través de la fórmula **$A = P D P^{-1}$**, es necesario que la matriz de transferencia $P$ sea válida.
$P$ es la matriz formada por los **autovectores** de $A$ alineados en sus columnas. Para que su respectiva inversa $P^{-1}$ exista matemáticamente, $P$ debe poseer rango completo $n$.
Esto significa que es indispensable hallar un conjunto exacto de $n$ autovectores que conformen un sistema de vectores **Linealmente Independientes (L.I.)**, generando una base en $\mathbb{R}^n$.

## Solución Analítica

Los autovectores que se asocian a un autovalor dado $\lambda_j$ generan un subespacio vectorial llamado **Autoespacio ($E_{\lambda_j}$)**, que corresponde al núcleo o *espacio nulo* de la matriz desplazada $(A - \lambda_j I)$.

La cantidad de autovectores linealmente independientes correspondientes al autovalor $\lambda_j$ está limitada por la dimensión su autoespacio, número que denominamos **Multiplicidad Geométrica (M.G.)**.
Acudiendo al Teorema del Rango-Nulidad:

$$
\text{M.G.}_j = \dim(E_{\lambda_j}) = \dim(\ker(A - \lambda_j I)) = n - \text{rg}(A - \lambda_j I)

$$
### Unión de Bases y Conjunto de Autovectores Totales

Dicho un espectro de $A$ compuesto por $k$ autovalores únicos (donde $k \le n$), el conjunto total de autovectores de autovectores se formará de la unión del conjunto de los extraídos de cada uno de sus autoespacios.

Los **autovectores provenientes de autovalores distintos son siempre linealmente independientes entre sí**. Esto significa que al unir todas las bases individuales extraídas de los subespacios $E_{\lambda_1}, E_{\lambda_2}, \dots, E_{\lambda_k}$, el subconjunto obtenido será íntegramente de elementos independientes.
La cantidad final de componentes correspondientes de autovectores totales será la sumatoria particular estricta de cada multiplicidad geométrica individual de la base:

$$
\text{Cantidad de Autovectores L.I.} = \sum_{j=1}^{k} \text{M.G.}_j

$$
### Consecuencias Estructurales del Teorema

Para que la matriz general sea diagonalizable, el conjunto de autovectores independientes totales debe ser igual al orden matricial $n$.

$$
\text{A matriz} \text{ Diagonalizable} \iff \sum_{j=1}^{k} \dim(E_{\lambda_j}) = n

$$
Adicionalmente, se estipula que una multiplicidad geométrica jamás puede promediar más que la multiplicidad algebraica o repetición modular en la identidad del propio Polinomio Característico ($\text{M.G.} \le \text{M.A.}$), y que la suma de autovalores es estrictamente exactamente igual a $n$. La única forma posible de que la sumatoria alcance el tope $n$, por lo tanto, yace en la propiedad estricta en la cual ninguna de las dimensiones entregue un valor inferior: $\text{M.G.}_j = \text{M.A.}_j \quad \forall \lambda_j$.

    Fin de la observación.

### Conclusión

Si la suma de dimensiones de los autoespacios iguala al orden matricial $n$, es posible estructurar una base generadora compuesta puramente por un conjunto completo de autovectores independientes. Esta matriz estructurada corresponde directamente a una operatoria final regular e inversible de la forma paramétrica de una Descomposición y diagonalizabilidad.

---

## Verificación Computacional

Se valida su comportamiento probabilístico en simulación empleando bloques de Jordan generados a través de la librería `NumPy`, demostrando vía la toleración métrica el funcionamiento de las bases correspondientes frente al fallo.

```python
import numpy as np

def test_diagonalizability(n=5):
    """
    Validation script checking that random constructible diagonalizable
    matrices strictly satisfy sum(M.G.) == n, and non-diagonalizable 
    matrices fail this criteria, withstading float tolerances.
    """
    print(f"--- Verificación Computacional Estocástica: Criterio de Diagonalizabilidad (n={n}) ---\n")
    
    # 1. GENERACIÓN DE MATRIZ DIAGONALIZABLE ASEGURADA
    # Construir M = P D P^-1 con autovalores reales pseudo-aleatorios
    # Nos aseguramos que haya autovalores repetidos para hacer la prueba interesante
    base_eigenvalues = np.random.randint(-5, 5, size=n-2) 
    eigenvalues = np.concatenate([base_eigenvalues, [base_eigenvalues[0], base_eigenvalues[0]]]) # Forzamos repetición
    
    D = np.diag(eigenvalues)
    P = np.random.randn(n, n)
    
    # Aseguramos invertibilidad de P
    while np.linalg.cond(P) > 1e4:
        P = np.random.randn(n, n)
    
    P_inv = np.linalg.inv(P)
    M_diag = P @ D @ P_inv
    
    print("Escenario A: Matriz M_diag (Forzadamente Diagonalizable por construcción)")
    print("Autovalores inyectados:", np.round(eigenvalues, 2))
    
    # Verificación en NumPy
    eigvals, eigvecs = np.linalg.eig(M_diag)
    
    # Agrupamos autovalores únicos usando tolerancias para float (np.isclose equivalent behavior)
    unique_lambdas = []
    for val in eigvals:
        if not any(np.isclose(val, u, atol=1e-5) for u in unique_lambdas):
            unique_lambdas.append(val)
            
    sum_mg = 0
    for u in unique_lambdas:
        # M.G = n - rank(M - lambda*I)
        matrix_to_rank = M_diag - u * np.eye(n)
        rank = np.linalg.matrix_rank(matrix_to_rank, tol=1e-5)
        mg = n - rank
        sum_mg += mg
        
    print(f"=> Suma total de Multiplicidades Geométricas: {sum_mg}")
    if sum_mg == n:
        print("[EXITO] Se cumple el teorema: sum(M.G) igual a n (dimensión) => Matriz Diagonalizable.\n")
    else:
        print(f"[FALLO] La suma {sum_mg} difiere de n={n}.")

    # 2. GENERACIÓN DE MATRIZ NO DIAGONALIZABLE (Bloque de Jordan)
    print("Escenario B: Matriz M_jordan (No Diagonalizable por construcción)")
    # Creamos un bloque de Jordan de tamaño n para lambda=2
    M_jordan = 2 * np.eye(n) + np.diag(np.ones(n-1), k=1)
    
    print("Autovalor inyectado: 2 (con M.A. = n)")
    
    matrix_to_rank_jordan = M_jordan - 2 * np.eye(n)
    rank_jordan = np.linalg.matrix_rank(matrix_to_rank_jordan, tol=1e-5)
    mg_jordan = n - rank_jordan
    
    print(f"=> Suma total de Multiplicidades Geométricas: {mg_jordan}")
    
    if mg_jordan < n:
        print("[EXITO] Se cumple el contra-recíproco: sum(M.G) menor a n => Matriz DEFECTIVA (No Diagonalizable).\n")
    else:
        print("[FALLO] Falló la detección de matriz defectiva.")
        
    print("--- FIN DE LA VERIFICACIÓN ---")

if __name__ == "__main__":
    np.random.seed(42) # Reproducibilidad
    test_diagonalizability(n=6)

```
