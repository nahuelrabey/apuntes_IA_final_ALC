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
