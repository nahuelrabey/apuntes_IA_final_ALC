# Cambio de Base: Matrices $B$ y $B^{-1}$

> **Demostración.** Dada una base $B = \{v_1, v_2, \dots, v_n\}$ de un espacio vectorial $V$, demostrar que la matriz $B$ (cuyas columnas son los vectores de la base) transforma coordenadas en base $B$ a la base canónica, y que su inversa $B^{-1}$ realiza la transformación opuesta.

## Interpretación del Enunciado

El objetivo es formalizar la relación entre un vector $x$ expresado en la base canónica y sus coordenadas $[x]_B$ respecto a una base arbitraria $B$. Esta distinción es fundamental para entender operaciones como la diagonalización o la construcción de proyectores oblicuos, donde "filtramos" componentes en direcciones específicas.

---

## Solución Analítica

### 1. La Matriz de Paso $B$ (de Base $B$ a Canónica)

Sea un vector $x \in V$. Por definición de base, $x$ se puede escribir de forma única como una combinación lineal de los vectores de $B$:

$$
x = c_1 v_1 + c_2 v_2 + \dots + c_n v_n

$$
Donde los escalares $c_i$ son las coordenadas de $x$ en la base $B$, denotadas como:

$$
[x]_B = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}

$$
Si disponemos los vectores $v_i$ como columnas de una matriz $B = [v_1 | v_2 | \dots | v_n]$, la combinación lineal anterior se traduce exactamente en el producto matriz-vector:

$$
x = \begin{pmatrix} | & | & & | \\ v_1 & v_2 & \dots & v_n \\ | & | & & | \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix} = B [x]_B

$$
Por lo tanto, **la matriz $B$ toma un vector de coordenadas $[x]_B$ y devuelve el vector $x$ en la base canónica**.

### 2. La Matriz Inversa $B^{-1}$ (de Canónica a Base $B$)

Puesto que los vectores $\{v_1, \dots, v_n\}$ forman una base, son linealmente independientes. Esto garantiza que la matriz $B$ es cuadrada y de rango completo, por lo tanto, es **invertible**.

Si multiplicamos a izquierda por $B^{-1}$ en la ecuación anterior:

$$
B^{-1} x = B^{-1} (B [x]_B)

$$
$$
B^{-1} x = (B^{-1} B) [x]_B

$$
$$
B^{-1} x = I [x]_B = [x]_B

$$
Esto demuestra que **la matriz $B^{-1}$ toma un vector en la base canónica y devuelve sus coordenadas en la base $B$**.

??? info "Conclusión Táctica"
    En la construcción de un proyector $P = B D B^{-1}$, el orden de aplicación (de derecha a izquierda) es:

    1.  **$B^{-1}$**: Lleva el vector al "espacio de la base $B$".
    2.  **$D$**: Opera sobre sus componentes (proyecta).
    3.  **$B$**: Devuelve el resultado al sistema de coordenadas estándar (canónico).

    Fin de la conclusión.

---

```python
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

```
