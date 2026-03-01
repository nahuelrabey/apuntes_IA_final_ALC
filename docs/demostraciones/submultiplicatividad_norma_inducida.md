# Submultiplicatividad de Normas Matriciales Inducidas

## Enunciado del Teorema

> Sea $\|\cdot\|$ una norma matricial **inducida** por una norma vectorial $\|\cdot\|_v$. Entonces para toda matriz $M \in \mathbb{R}^{n \times n}$ y todo vector $v \in \mathbb{R}^n$:
>
> $$
> \|Mv\|_v \leq \|M\| \cdot \|v\|_v
> $$
>

Este resultado (llamado **consistencia** o **submultiplicatividad** entre matriz y vector) es lo que justifica el paso:

$$
\|A^{-1}(A - B)x\| \leq \|A^{-1}\| \cdot \|(A - B)x\|
$$

utilizado en la demostración del inciso A del ejercicio de condicionamiento. No se trata de la desigualdad de Cauchy-Schwarz (que relaciona productos internos entre vectores), sino de una consecuencia directa de la **definición** de norma inducida.

---

## Demostración

La norma matricial inducida por una norma vectorial $\|\cdot\|$ se define como:

$$
\|M\| = \max_{w \neq 0} \frac{\|Mw\|}{\|w\|}
$$

Esta definición implica que para **cualquier** vector $w \neq 0$:

$$
\frac{\|Mw\|}{\|w\|} \leq \max_{u \neq 0} \frac{\|Mu\|}{\|u\|} = \|M\|
$$

Multiplicando ambos miembros por $\|w\| > 0$:

$$
\|Mw\| \leq \|M\| \cdot \|w\|
$$

El caso $w = 0$ es trivial: $\|M \cdot 0\| = 0 \leq \|M\| \cdot 0$. $\blacksquare$

??? info "Observación Teórica: ¿Por qué esto NO es Cauchy-Schwarz?"
    La desigualdad de Cauchy-Schwarz establece que para dos vectores $u, v$:

$$
|\langle u, v \rangle| \leq \|u\| \cdot \|v\|
$$

    y su generalización para matrices dice que $|\langle Au, v \rangle| \leq \|A\| \cdot \|u\| \cdot \|v\|$.

    En cambio, la propiedad aquí demostrada relaciona la **norma de un producto matriz-vector** $\|Mv\|$ con el **producto** de la norma matricial $\|M\|$ y la norma vectorial $\|v\|$. Son objetos distintos: Cauchy-Schwarz compara un producto interno (un escalar) con el producto de normas; la submultiplicatividad compara una norma vectorial (el resultado de aplicar $M$ a $v$) con el producto de una norma matricial y una norma vectorial.

    La confusión es natural porque ambas desigualdades tienen la misma "forma" ($\|\cdot\| \leq \|\cdot\| \cdot \|\cdot\|$), pero sus objetos y su fundamentación son completamente diferentes.

??? info "Observación Teórica: ¿Es válido para cualquier norma, o sólo las inducidas?"
    Esta propiedad de consistencia **se cumple por definición** en las normas inducidas. Para normas matriciales no inducidas (como la norma de Frobenius), la propiedad puede o no cumplirse dependiendo de cómo esté definida. Sin embargo, la norma de Frobenius sí satisface $\|Mv\|_2 \leq \|M\|_F \cdot \|v\|_2$, aunque $\|\cdot\|_F$ no sea una norma inducida.

    En el contexto de este ejercicio, el enunciado especifica explícitamente que $\|\cdot\|$ es una norma matricial **inducida**, lo cual garantiza la propiedad sin necesidad de verificaciones adicionales.

---

## Aplicación al Ejercicio de Condicionamiento

En la demostración del inciso A, tenemos $M = A^{-1}$ y $w = (A-B)x$. Dado que $\|\cdot\|$ es una norma inducida, el teorema se aplica directamente:

$$
\|A^{-1}(A-B)x\| \leq \|A^{-1}\| \cdot \|(A-B)x\|
$$

El segundo paso, $\|(A-B)x\| \leq \|A-B\| \cdot \|x\|$, usa exactamente el mismo teorema con $M = A - B$ y $w = x$.

---

## Verificación Computacional

```python
--8<-- "docs/demostraciones/submultiplicatividad_norma_inducida.py"
```
