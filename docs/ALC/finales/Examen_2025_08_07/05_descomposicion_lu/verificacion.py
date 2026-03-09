import numpy as np
import scipy.linalg as la

def descomposicion_lu_plana(A_in, tol=1e-12):
    """
    Intenta un escalonamiento LU sin pivoteo.
    Devuelve (L, U) si es exitoso, (None, None) caso contrario.
    """
    n = A_in.shape[0]
    A = A_in.astype(float).copy()
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n-1):
        if abs(A[k, k]) < tol:
            return None, None
            
        U[k, k:] = A[k, k:]
        
        for i in range(k+1, n):
            L[i, k] = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - L[i, k] * U[k, k:]
            
    # El último término u_nn queda suelto y nunca cae bajo división, puede ser cero sin arruinar LU
    U[-1, -1] = A[-1, -1]
            
    return L, U

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 5...")
    
    A = np.array([
        [ 1,  1, -1,  1],
        [ 1,  0,  1, -1],
        [-1, -1,  0,  1],
        [ 0,  1, -2,  2]
    ], dtype=float)

    # Resoluciones Teóricas (deducidas a mano en Markdown)
    L_teo = np.array([
        [ 1,  0,  0,  0],
        [ 1,  1,  0,  0],
        [-1,  0,  1,  0],
        [ 0, -1,  0,  1]
    ], dtype=float)

    U_teo = np.array([
        [ 1,  1, -1,  1],
        [ 0, -1,  2, -2],
        [ 0,  0, -1,  2],
        [ 0,  0,  0,  0]
    ], dtype=float)

    print("\n1) Verificando producto matricial manual (Teoría):")
    print("Determinante de A: ", np.linalg.det(A)) # Debería ser 0 porque u_nn = 0
    print("L_teo @ U_teo =")
    A_rec = L_teo @ U_teo
    print(np.round(A_rec, 2))
    assert np.allclose(A, A_rec), "Fallo: la L y U teóricas descritas no componen matricialmente a A."

    print("\n2) Verificando Función Algorítmica Python LU plana:")
    L_alg, U_alg = descomposicion_lu_plana(A)
    
    if L_alg is None or U_alg is None:
        print("La matriz no admite LU de acuerdo a la implementación (Pivot cero detectado).")
        assert False, "Fallo: La matriz A natural sí que admite LU."
    else:
        print("L Algorítmico =")
        print(np.round(L_alg, 2))
        print("U Algorítmico =")
        print(np.round(U_alg, 2))
        
        # Validamos aserciones cruzadas
        assert np.allclose(L_teo, L_alg), "Fallo: La L del algoritmo difiere de la L deducida en papel."
        assert np.allclose(U_teo, U_alg), "Fallo: La U del algoritmo difiere de la U deducida en papel."
        assert np.allclose(A, L_alg @ U_alg), "Fallo empírico: L*U reconstituido analgítimico perdió integridad respecto a original A."

    print("\n3) Probando fracaso deliberado con matrices truncadas:")
    # Alteramos el pivote u22 forzándolo artificialmente a cero
    # A_bad = L @ U_bad donde U_bad tiene u22 = 0
    U_bad = U_teo.copy()
    U_bad[1, 1] = 0.0
    A_bad = L_teo @ U_bad
    
    L_bad_res, U_bad_res = descomposicion_lu_plana(A_bad)
    assert L_bad_res is None and U_bad_res is None, "Fallo algorítmico: La función implementada no detectó el colapso del pivote."

    print("\n[OK] Verificación completada con éxito. Implementación sólida testeada contra resoluciones matriciales a nivel componente.")

if __name__ == '__main__':
    run_verification()
