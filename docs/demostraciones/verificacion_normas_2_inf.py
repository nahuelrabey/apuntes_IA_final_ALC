import numpy as np

def verify_norms_2_inf():
    print("Verificando numéricamente: ||x||_inf <= ||x||_2 <= sqrt(n)||x||_inf")
    
    np.random.seed(42)
    n_dims = [2, 10, 100, 1000]
    n_trials = 1000
    
    for n in n_dims:
        sqrt_n = np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            # Generar vector aleatorio en R^n
            x = np.random.randn(n)
            
            norm_inf = np.linalg.norm(x, ord=np.inf)
            norm_2 = np.linalg.norm(x, ord=2)
            
            # Verificar desigualdades con tolerancia para floats
            lower_bound = norm_inf <= norm_2 + 1e-12
            upper_bound = norm_2 <= sqrt_n * norm_inf + 1e-12
            
            if not (lower_bound and upper_bound):
                success = False
                break
        
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión n={n:4}: Verificadas {n_trials} pruebas aleatorias.")

if __name__ == "__main__":
    verify_norms_2_inf()
