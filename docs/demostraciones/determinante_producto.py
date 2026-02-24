import numpy as np

def verificar_multiplicatividad_determinante(n: int = 4, iteraciones: int = 1500):
    """
    Verifica estocásticamente el cumplimiento asintótico del corolario
    matemático que postula que det(A * B) = det(A) * det(B).
    
    A través del método iterativo de Monte Carlo generamos innumerables
    parejas de matrices (A, B) con magnitudes estresadas al azar para
    certificar que, tras las sucias y complejas ligaduras cruzadas originadas
    en el producto, la propiedad del determinante absorbe su multiplicidad.
    
    Args:
        n: Dimensión base cuadradática evaluada.
        iteraciones: Cantidad de simulacros matriciales aleatorios ininterrumpidos.
    """
    np.random.seed(33)  # Fijación determinista de trazabilidad.
    exitos = 0
    
    for _ in range(iteraciones):
        # 1. Armamos dos Matrices Completamente Aleatorias pero densas (Cercanía o Lejanía a 0 no pactada).
        A = np.random.randn(n, n) * np.random.uniform(1, 100)
        B = np.random.randn(n, n) * np.random.uniform(1, 100)
        
        # 2. Exigimos al hardware multiplicar a la fuerza bruta A \cdot B
        AB = A @ B
        
        # 3. Calculamos la resultante determinante agrupada
        det_AB = np.linalg.det(AB)
        
        # 4. Calculamos cada determinante segregado asilado y lo amalgamamos mediante multiplicación
        producto_det = np.linalg.det(A) * np.linalg.det(B)
        
        # 5. La prueba de oro de las Matrices Elementales Computacionales.
        # ¿Sobrevive el corolario a las tolerancias flotantes relativas (rtol)?
        # Nótese que al lidiar con factoriales y escalas x100 en potencias de n=4, 
        # el float64 genera ruidos altos por acarreo; se usa isclose() con tolerancia relativa sana.
        if np.isclose(det_AB, producto_det, rtol=1e-5):
            exitos += 1
            
    # Resultados del Estrés
    print(f"\n--- Verificador de Producto Determinante (n={n}, rtol=1e-5) ---")
    print(f"Bucle Masivo Efectuado: {iteraciones} colisiones matriciales testeadas.")
    print(f"Matrices aprobando el dictamen det(AB) = det(A)det(B): {exitos}/{iteraciones}")
    
    if exitos == iteraciones:
        print(">> CONLCUSIÓN: Validado Empíricamente. La aserción del Lema es una máxima absoluta.")
    else:
        print(">> ANOMALÍA: Colapso detectado. Ruido asintótico o descarte del Lema.")

if __name__ == "__main__":
    verificar_multiplicatividad_determinante()
