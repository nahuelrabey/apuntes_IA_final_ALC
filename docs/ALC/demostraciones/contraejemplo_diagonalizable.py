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
