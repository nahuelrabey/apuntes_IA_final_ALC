import numpy as np

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 1...")
    
    A = np.array([
        [-1,  1,  0,  1],
        [ 1, -1, -1, -2],
        [ 1, -1,  0, -1],
        [ 1, -1,  1,  0]
    ], dtype=float)

    # Bases calculadas en la teoría
    B_Im = np.array([
        [-1,  0],
        [ 1, -1],
        [ 1,  0],
        [ 1,  1]
    ], dtype=float)

    B_Nu = np.array([
        [1,  1],
        [1,  0],
        [0, -1],
        [0,  1]
    ], dtype=float)

    print("\n1) Verificando que B_Nu pertenece al núcleo de A:")
    print("A @ B_Nu =")
    print(np.round(A @ B_Nu, 5))
    assert np.allclose(A @ B_Nu, 0), "Fallo: B_Nu no pertenece al álgebra de Nu(A)"

    print("\n2) Verificando suma directa (Independencia Lineal de B):")
    B = np.hstack([B_Im, B_Nu])
    det_B = np.linalg.det(B)
    print(f"Det(B) = {det_B:.5f}")
    assert np.abs(det_B) > 1e-10, "Fallo: Las bases no forman suma directa Im(A) (+) Nu(A) = R^4"

    print("\n3) Construyendo matriz del proyector P = B * D * B^-1:")
    B_inv = np.linalg.inv(B)
    D = np.diag([1, 1, 0, 0])
    P = B @ D @ B_inv
    print("P =")
    print(np.round(P, 3))

    print("\n4) Verificando propiedes del proyector:")
    # Idempotencia: P^2 = P
    is_idempotent = np.allclose(P @ P, P)
    print(f"¿P^2 = P? {is_idempotent}")
    assert is_idempotent, "Fallo: P no es idempotente (no es un proyector)"

    # Ortogonalidad: P = P^T
    is_symmetric = np.allclose(P, P.T)
    print(f"¿P ortogonal (P = P^T)? {is_symmetric}")
    # En la teoría dedujimos que NO es ortogonal
    assert not is_symmetric, "Fallo: P no debe ser ortogonal"

    # Coincidencia: P = A
    is_A = np.allclose(P, A)
    print(f"¿P idéntico a A? {is_A}")
    assert not is_A, "Fallo: P no debe ser idéntico a A"

    print("\n5) Abstracción al Caos (Randomization Testing):")
    # Generamos vectores aleatorios proyectados y verificamos que caen en la imagen original
    np.random.seed(42)
    for _ in range(50):
        # Tomamos un vector aleatorio r en R^4
        r = np.random.randn(4)
        # Lo proyectamos p_r = P @ r
        p_r = P @ r
        # Verificamos si podemos representar p_r como combinación lineal de B_Im
        # p_r = B_Im @ x -> x resoluble con cuadrados mínimos con residuo casi nulo
        x, residuals, _, _ = np.linalg.lstsq(B_Im, p_r, rcond=None)
        assert len(residuals) == 0 or np.allclose(residuals, 0), "Fallo empírico: Un vector proyectado cayó fuera de la Imagen."
    
    print("\n[OK] Verificación completada con éxito. Robustez estipulada tolerando floats.")

if __name__ == '__main__':
    run_verification()
