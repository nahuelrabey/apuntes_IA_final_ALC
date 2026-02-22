import numpy as np

def run_tests():
    print("--- Validación Computacional: Desigualdad de Cauchy-Schwartz ---")
    np.random.seed(81)

    ITERACIONES = 100_000
    violaciones = 0
    tolerancia_precision = 1e-10

    # Probando sobre diferentes espacios dimensionales complejos
    for _ in range(ITERACIONES):
        dim = np.random.randint(2, 50)
        
        # Universo Real y Complejo
        x = np.random.randn(dim) + 1j * np.random.randn(dim)
        y = np.random.randn(dim) + 1j * np.random.randn(dim)

        # Variables en contención de Cauchy-Schwartz
        # |x* y|
        # x.conj().T es el Hermitiano equivalente a x*
        x_start_y = np.abs(np.vdot(x, y))  # Producto interno complejo devuelve el módulo de la covarianza

        # ||x||_2 ||y||_2
        norma_x = np.linalg.norm(x, ord=2)
        norma_y = np.linalg.norm(y, ord=2)
        producto_normas = norma_x * norma_y

        # Condición Cauchy-Schwartz
        # |x* y| <= ||x||_2 ||y||_2
        # Relajando apenas por cuestiones binomicas del coma flotante para no escupir falsos negativos
        if x_start_y > (producto_normas + tolerancia_precision):
            violaciones += 1

    print(f"\n--- Resultados del Laboratorio Estadístico ---")
    print(f"Número de iteraciones probadas masivamente: {ITERACIONES} (Vectores $\\mathbb{{C}}^N$)")
    print(f"Inconsistencias halladas superando el límite analítico: {violaciones}")
    print(f"Veredicto del Ordenador sobre la Desigualdad: {'INQUEBRANTABLE' if violaciones == 0 else 'REFUTADO'}")

    print("\n[Ejemplo Gráfico a Escala para un N]")
    print(f"Norma L2 del Vector Experimento X: {norma_x:.4f}")
    print(f"Norma L2 del Vector Experimento Y: {norma_y:.4f}")
    print(f"Magnitud Combinada Limítrofe (||X|| * ||Y||): {producto_normas:.4f}")
    print(f"Valor Absoluto Interno Medido (|X* Y|): {x_start_y:.4f}")

if __name__ == "__main__":
    run_tests()
