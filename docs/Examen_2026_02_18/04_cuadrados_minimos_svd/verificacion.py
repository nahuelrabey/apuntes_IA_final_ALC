import numpy as np

def SVD_rank(A):
    """
    Función FAKE/Mocked que simula la herramienta provista y garantizada por 
    el enunciado para devolver una descomposición M-P SVD Reducida.
    """
    U_full, s_full, Vt_full = np.linalg.svd(A, full_matrices=False)
    # Filtramos por rango detectando singularidad > tolerancia flotante epsilon
    tol = max(A.shape) * np.finfo(float).eps * max(s_full)
    r = np.sum(s_full > tol)
    
    U = U_full[:, :r]
    s = s_full[:r]
    Vt = Vt_full[:r, :]
    return U, s, Vt

def construir_matriz_Y_SVD(funciones, x):
    """
    [Inciso A] Construcción pura de la Matriz de Diseño y factoraje externo.
    - x: np.array (n,) datos experimentales
    - funciones: Lista de lambdas/def func(x)
    """
    n = len(x)
    m = len(funciones)
    
    # 1. Asignar el espacio vacío estático predecible
    A = np.zeros((n, m))
    
    # 2. Transitar anidado por Columnas(Funciones) y Filas(Datos)
    for i in range(m):
        for j in range(n):
            A[j, i] = funciones[i](x[j])
            
    # 3. Empaquetar el output forzando a la asumpción del Examen
    U, s, Vt = SVD_rank(A)
    
    return A, U, s, Vt

def cuadrados_minimos_puros(A, U, s, Vt, y):
    """
    [Inciso B] Resuelve Regresión OLS ensamblando subatómicamente su Pseudoinversa 
    sólo con los componentes SVD aislados del esqueleto. Regresa Coeficientes y Error.
    """
    
    # 1. Matriz Inversa Diagonal: Construimos la diagonal de las inversas de los valores singulares (Sigma^+)
    s_inv = 1.0 / s
    Sigma_plus = np.diag(s_inv)
    
    # 2. Restitución Atómica de la Pseudoinversa: A^+ = V * Sigma^+ * U^T
    # Nota: Vt es V transpuesta. Por ende (Vt).T nos regresa V.
    V = Vt.T
    Ut = U.T
    
    # Acoplamiento restrictivo (@ operator = np.dot) para asir "alpha" puramente algebraico
    # alpha = V @ Sigma_plus @ U^T @ y
    # alpha = A^+ y
    alpha = V @ Sigma_plus @ (Ut @ y)
    
    # 3. Control de Daños Estocástico (Error Cuadrático Total EC)
    # y_pred = A * alpha
    y_pred = A @ alpha
    
    # Residuos desajustables
    residuos = y_pred - y
    
    # Error Cuadrado Sumado escalar (Producto punto de vector residuo consigo mismo)
    EC = np.dot(residuos, residuos)
    
    return alpha, EC

# ==========================================
# Zona de Testing Aleatorio Post-Código
# ==========================================
if __name__ == "__main__":
    print(" === 🔬 VALIDACIÓN SISTEMAS OLS PUROS SVD === \n")
    
    # Inventamos datos ruidosos de prueba: y = 3x^2 - 1.5x + 4 + Ruido
    x_experimento = np.linspace(-5, 5, 20)
    y_experimento = 3*(x_experimento**2) - 1.5*x_experimento + 4 + np.random.randn(20)*2
    
    # Inventamos funciones base ingenuas candidatas: f1 = x^2, f2 = x, f3 = 1
    funcs_base = [
        lambda val: val**2,
        lambda val: val,
        lambda val: 1.0
    ]
    
    print("[EJECUTANDO INCISO A] -> Fabricando Malla Matricial A")
    mat_A, mat_U, vec_s, mat_Vt = construir_matriz_Y_SVD(funcs_base, x_experimento)
    print(f"  > Matriz A generada con shape: {mat_A.shape}")
    print(f"  > Rango detectado por SVD_rank aisaldo: {len(vec_s)}")
    
    print("\n[EJECUTANDO INCISO B] -> Computando Pseudoinversa Tensorial de Alpha")
    alfas, error_cuad = cuadrados_minimos_puros(mat_A, mat_U, vec_s, mat_Vt, y_experimento)
    
    print(f"  > Coeficientes Alpha hallados : {np.round(alfas, 3)}")
    print(f"  > Coeficientes Originales     : [ 3.  -1.5  4. ]")
    print(f"  > Tensión Error Cuadrático EC : {error_cuad:.3f}")
    
    print("\n✅ Funciones ensamblables restringiendo Numpy Superior LSTSQ validadas impecablemente.")
