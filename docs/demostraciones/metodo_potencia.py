import numpy as np

def verificar_induccion_potencia(n=5, K=15):
    """
    Simulador que comprueba empíricamente el teorema de equivalencia direccional
    durante el bucle iterativo de normalización del Método de la Potencia.
    
    Verificará si:  x^(k) [Calculado iterativamente con renormalización individual]
    es en realidad una copia bidimensional perfecta de:  (B^k x^(0)) / ||B^k x^(0)||
    """
    
    # Aseguramos condiciones de replicado estocástico
    np.random.seed(42)
    
    # 1. Creamos el operador B simulando datos reales (Haciéndola definida positiva y densa)
    M = np.random.rand(n, n)
    B = M @ M.T + np.eye(n) * 0.1
    
    # 2. Partimos de un vector primigenio genérico puro x^(0)
    x_0 = np.random.rand(n)
    x_0 = x_0 / np.linalg.norm(x_0)
    
    print("-" * 65)
    print("Iniciando validación empírica en paralelo...")
    print(f"Dimensiones de espacio: R^{n}")
    print(f"Número de iteraciones a comprobar (k): {K}")
    print("-" * 65)
    
    # =======================================================
    # ABORDAJE A: Paso a Paso Iterativo del For Loop Interno
    # =======================================================
    # El algoritmo industrial tal y como está escrito en Python iterativamente
    x_paso_a_paso = x_0.copy()
    
    for iteracion in range(K):
        y_temporal = B @ x_paso_a_paso
        # Aquí nace la "muerte recursiva" normalizando el resultado fresco continuamente
        x_paso_a_paso = y_temporal / np.linalg.norm(y_temporal)
        
    # =======================================================
    # ABORDAJE B: Cálculo Analítico y Limpio Matemático (Por Teorema)
    # =======================================================
    # Calculamos de una sola vez levantando matemáticamente B a la potencia de K (B^k)
    B_a_la_k = np.linalg.matrix_power(B, K)
    
    # Se impone directamente sobre el vector primigenio original
    y_analitico_directo = B_a_la_k @ x_0
    
    # Se divide el colosal vector gigante en sí mismo una única y final vez
    x_teorema_directo = y_analitico_directo / np.linalg.norm(y_analitico_directo)
    
    # =======================================================
    # CORROBORACIÓN Y COTEJO COMPUTACIONAL FINAL ESTOCÁSTICO
    # =======================================================
    # Utilizamos isclose tolerando errores naturales del silicio e imprecisiones de los Floating Points IEEE 754
    coincidencia_exacta = np.allclose(x_paso_a_paso, x_teorema_directo, atol=1e-8) 
    coincidencia_opuesta = np.allclose(x_paso_a_paso, -x_teorema_directo, atol=1e-8)
    
    print("Vectores Resultantes (Primeras Componentes):")
    print(f"[Iteración en Bucle]: {x_paso_a_paso[:3]}...")
    print(f"[Fórmula Analítica]:  {x_teorema_directo[:3]}...")
    print("-" * 65)
    
    if coincidencia_exacta or coincidencia_opuesta:
        print("✅ VERIFICACIÓN RIGUROSA ÉXITOSA:")
        print("   -> El procesador confirma que ambos enfoques producen matemáticamente")
        print("   la misma orientación física y topológica.")
        print("   La identidad x^(k) = B^k * x^(0) / ||B^k * x^(0)|| es computacionalmente firme.")
    else:
        print("❌ ERROR GRAVE: Ambos enfoques divergen.")

if __name__ == "__main__":
    verificar_induccion_potencia()
