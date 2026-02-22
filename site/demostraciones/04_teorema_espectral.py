import numpy as np

def verificar_teorema_espectral(n: int = 5, iteraciones: int = 1500):
    """
    Verifica estocásticamente el dictamen del Teorema Espectral para
    matrices rigurosamente Reales y Simétricas (A = A^T).
    
    A través de la fuerza estocástica iterativa validamos que:
    1) Sus Eigenvalues no escapan jamás al plano Complejo (Parte imaginaria nula).
    2) El producto vectorial interno de sus combinaciones de Eigenvectors dispares
       rinde ceros perfectos, dictaminando Ortogonalidad Espacial (Angulo de 90° grados).
    
    Args:
        n: Dimensión base cuadrada evaluada.
        iteraciones: Cantidad de matrices simétricas estresadas al azar.
    """
    np.random.seed(42)  
    
    exitos_reales = 0
    exitos_ortogonalidad = 0
    
    for _ in range(iteraciones):
        # 1. Armamos una matriz aleatoria de partida
        M = np.random.randn(n, n) * 10
        
        # 2. Obligamos su simetría matemática sumándola a su transpuesta (A = A^T garantizado)
        A = M + M.T
        
        # 3. Solicitamos autovalores y autovectores sin restricción forzada a librería hermítica de numpy
        # (Usamos `eig` estándar y no `eigh` para atrapar si numpy fugase a memoria compleja por error algorítmico)
        valores_propios, matriz_autovectores = np.linalg.eig(A)
        
        # --- TEST 1: INEXISTENCIA DE RAÍCES COMPLEJAS ---
        # Verificamos si la suma de todas las partes imaginarias absolutas es asintóticamente nula.
        suma_imaginaria = np.sum(np.abs(np.imag(valores_propios)))
        if np.isclose(suma_imaginaria, 0, atol=1e-12):
            exitos_reales += 1
            
        # --- TEST 2: ORTOGONALIDAD ESTRICTA ENTRE PARES DE AUTOVECTORES ---
        ortogonal_check = True
        
        # Hacemos iteraciones comparando cada posible par (i, j) donde i != j
        for i in range(n):
            for j in range(i + 1, n):
                # Extraemos las dos columnas correspondientes
                v1 = matriz_autovectores[:, i]
                v2 = matriz_autovectores[:, j]
                
                # Obtenemos su producto interno empírico con el vector transpuesto
                producto_punto = np.dot(v1, v2)
                
                # Tolerancia flotante: Las matrices de rotaciones/componentes de autovectores
                # tras cálculos pesados de descomposición acarrean bits de ruido en mantisa base 2.
                # Exigir un cero flotante estricto (0.0 == 0.0) rompería por error de hadware en R10 o R20.
                if not np.isclose(producto_punto, 0, atol=1e-10):
                    ortogonal_check = False
                    break
                    
            if not ortogonal_check:
                break
                
        if ortogonal_check:
            exitos_ortogonalidad += 1
            
    # Resultados del Estrés
    print(f"\n--- Verificador del Teorema Espectral Real (n={n}) ---")
    print(f"Bucle Masivo Efectuado: {iteraciones} matrices simétricas generadas.")
    print(f"> Raíces 100% Reales comprobadas: {exitos_reales}/{iteraciones}")
    print(f"> Bases Autovectoriales 100% Ortogonales comprobadas: {exitos_ortogonalidad}/{iteraciones}")
    
    if exitos_reales == iteraciones and exitos_ortogonalidad == iteraciones:
        print("\n>> CONLCUSIÓN: Validado Empíricamente. La aserción del Lema Espectral domina la matriz.")
    else:
        print("\n>> ANOMALÍA: Colapso detectado por falla teórica o ruido de hardware masivo en mantisa.")

if __name__ == "__main__":
    verificar_teorema_espectral()
