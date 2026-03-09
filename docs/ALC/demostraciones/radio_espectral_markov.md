# Radio Espectral de una Matriz de Markov

> **Teorema.**
> Sea $P \in \mathbb{R}^{n \times n}$ una matriz estocástica por columnas (es decir, $p_{ij} \ge 0$ para todo $i,j$ y $\sum_{i=1}^n p_{ij} = 1$ para todo $j$). Entonces, su radio espectral es exactamente 1:
>
>

$$
> \rho(P) = 1
>

$$
>

## Interpretación del Enunciado

En el estudio de las **Cadenas de Markov**, la matriz de transición $P$ dicta cómo evoluciona la probabilidad de los estados de un sistema. El hecho de que el radio espectral sea siempre igual a 1 es fundamental porque garantiza que las probabilidades globales no diverjan ni se desvanezcan, posibilitando la existencia de al menos un **estado de equilibrio estacionario**.

---

## Demostración

La demostración se divide en dos secciones fundamentales: validar que $\lambda = 1$ es siempre un autovalor de $P$, y constatar deductivamente que no puede postularse ningún autovalor general con un módulo estrictamente mayor a 1 para esta matriz.

### 1. $\lambda = 1$ es autovalor de $P$

Las columnas de una matriz estocástica suman de a conjuntos a un total de 1. Aprovechamos un vector constituido por la constante unos $e = (1, 1, \dots, 1)^T$ para exponer la evaluación.

Multiplicar $e^T$ por $P$ corresponde numéricamente a sumar las filas de cada columna. Dado el axioma fundamental dictado en que cada columna suma 1, el vector resultante transpone su valor sin ser transmutado a nuevas proporciones:

$$
e^T P = (1, 1, \dots, 1) P = \left( \sum_{i=1}^n p_{i1}, \sum_{i=1}^n p_{i2}, \dots, \sum_{i=1}^n p_{in} \right) = (1, 1, \dots, 1) = e^T

$$
Aplicando el factor iterativo transpuesto respectivo sobre el equilibrio logrado en la igualdad:

$$
(e^T P)^T = (e^T)^T \implies P^T e = e = 1 \cdot e

$$
Esto demuestra directamente que **$e$ es un autovector de $P^T$ asociado al autovalor $\lambda = 1$**.

Comprendiendo en análisis formal que una formulación escalar de una matriz analizada $P$ y su matriz homóloga traspuesta $P^T$ son dependientes rigurosas de un polinomio característico uniforme y determinantes análogas entre sí (ver [Determinante de la Traspuesta](./determinante_producto.md)), entonces invariablemente **$\lambda = 1$ es un autovalor general también contenido por $P$**.

### 2. Ningún autovalor excede 1 en módulo ($|\lambda| \le 1$)

Sea $\lambda$ un coeficiente modular de cualquier autovalor base de $P$ asociado estructuralmente a un autovector no-nulo de la misma matriz $v = (v_1, v_2, \dots, v_n)^T$ de orden vectorial ($v \neq 0$). Dado que los autovalores y autovectores frecuentan dominios complejos interdimensionales, la aserción debe acotarse midiendo de base sus respectivos módulos integrales de origen.

La ecuación de autovalores es $P v = \lambda v$. Evaluando aisladamente frente a la función suma de la componente formal del elemento estructural $i$-ésimo dependiente paramétrico del álgebra base:

$$
\lambda v_i = \sum_{j=1}^n p_{ij} v_j

$$
Mediante uso estricto del valor modular subrogante y sumando la desigualdad triangular pertinente al escenario algebraico analizado ($|a+b| \le |a|+|b|$), llegamos a lo predispuesto en formato final:

$$
|\lambda| |v_i| = \left| \sum_{j=1}^n p_{ij} v_j \right| \le \sum_{j=1}^n |p_{ij} v_j| = \sum_{j=1}^n p_{ij} |v_j|

