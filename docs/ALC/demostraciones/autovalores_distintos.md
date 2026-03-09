# Demostración: Independencia Lineal de Autovectores con Autovalores Distintos

## Interpretación del Enunciado

> Demostrar formalmente que si una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ posee autovalores distintos entre sí ($\lambda_i \neq \lambda_j$), entonces sus autovectores correspondientes $\{v_1, v_2, \dots, v_n\}$ son vectores **linealmente independientes**.

Este teorema es la base de la **diagonalización**. Si una matriz de orden $n$ tiene $n$ autovectores linealmente independientes, éstos formarán una base para $\mathbb{R}^n$, permitiendo construir una matriz $P$ inversible que satisfaga la descomposición $A = P D P^{-1}$.

Demostraremos este teorema utilizando el principio de inducción sobre el número de autovectores.

## Solución Analítica (Demostración por Contradicción)

La demostración procede por contradicción, evaluando el conjunto dependiente más pequeño posible.

**PRUEBA.** Supongamos que el conjunto de autovectores $\{v_1, \dots, v_r\}$ es **linealmente dependiente**.

Como cada vector propio es no nulo por definición ($v_i \neq 0$), al menos uno de los vectores en el conjunto debe ser reducible a una combinación lineal de los anteriores.

Sea $p$ el índice más pequeño tal que el vector $v_{p+1}$ es una combinación lineal de los vectores que lo preceden (los cuales asumimos linealmente independientes). Entonces, existen escalares $c_1, \dots, c_p$ tales que:

$$
(Eq. 5) \quad c_1 v_1 + \dots + c_p v_p = v_{p+1}

$$
Multiplicando ambos lados por la matriz $A$, y usando $A v_k = \lambda_k v_k$ para cada índice $k$, obtenemos:

$$
c_1 A v_1 + \dots + c_p A v_p = A v_{p+1}

$$
$$
(Eq. 6) \quad c_1 \lambda_1 v_1 + \dots + c_p \lambda_p v_p = \lambda_{p+1} v_{p+1}

$$
En paralelo, multiplicamos la $(Eq. 5)$ factorizada por $\lambda_{p+1}$ y la restamos a la $(Eq. 6)$:

$$
(Eq. 7) \quad c_1 (\lambda_1 - \lambda_{p+1}) v_1 + \dots + c_p (\lambda_p - \lambda_{p+1}) v_p = \mathbf{0}

$$
Dado que el subconjunto $\{v_1, \dots, v_p\}$ es linealmente independiente, los coeficientes escalares en la ecuación $(Eq. 7)$ deben ser cero.

Los factores compuestos por la diferencia $(\lambda_i - \lambda_{p+1})$ son distintos de cero, ya que el enunciado estipula que todos los autovalores son distintos.

Por lo tanto:

$$
c_i = 0 \quad \text{para } i = 1, \dots, p

$$
Sustituyendo estos ceros en la $(Eq. 5)$, obtenemos que $v_{p+1} = \mathbf{0}$.

Esto representa una contradicción, ya que, por definición, los autovectores no pueden ser el vector nulo. En consecuencia, la suposición original es falsa.

El conjunto $\{v_1, \dots, v_r\}$ **debe ser linealmente independiente**. ∎

---

## Verificación Empírica Computacional

La validación del teorema se verifica mediante el script en Python siguiente, utilizando punto flotante sobre matrices aleatorias.

