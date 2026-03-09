# Demostración: El Teorema Espectral (Matrices Simétricas Reales)

## Interpretación del Enunciado

> Demostrar formalmente el **Teorema Espectral aplicado a Matrices Reales**: si una matriz $A \in \mathbb{R}^{n \times n}$ es simétrica ($A = A^t$), entonces satisface dos propiedades espectrales:
>
> 1) Todos sus autovalores $\lambda_i$ son **números reales** (ninguno es complejo).
> 2) Los autovectores $v_i$ correspondientes a autovalores distintos son **ortogonales** entre sí, lo que garantiza una base ortonormal para $\mathbb{R}^n$ ($A$ es diagonalizable ortogonalmente).

Este teorema es la base de transformaciones como SVD (Descomposición en Valores Singulares) y PCA (Análisis de Componentes Principales).

La demostración se divide en dos partes.

---

## Solución Analítica

### Parte I: Los Autovalores son Reales

Supongamos que $A$ tiene un autovalor complejo genérico $\lambda = \alpha + \beta i$, con autovector asociado $v \in \mathbb{C}^n$.

Planteamos la ecuación de autovalores:

$$
(Eq. 1) \quad A v = \lambda v
$$

Tomamos el conjugado complejo de ambos lados. Como $A \in \mathbb{R}^{n \times n}$, se cumple $\overline{A} = A$, por lo que el conjugado afecta únicamente al autovector y al autovalor:

$$
(Eq. 2) \quad A \overline{v} = \overline{\lambda} \overline{v}
$$

Pre-multiplicamos $(Eq. 1)$ por $\overline{v}^t$:

$$
\overline{v}^t (A v) = \overline{v}^t (\lambda v) = \lambda (\overline{v}^t v)
$$

Transponemos $(Eq. 2)$ y post-multiplicamos por $v$:

$$
(A \overline{v})^t = (\overline{\lambda} \overline{v})^t
$$

$$
\overline{v}^t A^t = \overline{\lambda} \overline{v}^t
$$

$$
\overline{v}^t A^t v = (\overline{\lambda} \overline{v}^t) v = \overline{\lambda} (\overline{v}^t v)
$$

Como $A$ es simétrica ($A^t = A$), el lado izquierdo de ambas expresiones coincide: $\overline{v}^t A^t v = \overline{v}^t A v$.
Igualando los lados derechos:

$$
\lambda (\overline{v}^t v) = \overline{\lambda} (\overline{v}^t v)
$$

Restando:

$$
(\lambda - \overline{\lambda}) (\overline{v}^t v) = 0
$$

El factor $\overline{v}^t v = \sum |v_k|^2$ es la suma de los cuadrados de los módulos de las componentes del autovector. Como el autovector es no nulo, se tiene $\overline{v}^t v > 0$.

Por lo tanto, el único factor que puede anularse es el primero:

$$
\lambda - \overline{\lambda} = 0
$$

$$
\lambda = \overline{\lambda}
$$

Para que un número complejo sea igual a su conjugado ($\alpha + \beta i = \alpha - \beta i$), su parte imaginaria debe ser cero ($\beta = 0$). Por lo tanto, **$\lambda$ es real**. $\square$

### Parte II: Ortogonalidad de Autovectores

Dados dos autovalores distintos $\lambda_1 \neq \lambda_2$ con autovectores $v_1$ y $v_2$ respectivamente:

$$
A v_1 = \lambda_1 v_1
$$

$$
A v_2 = \lambda_2 v_2
$$

Pre-multiplicamos la primera ecuación por $v_2^t$:

$$
v_2^t A v_1 = v_2^t (\lambda_1 v_1) = \lambda_1 (v_2^t v_1)
$$

Transponemos la segunda ecuación y post-multiplicamos por $v_1$:

$$
(A v_2)^t = (\lambda_2 v_2)^t
$$

$$
v_2^t A^t = \lambda_2 v_2^t
$$

$$
v_2^t A^t v_1 = (\lambda_2 v_2^t) v_1 = \lambda_2 (v_2^t v_1)
$$

Como $A$ es simétrica ($A^t = A$), los lados izquierdos coinciden: $v_2^t A^t v_1 = v_2^t A v_1$.
Igualando los lados derechos:

$$
\lambda_1 (v_2^t v_1) = \lambda_2 (v_2^t v_1)
$$

Despejando:

$$
(\lambda_1 - \lambda_2) (v_2^t v_1) = 0
$$

Como $\lambda_1 \neq \lambda_2$, se tiene $(\lambda_1 - \lambda_2) \neq 0$. Por lo tanto:

$$
v_2^t v_1 = 0
$$

El producto interno entre $v_1$ y $v_2$ es cero, lo que significa que ambos vectores son **ortogonales**. $\square$

### Conclusión

La simetría de $A$ garantiza que $A^t = A$, lo que implica dos consecuencias estructurales: todos sus autovalores son reales (ya que $\lambda = \overline{\lambda}$) y sus autovectores asociados a autovalores distintos son ortogonales (ya que $v_i \cdot v_j = 0$). Esto establece la diagonalización ortogonal de $A$.

---

## Referencias para Validación

* [Wikipedia: Spectral Theorem (Symmetric matrices)](https://en.wikipedia.org/wiki/Spectral_theorem#Symmetric_matrices): Marco demostrativo formal del Teorema Espectral para operadores auto-adjuntos en dimensión finita.
* [MIT 18.06 OpenCourseWare - Clase 25 (Symmetric Matrices and Positive Definiteness) - Prof. Gilbert Strang](https://www.youtube.com/watch?v=13r9QY6cmjc): Clase donde se desarrolla la misma demostración dual: autovalores reales (Min. 09:30) y ortogonalidad de autovectores (Min. 16:00).

---

## Verificación Empírica Computacional

La demostración se verifica computacionalmente (con una tolerancia de $1e^{-10}$ para errores de punto flotante en el cálculo de autovectores mediante iteración QR en NumPy) en el script adjunto, que evalúa matrices simétricas aleatorias.

```python
--8<-- "demostraciones/teorema_espectral.py"
```