$$
*(Nota de aclaración: se considera algorítmicamente que como $p_{ij} \ge 0$, se infiere analíticamente por equivalencia modular $|p_{ij}| = p_{ij}$).*

Seleccionamos mediante iteración general paramétrica $k$ de acuerdo con el índice de la componente contenida de la forma analizada puntual y delimitando al valor escalar de módulo máximo: $|v_k| = \max_j |v_j|$.
Reemplazamos correspondientemente la cuota equivalente acotando todo el conjunto del grupo mediante la ponderación unificada sobre las partes del módulo $|v_k|$, la cual delimitará algebraicamente por medio posicional y formal al formato integral una estimación del valor máximo tolerado final de mayor espectro a favor de una desigualdad con estrictez general:

$$
|\lambda| |v_i| \le \sum_{j=1}^n p_{ij} |v_k| = |v_k| \sum_{j=1}^n p_{ij}

$$
Sujeto a generalización subestratificada algorítmicamente y en igualdad paramétrica base a su condición puntual para fila abstracta equivalente a $k$:

$$
|\lambda| |v_k| \le |v_k| \sum_{j=1}^n p_{kj}

$$
En base al condicionamiento algorítmico natural originado para matrices dictado y estocástico general, formalizamos a su vez que de presentarse estrictamente la conformación particular referida sobre validaciones **por columnas**, y al ser inyectados valores que no provienen dependientes vectorialmente por filas absolutas (es pertinente acotar que iterar el coeficiente transitorio $\sum_{j=1}^n p_{kj}$ correspondiente a la forma global total de fila dependiente asignada para la posición $k$ no está normado bajo base integral igual al rango unificado estricto posicional número $1$ de antemano).

Podemos solventar la carencia dimensional y validar estocásticamente invocando para la matriz homóloga evaluando algorítmicamente y asintoticamente equivalente el desglose paramétrico evaluado antes asignado al parámetro sobre la estructura subrogante transpuesta formal $P^T$ en condición simétrica y evaluada ($P$ es equivalente por bases al igual contenido y matriz simétrica de conformación escalar integral original formal). La ecuación deducida $P^T u = \lambda u$ para la componente asignada equivalente general estricta transpuesta posicional iterativa paramétrica en concordancia algorítmica y su componente general simétrica de valor equivalente de índice $k$ del formato vectorial paramétrico acotado genérico $u$ estipula que la sumatoria arroja un resultado analíticamente preestimado igualitario a la totalidad uno paramétrica a la postre posicional por variable base y dimensional dictado al uno analizado posicionalmente en la unidad fundamental final lograda formal:

$$
|\lambda| |u_k| \le |u_k| \sum_{j=1}^n (P^T)_{kj} = |u_k| \underbrace{\sum_{j=1}^n p_{jk}}_{= 1} = |u_k| \cdot 1

$$
Con base al entendimiento originado desde los formatos formales, para el vector genérico iterativo subrogante estructurado algebraico ($u$), si este de base por análisis matricial previo expone dependencia con vector genérico fundamental dependiente vectorial del nexo de espectros formal originados por subrogar los dictados paramétricos interconectados que derivan e implican dictaminar a $u \neq 0$ originando en equivalencia iterativa la constante iterativa estricta posicional $|u_k| > 0$. Esto permite seccionar transversal y vectorialmente dividiendo y despejando hacia su espectro:

$$
|\lambda| \le 1

$$
### 3. Conclusión

Dado de forma conclusiva y preambular por vía procedimental deductiva que cualquier conjunto variable o componente estructural de autovalores genéricos de autovalores de la matriz origen (y recíprocamente de la originada tras ser transpuesta base y analítica) cumple inequívocamente $| \lambda| \le 1$ como se formalizó iterativamente su dependencia de rango y al estar deducida explícitamente la presencia base inicial y general iterativa constante escalar igual analítica $\lambda = 1$, el autovalor originado tras los cómputos que conformará la medida asintótica máxima modular máxima originará iterativamente el valor equivalente estricto uno algebraico estipulado. Atendiendo estructural y por base formal la definición preestablecida en general aplicable paramétrica el radio paramétrico de su espectro arroja algoritmizada y deductivamente el escalar unario de la equivalencia dimensional precalculado:

