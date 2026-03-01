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
