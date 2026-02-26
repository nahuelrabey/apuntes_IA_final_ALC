import sympy as sp

def verify_sor_characteristic():
    print("Calculando Ecuación Característica SOR simbólicamente...")
    
    # Definir símbolos
    lam = sp.symbols('lambda')
    
    # Matrices base
    D = sp.Matrix([[2, 0], [0, -1]])
    L = sp.Matrix([[0, 0], [1, 0]])
    U = sp.Matrix([[0, 1], [0, 0]])
    omega = sp.Rational(1, 2)
    
    # Matriz de iteración B
    # B = (D + omega*L)^-1 * ((1-omega)*D - omega*U)
    M = D + omega * L
    N = (1 - omega) * D - omega * U
    
    B = M.inv() * N
    print(f"Matriz de iteración B:\n{B}")
    
    # Polinomio característico
    char_poly = B.charpoly(lam).as_expr()
    print(f"\nPolinomio característico: {char_poly} = 0")
    
    # Coeficientes esperados: lam^2 - 7/8*lam + 1/4
    expected_poly = lam**2 - sp.Rational(7, 8)*lam + sp.Rational(1, 4)
    
    if sp.simplify(char_poly - expected_poly) == 0:
        print("\n✓ VERIFICACIÓN EXITOSA: El polinomio coincide con el obtenido manualmente.")
        
        # Calcular autovalores
        eigenvals = B.eigenvals()
        print(f"Autovalores: {list(eigenvals.keys())}")
        print(f"Módulo de los autovalores: {[sp.Abs(ev).evalf() for ev in eigenvals.keys()]}")
    else:
        print("\n✗ ERROR: El polinomio calculado no coincide.")

if __name__ == "__main__":
    verify_sor_characteristic()
