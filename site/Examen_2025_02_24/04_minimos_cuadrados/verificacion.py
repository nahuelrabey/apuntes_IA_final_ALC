import numpy as np

def separar_seccion(titulo):
    print("\n" + "="*75)
    print(f" {titulo} ")
    print("="*75)

# ==========================================
# 1. Preparación del Sistema Matemático Base
# ==========================================
separar_seccion("1. Generación de Puntos y Solución Única Mínima")

# Creamos parámetros "secretos" o ideales que la máquina debe reconstruir
a_real = 4.5
b_real = -1.2
c_real = 2.0

def generar_Z_real(x, y):
    """ Función original z = a * y^b * e^(cx + 2) """
    Z_val = a_real * (y**b_real) * np.exp(c_real * x + 2)
    return Z_val

# Evaluamos con la "mínima cantidad de puntos" propuesta teóricamente: m = 3
# Recordemos el inciso 2: elegí (1, 1), (0, e), (-1, 1) que demostraron independencia
puntos = [
    (1, 1),
    (0, np.exp(1)),
    (-1, 1)
]

x_array = np.array([p[0] for p in puntos])
y_array = np.array([p[1] for p in puntos])
z_array = generar_Z_real(x_array, y_array)

print(f"Parámetros intrínsecos ocultos: a={a_real}, b={b_real}, c={c_real}")
print(f"Cantidad de puntos inyectados: {len(puntos)} (El mínimo teórico estipulado)")


# ==========================================
# 2. Resolución de Mínimos Cuadrados
# ==========================================
separar_seccion("2. Reconstrucción Paramétrica usando Mínimos Cuadrados Ordinarios (MCO)")

# Modelado Vectorial de la Transformación:
# M = [1, ln(y), x]
# Z_transformed = ln(z) - 2

M = np.column_stack((
    np.ones(len(puntos)),
    np.log(y_array),
    x_array
))

Z_transformado = np.log(z_array) - 2

print("Matriz de Diseño (M):")
print(M)
rango = np.linalg.matrix_rank(M)
print(f"\nRango calculado de la Matriz M: {rango}")
if rango == 3:
    print(">> Rango Completo detectado: M^T M es estrictamente invertible, existe SOLO 1 SOLUCION.")

# Calculamos Ecuaciones Normales explícitamete: (M^T M) θ = M^T Z
Mt = M.T
Mt_M = Mt @ M
Mt_Z = Mt @ Z_transformado

try:
    parametros_estimados_theta = np.linalg.inv(Mt_M) @ Mt_Z
    A_est, b_est, c_est = parametros_estimados_theta
    a_est = np.exp(A_est)
    
    print("\nResultados del Fitteo de Mínimos Cuadrados:")
    print(f"a_estimado : {a_est:.4f}  (Real: {a_real})")
    print(f"b_estimado : {b_est:.4f}  (Real: {b_real})")
    print(f"c_estimado : {c_est:.4f}  (Real: {c_real})")
    
    # Tolerancia
    if np.allclose([a_est, b_est, c_est], [a_real, b_real, c_real]):
        print("\n>> EXITO: Los estimadores convergieron idénticos con precisión perfecta usando solo 3 puntos.")

except np.linalg.LinAlgError:
    print(">> ERROR: La matriz M^T M generada resultó escalarmente singular (Puntos colineales o dependientes).")


# ==========================================
# 3. Prueba de Fallo con puntos insuficientes
# ==========================================
separar_seccion("3. Comprobación de Sub-determinación (N < 3)")

print("Intentando predecir MCO usando sub-muestreo intencionado (sólo usando 2 puntos):")
M_deficiente = M[:2, :]  # Agarro nomás las primeras dos filas
rango_deficiente = np.linalg.matrix_rank(M_deficiente)
print(f"Rango M_deficiente: {rango_deficiente}")
print("El sistema posee columnas linealmente dependientes por defecto. Las variables libres arrojan infinitas soluciones viables.")
try:
    np.linalg.inv(M_deficiente.T @ M_deficiente)
except np.linalg.LinAlgError as e:
    print(f"\n>> VALIDADO: linalg.inv() disparó la protección matemática LinAlgError -> {e}.")
    print("Imposible hallar solución única paramétrica con menos de 3 puntos, reafirmando lo resuelto analíticamente.")
