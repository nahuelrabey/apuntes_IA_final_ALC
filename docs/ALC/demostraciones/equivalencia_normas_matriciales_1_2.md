# Equivalencia de Normas Matriciales: $\|A\|_1$ y $\|A\|_2$

**Demostración.** Sea $A \in \mathbb{R}^{n \times n}$. Demostrar las siguientes desigualdades que relacionan la norma matricial inducida $\ell_1$ (máxima suma por columnas) con la norma matricial inducida $\ell_2$ (norma espectral):

$$
\frac{1}{\sqrt{n}}\|A\|_1 \leq \|A\|_2 \leq \sqrt{n}\|A\|_1
$$
## Interpretación del Enunciado

Al igual que con la norma infinito, la norma $\ell_1$ matricial es mucho más barata computacionalmente que la norma $\ell_2$. Estas cotas permiten estimar el radio espectral o la estabilidad de una matriz sin recurrir a la descomposición en valores singulares (SVD). La simetría de los factores $\sqrt{n}$ y $1/\sqrt{n}$ refleja la dualidad entre las normas vectoriales $\ell_1$ y $\ell_\infty$.

---

## Solución Analítica

### 1. Demostración de $\|A\|_2 \leq \sqrt{n}\|A\|_1$

Utilizamos las equivalencias vectoriales: $\|v\|_2 \leq \|v\|_1$ y $\|v\|_1 \leq \sqrt{n}\|v\|_2 \implies \frac{1}{\|v\|_2} \leq \frac{\sqrt{n}}{\|v\|_1}$.

$$
\|Ax\|_2 \leq \|Ax\|_1

$$
$$
\frac{1}{\|x\|_2} \leq \frac{\sqrt{n}}{\|x\|_1}

$$
Multiplicando:

$$
\frac{\|Ax\|_2}{\|x\|_2} \leq \frac{\sqrt{n}\|Ax\|_1}{\|x\|_1}

$$
Tomando el máximo sobre $x \neq 0$:

$$
\|A\|_2 \leq \sqrt{n}\|A\|_1

$$
### 2. Demostración de $\frac{1}{\sqrt{n}}\|A\|_1 \leq \|A\|_2$

Usamos: $\|v\|_1 \leq \sqrt{n}\|v\|_2$ y $\|v\|_2 \leq \|v\|_1 \implies \frac{1}{\|v\|_1} \leq \frac{1}{\|v\|_2}$.

$$
\|Ax\|_1 \leq \sqrt{n}\|Ax\|_2

$$
$$
\frac{1}{\|x\|_1} \leq \frac{1}{\|x\|_2}

$$
Multiplicando:

$$
\frac{\|Ax\|_1}{\|x\|_1} \leq \frac{\sqrt{n}\|Ax\|_2}{\|x\|_2}

$$
Tomando el máximo sobre $x \neq 0$:

$$
\|A\|_1 \leq \sqrt{n}\|A\|_2 \implies \frac{1}{\sqrt{n}}\|A\|_1 \leq \|A\|_2

$$
Combinando ambos resultados:

$$
\frac{1}{\sqrt{n}}\|A\|_1 \leq \|A\|_2 \leq \sqrt{n}\|A\|_1

$$
---

```python
import numpy as np

def verify_matrix_norms_1_2():
    print("Verificando numéricamente: (1/sqrt(n))||A||_1 <= ||A||_2 <= sqrt(n)||A||_1")
    
    np.random.seed(42)
    sizes = [2, 5, 10, 50]
    n_trials = 500
    
    for n in sizes:
        inv_sqrt_n = 1.0 / np.sqrt(n)
        sqrt_n = np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            A = np.random.randn(n, n)
            
            norm_1 = np.linalg.norm(A, ord=1)
            norm_2 = np.linalg.norm(A, ord=2)
            
            # Verificar desigualdades
            lower_ok = inv_sqrt_n * norm_1 <= norm_2 + 1e-12
            upper_ok = norm_2 <= sqrt_n * norm_1 + 1e-12
            
            if not (lower_ok and upper_ok):
                success = False
                break
                
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión {n}x{n}: Verificadas {n_trials} matrices.")

if __name__ == "__main__":
    verify_matrix_norms_1_2()

```
