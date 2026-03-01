# Demostración: Criterio de Diagonalizabilidad por Bases de Autoespacios

> **Teorema a Demostrar:**
> Una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ es diagonalizable si y solo si la suma de las multiplicidades geométricas de todos sus autovalores es estrictamente igual a $n$ (el orden de la matriz), lo cual implica equivalentemente que para cada autovalor $\lambda_i$, su multiplicidad algebraica coincide con su multiplicidad geométrica.

## Interpretación del Enunciado

Para que una matriz $A$ pueda entrar en la descomposición canónica constitutiva **$A = P D P^{-1}$**, el requisito operacional indispensable recae sobre la matriz de transferencia $P$.
$P$ es la matriz cuyas **columnas son los autovectores** de $A$. Para que la inversa $P^{-1}$ pueda existir matemáticamente (y así el isomorfismo se consolide), $P$ debe poseer rango completo n.
Esto significa que necesitamos recopilar un set exacto de $n$ autovectores que sean **Linealmente Independientes (L.I.)** que conformen una base en $\mathbb{R}^n$.

## Solución Analítica

El conjunto de todos los autovectores asociados a un autovalor particular $\lambda_j$ genera un subespacio vectorial llamado **Autoespacio ($E_{\lambda_j}$)**, que corresponde al núcleo o *espacio nulo* de la transformación desplazada $(A - \lambda_j I)$.

La cantidad de autovectores linealmente independientes que podemos "extraer" del autovalor $\lambda_j$ está limitada dictada estrictamente por la **dimensión topológica** de su autoespacio, número que denominamos **Multiplicidad Geométrica (M.G.)**.
Por el Teorema del Rango-Nulidad:

$$
\text{M.G.}_j = \dim(E_{\lambda_j}) = \dim(\ker(A - \lambda_j I)) = n - \text{rg}(A - \lambda_j I)
$$

### Unión de Bases y Generación Total

Si consideramos al espectro de $A$ compuesto por $k$ autovalores únicos (donde $k \le n$), sabemos que el conjunto total de autovectores de $A$ surgirá de agrupar los vectores extraídos de los *subespacios propios* inconexos.

Existe un teorema fundamental que establece que **los autovectores que provienen de autovalores distintos son siempre linealmente independientes entre sí**. Esto significa que al "unir" las bases de cada subespacio $E_{\lambda_1}, E_{\lambda_2}, \dots, E_{\lambda_k}$, no generaremos vectores redundantes a nivel matricial abstracto.
La cantidad final de autovectores en nuestro "bolso colector" $P$ será equivalente a la suma estricta de las multiplicidades geométricas:

$$
\text{Dimensión de Autovectores Totales} = \sum_{j=1}^{k} \text{M.G.}_j
$$

### El Cierre de la Demostración

Si deseamos que la matriz sea diagonalizable, este bolso colector de autovectores debe aportarnos una base completa de $\mathbb{R}^n$. Traducido a nuestro planteamiento numérico, necesitamos recolectar un número exacto de $n$ vectores para que la matriz $P \in \mathbb{R}^{n \times n}$ expanda todo su volumen y sea, en consecuencia, inversible.

$$
\text{Para ser Diagonalizable} \iff \sum_{j=1}^{k} \text{dim}(E_{\lambda_j}) = n
$$

A esto le sumamos el axioma restrictivo superior, donde una multiplicidad geométrica jamás puede superar a la multiplicidad algebraica (las veces que la raíz aparece en el Polinomio Característico), y que la suma de todas las M.A. (incluidos los autovalores complejos) da exactamente $n$. Por consiguiente, **la única forma** fáctica de alcanzar que la suma rinda $n$ es si y solo si cada bloque particular entrega su techo máximo permitido: $\text{M.G.}_j = \text{M.A.}_j \quad \forall \lambda_j$.

### Conclusión

Si la suma de dimensiones de los autoespacios iguala al orden de la matriz matriz $n$, logramos blindar los escalones faltantes de la matriz $P$, armando una base conformada por los autovectores, volviéndola matriz regular e inversible, y avalando la tan ansiada factorización de autodescomposición que le da nombre al fenómeno matemático de diagonalizabilidad.

---

## Verificación Computacional en Abstracción a Caos

Apoyando las reglas de resolución matricial estipuladas, no basta con la inducción teórica. Validamos probabilísticamente esta propiedad generando matrices diagonales pseudo-aleatorias y matrices intencionalmente defectivas (Bloques de Jordan) mediante desorden controlado vía `NumPy`, demostrando cómo este corolario matemático de la suma de M.G. persiste e incide perimetralmente independientemente de fallos de punto flotante en cálculo espectral de grado alto, soportado con una tolerancia booleana.

```python
--8<-- "demostraciones/verificacion_criterio_diagonalizabilidad.py"
```
