import numpy as np

def testear_equivalencia_sor_estocastica(n, num_tests=1000):
    """
    Simula estocásticamente el Inciso A frente a n-puntos dimensionales valiéndose de NumPy.
    Usando perturbación aleatoria masiva (Monte Carlo).
    """
    tolerancias_pasadas = 0

    for _ in range(num_tests):
        # Generar una matriz random y vector aleatorio
        A = np.random.randn(n, n)
        # Garantizar a_ii no nulo agregando peso a la diagonal (solo para estabilidad numérica)
        np.fill_diagonal(A, np.diag(A) + np.sign(np.diag(A)) * 0.1) 
        
        # Desarmamos el esqueleto (Inciso a)
        D = np.diag(np.diag(A))
        L = np.tril(A, -1)
        U = np.triu(A, 1)
        
        # Generamos variables incógnitas y parámetros iterativos aleatorios estocásticos
        x = np.random.randn(n)
        b = np.dot(A, x)
        
        # Sorteamos un w \neq 0 arbitrario entre un espacio masivo [-10, 10]
        w = np.random.uniform(-10, 10)
        while np.isclose(w, 0): # prevemos el zero marginal
            w = np.random.uniform(-10, 10)
            
        # Planteamos la barrera estocástica Izquierda y Derecha del Inciso a
        lado_izq = np.dot(D + w * L, x)
        lado_der = np.dot((1 - w) * D - w * U, x) + w * b
        
        # Validación bajo Floating Points laxos de arquitectura binaria
        if np.allclose(lado_izq, lado_der, atol=1e-8):
            tolerancias_pasadas += 1

    print(f"✅ Equivalencia de Sistemas SOR pasadas {tolerancias_pasadas}/{num_tests} iteraciones exitosas con np.allclose(). Magia pura.")

def testear_determinante_iterativo(n, num_tests=1000):
    """
    Evalua algorítmicamente y tolerablemente probabilístico el Inciso B:
    det(B(w)) == (1-w)^n.
    """
    tolerancias_pasadas = 0
    
    for _ in range(num_tests):
        A = np.random.randn(n, n)
        np.fill_diagonal(A, np.diag(A) + np.sign(np.diag(A)) * 0.5) 
        
        D = np.diag(np.diag(A))
        L = np.tril(A, -1)
        U = np.triu(A, 1)
        
        w = np.random.uniform(0.1, 1.9)
        
        D_wL_inv = np.linalg.inv(D + w * L)
        matriz_B = np.dot(D_wL_inv, (1 - w) * D - w * U)
        
        # Extracción booleana (Flotante) comparativo del determinante calculado vs la ley probada
        calc_det = np.linalg.det(matriz_B)
        ley_teorica = (1 - w)**n
        
        if np.isclose(calc_det, ley_teorica, atol=1e-5):
            tolerancias_pasadas += 1
            
    print(f"✅ Ley de Determinante det(B)=(1-w)^n validada tolerando punto flotante {tolerancias_pasadas}/{num_tests} matrices aleatorias!")

def test_particular_inciso_c():
    """Validación específica del caso provisto en examen"""
    A = np.array([[2, 1], [1, -1]])
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    # ------------------
    # Evaluamos W=1/2
    # ------------------
    w1 = 0.5
    B_w1 = np.linalg.inv(D + w1 * L).dot((1 - w1) * D - w1 * U)
    eigenval_1 = np.linalg.eigvals(B_w1)
    rho_1 = np.max(np.abs(eigenval_1))
    
    print(f"--- Caso w=1/2 ---")
    print(f"B(1/2) computacional = \n{B_w1}")
    print(f"Rho detectado: {rho_1:.3f} | ¿Converge? {'Sí' if rho_1 < 1 else 'No'}")
    
    # ------------------
    # Evaluamos W=3/2
    # ------------------
    w2 = 1.5
    B_w2 = np.linalg.inv(D + w2 * L).dot((1 - w2) * D - w2 * U)
    eigenval_2 = np.linalg.eigvals(B_w2)
    rho_2 = np.max(np.abs(eigenval_2))
    
    print(f"--- Caso w=3/2 ---")
    print(f"B(3/2) computacional = \n{B_w2}")
    print(f"Rho detectado: {rho_2:.3f} | ¿Converge? {'Sí' if rho_2 < 1 else 'No'}")


if __name__ == "__main__":
    testear_equivalencia_sor_estocastica(n=50, num_tests=500)
    testear_determinante_iterativo(n=30, num_tests=500)
    print("\n")
    test_particular_inciso_c()
