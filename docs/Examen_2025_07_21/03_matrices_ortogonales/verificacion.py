import numpy as np

def run_tests():
    print("--- Analizando Numéricamente Propiedades de Matriz A y B ---")

    # Inciso D: Vamos a someter nuestra deducción final al veredicto del hardware.
    B = np.array([
        [ 0.5,    -0.5,    -0.1,    -0.7   ],
        [-0.5,     0.5,    -0.1,    -0.7   ],
        [-0.1,    -0.1,     0.98,   -0.14  ],
        [-0.7,    -0.7,    -0.14,    0.02  ]
    ])

    print("\n--- Comprobando Axiomas Categóricos Iniciales sobre la Matriz B ---")
    
    # 1. Simetría B = B^t
    es_simetrica = np.allclose(B, B.T)
    print(f"¿La matriz posee simetría morfológica (B = B^t)?: {es_simetrica}")

    # 2. Involución B^2 = I
    I_ref = np.eye(4)
    B_cuadrado = B @ B
    es_involutiva = np.allclose(B_cuadrado, I_ref)
    print(f"¿El cuadrado autopropagado de la Matriz recae en la Identidad (B^2 = I)?: {es_involutiva}")
    
    # Dado que se infieren como True, inferimos colateralmente la ortogonalidad:
    B_inv = np.linalg.inv(B)
    es_ortogonal = np.allclose(B.T, B_inv)
    print(f"(Deducimos Inversa igual a Transpuesta causal) ¿Ortogonalidad?: {es_ortogonal}")

    print("\n--- Verificando Espectro Analítico Sugerido (Inciso D) ---")
    
    # La computadora extraerá de las entrañas matemáticas el polinomio
    lambdas_computadora, _ = np.linalg.eig(B)
    
    # Debido a fluctuaciones estadísticas binarias flotantes (e.g., 0.999999999) rodeamos el valor empírico
    lambdas_redondeados = np.round(lambdas_computadora).astype(int)
    # Ordenados descendentemente por prolijidad
    lambdas_redondeados = np.sort(lambdas_redondeados)[::-1] 
    
    print(f"Autovalores extraídos desde `numpy.linalg.eig` (Redondeados): {list(lambdas_redondeados)}")
    
    # Cotejando contra deducción escrita e inmaculada:
    espectro_inferido = [1, 1, 1, -1]
    espectro_inmaculado = np.allclose(lambdas_redondeados, espectro_inferido)
    print(f"¿Los autovalores empíricos coinciden sin piedad con la deducción analítica de la Traza y Rango?: {espectro_inmaculado}")
    
    print("\n--- Inciso C: Corroborando Sigma Identidad frente a SVD de un Ortogonal ---")
    _, S_observado, _ = np.linalg.svd(B)
    sigma_redondeado = np.round(S_observado).astype(int)
    print(f"La colección de valores Sigmas (Singulares): {list(sigma_redondeado)}")
    print(f"¿En efecto, toda SVD diagonal subyacente de Ortogonales en sus valores sigmas re-arma la Matriz Identidad?: {np.allclose(sigma_redondeado, [1, 1, 1, 1])}")


if __name__ == "__main__":
    run_tests()
