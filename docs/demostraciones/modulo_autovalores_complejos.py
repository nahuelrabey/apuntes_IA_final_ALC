import sympy as sp

def verify_complex_eigenvalue_modulus():
    print("Verificando relación entre término independiente y módulo de raíces complejas...")
    
    # Caso SOR Examen 18-02-2026: lam^2 - 7/8*lam + 1/4 = 0
    lam = sp.symbols('lambda')
    b = sp.Rational(-7, 8)
    c = sp.Rational(1, 4)
    poly = lam**2 + b*lam + c
    
    print(f"\nPolinomio: {poly} = 0")
    
    # 1. Calcular discriminante
    delta = b**2 - 4*c
    print(f"Discriminante (Delta): {delta} ({float(delta):.4f})")
    
    # 2. Hallar raíces
    roots = sp.solve(poly, lam)
    print(f"Raíces calculadas: {roots}")
    
    # 3. Calcular módulos
    for i, r in enumerate(roots):
        mod = sp.Abs(r)
        print(f"|lambda_{i+1}| = {mod} (dec: {float(mod):.4f})")
        
        # Verificar contra sqrt(c)
        if sp.simplify(mod - sp.sqrt(c)) == 0:
            print(f"  ✓ Coincide con sqrt(c) = sqrt({c})")
        else:
            print(f"  ✗ error en la coincidencia")

if __name__ == "__main__":
    verify_complex_eigenvalue_modulus()
