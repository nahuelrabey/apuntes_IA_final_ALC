# Demostración: Criterio de Diagonalizabilidad por Bases de Autoespacios

> **Teorema a Demostrar:**
> Una matriz cuadrada $A \in \mathbb{R}^{n \times n}$ es diagonalizable si y solo si la suma de las multiplicidades geométricas de todos sus autovalores es estrictamente igual a $n$ (el orden de la matriz), lo cual implica que para cada autovalor $\lambda_i$, su multiplicidad algebraica coincide con su multiplicidad geométrica.

## Interpretación del Enunciado

Para que una matriz $A$ pueda descomponerse algebraicamente a través de la fórmula **$A = P D P^{-1}$**, es necesario que la matriz de transferencia $P$ sea válida.
$P$ es la matriz formada por los **autovectores** de $A$ alineados en sus columnas. Para que su respectiva inversa $P^{-1}$ exista matemáticamente, $P$ debe poseer rango completo $n$.
Esto significa que es indispensable hallar un conjunto exacto de $n$ autovectores que conformen un sistema de vectores **Linealmente Independientes (L.I.)**, generando una base en $\mathbb{R}^n$.

## Solución Analítica

Los autovectores que se asocian a un autovalor dado $\lambda_j$ generan un subespacio vectorial llamado **Autoespacio ($E_{\lambda_j}$)**, que corresponde al núcleo o *espacio nulo* de la matriz desplazada $(A - \lambda_j I)$.

La cantidad de autovectores linealmente independientes correspondientes al autovalor $\lambda_j$ está limitada por la dimensión su autoespacio, número que denominamos **Multiplicidad Geométrica (M.G.)**.
Acudiendo al Teorema del Rango-Nulidad:

$$
\text{M.G.}_j = \dim(E_{\lambda_j}) = \dim(\ker(A - \lambda_j I)) = n - \text{rg}(A - \lambda_j I)
$$

### Unión de Bases y Conjunto de Autovectores Totales

Dicho un espectro de $A$ compuesto por $k$ autovalores únicos (donde $k \le n$), el conjunto total de autovectores de autovectores se formará de la unión del conjunto de los extraídos de cada uno de sus autoespacios.

Los **autovectores provenientes de autovalores distintos son siempre linealmente independientes entre sí**. Esto significa que al unir todas las bases individuales extraídas de los subespacios $E_{\lambda_1}, E_{\lambda_2}, \dots, E_{\lambda_k}$, el subconjunto obtenido será íntegramente de elementos independientes.
La cantidad final de componentes correspondientes de autovectores totales será la sumatoria particular estricta de cada multiplicidad geométrica individual de la base:

$$
\text{Cantidad de Autovectores L.I.} = \sum_{j=1}^{k} \text{M.G.}_j
$$

### Consecuencias Estructurales del Teorema

Para que la matriz general sea diagonalizable, el conjunto de autovectores independientes totales debe ser igual al orden matricial $n$.

$$
\text{A matriz} \text{ Diagonalizable} \iff \sum_{j=1}^{k} \dim(E_{\lambda_j}) = n
$$

Adicionalmente, se estipula que una multiplicidad geométrica jamás puede promediar más que la multiplicidad algebraica o repetición modular en la identidad del propio Polinomio Característico ($\text{M.G.} \le \text{M.A.}$), y que la suma de autovalores es estrictamente exactamente igual a $n$. La única forma posible de que la sumatoria alcance el tope $n$, por lo tanto, yace en la propiedad estricta en la cual ninguna de las dimensiones entregue un valor inferior: $\text{M.G.}_j = \text{M.A.}_j \quad \forall \lambda_j$.

### Conclusión

Si la suma de dimensiones de los autoespacios iguala al orden matricial $n$, es posible estructurar una base generadora compuesta puramente por un conjunto completo de autovectores independientes. Esta matriz estructurada corresponde directamente a una operatoria final regular e inversible de la forma paramétrica de una Descomposición y diagonalizabilidad.

---

## Verificación Computacional

Se valida su comportamiento probabilístico en simulación empleando bloques de Jordan generados a través de la librería `NumPy`, demostrando vía la toleración métrica el funcionamiento de las bases correspondientes frente al fallo.

```python
--8<-- "demostraciones/verificacion_criterio_diagonalizabilidad.py"
```
