import numpy as np

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 3...")
    
    # 1. Abstracción al caos: M y N aleatorios (m > n) con rango completo casi seguro.
    np.random.seed(101)
    m, n = 8, 4
    
    # Matriz A aleatoria asimétrica "skinny"
    A = np.random.randn(m, n) * 10 
    # Validar que Rango Columna Completo se mantiene en la simulación estocástica
    rank = np.linalg.matrix_rank(A)
    assert rank == n, f"Fallo en instanciación: El rango (r={rank}) no es completo (n={n})."

    # Vector extendido ruidoso b
    b = np.random.randn(m) * 15

    print("\n1) Resolviendo por Ecuaciones Normales explícitas (Solución Algebraica):")
    # x = (A^T A)^-1 A^T b
    AtA = A.T @ A
    AtA_inv = np.linalg.inv(AtA)
    x_eq_normales = AtA_inv @ A.T @ b
    print("Resultado x_cm (Ec. Normales):")
    print(np.round(x_eq_normales, 5))

    print("\n2) Resolviendo por minimización algorítmica robusta de Mínimos Cuadrados:")
    # np.linalg.lstsq min( ||Ax - b||_2 ) internamente vía SVD o QR robusto.
    x_lstsq, residuals, _, _ = np.linalg.lstsq(A, b, rcond=None)
    print("Resultado x_cm (np.linalg.lstsq):")
    print(np.round(x_lstsq, 5))

    print("\n3) Resolviendo por cálculo puro de Pseudo-inversa (Pinza Computacional Teorizada):")
    # np.linalg.pinv genera la inversa de Moore-Penrose (A^dagger)
    A_pinv = np.linalg.pinv(A)
    x_pinv = A_pinv @ b
    print("Resultado x_cm (A_pseudo * b):")
    print(np.round(x_pinv, 5))

    # Comparación de Tolerancias Flotantes para la Aprobación Definitiva
    assert np.allclose(x_eq_normales, x_lstsq, rtol=1e-5), "Fallo: x_eq_normales difiere de x_lstsq."
    assert np.allclose(x_lstsq, x_pinv, rtol=1e-5), "Fallo: La pseudo-inversa no converge al minimizador de norma 2."
    
    print("\n[OK] Verificación completada con éxito. La pseudo-inversa equivale analíticamente a los cuadrados mínimos para bases de rango completo, resistiéndose a desbordes de coma flotante.")

if __name__ == '__main__':
    run_verification()