$$
\rho(P) = \max \{ |\lambda| : \lambda \in \sigma(P) \} = 1

$$
---

## Referencias Externas

*   **Libro**: *Linear Algebra and Its Applications* (David C. Lay). **Capítulo 4, Sección 4.9: "Applications to Markov Chains"**. Demuestra estructuralmente cómo una matriz estocástica siempre admite el estado estacionario iterativo $\lambda=1$.
*   **Libro**: *Matrix Computations* (Golub & Van Loan). **Capítulo 7, Sección 7.1**. Demostración analítica usando el Teorema de Gershgorin para acotar el espectro matricial dentro de discos unitarios basándose en las normas de transición.
*   **Web**: [Markov Matrices and Eigenvectors](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/video-lectures/) - *MIT OpenCourseWare (Gilbert Strang, Lecture 24)*. Expone en video la deducción con el vector de unos para $P^T$.

---

## Verificación Empírica Computacional

Aplicamos el testeo mediante simulación de matrices de Markov aleatorias y verificamos algorítmicamente mediante ejecución del submódulo computacional NumPy su rango paramétrico por variables escalares:

```python
import numpy as np

def verify_markov_spectral_radius(n_size=10, num_tests=5):
    """
    Simula matrices estocásticas por columnas aleatorias de tamaño n_size
    y verifica empíricamente que:
    1. El mayor módulo de sus autovalores es 1 (dentro de tolerancia numérica).
    2. El vector de unos e=(1,...,1) es autovector a izquierda (autovector de P.T).
    """
    np.random.seed(42)
    print(f"VERIFICACIÓN TEÓRICA: Radio Espectral de Matrices de Markov")
    print("-" * 65)

    all_passed = True
    for i in range(num_tests):
        # Generar matriz aleatoria con entradas >= 0 (distribución uniforme [0, 1))
        P_raw = np.random.rand(n_size, n_size)
        
        # Normalizar por columnas (para que la suma de cada columna sea exactamente 1)
        # sum_cols tiene shape (n_size,), la estiramos a (1, n_size) para hacer broadcasting
        sum_cols = np.sum(P_raw, axis=0) 
        P = P_raw / sum_cols
        
        # Extraemos los autovalores
        eigenvalues = np.linalg.eigvals(P)
        
        # Obtenemos sus módulos (magnitudes en el plano complejo)
        mods = np.abs(eigenvalues)
        
        # Encontramos el módulo máximo (debería ser el radio espectral)
        spectral_radius = np.max(mods)
        
        # Comprobación de que el autovalor "1" está presente y no hay mayores
        is_radius_one = np.isclose(spectral_radius, 1.0, atol=1e-10)
        all_passed = all_passed and is_radius_one
        
        print(f"Test {i+1}: ρ(P) calculado = {spectral_radius:.10f} | ¿Es 1.0?: {is_radius_one}")
        
    print("-" * 65)
    
    # Verificación del vector propio de P^T
    e_vector = np.ones(n_size)
    P_T_e = P.T @ e_vector
    
    # Comprobación estricta tolerante
    eigen_check = np.allclose(P_T_e, e_vector, atol=1e-10)
    print(f"¿Se cumple P^T * e = e?: {eigen_check}")
    
    if all_passed and eigen_check:
        print("\nResultado: LA PROPIEDAD SE CUMPLE. El radio espectral ρ(P) = 1 estricto.")
    else:
        print("\nError detectado: La propiedad falla o problemas de precisión (allclose).")

if __name__ == "__main__":
    verify_markov_spectral_radius(n_size=50, num_tests=10)

```
