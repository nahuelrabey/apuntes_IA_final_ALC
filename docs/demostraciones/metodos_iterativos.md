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
    - **Condición Necesaria**: El método converge solo si $\omega \in (0, 2)$. Ver [demostración del determinante](../Examen_2026_02_18/01_metodo_sor/teoria.md#inciso-b-determinante-de-iteracion-y-condicion-de-rango-cota).
    - **Matrices SPD**: Si $A$ es Simétrica Definida Positiva, SOR converge para cualquier $\omega \in (0, 2)$.
    - **Diagonal Dominante**: GS y Jacobi convergen si $A$ es estrictamente dominante por filas.

---

## Verificación Computacional

A continuación se presenta un script que compara la velocidad de convergencia de los tres métodos para una matriz aleatoria de predominio diagonal:

```python
--8<-- "demostraciones/metodos_iterativos.py"
```
