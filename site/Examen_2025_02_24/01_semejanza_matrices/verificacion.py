import numpy as np

def separar_seccion(titulo):
    print("\n" + "="*70)
    print(f" {titulo} ")
    print("="*70)

# ==========================================
# 1. Verificación de Relación de Equivalencia
# ==========================================
separar_seccion("1. Verificando Relación de Equivalencia (Casos Prácticos)")

def generar_matriz_invertible(n):
    """Genera matrices aleatorias hasta garantizar que su determinante no sea 0."""
    while True:
        S = np.random.rand(n, n)
        if np.linalg.det(S) != 0:
            return S

n = 3
A = np.random.rand(n, n)

print("A) Reflexividad (A ~ A)")
I = np.eye(n)
A_ref = I @ A @ np.linalg.inv(I)
print("A es semejante a sí misma (probado con la matriz Identidad).")
print("¿Resultado idéntico a A original?:", np.allclose(A, A_ref))

print("\nB) Simetría (A ~ B implica B ~ A)")
S = generar_matriz_invertible(n)
B = S @ A @ np.linalg.inv(S)

S_inv = np.linalg.inv(S)
A_sim = S_inv @ B @ np.linalg.inv(S_inv)
print("¿Recuperamos A a partir de B usando la inversa de la transformación?:", np.allclose(A, A_sim))

print("\nC) Transitividad (A ~ B y B ~ C implica A ~ C)")
T = generar_matriz_invertible(n)
C = T @ B @ np.linalg.inv(T)

U = T @ S
C_trans = U @ A @ np.linalg.inv(U)
print("¿Obtenemos la misma matriz C operando desde A directamente con (T*S)?:", np.allclose(C, C_trans))

# ==========================================
# 2. Verificación de la Tr(A) = Tr(B)
# ==========================================
separar_seccion("2. Verificación de Tr(A) = Tr(B) para matrices semejantes")
S_trace = generar_matriz_invertible(n)
A_trace = np.random.rand(n, n)
B_trace = S_trace @ A_trace @ np.linalg.inv(S_trace)

tr_A = np.trace(A_trace)
tr_B = np.trace(B_trace)
print(f"Traza de A original: {tr_A:.6f}")
print(f"Traza de B semejante: {tr_B:.6f}")
print("¿Trazas son matemáticamente iguales?:", np.isclose(tr_A, tr_B))

# ==========================================
# 3. Verificación de A^2 = A
# ==========================================
separar_seccion("3. Verificación de A^2 = A para matriz diagonalizable (autovalores 0 y 1)")

# Crear matriz diagonal que contenga estrictamente 0s y 1s
D = np.diag(np.random.choice([0, 1], size=n))
print("Matriz Diagonal D:\n", D)

# Generar una base S cualquiera y aplicarla para construir A
S_idem = generar_matriz_invertible(n)
A_idem = S_idem @ D @ np.linalg.inv(S_idem)

A_cuadrado = A_idem @ A_idem

print("\nValidación con np.allclose de A^2 == A:", np.allclose(A_idem, A_cuadrado))
print("\nMatriz A original generada:\n", A_idem.round(4))
print("\nMatriz A^2 calculada:\n", A_cuadrado.round(4))

print("\nTodas las verificaciones completadas con éxito.")
