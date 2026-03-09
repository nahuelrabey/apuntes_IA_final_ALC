# Simetría y Ortogonalidad de Proyectores

> **Teorema.** Sea $p: \mathbb{R}^n \to \mathbb{R}^n$ un proyector (operador idempotente, $p^2 = p$). $p$ es un proyector **ortogonal** si y solo si su matriz asociada $P$ en la base canónica es **simétrica** ($P = P^T$).

## Interpretación del Enunciado

Un proyector se define geométricamente por su imagen ($S$) y su núcleo ($W$), donde $\mathbb{R}^n = S \oplus W$. Decimos que el proyector es **ortogonal** si la proyección se realiza de forma perpendicular al subespacio imagen, lo que implica que el núcleo debe ser exactamente el complemento ortogonal de la imagen ($W = S^\perp$).

El teorema establece un puente directo entre esta propiedad geométrica ($S \perp W$) y una propiedad algebraica de la matriz ($P = P^T$).

## Solución del Ejercicio (Demostración)

Para demostrar la equivalencia ($p$ es ortogonal $\iff P = P^T$), procederemos en ambos sentidos.

### 1. Implicación Directa ($\implies$)
*Si $p$ es un proyector ortogonal, entonces $P = P^T$.*

Sea $x, y \in \mathbb{R}^n$ dos vectores cualesquiera. Podemos descomponer cada uno en su parte en la imagen ($S$) y su parte en el núcleo ($W$):
$x = s_x + n_x$ con $s_x \in S, n_x \in W$
$y = s_y + n_y$ con $s_y \in S, n_y \in W$

Por definición de proyector: $Px = s_x$ y $Py = s_y$.
Si el proyector es ortogonal, entonces $S \perp W$, lo que significa que el producto interno entre cualquier vector de $S$ y cualquier vector de $W$ es cero.

Evaluamos el producto interno $\langle Px, y \rangle$:

$$
\langle Px, y \rangle = \langle s_x, s_y + n_y \rangle = \langle s_x, s_y \rangle + \underbrace{\langle s_x, n_y \rangle}_{0 \text{ (por ortogonalidad)}} = \langle s_x, s_y \rangle
$$

Ahora evaluamos $\langle x, Py \rangle$:

$$
\langle x, Py \rangle = \langle s_x + n_x, s_y \rangle = \langle s_x, s_y \rangle + \underbrace{\langle n_x, s_y \rangle}_{0 \text{ (por ortogonalidad)}} = \langle s_x, s_y \rangle
$$

Como $\langle Px, y \rangle = \langle x, Py \rangle$ para todo $x, y$, el operador es **autoadjunto**. En la base canónica, esto implica que la matriz es simétrica: $P = P^T$.

### 2. Implicación Recíproca ($\impliedby$)
*Si $P = P^T$, entonces $p$ es un proyector ortogonal.*

Sabemos que para cualquier matriz $P$, se cumple la propiedad fundamental de los espacios subyacentes:

$$
Im(P)^\perp = Nu(P^T)
$$

Si la matriz es simétrica, entonces $P^T = P$. Sustituyendo en la igualdad anterior obtenemos:

$$
Im(P)^\perp = Nu(P)
$$

Como el núcleo del proyector es exactamente el complemento ortogonal de su imagen, la proyección es, por definición, ortogonal.

**Q.E.D.**

---

## Verificación Computacional

Para validar esta equivalencia en múltiples dimensiones y con matrices aleatorias, se ha desarrollado un script que genera tanto proyectores ortogonales (vía descomposición QR) como oblicuos, verificando la relación entre su simetría y la ortogonalidad de sus subespacios.

--8<-- "docs/demostraciones/verificacion_proyector_ortogonal.py"
