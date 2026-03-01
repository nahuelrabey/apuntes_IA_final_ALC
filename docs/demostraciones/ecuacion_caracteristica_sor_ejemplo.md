# Derivación de la Ecuación Característica SOR (Ejemplo)

Este documento detalla el cálculo paso a paso para obtener la ecuación característica de la matriz de iteración SOR para el caso analizado en el [Examen 18-02-2026](../Examen_2026_02_18/01_metodo_sor/teoria.md).

## 1. Planteo del Problema

Se tiene la matriz $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$ y el parámetro de relajación $\omega = 1/2$.
Queremos hallar el polinomio característico de $B(\omega) = (D + \omega L)^{-1} ((1-\omega)D - \omega U)$.

### Descomposición de A
Matriz Diagonal: $D = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}$
Matriz Triangular Inferior Estricta: $L = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$
Matriz Triangular Superior Estricta: $U = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

## 2. Cálculo de B(1/2)

### Matriz M = D + (1/2)L

$$
(D + 0.5L) = \begin{pmatrix} 2 & 0 \\ 0.5 & -1 \end{pmatrix}
$$

Su inversa:

$$
(D + 0.5L)^{-1} = \frac{1}{-2 - 0} \begin{pmatrix} -1 & 0 \\ -0.5 & 2 \end{pmatrix} = \begin{pmatrix} 1/2 & 0 \\ 1/4 & -1 \end{pmatrix}
$$

### Matriz N = (1/2)D - (1/2)U

$$
(0.5D - 0.5U) = \begin{pmatrix} 1 & -0.5 \\ 0 & -0.5 \end{pmatrix}
$$

### Producto B = M⁻¹ N

$$
B = \begin{pmatrix} 1/2 & 0 \\ 1/4 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1/2 \\ 0 & -1/2 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/4 \\ 1/4 & -1/8 + 1/2 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/4 \\ 1/4 & 3/8 \end{pmatrix}
$$

## 3. Polinomio Característico

$$
\det(B - \lambda I) = \det \begin{pmatrix} 1/2 - \lambda & -1/4 \\ 1/4 & 3/8 - \lambda \end{pmatrix}
$$

Expandiendo el determinante:

$$
(1/2 - \lambda)(3/8 - \lambda) - (-1/4)(1/4) = 0
$$

$$
\lambda^2 - (1/2 + 3/8)\lambda + (3/16) + (1/16) = 0
$$

$$
\lambda^2 - \frac{4+3}{8}\lambda + \frac{4}{16} = 0
$$

$$
\lambda^2 - \frac{7}{8}\lambda + \frac{1}{4} = 0
$$

Esta es la **Ecuación Característica** presentada en el archivo de teoría. Como las raíces son complejas conjugadas, su módulo es directamente $\sqrt{1/4} = 0.5$ (ver [demostración detallada](modulo_autovalores_complejos.md)).

---

## Verificación con SymPy

Se utiliza cálculo simbólico para corroborar la exactitud de los coeficientes y obtener los autovalores exactos.

```python
--8<-- "demostraciones/ecuacion_caracteristica_sor_ejemplo.py"
```
