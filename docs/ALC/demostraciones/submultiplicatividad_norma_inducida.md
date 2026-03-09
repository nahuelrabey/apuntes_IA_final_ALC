# Submultiplicatividad de Normas Matriciales Inducidas

## Enunciado del Teorema

Sea $\|\cdot\|$ una norma matricial **inducida** por una norma vectorial $\|\cdot\|_v$. Entonces para toda matriz $M \in \mathbb{R}^{n \times n}$ y todo vector $v \in \mathbb{R}^n$:

$$
\|Mv\|_v \leq \|M\| \cdot \|v\|_v
$$


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

<Info titulo="Observación Teórica: ¿Por qué esto NO es Cauchy-Schwarz?">

La desigualdad de Cauchy-Schwarz establece que para dos vectores $u, v$:

</Info>

$$
|\langle u, v \rangle| \leq \|u\| \cdot \|v\|

$$
    y su generalización para matrices dice que $|\langle Au, v \rangle| \leq \|A\| \cdot \|u\| \cdot \|v\|$.

    En cambio, la propiedad aquí demostrada relaciona la **norma de un producto matriz-vector** $\|Mv\|$ con el **producto** de la norma matricial $\|M\|$ y la norma vectorial $\|v\|$. Son objetos distintos: Cauchy-Schwarz compara un producto interno (un escalar) con el producto de normas; la submultiplicatividad compara una norma vectorial (el resultado de aplicar $M$ a $v$) con el producto de una norma matricial y una norma vectorial.

    La confusión es natural porque ambas desigualdades tienen la misma "forma" ($\|\cdot\| \leq \|\cdot\| \cdot \|\cdot\|$), pero sus objetos y su fundamentación son completamente diferentes.

    Fin de la observación.

<Info titulo="Observación Teórica: ¿Es válido para cualquier norma, o sólo las inducidas?">

Esta propiedad de consistencia **se cumple por definición** en las normas inducidas. Para normas matriciales no inducidas (como la norma de Frobenius), la propiedad puede o no cumplirse dependiendo de cómo esté definida. Sin embargo, la norma de Frobenius sí satisface $\|Mv\|_2 \leq \|M\|_F \cdot \|v\|_2$, aunque $\|\cdot\|_F$ no sea una norma inducida.

En el contexto de este ejercicio, el enunciado especifica explícitamente que $\|\cdot\|$ es una norma matricial **inducida**, lo cual garantiza la propiedad sin necesidad de verificaciones adicionales.

Fin de la observación.

</Info>

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
"""
Verificación de la submultiplicatividad de normas matriciales inducidas.

Confirma que ||Mv|| <= ||M|| * ||v|| para:
- Normas inducidas 1, 2 e inf.
- Matrices y vectores aleatorios de distinto tamaño.
"""

import numpy as np

np.random.seed(42)
SIZES = [3, 5, 10, 50]
NORMS = [1, 2, np.inf]
NORM_NAMES = {1: "1", 2: "2", np.inf: "inf"}
TRIALS = 1_000


def matrix_induced_norm(M: np.ndarray, p) -> float:
    """Norma matricial inducida por la norma vectorial p."""
    if p == 1:
        return np.max(np.sum(np.abs(M), axis=0))   # máxima suma por columna
    elif p == np.inf:
        return np.max(np.sum(np.abs(M), axis=1))   # máxima suma por fila
    elif p == 2:
        return np.linalg.norm(M, ord=2)             # mayor valor singular


print("=" * 65)
print("  Verificación: ||Mv|| <= ||M|| * ||v||  para normas inducidas")
print("=" * 65)

all_passed = True

for n in SIZES:
    for p in NORMS:
        violations = 0
        max_ratio = 0.0

        for _ in range(TRIALS):
            M = np.random.randn(n, n)
            v = np.random.randn(n)

            lhs = np.linalg.norm(M @ v, ord=p)
            rhs = matrix_induced_norm(M, p) * np.linalg.norm(v, ord=p)

            # Permitir un margen numérico muy pequeño por punto flotante
            if lhs > rhs + 1e-10:
                violations += 1

            if np.linalg.norm(v, ord=p) > 1e-14:
                max_ratio = max(max_ratio, lhs / rhs)

        status = "✓ PASS" if violations == 0 else f"✗ FAIL ({violations} violaciones)"
        print(
            f"  n={n:3d} | norma-{NORM_NAMES[p]:>3s} | {status} | "
            f"max(||Mv|| / (||M|| ||v||)) = {max_ratio:.6f}"
        )
        if violations > 0:
            all_passed = False

print("=" * 65)
print(f"\n  Resultado global: {'TODAS LAS PRUEBAS PASARON ✓' if all_passed else 'EXISTEN FALLAS ✗'}")
print(
    "\n  Nota: max_ratio <= 1.0 en todos los casos confirma que la cota\n"
    "  es ajustada y válida, sin excederse nunca (salvo ruido numérico)."
)

```
