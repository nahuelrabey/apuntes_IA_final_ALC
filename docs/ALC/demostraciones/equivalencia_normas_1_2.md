# Equivalencia de Normas: $\ell_1$ y $\ell_2$

> **Demostración.** Sea $x \in \mathbb{R}^n$. Demostrar las siguientes desigualdades que relacionan la norma del taxi ($\|x\|_1$) con la norma euclídea ($\|x\|_2$):
>
>

$$
> \frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2 \leq \|x\|_1
>

$$
## Interpretación del Enunciado

Esta relación técnica es crucial en optimización y aprendizaje automático (ML). Establece que la norma $\ell_2$ siempre es "más corta" que la $\ell_1$ (que recorre los ejes), pero nunca menor a una fracción dependiente de la dimensión del espacio.

---

## Solución Analítica

Sea $x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$.

### 1. Demostración de $\|x\|_2 \leq \|x\|_1$

Elevamos al cuadrado la norma $\ell_1$:

$$
\|x\|_1^2 = \left( \sum_{i=1}^n |x_i| \right)^2 = \sum_{i=1}^n |x_i|^2 + \sum_{i \neq j} |x_i||x_j|

$$
Como la segunda sumatoria contiene términos no negativos ($|x_i||x_j| \geq 0$):

$$
\|x\|_1^2 \geq \sum_{i=1}^n |x_i|^2 = \sum_{i=1}^n x_i^2 = \|x\|_2^2

$$
Aplicando raíz cuadrada:

$$
\|x\|_1 \geq \|x\|_2 \implies \|x\|_2 \leq \|x\|_1

$$
### 2. Demostración de $\frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2$

Para esta parte utilizaremos la **Desigualdad de Cauchy-Schwarz**, que establece que para dos vectores $a, b$:
$|\langle a, b \rangle| \leq \|a\|_2 \|b\|_2$.

Sea $a = (|x_1|, |x_2|, \dots, |x_n|)$ y sea $b = (1, 1, \dots, 1)$. Aplicando la desigualdad:

$$
\sum_{i=1}^n |x_i| \cdot 1 \leq \sqrt{\sum_{i=1}^n |x_i|^2} \cdot \sqrt{\sum_{i=1}^n 1^2}

$$
Reconociendo los términos:
-   La sumatoria de la izquierda es $\|x\|_1$.
-   La primera raíz de la derecha es $\|x\|_2$.
-   La segunda raíz de la derecha es $\sqrt{n}$.

Entonces:

$$
\|x\|_1 \leq \|x\|_2 \cdot \sqrt{n}

$$
Dividiendo por $\sqrt{n}$:

$$
\frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2

$$
Combinando ambos resultados obtenemos la cadena buscada:

$$
\frac{1}{\sqrt{n}}\|x\|_1 \leq \|x\|_2 \leq \|x\|_1

$$
---

```python
import numpy as np

def verify_norms_1_2():
    print("Verificando numéricamente: (1/sqrt(n))||x||_1 <= ||x||_2 <= ||x||_1")
    
    np.random.seed(42)
    n_dims = [2, 10, 100, 1000]
    n_trials = 1000
    
    for n in n_dims:
        inv_sqrt_n = 1.0 / np.sqrt(n)
        success = True
        
        for _ in range(n_trials):
            x = np.random.randn(n)
            
            norm_1 = np.linalg.norm(x, ord=1)
            norm_2 = np.linalg.norm(x, ord=2)
            
            # Verificar desigualdades
            lower_bound = inv_sqrt_n * norm_1 <= norm_2 + 1e-12
            upper_bound = norm_2 <= norm_1 + 1e-12
            
            if not (lower_bound and upper_bound):
                success = False
                break
        
        status = "[OK]" if success else "[FALLO]"
        print(f"{status} Dimensión n={n:4}: Verificadas {n_trials} pruebas aleatorias.")

if __name__ == "__main__":
    verify_norms_1_2()

```
