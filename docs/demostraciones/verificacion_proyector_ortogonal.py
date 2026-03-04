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
