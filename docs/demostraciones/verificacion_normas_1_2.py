import numpy as np

def verify_norms_1_2():
    print("Verificando numéricamente: (1/sqrt(n))||x||_1 <= ||x||_2 <= ||x||_1")
    
    np.random.seed(42)
    n_dims = [2, 10, 100, 1000]
    n_trials = 1000
    
    for n in n_dims:
        inv_sqrt_n = 1.0 / np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            x = np.random.randn(n)
            
            norm_1 = np.linalg.norm(x, ord=1)
            norm_2 = np.linalg.norm(x, ord=2)
            
            # Verificar desigualdades
            lower_bound = inv_sqrt_n * norm_1 <= norm_2 + 1e-12
            upper_bound = norm_2 <= norm_1 + 1e-12
            
            if not (lower_bound and upper_bound):
                success = False
                break
        
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión n={n:4}: Verificadas {n_trials} pruebas aleatorias.")

if __name__ == "__main__":
    verify_norms_1_2()
