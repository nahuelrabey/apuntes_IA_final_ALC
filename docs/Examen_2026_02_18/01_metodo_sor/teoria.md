# Ejercicio 1: Relajación de Métodos Iterativos (SOR)

> **Ejercicio 1.** Dada $A \in \mathbb{R}^{n \times n}$ con $a_{ii} \neq 0$, $1 \leq i \leq n$. $A = L + D + U$.
> 
> **a)** Demostrar que el sistema $Ax = b$ es equivalente al sistema $(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b$, cualquiera sea $\omega \neq 0$.
> 
> **b)** Considere el método iterativo $x^{k+1} = B(\omega)x^k + c$ con $B(\omega) = (D + \omega L)^{-1} ((1 - \omega)D - \omega U)$. Probar que $\det(B(\omega)) = (1 - \omega)^n$ y concluir que si el método converge $\implies \omega \in (0, 2)$.
> 
> **c)** Sea $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$. Analizar que sucede con el método definido en b) para los casos $\omega = \frac{1}{2}$ y $\omega = \frac{3}{2}$.

## Interpretación del Enunciado

El ejercicio analiza el **Método de Sobrerrelajación Sucesiva (SOR)**, una variante de *Gauss-Seidel*. Para una base teórica completa de estos métodos y su derivación matricial (Jacobi, Gauss-Seidel y SOR), consulte la [demostración general](../../demostraciones/metodos_iterativos.md).

El parámetro $\omega$ (omega) funciona como un factor de ajuste: 

- Si $\omega = 1$, el método es equivalente a *Gauss-Seidel*.
- Si $\omega > 1$, se aplica sobrerrelajación (para acelerar la convergencia).
- Si $\omega < 1$, se aplica subrrelajación.

Procederemos con el desarrollo matricial para demostrar la equivalencia y las propiedades de convergencia.

---

## Solución del Ejercicio

### Inciso A: Derivación de la Equivalencia Algebraica

> **a)** Demostrar que el sistema $Ax = b$ es equivalente al sistema $(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b$, cualquiera sea $\omega \neq 0$.

Partiendo de la descomposición $A = L + D + U$:

$$
(L + D + U)x = b
$$

Multiplicamos por el escalar $\omega \neq 0$:

$$
\omega (L + D + U)x = \omega b
$$

$$
\omega Lx + \omega Dx + \omega Ux = \omega b
$$

Sumamos $Dx$ a ambos lados:

$$
Dx + \omega Lx + \omega Dx + \omega Ux = Dx + \omega b
$$

Agrupamos los términos de $D$ y $L$ en el lado izquierdo:

$$
(D + \omega L)x = Dx - \omega Dx - \omega Ux + \omega b
$$

Extrayendo $x$ como factor común:

$$
(D + \omega L)x = (1 - \omega)Dx - \omega Ux + \omega b
$$

$$
(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b
$$

Queda demostrada la equivalencia.

---

### Inciso B: Determinante de Iteración y Condición de Rango Cota

> **b)** Considere el método iterativo $x^{k+1} = B(\omega)x^k + c$ con 
>
> $$B(\omega) = (D + \omega L)^{-1} ((1 - \omega)D - \omega U)$$
>
> Probar que $\det(B(\omega)) = (1 - \omega)^n$ y concluir que si el método converge $\implies \omega \in (0, 2)$.

El determinante de la matriz de iteración se calcula como:

$$
\det(B(\omega)) = \det\Big((D + \omega L)^{-1}\Big) \cdot \det\Big((1 - \omega)D - \omega U\Big)
$$

Analizamos cada factor:

1. El bloque $(D + \omega L)$ es una **matriz triangular inferior**. Su determinante es el producto de su diagonal, que coincide con la diagonal $D$ de $A$:

$$\det(D + \omega L) = \det(D) = \prod_{i=1}^{n} a_{ii}$$

2. El bloque $((1-\omega)D - \omega U)$ es una **matriz triangular superior**, con diagonal $(1-\omega)a_{ii}$. Su determinante es:

$$\det\big((1-\omega)D - \omega U\big) = \prod_{i=1}^{n} (1-\omega)a_{ii} = (1-\omega)^n \det(D)$$

??? info "Demostración formal de esta propiedad"

    > 📎 Demostración formal: [General](../../demostraciones/det_escalar_matriz.md)

    > 📎 Demostración formal: [Específica SOR](../../demostraciones/det_triangular_superior_sor.md)

Sustituyendo en la expresión inicial:

$$
\det(B(\omega)) = \frac{1}{\det(D)} \cdot \Big[ (1-\omega)^n \det(D) \Big] = (1-\omega)^n
$$

#### Condición Necesaria de Convergencia

Para que el método converja, el **Radio Espectral** debe ser menor a 1 ($\rho(B) < 1$). Consulte la [demostración formal](../../demostraciones/convergencia_radio_espectral.md) de esta condición.

$$
\text{Si converge} \implies \rho(B(\omega)) = \max_{i} |\lambda_i| < 1
$$

Notemos que el determinante de una matriz es igual al producto de sus autovalores: $\det(B) = \prod_{i=1}^n \lambda_i$.

Si todos los autovalores cumplen $|\lambda_i| < 1$, su producto también tendrá un módulo menor a 1. De esto se desprende que una condición necesaria para la convergencia es que el módulo del determinante sea menor a la unidad: $| \det(B) | < 1$.

$$
| (1-\omega)^n | < 1 \implies |1-\omega| < 1
$$

Para una justificación detallada de esta implicancia y la propiedad $|a^n| = |a|^n$, consulte la [demostración formal](../../demostraciones/potencia_modulo.md).

De donde obtenemos:

$$
-1 < 1 - \omega < 1 \implies 0 < \omega < 2
$$

Queda demostrada la condición necesaria.

??? info "Observación: Condición Necesaria vs Suficiente"
    Que $\omega \in (0, 2)$ es una condición **necesaria**, no suficiente. No garantiza convergencia, pero es un requisito previo.

---

### Inciso C: Análisis Particular para una Matriz A

> **c)** Analizar $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$ para $\omega = \frac{1}{2}$ y $\frac{3}{2}$.

