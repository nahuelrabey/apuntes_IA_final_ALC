import sympy as sp

def verify_base_change():
    print("Verificando formalmente las matrices de cambio de base...")

    # Definir dimensión y símbolos para los vectores de la base y coordenadas
    n = 3
    # Generamos una base genérica v1, v2, v3
    V = sp.Matrix(n, n, lambda i, j: sp.symbols(f'v_{i+1}{j+1}'))
    # Generamos coordenadas genéricas c1, c2, c3
    C = sp.Matrix(n, 1, lambda i, j: sp.symbols(f'c_{i+1}'))

    # 1. Definimos x como la combinación lineal: x = c1*v1 + c2*v2 + c3*v3
    # Esto es equivalente a V * C
    x = V * C
    
    print("\nVector x (en base canónica) expresado como V * [x]_B:")
    sp.pprint(x)

    # 2. Verificamos que si aplicamos V^-1 a x, obtenemos C ([x]_B)
    print("\nCalculando V^-1 * x...")
    res = V.inv() * x
    
    # Simplificamos para asegurar que SymPy reconozca la identidad
    res_simplified = sp.simplify(res)
    
    if res_simplified == C:
        print("\n✓ VERIFICACIÓN EXITOSA: V^-1 * x devuelve el vector de coordenadas [x]_B.")
        sp.pprint(res_simplified)
    else:
        print("\n✗ ERROR: La identidad no se cumplió.")

if __name__ == "__main__":
    verify_base_change()
