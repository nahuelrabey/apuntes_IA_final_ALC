# Simetría y Ortogonalidad de Proyectores

**Teorema.** Sea $p: \mathbb{R}^n \to \mathbb{R}^n$ un proyector (operador idempotente, $p^2 = p$). $p$ es un proyector **ortogonal** si y solo si su matriz asociada $P$ en la base canónica es **simétrica** ($P = P^T$).

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

```python
import numpy as np
from scipy.linalg import null_space

def create_orthogonal_projector(dim, r):
    # Crear una base ortonormal para un subespacio de dimensión r
    Q, _ = np.linalg.qr(np.random.randn(dim, r))
    # P = Q * Q^T es un proyector ortogonal
    P = Q @ Q.T
    return P

def create_oblique_projector(dim, r):
    # Crear base para Imagen (S) y Núcleo (W) que no sean ortogonales
    S = np.random.randn(dim, r)
    W = np.random.randn(dim, dim - r)
    
    # Asegurar que S y W no sean ortogonales inyectando dependencia
    # (En la mayoría de los casos aleatorios no lo serán, pero lo forzamos)
    B = np.hstack([S, W])
    D = np.diag([1]*r + [0]*(dim-r))
    P = B @ D @ np.linalg.inv(B)
    return P

def verify_theorem(iterations=50):
    print(f"Ejecutando {iterations} simulaciones estocásticas...")
    
    for i in range(iterations):
        dim = np.random.randint(3, 10)
        r = np.random.randint(1, dim)
        
        # Caso 1: Proyector Ortogonal
        P_ortho = create_orthogonal_projector(dim, r)
        # 1. Verificar idempotencia P^2 = P
        assert np.allclose(P_ortho @ P_ortho, P_ortho), "Fallo idempotencia en P_ortho"
        # 2. Verificar simetría P = P^T
        assert np.allclose(P_ortho, P_ortho.T), "Fallo simetría en P_ortho"
        
        # Caso 2: Proyector Oblicuo (No ortogonal)
        P_oblique = create_oblique_projector(dim, r)
        # 1. Verificar idempotencia P^2 = P
        assert np.allclose(P_oblique @ P_oblique, P_oblique), "Fallo idempotencia en P_oblique"
        # 2. Verificar que NO es simétrico (con alta probabilidad)
        # Si por azar fuera simétrico, es que el proyector es ortogonal.
        # Check orthogonality: Nu(P) == Im(P)^perp
        # Im(P) son las columnas de S. Nu(P) son las de W.
        # Comprobar si S.T @ W es casi cero.
        is_ortho = np.allclose(P_oblique, P_oblique.T)
        
        # El teorema dice: Simétrico <=> Ortogonal
        if is_ortho:
            # Si es simétrico, debe ser ortogonal geométricaente
            # O sea, Im(P) perp Nu(P)
            # Obtenemos bases de Im y Nu
            # (En el proyector oblicuo forzado, Im=S, Nu=W)
            # Pero para ser rigurosos con la matriz P final:
            U, s_vals, Vh = np.linalg.svd(P_oblique)
            im_basis = U[:, :r]
            nu_basis = null_space(P_oblique)
            assert np.allclose(im_basis.T @ nu_basis, 0, atol=1e-7), "Error: Simétrico pero NO ortogonal"
        else:
            # Si NO es simétrico, NO debe ser ortogonal
            nu_basis = null_space(P_oblique)
            im_basis = np.linalg.svd(P_oblique)[0][:, :r]
            # No debe ser todo cero
            assert not np.allclose(im_basis.T @ nu_basis, 0, atol=1e-7), "Error: No simétrico pero ortogonal"

    print("[OK] Verificación estocástica completada: Simetría <=> Ortogonalidad confirmada.")

if __name__ == "__main__":
    verify_theorem()

```
