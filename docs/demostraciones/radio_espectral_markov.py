import numpy as np

def verify_markov_spectral_radius(n_size=10, num_tests=5):
    """
    Simula matrices estocásticas por columnas aleatorias de tamaño n_size
    y verifica empíricamente que:
    1. El mayor módulo de sus autovalores es 1 (dentro de tolerancia numérica).
    2. El vector de unos e=(1,...,1) es autovector a izquierda (autovector de P.T).
    """
    np.random.seed(42)
    print(f"VERIFICACIÓN TEÓRICA: Radio Espectral de Matrices de Markov")
    print("-" * 65)

    all_passed = True
    for i in range(num_tests):
        # Generar matriz aleatoria con entradas >= 0 (distribución uniforme [0, 1))
        P_raw = np.random.rand(n_size, n_size)
        
        # Normalizar por columnas (para que la suma de cada columna sea exactamente 1)
        # sum_cols tiene shape (n_size,), la estiramos a (1, n_size) para hacer broadcasting
        sum_cols = np.sum(P_raw, axis=0) 
        P = P_raw / sum_cols
        
        # Extraemos los autovalores
        eigenvalues = np.linalg.eigvals(P)
        
        # Obtenemos sus módulos (magnitudes en el plano complejo)
        mods = np.abs(eigenvalues)
        
        # Encontramos el módulo máximo (debería ser el radio espectral)
        spectral_radius = np.max(mods)
        
        # Comprobación de que el autovalor "1" está presente y no hay mayores
        is_radius_one = np.isclose(spectral_radius, 1.0, atol=1e-10)
        all_passed = all_passed and is_radius_one
        
        print(f"Test {i+1}: ρ(P) calculado = {spectral_radius:.10f} | ¿Es 1.0?: {is_radius_one}")
        
    print("-" * 65)
    
    # Verificación del vector propio de P^T
    e_vector = np.ones(n_size)
    P_T_e = P.T @ e_vector
    
    # Comprobación estricta tolerante
    eigen_check = np.allclose(P_T_e, e_vector, atol=1e-10)
    print(f"¿Se cumple P^T * e = e?: {eigen_check}")
    
    if all_passed and eigen_check:
        print("\nResultado: LA PROPIEDAD SE CUMPLE. El radio espectral ρ(P) = 1 estricto.")
    else:
        print("\nError detectado: La propiedad falla o problemas de precisión (allclose).")

if __name__ == "__main__":
    verify_markov_spectral_radius(n_size=50, num_tests=10)
