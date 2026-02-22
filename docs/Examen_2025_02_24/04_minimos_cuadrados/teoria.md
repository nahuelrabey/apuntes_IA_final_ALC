# Solución del Ejercicio 4

Dada la función no lineal:
$$z = a \cdot y^b \cdot e^{cx + 2}$$

## 1. Plantear las ecuaciones de mínimos cuadrados para estimar los parámetros $a, b$ y $c$.

Para aplicar el método de Mínimos Cuadrados Lineales Clásicos, primero debemos transformar (linealizar) el modelo geométrico/exponencial aplicando logaritmo natural ($\ln$) a ambos lados de la ecuación:
$$\ln(z) = \ln(a \cdot y^b \cdot e^{cx + 2})$$
Por las propiedades de los logaritmos (el logaritmo de un producto es la suma de los logaritmos, y el exponente baja multiplicando), la expresión queda:
$$\ln(z) = \ln(a) + b \ln(y) + (cx + 2)$$
Reagrupando los términos para independizar las incógnitas de las constantes conocidas:
$$\ln(z) - 2 = \ln(a) + b \ln(y) + c x$$

A partir de esta estructura lineal en sus parámetros, efectuamos los siguientes cambios de variable para llevarlo a un modelo lineal estándar de la forma $Z_i = \beta_0 + \beta_1 Y_i + \beta_2 X_i$:
- $Z = \ln(z) - 2$ *(variable dependiente transformada)*
- $A = \ln(a)$ *(nuevo parámetro ordenado al origen, luego $a = e^A$)*
- El parámetro $b$ queda libre.
- El parámetro $c$ queda libre.
- La variable asociada a $b$ es $\ln(y)$
- La variable asociada a $c$ es $x$

Para un conjunto de $m$ puntos experimentales $(x_i, y_i, z_i)$, definimos el sistema de ecuaciones sobre-determinado en forma matricial $M \vec{\theta} = \vec{Z}$ como:
$$
\begin{pmatrix} 
1 & \ln(y_1) & x_1 \\
1 & \ln(y_2) & x_2 \\
\vdots & \vdots & \vdots \\
1 & \ln(y_m) & x_m
\end{pmatrix}
\begin{pmatrix}
A \\
b \\
c
\end{pmatrix}
=
\begin{pmatrix}
\ln(z_1) - 2 \\
\ln(z_2) - 2 \\
\vdots \\
\ln(z_m) - 2
\end{pmatrix}
$$

**Las ecuaciones normales de Mínimos Cuadrados** se construyen multiplicando por izquierda la transpuesta de la matriz de diseño $M$:
$$(M^T M) \vec{\theta} = M^T \vec{Z}$$
Resolviendo este sistema lineal $(3 \times 3)$ se obtienen los estimadores paramétricos óptimos $\hat{A}$, $\hat{b}$ y $\hat{c}$. Posteriormente se recupera $\hat{a} = e^{\hat{A}}$.

---

## 2. Proponer puntos de datos para que la solución sea única.

Para que las ecuaciones de mínimos cuadrados posean una **solución única**, la matriz normal cuadrada $(M^T M)$ debe ser estrictamente invertible. Esto ocurre si y solo si la matriz de diseño $M$ posee **rango completo por columnas**.
Como $M$ tiene 3 columnas, necesitamos que el $\text{Rango}(M) = 3$. Geométricamente, los vectores columna de la matriz $M$ formados por las mediciones no deben ser dependientes entre sí.

En el contexto físico del problema, esto implica que:
- Los puntos de los datos $(x_i, y_i)$ no deben formar una combinación lineal perfecta. No vale que para todas las mediciones sea siempre $x_i = k \cdot \ln(y_i) + C$ (es decir, no pueden ser colineales en el plano de las características transformadas).
- La variable $y_i$ **debe ser estrictamente positiva ($y_i > 0$)** para todo $i$, dado que el dominio natural del $\ln(y_i)$ no admite valores negativos ni ceros.

**Propuesta de puntos experimentalmente válidos y robustos:**
(Para garantizar que no sean colineales ni constantes, basta con alterar alternativamente las magnitudes en los ejes):
- $P_1 = (x_1=1,\, y_1=1,\, z_1)$
- $P_2 = (x_2=0,\, y_2=e,\, z_2)$
- $P_3 = (x_3=-1,\, y_3=1,\, z_3)$

Evaluemos cómo queda nuestra matriz de muestras con estos puntos de prueba para confirmar su independencia:
$$M_{\text{propuesta}} = \begin{pmatrix} 1 & \ln(1) & 1 \\ 1 & \ln(e) & 0 \\ 1 & \ln(1) & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & -1 \end{pmatrix}$$
El determinante de esta matriz $3 \times 3$ no es cero (en efecto, vale $-2$):
$\det(M_{\text{propuesta}}) = 1 \cdot (-1 - 0) - 0 \cdot (-1 -0) + 1 \cdot (0 - 1) = -1 - 1 = -2$.
Por tanto, el determinante de la matriz normal $\det(M^T M) = \det(M)^2 = 4 \neq 0$. El rango es completo, y **la solución de los parámetros está garantizada demostráblemente única**.

---

## 3. Determinar la mínima cantidad de puntos necesarios para que la solución sea única.

El sistema general de mínimos cuadrados tiene como incógnita el vector $\vec{\theta} = [A, b, c]^T$, el cual contiene **3 parámetros** a estimar libremente.

Por el Teorema de Rouché-Frobenius y el Rango fundamental del álgebra matricial:
- Si aportamos $m < 3$ puntos, el sistema quedará sub-determinado (tendrá infinitas soluciones lógicas porque habrán variables libres, el rango máximo será menor a 3 penalizando a $M^T M$).
- Para que la matriz de diseño $M \in \mathbb{R}^{m \times 3}$ logre poseer un Rango por Columnas exactamente igual a 3 (condición forzosa e innegociable para que la inversa de $M^T M$ exista), necesitamos aportar un mínimo estricto de **$m = 3$ puntos**.

**Conclusión:** Se necesitan **como mínimo 3 puntos empíricos** (siempre y cuando estos no formen un subespacio degenerado de dimensiones menores, según lo exigido en el inciso 2).

---

## Verificación Computacional en Python

```python
--8<-- "04_minimos_cuadrados/verificacion.py"
```
