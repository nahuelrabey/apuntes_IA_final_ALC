import numpy as np

def run_tests():
    print("--- Verificación Computacional de Bases Ortonormales y Residuales MCO ---")

    np.random.seed(33)
    
    # Vamos a simular la base Q de R^5 estocásticamente usando factorizacion QR de una random
    # La descomposicion QR de numpy es óptima porque Q conforma per se una matriz Ortonormal.
    R5_caotica = np.random.randn(5, 5)
    Q, _ = np.linalg.qr(R5_caotica)
    
    print("\n[VALIDACIÓN PREVIA DEL AXIOMA EXPERIMENTAL]")
    print(f"¿Los 5 vectores resultantes (Q) son fehacientemente Ortogonales Unitarios?: {np.allclose(Q.T @ Q, np.eye(5))}")
    
    # Estilizamos variables para mantener correlación nominal.
    # Q contiene las columnas q1, q2, q3, q4, q5
    q1 = Q[:, 0].reshape(-1, 1)
    q2 = Q[:, 1].reshape(-1, 1)
    q3 = Q[:, 2].reshape(-1, 1)
    q4 = Q[:, 3].reshape(-1, 1)
    q5 = Q[:, 4].reshape(-1, 1)
    
    # Estructura del examen
    A = np.column_stack((q1, q2, q3))
    
    b = 1*q1 + 2*q2 + 3*q3 + 4*q4 + 5*q5
    
    print("\n--- Inciso A: Vector Estimado \hat{x} MCO ---")
    
    # Forma ortodoxa general de librerías para Least Squares
    x_hat_libreria, residuos, rank, s = np.linalg.lstsq(A, b, rcond=None)
    
    print("El procesador calculó que b carecía de solución en Ax=b. Recortó la proyección al plano A.")
    print("El Numpy lstsq arrojó el \hat{x} minimizado de respuesta:")
    print(np.round(x_hat_libreria.flatten(), 5))
    
    # Forma axiomática que dedujimos nosotros
    x_hat_deducido = np.array([[1], [2], [3]])
    print("Comprobando con nuestra deducción matemática analítica [1, 2, 3]^T.")
    print(f"¿Ambos vectores son el mismo punto (np.allclose)?: {np.allclose(x_hat_libreria, x_hat_deducido)}")
    
    print("\n--- Inciso B: Magnitud de Error Cuadrático ---")
    
    # Calcular proyeccion
    p = A @ x_hat_libreria
    e = b - p
    
    error_num_norm = np.linalg.norm(e, ord=2)
    # Deducción del papel dictaba Raíz Cuadrada de 41:
    error_analitico_raiz = np.sqrt(41)
    
    print(f"La computadora calculó el error residuo puramente numérico (np.norm) en: {error_num_norm:.6f}")
    print(f"Nuestro modelo en folio de raiz de 41 estipulaba estáticamente:       {error_analitico_raiz:.6f}")
    print(f"¿Concuerdan a nivel microscópico?: {np.isclose(error_num_norm, error_analitico_raiz)}")
    
    print("\n--- Inciso C: A_pseudiinversa = A_transpuesta ---")
    
    # Pinacle algorithm
    A_pseudoinversa_calculada = np.linalg.pinv(A)
    
    # Axioma nuestro
    A_transpuesta_axioma = A.T
    
    print(f"Distancia norma matriz entre el Módulo SVD del PC (Pseudoinverse) y A_transpuesta: {np.linalg.norm(A_pseudoinversa_calculada - A_transpuesta_axioma):.5e}")
    print(f"Determinamos que el módulo se reemplaza 1 a 1 para matrices extraídas de Q-Bases.")
    print(f"¿Son matemáticamente la misma matriz idéntica? {np.allclose(A_pseudoinversa_calculada, A_transpuesta_axioma)}")

if __name__ == "__main__":
    run_tests()
