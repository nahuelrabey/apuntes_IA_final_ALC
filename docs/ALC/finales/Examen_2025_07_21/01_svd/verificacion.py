import numpy as np

def run_tests():
    print("--- Verificación Inciso A ---")
    np.random.seed(42)  # Para la consistencia lógica de todo el script
    n = 5
    A = np.random.randn(n, 2)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    sigma_1, sigma_2 = S[0], S[1]
    
    # Construcción referencial de la aproximación de rango 1
    u1 = U[:, 0].reshape(-1, 1)
    v1 = Vt[0, :].reshape(-1, 1)
    A_tilde = sigma_1 * (u1 @ v1.T)
    
    # Simular vector aleatorio unitario probabilístico (Círculo Unitario)
    theta = np.random.uniform(0, 2 * np.pi)
    x = np.array([[np.cos(theta)], [np.sin(theta)]])
    
    # Efectuar la predicción restada a la original para hallar residuo
    error = np.linalg.norm(A @ x - A_tilde @ x, ord=2)
    print(f"Error calculado euclidiamente ||Ax - A_tilda x||_2:\t {error:.4f}")
    print(f"Cota superior límite exigida analíticamente (sigma_2):\t {sigma_2:.4f}")
    print(f"¿Atiende la aserción teórica? (Error <= sigma_2):\t {error <= sigma_2}")
    
    
    print("\n--- Verificación Inciso B y Solución Empírica Inciso C ---")
    
    B = A.T @ A
    
    # Rutina iterativa solicitada en el inciso C, donde la norma explícita no puede usar linalg.norm
    def best_rank_1_approximation(mat_A, num_iterations=100):
        """
        Rutina puramente axiomática fundamentada en matrices elementales sin svd.
        Halla la aproximación computacional limitándose al producto de matrices algebraico y potencias.
        """
        mat_B = mat_A.T @ mat_A
        
        # Iniciación del vector aleatorio x (Inciso B)
        x_k = np.random.randn(2, 1)
        
        # Iteración asintótica (N -> Infinito, para nosotros 100)
        for _ in range(num_iterations):
            x_k = mat_B @ x_k
            
            # Normalización manual a nivel matricial (x[0]^2 + x[1]^2)^0.5
            norm_xk = (x_k[0, 0]**2 + x_k[1, 0]**2)**0.5
            x_k = x_k / norm_xk
            
        v_1_approx = x_k
        
        # Hallar Rayleigh quotient para aproximar lambda_1
        # Lambda_1 = (v_1^T B v_1) / (v_1^T v_1) => al ser v_1 unitario, omitimos la división.
        lambda_1 = (v_1_approx.T @ (mat_B @ v_1_approx))[0, 0]
        
        # Recuperar parámetro principal sigma_1 como la raíz limitante estática de la varianza espectral
        sigma_1_approx = lambda_1**0.5
        
        # Recobrar u_1 aislando el vector matricial en la relación (A v_1 = sigma_1 u_1)
        u_1_approx = (mat_A @ v_1_approx) * (1.0 / sigma_1_approx)
        
        # Compilar y emparejar la expresión final A_tilde
        A_tilde_approx = sigma_1_approx * (u_1_approx @ v_1_approx.T)
        
        return A_tilde_approx, v_1_approx

    A_tilde_approx, v1_approx = best_rank_1_approximation(A, 100)
    
    v1_true = Vt[0, :].reshape(-1, 1)
    # El producto interno entre dos vectores unitarios paralelos es 1 o -1
    dot_product = float(abs(v1_approx.T @ v1_true)[0, 0])
    print(f"Producto interno abs(v1_approx^T * v1_true):\t\t {dot_product:.6f} (Demuestra el límite en Inciso B)")
    
    print("\n--- Discrepancia Global entre Matrices A_tilde ---")
    divergencia_absoluta = np.sum(np.abs(A_tilde - A_tilde_approx))
    print(f"Desfase posicional absoluto entre nuestra Rutina y la SVD natural: {divergencia_absoluta:.8e}")
    print("¿Son matemáticamente equivalentes sin discrepancia del hardware? (np.allclose):", np.allclose(A_tilde, A_tilde_approx))

if __name__ == "__main__":
    run_tests()
