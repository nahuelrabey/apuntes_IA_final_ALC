# Ejercicio 1: Relajación de Métodos Iterativos (SOR)

> **Ejercicio 1.** Dada $A \in \mathbb{R}^{n \times n}$ con $a_{ii} \neq 0$, $1 \leq i \leq n$. $A = L + D + U$.
> 
> **a)** Demostrar que el sistema $Ax = b$ es equivalente al sistema $(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b$, cualquiera sea $\omega \neq 0$.
> 
> **b)** Considere el método iterativo $x^{k+1} = B(\omega)x^k + c$ con $B(\omega) = (D + \omega L)^{-1} ((1 - \omega)D - \omega U)$. Probar que $\det(B(\omega)) = (1 - \omega)^n$ y concluir que si el método converge $\implies \omega \in (0, 2)$.
> 
> **c)** Sea $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$. Analizar que sucede con el método definido en b) para los casos $\omega = \frac{1}{2}$ y $\omega = \frac{3}{2}$.

## Interpretación del Enunciado

El ejercicio evalúa la comprensión profunda del **Método de Sobrerrelajación Sucesiva (SOR)**, una variante optimizada algorítmicamente y generalizada de *Gauss-Seidel*. El parámetro $\omega$ (omega) funciona como un "factor de inercia" computacional: 
- Si $\omega = 1$, la fórmula degenera lógicamente y recuperamos a *Gauss-Seidel* original puro.
- Si $\omega > 1$, forzamos la sobrerrelajación (acelerando un sistema que converge muy lento).
- Si $\omega < 1$, aplicamos subrrelajación (frenando para asegurar convergencia ante sistemas muy elásticos).

Procederemos a aplicar un desarrollo táctico matemático de manipulación matricial, demostrando cómo nace el bloque central de la iteración.

---

## Solución del Ejercicio

### Inciso A: Derivación de la Equivalencia Algebraica

> **a)** Demostrar que el sistema $Ax = b$ es equivalente al sistema $(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b$, cualquiera sea $\omega \neq 0$.

Partiendo del planteo nativo con la descomposición canónica de $A$:

$$
(L + D + U)x = b
$$

Como $\omega$ es estrictamente no-nulo por consigna ($\omega \neq 0$), el álgebra nos ampara a pre-multiplicar la ecuación completa por este escalar sin perturbar el espacio de soluciones:

$$
\omega (L + D + U)x = \omega b
$$
$$
\omega Lx + \omega Dx + \omega Ux = \omega b
$$

Nuestro objetivo anatómico de llegada consta de forjar un componente $(D + \omega L)x$ aglomerado a la izquierda del equal. Sumemos estratégicamente el bloque neutro $Dx$ a _ambos_ lados de la simetría:

$$
Dx + \omega Lx + \omega Dx + \omega Ux = Dx + \omega b
$$

Procederemos ahora a agrupar los componentes a conveniencia, reteniendo sólo $D$ y $L$ en la barrera izquierda:

$$
(D + \omega L)x = Dx - \omega Dx - \omega Ux + \omega b
$$

Extrayendo de manera implacable el vector $x$ como factor común de manera reculada hacia la derecha del binomio restante:

$$
(D + \omega L)x = (1 - \omega)Dx - \omega Ux + \omega b
$$

$$
(D + \omega L)x = ((1 - \omega)D - \omega U)x + \omega b
$$

Queda inequívocamente probada y construida la equivalencia del sistema paramétrico.

---

### Inciso B: Determinante de Iteración y Condición de Rango Cota

> **b)** Considere el método... Probar que $\det(B(\omega)) = (1 - \omega)^n$ y concluir que si el método converge $\implies \omega \in (0, 2)$.

Desentrañaremos el valor determinante de la matriz matriz de iteraciones operando por fracciones bajo la Ley de Multiplicatividad: $\det(XY) = \det(X)\det(Y)$.

$$
\det(B(\omega)) = \det\Big((D + \omega L)^{-1}\Big) \cdot \det\Big((1 - \omega)D - \omega U\Big)
$$

