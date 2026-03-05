import numpy as np

def verify_matrix_norms_1_2():
    print("Verificando numéricamente: (1/sqrt(n))||A||_1 <= ||A||_2 <= sqrt(n)||A||_1")
    
    np.random.seed(42)
    sizes = [2, 5, 10, 50]
    n_trials = 500
    
    for n in sizes:
        inv_sqrt_n = 1.0 / np.sqrt(n)
        sqrt_n = np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            A = np.random.randn(n, n)
            
            norm_1 = np.linalg.norm(A, ord=1)
            norm_2 = np.linalg.norm(A, ord=2)
            
            # Verificar desigualdades
            lower_ok = inv_sqrt_n * norm_1 <= norm_2 + 1e-12
            upper_ok = norm_2 <= sqrt_n * norm_1 + 1e-12
            
            if not (lower_ok and upper_ok):
                success = False
                break
                
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión {n}x{n}: Verificadas {n_trials} matrices.")

if __name__ == "__main__":
    verify_matrix_norms_1_2()
