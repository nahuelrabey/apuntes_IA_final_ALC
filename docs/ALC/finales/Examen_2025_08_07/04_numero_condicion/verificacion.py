import numpy as np

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 4...")
    
    # 1. Abstracción a distintos Ks paramétricos
    ks = [2, 10, 50]
    
    print("\n1) Verificando Condicionamiento cota inf L2 y L_inf:")
    for k in ks:
        print(f"\n--- Evaluando k = {k} ---")
        A = np.array([
            [1.0, 1.0, 1.0],
            [1.0, 1.0, 0.0],
            [k**2, 0.0, k**2]
        ])
        
        # Normas
        norm_inf_A = np.linalg.norm(A, np.inf)
        norm_inf_invA = np.linalg.norm(np.linalg.inv(A), np.inf)
        cond_inf = norm_inf_A * norm_inf_invA 
        
        cond_2 = np.linalg.cond(A, p=2)
        
        cota_inf_teorica = k**2
        cota_2_teorica = (4/3) * (k**2)
        
        print(f"Cond_inf(A) analítico aproximado = {cond_inf:.2f} (Teórico >= {cota_inf_teorica})")
        print(f"Cond_2(A) algorítmico exacto   = {cond_2:.2f} (Teórico >= {cota_2_teorica:.2f})")
        
        assert cond_inf >= cota_inf_teorica, f"Fallo empírico: Condicionamiento infinito debe ser mayor a {cota_inf_teorica}"
        assert cond_2 >= cota_2_teorica - 1e-5, f"Fallo empírico: Condicionamiento L2 debe ser c proporcional mayor a {cota_2_teorica}"

    print("\n2) Precondicionador Diagonal (C = Diag(A)^-1):")
    k = 100 # Empleamos uno masivo para acentuar el escape numérico y posterior cura
    A_bad = np.array([
            [1.0, 1.0, 1.0],
            [1.0, 1.0, 0.0],
            [k**2, 0.0, k**2]
    ])
    
    cond_2_antes = np.linalg.cond(A_bad, 2)
    print(f"Condicionamiento catastrófico natural L2 SIN precondicionar (k={k}): {cond_2_antes:.3f}")
    
    # Construimos iteración precondicionadora de Jacobi
    diag_A = np.diag(np.diag(A_bad))
    C = np.linalg.inv(diag_A)
    CA = C @ A_bad
    
    cond_2_despues = np.linalg.cond(CA, 2)
    print(f"Matriz curada (CA):")
    print(np.round(CA, 3))
    print(f"Condicionamiento óptimo L2 CON precondicionador (Iteración de Jacobi): {cond_2_despues:.3f}")
    
    # Validamos desconexión dependiente del parámetro paramétrico dinámico k
    assert cond_2_despues < 10.0, "Fallo: El precondicionador no aisló exitosamente el condicionamiento a valores de escala constantes O(1)."

    print("\n[OK] Verificación completada con éxito. Crecimiento analítico de L2 ratificado, al igual curaciones mediante precondicionamiento diagonal constante.")

if __name__ == '__main__':
    run_verification()
