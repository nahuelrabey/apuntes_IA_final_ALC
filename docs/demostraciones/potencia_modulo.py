import numpy as np

def verify_power_module():
    print("Verificando propiedad |a^n| = |a|^n ...")
    
    # Casos de prueba: (a, n)
    test_cases = [
        (2, 3),            # Real positivo
        (-3, 2),           # Real negativo, potencia par
        (-3, 3),           # Real negativo, potencia impar
        (1 + 1j, 4),       # Complejo
        (0.5, 10),         # Menor que 1
        (1.2, 5)           # Mayor que 1
    ]
    
    for a, n in test_cases:
        left_side = abs(a**n)
        right_side = abs(a)**n
        
        match = np.isclose(left_side, right_side)
        print(f"a = {a:10}, n = {n:2} | |a^n| = {left_side:10.4f}, |a|^n = {right_side:10.4f} | Match: {match}")

    print("\nVerificando implicancia |a^n| < 1 => |a| < 1 ...")
    for a in [0.9, 1.1, -0.9, -1.1, 0.5 + 0.5j, 1+1j]:
        n = 5
        val_an = abs(a**n)
        val_a = abs(a)
        condition = val_an < 1
        conclusion = val_a < 1
        print(f"|a^n| = {val_an:8.4f} (<1? {condition:5}) => |a| = {val_a:8.4f} (<1? {conclusion:5})")

if __name__ == "__main__":
    verify_power_module()
