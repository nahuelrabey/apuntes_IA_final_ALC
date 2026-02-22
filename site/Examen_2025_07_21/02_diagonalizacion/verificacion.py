import numpy as np

def run_tests():
    np.random.seed(84)
    print("--- Demostrando las Propiedades de la Diagonalización ---")

    # Vamos a generar una Matriz A que garantice nuestros supuestos iniciales
    # n autovalores > 0 y distintos. (Vamos a fijar en este caso n=4)
    n = 4
    
    # 1. Definimos autovalores estrictamente positivos y dispares
    lambdas_true = np.array([12.5, 7.8, 3.1, 1.2])
    S_true = np.diag(lambdas_true)
    
    # 2. Fabricamos una base C aleatoria que sea inversible
    # (El teorema nos dice que autovalores dispares arman una base estocástica)
    C_true = np.random.randn(n, n)
    
    # 3. Formamos la matriz A en la naturaleza y ocultamos los parámetros
    A = C_true @ S_true @ np.linalg.inv(C_true)
    
    # --- INCISO A: Autovectores Base ---
    # Usando el procesador para calcular los autovalores y autovectores en crudo que ve frente a A
    lambdas_calc, C_calc = np.linalg.eig(A)
    
    print(f"\nAutovalores re-calculados nativamente:\n{lambdas_calc}")
    print(f"¿Los {n} valores son estrictamente mayores a 0?:", np.all(lambdas_calc > 0))
    # Para ver si los vectores conforman una Base Rn, su matriz debe tener Rango Pleno (o Det != 0)
    rango = np.linalg.matrix_rank(C_calc)
    det_C = np.linalg.det(C_calc)
    print(f"\nInciso A - ¿Los autovectores de C conforman base de R^{n}?")
    print(f"Rango de la Matriz C calculada:\t {rango} (Debe ser {n} para abarcar R^{n})")
    print(f"Determinante |C| != 0:\t\t {det_C:.5f} != 0")
    print("Resultado: Éxito formal probando Independencia Lineal.")
    
    # --- INCISO B: AC = CS ---
    S_calc = np.diag(lambdas_calc)
    
    LHS = A @ C_calc
    RHS = C_calc @ S_calc
    
    print(f"\nInciso B - Demostrando el Axioma Trascendental AC = CS")
    distancia = np.linalg.norm(LHS - RHS)
    print(f"Norma L2 del residuo (AC - CS) frente a la máquina flotante: {distancia:.5e}")
    # Consideramos np.allclose porque matemáticamente son iguales tras redondear
    print("¿Son funcionalmente la misma matriz? (np.allclose):", np.allclose(LHS, RHS))
    
    # --- INCISO C: Diagonalizabilidad (A = C S C^-1) ---
    print(f"\nInciso C - Demostrando que Matrix es Diagonalizable (Cambio de Base)")
    C_inv = np.linalg.inv(C_calc)
    A_reconstructed = C_calc @ S_calc @ C_inv
    
    distancia_rearmada = np.linalg.norm(A - A_reconstructed)
    print(f"Distancia norma del modelo A comparado a C * S * C^-1: {distancia_rearmada:.5e}")
    print("¿Se reconstruyó sin fallos estadísticos la identidad A? (np.allclose):", np.allclose(A, A_reconstructed))

if __name__ == "__main__":
    run_tests()
