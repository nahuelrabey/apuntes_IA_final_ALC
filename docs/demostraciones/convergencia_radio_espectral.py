import numpy as np

def verify_spectral_convergence():
    print("Iniciando validación de convergencia vs Radio Espectral...")
    
    # 1. Generar matriz convergente (rho < 1)
    # Usamos una matriz aleatoria y la normalizamos por su radio espectral
    A_conv = np.random.randn(5, 5)
    coeffs_conv = np.linalg.eigvals(A_conv)
    rho_A = max(abs(coeffs_conv))
    B_conv = A_conv * (0.8 / rho_A)  # rho(B) = 0.8
    
    # 2. Generar matriz divergente (rho > 1)
    B_div = A_conv * (1.2 / rho_A)   # rho(B) = 1.2
    
    def simulate_iterations(B, name):
        print(f"\nSimulando: {name} (rho = {max(abs(np.linalg.eigvals(B))):.2f})")
        e = np.random.randn(5)  # Error inicial
        history = []
        for k in range(20):
            norm_e = np.linalg.norm(e)
            history.append(norm_e)
            e = B @ e
            if k % 4 == 0 or k == 19:
                print(f"Iteración {k:2}: ||e|| = {norm_e:.6e}")
        
        return history

    h_conv = simulate_iterations(B_conv, "Sistema Convergente")
    h_div = simulate_iterations(B_div, "Sistema Divergente")
    
    # Verificación de tendencias
    if h_conv[-1] < h_conv[0] and h_div[-1] > h_div[0]:
        print("\n✓ RESULTADO EXITOSO: El sistema con rho < 1 converge, el de rho > 1 diverge.")
    else:
        print("\n✗ FALLO EN LA VALIDACIÓN: Comportamiento inesperado.")

if __name__ == "__main__":
    verify_spectral_convergence()
