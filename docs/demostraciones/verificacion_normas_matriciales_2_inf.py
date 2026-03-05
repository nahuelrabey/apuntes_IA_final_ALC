import numpy as np

def verify_matrix_norms_2_inf():
    print("Verificando numéricamente: (1/sqrt(n))||A||_inf <= ||A||_2 <= sqrt(n)||A||_inf")
    
    np.random.seed(42)
    sizes = [2, 5, 10, 50]
    n_trials = 500
    
    for n in sizes:
        inv_sqrt_n = 1.0 / np.sqrt(n)
        sqrt_n = np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            # Matriz aleatoria n x n
            A = np.random.randn(n, n)
            
            norm_inf = np.linalg.norm(A, ord=np.inf)
            norm_2 = np.linalg.norm(A, ord=2)
            
            # Verificar desigualdades
            lower_ok = inv_sqrt_n * norm_inf <= norm_2 + 1e-12
            upper_ok = norm_2 <= sqrt_n * norm_inf + 1e-12
            
            if not (lower_ok and upper_ok):
                success = False
                break
                
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión {n}x{n}: Verificadas {n_trials} matrices.")

if __name__ == "__main__":
    verify_matrix_norms_2_inf()
