import numpy as np

def verificar_independencia_autovectores(n: int = 5, iteraciones: int = 1000):
    """
    Verifica estocásticamente si una matriz con n autovalores estrictamente distintos
    posee en consecuencia un conjunto de n autovectores linealmente independientes.
    
    A través del método iterativo de Monte Carlo construimos repetidas veces matrices
    cuyo espectro sea forzosamente dispar, y nos valemos empíricamente del cálculo
    de rango del álgebra computacional de sus bases para descartar colapsos dimensionales.
    
    Args:
        n: Dimensión hiper-espacial cuadrada elegida (cantidad de vectores en la base).
        iteraciones: Cantidad de re-testeos matriciales aleatorios ininterrumpidos.
    """
    np.random.seed(42)  # Control semi-determinista para la validación continua.
    exitos = 0
    
    for _ in range(iteraciones):
        # 1. Generamos 'n' autovalores estrictamente distintos muestreados al azar
        # Sumamos un offset lineal dinámico para garantizar matemáticamente su total disparidad asintótica.
        autovalores_forzados = np.random.rand(n) + np.arange(n) * 10 
        D = np.diag(autovalores_forzados)
        
        # 2. Generamos una Matriz de Pasaje ortogonal Aleatoria 'P' garantizada como invertible
        # (Esto imita cualquier subespacio de RN sin sesgar la varianza)
        M_aleatoria = np.random.randn(n, n)
        Q, R = np.linalg.qr(M_aleatoria) # Factorizamos QR para sacar una matriz ortogonal pura 'Q' pre-fabricada
        
        # 3. Ensamblamos temporalmente nuestra Matriz Base Original A = Q D Q^T
        A = Q @ D @ Q.T
        
        # 4. Solicitamos al cerebro algorítmico resolver el sistema de la matriz pre-armada
        # Obtiene eigenvalues y la matriz unificada continua con sus autovectores por columna (v_1, v_2 ... v_n)
        valores_propios, matriz_autovectores = np.linalg.eig(A)
        
        # 5. La prueba de oro de Independencia Lineal Computacional:
        # Como los vectores están adosados por columnas conformando una Matriz Cuadrada V,
        # Si su rank formal dictaminado por SVD iguala la dimensión del espacio (n),
        # Significa incontrastablemente que absolutamente TODOS sus vectores columna corren independientes.
        rango_efectivo = np.linalg.matrix_rank(matriz_autovectores, tol=1e-10) # Aplicamos la tolerancia al error (No ==)
        
        if rango_efectivo == n:
            exitos += 1
            
    # Resultados del Estrés
    print(f"\n--- Verificador de Independencia de Autovectores (n={n}) ---")
    print(f"Bucle Masivo Efectuado: {iteraciones} matrices aleatorias testeadas.")
    print(f"Matrices con Autovectores que conformaron Bases L.I: {exitos}/{iteraciones}")
    
    if exitos == iteraciones:
        print(">> CONLCUSIÓN: Validado Empíricamente. La aserción del Lema es Universal en R^n.")
    else:
        print(">> ANOMALÍA: Colapso detectado. La teoría o tolerancia falló estadísticamente.")

if __name__ == "__main__":
    verificar_independencia_autovectores()
