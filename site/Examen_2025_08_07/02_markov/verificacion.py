import numpy as np

def run_verification():
    print("Iniciando verificación computacional del Ejercicio 2...")

    print("\n--- Inciso A: Autovalores en Ciclos ---")
    k = 5  # Elegimos un ciclo arbitrario de longitud 5
    C = np.zeros((k, k))
    for i in range(k-1):
        C[i+1, i] = 1.0
    C[0, k-1] = 1.0

    print(f"Matriz de permutación cíclica C_{k}x{k}:")
    print(C)

    vals, vecs = np.linalg.eig(C)
    print("\nSus autovalores son:")
    for val in vals:
        print(f"  {val:.4f} (Módulo: {np.abs(val):.4f})")
    
    # Comprobamos tolerancia
    modulos_unitarios = np.allclose(np.abs(vals), 1.0)
    hay_distintos_de_uno = np.any(np.abs(vals - 1.0) > 1e-5)
    
    assert modulos_unitarios, "Fallo: No todos los autovalores tienen módulo 1"
    assert hay_distintos_de_uno, "Fallo: No existen autovaores distintos a 1 en el ciclo"

    print("[OK] Comprobado empíricamente. Las matrices con componentes cíclicas poseen raíces de la unidad en su espectro.")

    print("\n--- Inciso B: Equilibrio en el Grafo de Markov ---")
    # Construcción de la matriz estocástica por columnas
    # Nodos: 1, 2, 3, 4, 5
    P = np.array([
        [0.0, 0.0, 0.0, 0.0, 0.0],
        [0.5, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.5, 0.5, 0.0, 1.0],
        [0.5, 0.5, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.5, 1.0, 0.0]
    ])

    print("Matriz P (por columnas):")
    print(P)
    
    # Verificamos que es matriz estocástica por columnas (sumas = 1)
    assert np.allclose(np.sum(P, axis=0), 1.0), "Fallo empírico: Las columnas de P deben sumar a 1 de probabilidad total"

    print("\n1) Búsqueda directa por Autovectores (Resolviendo el Espectro):")
    vals_P, vecs_P = np.linalg.eig(P)

    # Buscamos el autovector asociado al autovalor ~1
    idx_1 = np.argmin(np.abs(vals_P - 1.0))
    v_eq_eig = np.real(vecs_P[:, idx_1])
    
    # Normalizamos probabilidad
    v_eq_eig = v_eq_eig / np.sum(v_eq_eig)
    
    print("Estado Estacionario detectado (via autovector):")
    print(np.round(v_eq_eig, 5))

    print("\n2) Búsqueda por Simulación (Método iterativo asintótico k -> INF):")
    # Dado que la matriz probó ser aperiódica analíticamente para los estados 3 y 5
    # debe converger desde CUALQUIER vector randómico de partida
    np.random.seed(99)
    v_rand = np.random.rand(5)
    v_rand = v_rand / np.sum(v_rand)
    
    print("Estado de partida original ALEATORIO (v_0):")
    print(np.round(v_rand, 3))

    # Elevamos la matriz estocástica a una potencia alta (P^100)
    P_inf = np.linalg.matrix_power(P, 100)
    v_eq_sim = P_inf @ v_rand
    
    print("\nEstado tras P^100 iteraciones (P^100 * v_0):")
    print(np.round(v_eq_sim, 5))
    
    print("\nMatriz límite P^100 estática global:")
    print(np.round(P_inf, 5))

    # Validaciones robustas cruzadas
    v_teorico = np.array([0, 0, 2/3, 0, 1/3])
    assert np.allclose(v_eq_eig, v_teorico, atol=1e-5), "Fallo: El autovector analítico no coincide con la teoría."
    assert np.allclose(v_eq_sim, v_teorico, atol=1e-5), "Fallo: La simulación asintótica de estados aleatorios no converge al estado teórico esperado."

    print("\n[OK] Verificación completada con éxito. Todos los teoremas estocásticos validan tolerablemente frente a mutaciones algorítmicas.")

if __name__ == '__main__':
    run_verification()