Descomponemos $A$:
$D = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}$, $L = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $U = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

#### Caso 1: $\omega = 1/2$

$B(1/2) = (D + 0.5L)^{-1} (0.5D - 0.5U)$

1.  $(D + 0.5L) = \begin{pmatrix} 2 & 0 \\ 0.5 & -1 \end{pmatrix} \implies (D + 0.5L)^{-1} = \begin{pmatrix} 1/2 & 0 \\ 1/4 & -1 \end{pmatrix}$
2.  $(0.5D - 0.5U) = \begin{pmatrix} 1 & -0.5 \\ 0 & -0.5 \end{pmatrix}$
3.  $B(1/2) = \begin{pmatrix} 1/2 & -1/4 \\ 1/4 & 3/8 \end{pmatrix}$

Ecuación característica: $\lambda^2 - \frac{7}{8}\lambda + \frac{1}{4} = 0$. (Ver [derivación paso a paso](../../demostraciones/ecuacion_caracteristica_sor_ejemplo.md)).
El módulo de los autovalores es $|\lambda| = \sqrt{1/4} = 0.5 < 1$. (Ver [por qué el módulo es $\sqrt{c}$](../../demostraciones/modulo_autovalores_complejos.md)).
**Resultado**: El método **converge**.

#### Caso 2: $\omega = 3/2$

$B(3/2) = (D + 1.5L)^{-1} (-0.5D - 1.5U)$

1.  $(D + 1.5L) = \begin{pmatrix} 2 & 0 \\ 1.5 & -1 \end{pmatrix} \implies (D + 1.5L)^{-1} = \begin{pmatrix} 1/2 & 0 \\ 3/4 & -1 \end{pmatrix}$
2.  $(-0.5D - 1.5U) = \begin{pmatrix} -1 & -1.5 \\ 0 & 0.5 \end{pmatrix}$
3.  $B(3/2) = \begin{pmatrix} -1/2 & -3/4 \\ -3/4 & -13/8 \end{pmatrix}$

Autovalores: $\lambda_1 = -0.125$ y $\lambda_2 = -2.0$.
Como $\rho(B) = 2.0 > 1$:
**Resultado**: El método **diverge**.

---

## Verificación Empírica Computacional

Aplicamos el testeo cruzado estocástico con Python para las identidades matriciales subyacentes de SOR validando flujos tensoriales reales entre desniveles lógicos por desbordamientos (`np.allclose`) en consonancia con la _Metodología Algebraica Estricta_:

```python
--8<-- "Examen_2026_02_18/01_metodo_sor/verificacion.py"
```
