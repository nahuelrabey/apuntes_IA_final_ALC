# Demostración: ¿Por qué un autovector nunca puede ser nulo?

## Interpretación del Enunciado

> Demostrar lógicamente, apelando a la definición formal de autovalores, por qué un autovector $v$ asociado a una transformación lineal o matriz cuadrada $A$ requiere, por definición restrictiva, ser distinto del vector nulo ($v \neq \mathbf{0}$).

Este planteo suele presentarse como una "trampa conceptual" en parciales y exámenes finales. A diferencia de las demostraciones por inducción que operan con sumatorias para probar independencia lineal, esta demostración se centra en atacar la ecuación primitiva por las vías del **Absurdo** y la **Pérdida de la Direccionalidad Única**.

---

## Solución Analítica

Partimos de la definición dogmática y fundamental que rige toda la teoría espectral de transformaciones lineales. Dado un operador denotado por la matriz cuadrada $A \in \mathbb{R}^{n \times n}$, decimos que un vector $v$ es un *autovector* de $A$ si y sólo si existe algún escalar $\lambda \in \mathbb{R}$ tal que:

$$(Eq. 1) \quad A \cdot v = \lambda \cdot v$$

### Caso Hipotético (Demostración por el Absurdo)

Supongamos, temporalmente en contra de la doctrina, que permitimos que el vector de entrada sea íntegramente nulo, esto es $v = \mathbf{0} = (0, 0, \dots, 0)^T$.

Sustituimos forzosamente nuestro vector espurio dentro de la definición original ($Eq. 1$):

$$A \cdot \mathbf{0} = \lambda \cdot \mathbf{0}$$

Sin importar en absoluto qué matriz $A$ sea, ni qué coeficientes albergue en sus filas o columnas, nosotros sabemos axiomáticamente por las leyes fundacionales del producto matricial que toda matriz multiplicada por el vector cero colapsa y arroja ineludiblemente el vector nulo:

$$(Eq. 2) \quad \mathbf{0} = \lambda \cdot \mathbf{0}$$

Ahora enfoquémonos en el componente derecho de la balanza de $Eq. 2$. Tenemos a un escalar ignoto $\lambda$ escalando al vacío. Indiferentemente del valor que le ofrezcamos a ese escalar, todo se anulará.

Aquí se destapa de lleno la contradicción mortal: 

Si inyectamos un autovalor totalmente falso o inexistente para esta matriz, por ejemplo $\lambda = 999.000$:

$$\mathbf{0} = 999.000 \cdot \mathbf{0} \quad \implies \quad \mathbf{0} = \mathbf{0}$$

¡La igualdad matemática **sigue siendo perfectamente lícita y verdadera**! 

### Conclusión Axiomática

Si permitiéramos legalizar que $v = \mathbf{0}$ califique como un autovector, se desmorona de facto toda la integridad de la teoría. ¿Por qué? Porque bajo la protección estéril de que $A \cdot 0 = 0$, **literalmente cualquier número real infinito, irreal o arbitrario (todo $\lambda \in \mathbb{R}$) se convertiría mágicamente en un autovalor válido** para el sistema.

La esencia misma de buscar "autovectores" y espectros, trata puntualmente sobre encontrar aquellas **direcciones o rayas privilegiadas** exclusivas del hiperplano original, donde la transformación lineal de la matriz actúa unívoca y nativamente como un mero re-escalamiento. 

El vector cero no posee dirección, ni flecha en el espacio euclidiano, es un punto muerto en el origen. Carece de la capacidad geométrica para mostrarnos hacia dónde está empujando o estirando la matriz en sus dimensiones preferidas.

Ergo, por imperativo categórico para evitar el quiebre de la relación de identidad matricial:

> **El Autovector $v$ nunca puede asumir ser el vector nulo ($v \neq 0$), aunque su Autovalor asociado $\lambda$ sí puede serlo ($A \cdot v = 0 \cdot v \implies A \cdot v = 0$) siempre que se recaiga en el *Kernel* o *Espacio Nulo* de la propia matriz.**

Q.E.D.

---

## Verificación Empírica Computacional

La noción patológica de la trivialidad del vector cero insertado en un motor de resolución puede corroborarse algorítmicamente observando cómo cualquier $\lambda$ azaroso inyectado genera una coincidencia de `True`:

```python
--8<-- "demostraciones/vector_nulo_autovector.py"
```

---

## Fuentes y Material Bibliográfico de Apoyo

Para expandir los fundamentos al respecto de la exclusión por definición del vector nulo, recomendamos la lectura/visualización de los siguientes aportes:

- **[Khan Academy: Introducción a Vectores Propios y Valores Propios](https://es.khanacademy.org/math/linear-algebra/alternate-bases/eigen-everything/v/linear-algebra-introduction-to-eigenvalues-and-eigenvectors)**: (Video Introductorio). En el minuto 8:00 detalla explícitamente y con animaciones de los espacios en el plano por qué el vector nulo $v = 0$ siempre será solución para todos los múltiplos de lambda de manera aburrida, y por ende se lo descarta de cara a buscar aquellos que conforman un subespacio direccional.
- **Libro: Álgebra Lineal y sus Aplicaciones (Gilbert Strang)**. *Capítulo 6: Valores Propios y Vectores Propios*. Strang especifica dogmáticamente en las primeras premisas de su capítulo que la ecuación fundamental $(Ax = \lambda x)$ busca vectores no nulos a lo largo de cuyas líneas directrices sucedáneas $Ax$ resulte paralela a $x$. "El cero siempre obedece, pero los vectores propios rigen direcciones invariantes".
