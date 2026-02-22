import numpy as np

def separar_seccion(titulo):
    print("\n" + "="*75)
    print(f" {titulo} ")
    print("="*75)

c = 0.5 # Seleccionamos un valor dentro del intervalo de convergencia (|c| < 1)
print(f"Configurando parámetro modelo de prueba: c = {c}")

# Construcción de la matriz y el vector b
A = np.array([
    [1, c, 0],
    [0, 1, c],
    [0, c, 1]
])
# Vector solución deseado "arbitrario", por ende b = A @ x_real
x_real = np.array([1.0, 2.0, -1.0])
b = A @ x_real


# ==========================================
# 1. Verificación de Radios Espectrales
# ==========================================
separar_seccion("1. Verificación de Autovalores de Iteración")

D = np.diag(np.diag(A))
L = np.tril(A, -1)
U = np.triu(A, 1)

D_inv = np.linalg.inv(D)
T_J = -D_inv @ (L + U)

DL_inv = np.linalg.inv(D + L)
T_GS = -DL_inv @ U

autovalores_TJ = np.linalg.eigvals(T_J)
rho_TJ = max(abs(autovalores_TJ))

autovalores_TGS = np.linalg.eigvals(T_GS)
rho_TGS = max(abs(autovalores_TGS))

print(f"Autovalores teóricos esperados T_J: [0, {c}, {-c}]")
print(f"Autovalores computados T_J:         {autovalores_TJ.round(4)}")
print(f"Radio Espectral Rho(T_J) (Debería ser |c|={c}): {rho_TJ:.4f}")

print(f"\nAutovalores teóricos esperados T_GS: [0, 0, {c**2}]")
print(f"Autovalores computados T_GS:         {autovalores_TGS.round(4)}")
print(f"Radio Espectral Rho(T_GS) (Debería ser |c|²={c**2}): {rho_TGS:.4f}")

# ==========================================
# 2. Verificación de Velocidad de Convergencia Iterativa
# ==========================================
separar_seccion("2. Simulación de los Métodos Iterativos")

def norm_res(x):
    return np.linalg.norm((A @ x) - b)

tol = 1e-10
max_iter = 1000

# ----- JACOBI -----
x_j = np.zeros(3)
iter_j = 0
while norm_res(x_j) > tol and iter_j < max_iter:
    x_next = np.zeros(3)
    x_next[0] = b[0] - c * x_j[1]
    x_next[1] = b[1] - c * x_j[2]
    # En Jacobi siempre usa el modelo viejo
    x_next[2] = b[2] - c * x_j[1]
    x_j = x_next
    iter_j += 1

# ----- GAUSS-SEIDEL -----
x_gs = np.zeros(3)
iter_gs = 0
while norm_res(x_gs) > tol and iter_gs < max_iter:
    x_next = np.zeros(3)
    x_next[0] = b[0] - c * x_gs[1]
    x_next[1] = b[1] - c * x_gs[2]
    # En Gauss-Seidel usa la porción de x que viene de este mismo turno
    x_next[2] = b[2] - c * x_next[1] 
    x_gs = x_next
    iter_gs += 1


print(f"Tolerancia pautada: {tol}")
print(f"Iteraciones necesarias con Jacobi:       {iter_j}")
print(f"Iteraciones necesarias con Gauss-Seidel: {iter_gs}")
print("\n¿Gauss-Seidel tomó prácticamente la mitad del tiempo? (T_GS iter ~= T_J iter / 2)")
factor_velocidad = iter_j / iter_gs
print(f"-> Iteraciones_J / Iteraciones_GS = {factor_velocidad:.2f}")

print("\nVerificamos que ambas confluyeron a la solución final (1.0, 2.0, -1.0):")
print(f"x final Jacobi:       {x_j.round(5)}")
print(f"x final Gauss-Seidel: {x_gs.round(5)}")