Analicemos la fisiología topológica de ambos componentes internos:

1. El bloque $(D + \omega L)$ es estructuralmente una **matriz triangular inferior**, dado que asimila a una diagonal $D$ pura ensamblada adosada con un sector íntegramente de baja escalonada $\omega L$. Por leyes universales de determinantes, el determinante de toda triangular recae en atar y multiplicar a sus entradas diagonales. La diagonal de $(D + \omega L)$ es indubitablemente la mismísima diagonal canónica original unívoca $D$ de la matriz $A$ (asistida por la consigna original de $a_{ii} \neq 0$ habilitando su Inversa). Entonces:
   $$\det(D + \omega L) = \det(D) = \prod_{i=1}^{n} a_{ii}$$

2. El bloque adyacente antagonista, $((1-\omega)D - \omega U)$, reviste la cualidad natural de conformarse en una **matriz triangular superior**, resguardando a una diagonal principal escalada numéricamente por coeficientes $(1-\omega)$. Al computar su determinante, el escalar multiplicativo golpea el producto repetitivamente para el total de sus $n$ renglones, escupiendo homomórficamente hacia afuera de la sumatoria una extracción de grado enésima:
   $$\det\big((1-\omega)D - \omega U\big) = \prod_{i=1}^{n} (1-\omega)a_{ii} = (1-\omega)^n \det(D)$$

Ensamblando ambos milagros recíprocos con el conocimiento de que la determinante de las inversas desdoblan la inversa en fracciones espaciales:

$$
\det(B(\omega)) = \frac{1}{\det(D)} \cdot \Big[ (1-\omega)^n \det(D) \Big]
$$

El factor diagonal $\det(D)$ encuentra en el numerador a su clón aniquilador en el denominador para truncarse algebraicamente probando fehacientemente que:

$$
\det(B(\omega)) = (1-\omega)^n
$$

#### Demostración del Rango Necesario en Caso de Convergencia

Para que todo Método Iterativo goce certitidez teórica y pueda colapsar en una convergencia matemática frente sus repetidos asedios algorítmicos, resulta perentorio y decisivo que su **Radio Espectral (el autovalor absoluto magno, $\rho(B)$)** se refugie asilado al amparo dentro del radio métrico de la identidad (su magnitud sub-1).

$$
\text{Si converge} \implies \rho(B(\omega)) = \max_{i} |\lambda_i| < 1
$$

Conocemos subyacentemente que el determinante global de cualquier matriz representa geométricamente emparejamiento volumétrico final de todos sus multiplicadores autovalorales $\left( \det(B) = \prod_{i=1}^n \lambda_i \right)$.

Si la ley máxima dicta férreamente que absolutamente _todos_ los $|\lambda_i|$ yacen prisioneros por debajo de $1$, el peso volumétrico acumulado global entre ellos carece la fuerza productiva para inflacionarse.
Esa cota teórica se traslada impertérrita con un corolario incuestionable: el valor absoluto del propio determinante es siempre constribuyente directo inferior a uno ($|\det(B)| < 1$).

$$
| \det(B(\omega)) | < 1 \implies |(1-\omega)^n| < 1 \implies |1-\omega| < 1
$$

Desarmando el módulo algebráicamente por ambos cantos:
$$
-1 < 1 - \omega < 1
$$
$$
-2 < -\omega < 0 
$$
$$
2 > \omega > 0 \quad \text{o bien} \quad \omega \in (0, 2)
$$

Queda comprobada y zanjada la condición excluyente *necesaria*.

??? info "Observación Teórica: Condición Necesaria vs Suficiente"
    Que $\omega \in (0, 2)$ es únicamente una condición **necesaria**, no exime fallas. No es prueba garante y contundente de convergencia real; simplemente prohíbe las búsquedas ingenuas. Si escogieras un $\omega = 3.5$, las métricas te avisan por adelantado y descartan la viabilidad.

---

