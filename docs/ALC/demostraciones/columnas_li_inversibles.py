import numpy as np

def verificar_invertibilidad_y_rango(n: int = 4, num_trials: int = 1000) -> bool:
    """
    Verifica estocásticamente el Teorema de la Matriz Inversible:
    Una matriz cuadrada tiene columnas Linealmente Independientes (Rango Completo)
    SÍ Y SOLO SÍ su determinante es no nulo (Es Inversible).
    """
    todas_validas = True
    
    for _ in range(num_trials):
        # --- CASO 1: Matriz Inversible (Columnas L.I.) ---
        # Generamos una matriz aleatoria. La probabilidad de que sus columnas sean
        # linealmente dependientes por puro azar con floats es virtualmente cero.
        A_li = np.random.randn(n, n)
        
        # Calculamos el Rango (cantidad de columnas L.I.)
        rango_li = np.linalg.matrix_rank(A_li)
        
        # Calculamos el determinante
        det_li = np.linalg.det(A_li)
        
        # Verificamos la teoría: Si el rango es N (Full Rank), el determinante no debe ser 0.
        if rango_li != n or np.isclose(det_li, 0.0):
            todas_validas = False
            
            
        # --- CASO 2: Matriz Singular (Columnas L.D.) ---
        A_ld = np.random.randn(n, n)
        # Forzamos intencionalmente que la última columna sea una copia exacta de la primera
        # Esto destruye la independencia lineal del conjunto.
        A_ld[:, -1] = A_ld[:, 0]
        
        rango_ld = np.linalg.matrix_rank(A_ld)
        det_ld = np.linalg.det(A_ld)
        
        # Verificamos la teoría: Al sabotear la independencia (Rango < N), el det SE HACE 0.
        if rango_ld == n or not np.isclose(det_ld, 0.0):
            todas_validas = False
            
    return todas_validas

if __name__ == "__main__":
    n = 4
    print(f"--- Verificando el Teorema de la Matriz Inversible (R^{n}) ---")
    
    simulacion_exitosa = verificar_invertibilidad_y_rango(n=n, num_trials=5000)
    
    if simulacion_exitosa:
        print("\n✅ SIMULACIÓN EXITOSA en 5000 ciclos:")
        print("   -> Toda matriz con Rango Completo (Columnas L.I.) devolvió un Determinante != 0 (Es Inversible).")
        print("   -> Toda matriz saboteada con una columna L.D. devolvió un Determinante == 0 (Es Singular).")
        print("\n   Conclusión: La Invertibilidad y la Independencia Lineal de las columnas son lógicamente equivalentes para todo hiperplano R^n.")
    else:
        print("\n❌ FALLO EN LA SIMULACIÓN.")
