import numpy as np

def verificar_vector_nulo(n: int = 3, num_trials: int = 1000) -> bool:
    """
    Verifica iterativamente que la ecuación A * v = lambda * v 
    es patológicamente trivial y matemáticamente inútil para cualquier v = 0,
    ya que se cumple para absolutamente CUALQUIER escalar lambda.
    """
    todas_validas = True
    
    for _ in range(num_trials):
        # 1. Creamos una matriz aleatoria A
        A = np.random.randn(n, n)
        
        # 2. Obligamos a que nuestro "candidato a autovector" sea el vector nulo
        v_nulo = np.zeros(n)
        
        # 3. Generamos un escalar lambda TOTALMENTE aleatorio (que ni siquiera es autovalor real de A)
        lambda_falso = np.random.randn()
        
        # 4. Calculamos ambos lados de la ecuación de autovectores (A*v = lambda*v)
        left_side = A @ v_nulo 
        right_side = lambda_falso * v_nulo 
        
        # 5. La trampa: Ambos lados SIEMPRE van a dar el vector cero
        es_igual = np.allclose(left_side, right_side)
        
        if not es_igual:
            todas_validas = False
            
    return todas_validas

if __name__ == "__main__":
    n = 3
    print(f"--- Verificando la Trivialidad del Vector Nulo (R^{n}) ---")
    
    trivialidad_confirmada = verificar_vector_nulo(n=n, num_trials=5000)
    
    if trivialidad_confirmada:
        print("\n✅ SIMULACIÓN EXITOSA: La ecuación A*0 = λ*0 se cumple para CUALQUIER matriz y CUALQUIER escalar λ existente.")
        print("   -> Conclusión: El vector nulo absorbe el producto.")
        print("   -> Consecuencia: No aporta NINGUNA información sobre la transformación de A ni sirve como base direccional.")
    else:
        print("\n❌ FALLO EN LA SIMULACIÓN.")
