# Métodos Iterativos para Sistemas Lineales (Jacobi, Gauss-Seidel y SOR)

Los métodos iterativos se utilizan para resolver grandes sistemas de ecuaciones lineales de la forma $Ax = b$, especialmente cuando la matriz $A$ es rala (sparse). A diferencia de los métodos directos (como $LU$), generan una sucesión de aproximaciones $x^{(k)}$ que convergen a la solución exacta $x$.

## Descomposición de la Matriz $A$

Para derivar estos métodos, descomponemos $A$ en:

$$
A = L + D + U

$$
Donde:

- $D$: Matriz diagonal ($a_{ii}$).
- $L$: Matriz triangular inferior estricta ($a_{ij}$ con $i > j$).
- $U$: Matriz triangular superior estricta ($a_{ij}$ con $i < j$).

---

## 1. Método de Jacobi

Se basa en despejar la componente $x_i$ de la $i$-ésima ecuación asumiendo que las demás componentes son conocidas del paso anterior.

### Forma Matricial
Partimos de $(D + L + U)x = b \implies Dx = -(L + U)x + b$.

$$
x^{(k+1)} = D^{-1} [b - (L + U)x^{(k)}]

$$
### Forma Estructural (Componente a Componente)
Para cada fila $i$:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)

$$
---

## 2. Método de Gauss-Seidel

Mejora a Jacobi utilizando los valores ya calculados en la iteración actual ($k+1$) para las componentes anteriores.

### Forma Matricial
Partimos de $(D + L)x = -Ux + b$.

$$
x^{(k+1)} = (D + L)^{-1} [b - Ux^{(k)}]

$$
### Forma Estructural
Para cada fila $i$:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)} \right)

$$
---

## 3. Método de Sobrerrelajación Sucesiva (SOR)

Es una aceleración de Gauss-Seidel mediante un factor de relajación $\omega$.

### Definición
Sea $x_{GS}^{(k+1)}$ el valor que devolvería Gauss-Seidel. El paso SOR es una combinación convexa:

$$
x^{(k+1)} = (1 - \omega)x^{(k)} + \omega x_{GS}^{(k+1)}

$$
### Forma Matricial
Reordenando la equivalencia $Ax = b$, derivamos la matriz de iteración $B(\omega)$:

$$
(D + \omega L) x^{(k+1)} = [(1 - \omega)D - \omega U]x^{(k)} + \omega b

$$
??? info "Propiedades de Convergencia"

    - **Condición Necesaria**: El método converge solo si $\omega \in (0, 2)$. Ver [demostración del determinante](../finales/Examen_2026_02_18/01_metodo_sor/teoria.md#inciso-b-determinante-de-iteracion-y-condicion-de-rango-cota).
    - **Matrices SPD**: Si $A$ es Simétrica Definida Positiva, SOR converge para cualquier $\omega \in (0, 2)$.
    - **Diagonal Dominante**: GS y Jacobi convergen si $A$ es estrictamente dominante por filas.

    Fin de la observación.

---

## Referencias

### Libros

| Método | Referencia | Capítulo / Sección |
|---|---|---|
| Jacobi, GS, SOR | Golub, G. H., & Van Loan, C. F. — *Matrix Computations* (4ª ed., 2013). Johns Hopkins University Press. | Cap. 11: *Iterative Methods for Linear Systems* |
| Jacobi, GS | Burden, R. L., & Faires, J. D. — *Numerical Analysis* (10ª ed., 2016). Cengage Learning. | §7.3: *The Jacobi and Gauss-Siedel Iterative Techniques* |
| SOR | Young, D. M. — *Iterative Solution of Large Linear Systems* (1971). Academic Press. | Cap. 3–4 *(obra fundacional del método SOR)* |
| Jacobi, GS, SOR | Trefethen, L. N., & Bau, D. — *Numerical Linear Algebra* (1997). SIAM. | Lecture 40: *Iterative Methods* |
| Jacobi, GS, SOR | Quarteroni, A., Sacco, R., & Saleri, F. — *Numerical Mathematics* (2ª ed., 2007). Springer. | §4.2–§4.4 |

### Recursos Web

| Recurso | URL | Descripción |
|---|---|---|
| Wikipedia — Jacobi method | [https://en.wikipedia.org/wiki/Jacobi_method](https://en.wikipedia.org/wiki/Jacobi_method) | Derivación, pseudocódigo y condiciones de convergencia |
| Wikipedia — Gauss–Seidel method | [https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method) | Comparación con Jacobi, forma matricial |
| Wikipedia — Successive over-relaxation | [https://en.wikipedia.org/wiki/Successive_over-relaxation](https://en.wikipedia.org/wiki/Successive_over-relaxation) | Teorema de Kahan, $\omega$ óptimo para matrices SPD |
| MIT OpenCourseWare 18.335 | [https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/) | Apuntes y problem sets sobre métodos iterativos |
| Scipy — `scipy.sparse.linalg` | [https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html) | Implementaciones de referencia (CG, GMRES, etc.) |
| Gilbert Strang — MIT 18.06 (YouTube) | [https://www.youtube.com/watch?v=0bO4n6PuDSc](https://www.youtube.com/watch?v=0bO4n6PuDSc) | Clase sobre matrices iterativas y convergencia |

---

## Verificación Computacional

A continuación se presenta un script que compara la velocidad de convergencia de los tres métodos para una matriz aleatoria de predominio diagonal:

```python
import numpy as np

def jacobi(A, b, x0, tol=1e-10, max_iter=1000):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(D, b - LU @ x)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def gauss_seidel(A, b, x0, tol=1e-10, max_iter=1000):
    DL = np.tril(A)
    U = A - DL
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(DL, b - U @ x)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def sor(A, b, x0, omega, tol=1e-10, max_iter=1000):
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    
    M = D + omega * L
    N = (1 - omega) * D - omega * U
    
    x = x0.copy()
    for i in range(max_iter):
        x_new = np.linalg.solve(M, N @ x + omega * b)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def run_comparison():
    # Generar una matriz diagonalmente dominante para asegurar convergencia
    n = 10
    A = np.random.randn(n, n)
    A = A + np.diag(np.sum(np.abs(A), axis=1) + 1)
    b = np.random.randn(n)
    x0 = np.zeros(n)
    
    sol_exacta = np.linalg.solve(A, b)
    
    print(f"Comparación de Métodos Iterativos (n={n})")
    print("-" * 40)
    
    res_j, it_j = jacobi(A, b, x0)
    print(f"Jacobi:       {it_j:3} iteraciones | Error: {np.linalg.norm(res_j - sol_exacta):.2e}")
    
    res_gs, it_gs = gauss_seidel(A, b, x0)
    print(f"Gauss-Seidel: {it_gs:3} iteraciones | Error: {np.linalg.norm(res_gs - sol_exacta):.2e}")
    
    omega_opt = 1.1 # Aproximación simple
    res_sor, it_sor = sor(A, b, x0, omega_opt)
    print(f"SOR (w={omega_opt}): {it_sor:3} iteraciones | Error: {np.linalg.norm(res_sor - sol_exacta):.2e}")
    
    # Validaciones booleanas rigurosas
    assert np.allclose(res_j, sol_exacta, atol=1e-8)
    assert np.allclose(res_gs, sol_exacta, atol=1e-8)
    assert np.allclose(res_sor, sol_exacta, atol=1e-8)
    print("\n[OK] Todos los métodos convergen a la solución exacta.")

if __name__ == "__main__":
    run_comparison()

```
