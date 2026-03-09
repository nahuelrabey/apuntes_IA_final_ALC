import numpy as np

def separar_seccion(titulo):
    print("\n" + "="*75)
    print(f" {titulo} ")
    print("="*75)

# ==========================================
# 1. Descomposición en Valores Singulares (SVD)
# ==========================================
separar_seccion("1. Confirmación de SVD Analítica")
A = np.array([[0, -1, 0],
              [2,  0, 0],
              [0,  0, -3]])

# Matrices teóricas derivadas a mano
U_teoric = np.array([[ 0,  0, -1],
                     [ 0,  1,  0],
                     [-1,  0,  0]])
Sigma_teoric = np.diag([3, 2, 1])
Vt_teoric = np.array([[0, 0, 1],
                      [1, 0, 0],
                      [0, 1, 0]])

# Reconstruir A desde la teoría
A_reconstruida = U_teoric @ Sigma_teoric @ Vt_teoric
print("A reconstruida con matrices teóricas:")
print(A_reconstruida)
print("¿Coincide exactamente con la matriz original? :", np.allclose(A, A_reconstruida))

# Usar herramienta directa de NumPy (que a veces toma orientaciones de signo distintas al estar estandarizado)
U_np, s_np, Vt_np = np.linalg.svd(A)
print("\nValores singulares numéricos provistos por np.linalg.svd:")
print(s_np)
print("¿Coinciden los valores singulares extraídos (3, 2, 1)? :", np.allclose([3, 2, 1], s_np))

# ==========================================
# 2. Invarianzas ante Matrices de Permutación
# ==========================================
separar_seccion("2. Espectro inmutable bajo Transformaciones Ortogonales (Permutaciones)")

# Generar una matriz de permutación al azar mezclando la matriz identidad
I = np.eye(3)
P = I[np.random.permutation(3), :]
print("Matriz de Permutación generada (P):")
print(P)

print("\nVerificando que P sea ortogonal (P.T @ P == I):", np.allclose(P.T @ P, I))

# Analizamos PA y AP
PA = P @ A
AP = A @ P

_, s_PA, _ = np.linalg.svd(PA)
_, s_AP, _ = np.linalg.svd(AP)

print(f"\nValores singulares originales de A: {s_np.round(2)}")
print(f"Valores singulares de PA :        {s_PA.round(2)}")
print(f"Valores singulares de AP :        {s_AP.round(2)}")
print("¿Son matemáticamente equivalentes? :", np.allclose(s_np, s_PA) and np.allclose(s_np, s_AP))

# ==========================================
# 3. Norma-2 y Número de Condición
# ==========================================
separar_seccion("3. Cálculo Numérico de Norma y Condición")

norm_2_PA = np.linalg.norm(PA, ord=2)
cond_2_PA = np.linalg.cond(PA, p=2)

print(f"||PA||_2 obtenido por linalg  = {norm_2_PA:.4f}")
print(f"||PA||_2 de resultado teórico = 3")
print("¿Concuerda la Norma? :", np.isclose(norm_2_PA, 3))

print(f"\nCond2(PA) obtenido por linalg    = {cond_2_PA:.4f}")
print(f"Cond2(PA) de resultado teórico   = 3")
print("¿Concuerda el Condición Num? :", np.isclose(cond_2_PA, 3))

print("\nTodo el flujo analítico validado consistentemente.")