### Inciso C: Análisis Particular de Radio Espectral para $A$

> **c)** Analizar $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$ y $\omega = \frac{1}{2}$ y $\frac{3}{2}$.

Disgregamos minuciosamente al ejemplar propuesto respetando la anatomía:
$D = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}$, $L = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $U = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

#### Caso 1: $\omega = 1/2$

Aplicamos para cimentar $B(1/2) = (D + 0.5L)^{-1} (0.5D - 0.5U)$

1.  $(D + 0.5L) = \begin{pmatrix} 2 & 0 \\ 0.5 & -1 \end{pmatrix}$. Su Inversa, utilizando adyuntas de $2 \times 2$, es: $\begin{pmatrix} 1/2 & 0 \\ 1/4 & -1 \end{pmatrix}$.
2.  $(0.5D - 0.5U) = \begin{pmatrix} 1 & -0.5 \\ 0 & -0.5 \end{pmatrix}$.
3.  Multiplicabilidad cruzada por concatenación:
    $$B(1/2) = \begin{pmatrix} 1/2 & 0 \\ 1/4 & -1 \end{pmatrix} \begin{pmatrix} 1 & -0.5 \\ 0 & -0.5 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{4} \\ \frac{1}{4} & \frac{3}{8} \end{pmatrix}$$

Extraemos espectralidad polinomial buscando determinantes de $(B - \lambda I)$:
Traza $= 7/8$, Determinante $= 1/4$. 
Ecuación Característica: $\lambda^2 - \frac{7}{8}\lambda + \frac{1}{4} = 0$. 

Acarrea soluciones complejas ($\Delta < 0$). Pero su módulo nos importa para la métrica sub 1: $|\lambda| = \sqrt{1/4} = 0.5 < 1$.
**Dictamen final**: El radio espectral $\rho$ resguarda una dominancia sub1 estricta. Para $\omega = 0.5$, el esquema iterativo **converge de manera eficiente**.

#### Caso 2: $\omega = 3/2$

Aplicamos para cimentar $B(3/2) = (D + 1.5L)^{-1} (-0.5D - 1.5U)$

1.  $(D + 1.5L) = \begin{pmatrix} 2 & 0 \\ 1.5 & -1 \end{pmatrix} \implies \text{Inversa: } \begin{pmatrix} 1/2 & 0 \\ 3/4 & -1 \end{pmatrix}$.
2.  $(-0.5D - 1.5U) = \begin{pmatrix} -1 & -1.5 \\ 0 & 0.5 \end{pmatrix}$.
3.  Multiplicabilidad cruzada matriz a matriz:
    $$B(3/2) = \begin{pmatrix} 1/2 & 0 \\ 3/4 & -1 \end{pmatrix} \begin{pmatrix} -1 & -1.5 \\ 0 & 0.5 \end{pmatrix} = \begin{pmatrix} -\frac{1}{2} & -\frac{3}{4} \\ -\frac{3}{4} & -\frac{13}{8} \end{pmatrix}$$

Extraemos espectralidad en este segundo asalto: 
Traza $= -17/8$, Determinante $= 1/4$.
Raíces calculadas directamente resultan arrojando $\lambda_1 = -0.125$ y la contumaz autovalor $\lambda_2 = -2.0$.
**Dictamen final**: Nos asaltan métricas con radio espectral $\rho(B_{3/2}) = 2.0 > 1$. A pesar del amoldamiento a la cuota lícita restrictiva del inciso anterior de transitar en $(0, 2)$, poseer autovalores inflacionarios detona la geometría. **El método diverge irremediablemente.**

---

## Verificación Empírica Computacional

Aplicamos el testeo cruzado estocástico con Python para las identidades matriciales subyacentes de SOR validando flujos tensoriales reales entre desniveles lógicos por desbordamientos (`np.allclose`) en consonancia con la _Metodología Algebraica Estricta_:

```python
--8<-- "Examen_2026_02_18/01_metodo_sor/verificacion.py"
```
