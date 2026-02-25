import numpy as np

def test_ecosistema_markov():
    """
    Despliega simulaciones numéricas sobre la matriz del Ecosistema de Markov
    del Ejercicio 3 para validar afirmaciones de autoespacios y población límite.
    """
    print(" === 🔬 VALIDACIÓN COMPUTACIONAL: CADENA DE MARKOV ECOSISTÉMICA === \n")

    # 1. Instanciamos la Matriz Estocástica P por Celdas Columna->Fila
    # Columnas rutean: B, S, E, R
    P = np.array([
        [0.5, 0.5, 0.0, 0.0],  # Hacia Bosque
        [0.5, 0.5, 0.0, 0.0],  # Hacia Selva
        [0.0, 0.0, 1.0, 0.3],  # Hacia Estepa
        [0.0, 0.0, 0.0, 0.7]   # Hacia Río
    ])

    print("Matriz Transición P insertada.")
    print("Comprobando si es Matriz Estocástica (Filas/Columnas suman 1):")
    # Nota: Usamos convención donde las columnas actúan como vector derecho P*v 
    # por eso las sumas de sus columnas obligadamente deben destilar 1.0 (conservan biomasa)
    col_sums = np.sum(P, axis=0)
    print(f"Suma por Orígenes (Columnas): {col_sums}  | ¿Lícita? {np.allclose(col_sums, 1.0)}")
    print("-" * 50)

    # 2. Análisis Espectral Tensorial Computarizado
    eigenvalores, eigenvectores = np.linalg.eig(P)
    
    # Ordenamos y redondeamos para legibilidad flotante
    sorted_indices = np.argsort(np.abs(eigenvalores))[::-1]
    lambdas = np.round(eigenvalores[sorted_indices], 3)
    
    print(f"🎯 Espectro Mágico Diagonal (Autovalores capturados): \n {lambdas}")
    print("\n¿Posee la matriz P diagonalizabilidad?")
    
    # Comprobar la multiplicidad geométrica empíricamente (verificando independencia de la base eigenvectorial)
    rank_eigen_base = np.linalg.matrix_rank(eigenvectores)
    dims_totales = P.shape[0]
    
    if rank_eigen_base == dims_totales:
        print(f" -> Sí, rotundamente DIAGONALIZABLE. Rango de base tensorial = {rank_eigen_base} / Dimensiones={dims_totales}.")
    else:
        print(f" -> NO DIAGONALIZABLE (Matriz Deficiente). Rango de Base: {rank_eigen_base}.")

    print("-" * 50)

    # 3. Evolución Demográfica Asintótica Límite a las Estrellas
    v_inicial = np.array([300, 100, 200, 0])
    
    poderes_generacionales = [1, 5, 20, 100]
    
    print(f"🌱 Estado poblacional genésico v0 = {v_inicial}")
    
    for k in poderes_generacionales:
        # P^k * v_0
        P_to_k = np.linalg.matrix_power(P, k)
        v_k = np.dot(P_to_k, v_inicial)
        
        # Formateando números redondos para biomasa animal observable
        print(f"  > Generación k={k:<3} : {np.round(v_k, 1)}")

if __name__ == "__main__":
    test_ecosistema_markov()
