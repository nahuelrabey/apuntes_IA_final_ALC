import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(D, b - LU @ x)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def gauss_seidel(A, b, x0, tol=1e-10, max_iter=1000):
    DL = np.tril(A)
    U = A - DL
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(DL, b - U @ x)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def sor(A, b, x0, omega, tol=1e-10, max_iter=1000):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    M = D + omega * L
    N = (1 - omega) * D - omega * U
    
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(M, N @ x + omega * b)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def run_comparison():
    # Generar una matriz diagonalmente dominante para asegurar convergencia
    n = 10
    A = np.random.randn(n, n)
    A = A + np.diag(np.sum(np.abs(A), axis=1) + 1)
    b = np.random.randn(n)
    x0 = np.zeros(n)
    
    sol_exacta = np.linalg.solve(A, b)
    
    print(f"Comparación de Métodos Iterativos (n={n})")
    print("-" * 40)
    
    res_j, it_j = jacobi(A, b, x0)
    print(f"Jacobi:       {it_j:3} iteraciones | Error: {np.linalg.norm(res_j - sol_exacta):.2e}")
    
    res_gs, it_gs = gauss_seidel(A, b, x0)
    print(f"Gauss-Seidel: {it_gs:3} iteraciones | Error: {np.linalg.norm(res_gs - sol_exacta):.2e}")
    
    omega_opt = 1.1 # Aproximación simple
    res_sor, it_sor = sor(A, b, x0, omega_opt)
    print(f"SOR (w={omega_opt}): {it_sor:3} iteraciones | Error: {np.linalg.norm(res_sor - sol_exacta):.2e}")
    
    # Validaciones booleanas rigurosas
    assert np.allclose(res_j, sol_exacta, atol=1e-8)
    assert np.allclose(res_gs, sol_exacta, atol=1e-8)
    assert np.allclose(res_sor, sol_exacta, atol=1e-8)
    print("\n[OK] Todos los métodos convergen a la solución exacta.")

if __name__ == "__main__":
    run_comparison()