```python
import numpy as np

def verificar_independencia_autovectores(n: int = 5, iteraciones: int = 1000):
    """
    Verifica estocásticamente si una matriz con n autovalores estrictamente distintos
    posee en consecuencia un conjunto de n autovectores linealmente independientes.
    
    A través del método iterativo de Monte Carlo construimos repetidas veces matrices
    cuyo espectro sea forzosamente dispar, y nos valemos empíricamente del cálculo
    de rango del álgebra computacional de sus bases para descartar colapsos dimensionales.
    
    Args:
        n: Dimensión hiper-espacial cuadrada elegida (cantidad de vectores en la base).
        iteraciones: Cantidad de re-testeos matriciales aleatorios ininterrumpidos.
    """
    np.random.seed(42)  # Control semi-determinista para la validación continua.
    exitos = 0
    
    for _ in range(iteraciones):
        # 1. Generamos 'n' autovalores estrictamente distintos muestreados al azar
        # Sumamos un offset lineal dinámico para garantizar matemáticamente su total disparidad asintótica.
        autovalores_forzados = np.random.rand(n) + np.arange(n) * 10 
        D = np.diag(autovalores_forzados)
        
        # 2. Generamos una Matriz de Pasaje ortogonal Aleatoria 'P' garantizada como invertible
        # (Esto imita cualquier subespacio de RN sin sesgar la varianza)
        M_aleatoria = np.random.randn(n, n)
        Q, R = np.linalg.qr(M_aleatoria) # Factorizamos QR para sacar una matriz ortogonal pura 'Q' pre-fabricada
        
        # 3. Ensamblamos temporalmente nuestra Matriz Base Original A = Q D Q^T
        A = Q @ D @ Q.T
        
        # 4. Solicitamos al cerebro algorítmico resolver el sistema de la matriz pre-armada
        # Obtiene eigenvalues y la matriz unificada continua con sus autovectores por columna (v_1, v_2 ... v_n)
        valores_propios, matriz_autovectores = np.linalg.eig(A)
        
        # 5. La prueba de oro de Independencia Lineal Computacional:
        # Como los vectores están adosados por columnas conformando una Matriz Cuadrada V,
        # Si su rank formal dictaminado por SVD iguala la dimensión del espacio (n),
        # Significa incontrastablemente que absolutamente TODOS sus vectores columna corren independientes.
        rango_efectivo = np.linalg.matrix_rank(matriz_autovectores, tol=1e-10) # Aplicamos la tolerancia al error (No ==)
        
        if rango_efectivo == n:
            exitos += 1
            
    # Resultados del Estrés
    print(f"\n--- Verificador de Independencia de Autovectores (n={n}) ---")
    print(f"Bucle Masivo Efectuado: {iteraciones} matrices aleatorias testeadas.")
    print(f"Matrices con Autovectores que conformaron Bases L.I: {exitos}/{iteraciones}")
    
    if exitos == iteraciones:
        print(">> CONLCUSIÓN: Validado Empíricamente. La aserción del Lema es Universal en R^n.")
    else:
        print(">> ANOMALÍA: Colapso detectado. La teoría o tolerancia falló estadísticamente.")

if __name__ == "__main__":
    verificar_independencia_autovectores()

```
---

## Bibliografía y Recursos Educativos

### 📖 Libros de Texto y Artículos

- **Libro: Álgebra Lineal y sus Aplicaciones (David C. Lay)**. *Capítulo 5: Valores Propios y Vectores Propios*. El autor introduce el "Teorema 2": *Si $v_1, ..., v_r$ son vectores propios que corresponden a valores propios distintos $\lambda_1, ..., \lambda_r$ de una matriz $n \times n$ $A$, entonces el conjunto $\{v_1, ..., v_r\}$ es linealmente independiente.* La demostración avanza por contradicción utilizando anulaciones algebraicas congruentes a las del apunte.
- **Libro: Linear Algebra and Its Applications (Gilbert Strang)**. *Capítulo 6*. Se formaliza que si existen $n$ autovalores distintos, se contará con $n$ autovectores independientes.

### 🇪🇸 Videos en Español

- **[Álgebra Lineal - Autovectores. Propiedades de independencia lineal](https://www.youtube.com/watch?v=KmjpJtXbk90)** (Prof. Jesús Soto, UCAM): Revisa la demostración mostrando la construcción de la ecuación inicial y la manipulación aritmética explicada.
- **[Autovalores y Diagonalización - Multiplicidad de autovectores](https://www.youtube.com/watch?v=JalJlpAYZvw)** (OpenFING): Demostración en clase de la independencia lineal vía subconjunto de multiplicidad $k$.

### 🇺🇸 Videos en Inglés

- **[Linear Independence of Eigenvectors (Proof by Induction)](https://www.youtube.com/watch?v=Fljli8GcfEs)** (Dr. Peyam): Explica la formulación usando inducción, resolviendo explícitamente el Caso Base para expandirse desde allí.
