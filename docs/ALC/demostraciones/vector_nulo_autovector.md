# Demostración: ¿Por qué un autovector nunca puede ser nulo?

## Interpretación del Enunciado

> Demostrar lógicamente, a partir de la definición formal de autovalores, por qué un autovector $v$ asociado a una transformación lineal o matriz cuadrada $A$ requiere, por definición restrictiva, ser distinto del vector nulo ($v \neq \mathbf{0}$).

Esta demostración utiliza el método de reducción al absurdo para ilustrar qué sucedería si se omitiera la restricción de que el autovector debe ser no nulo.

---

## Solución Analítica

La teoría espectral define formalmente la relación de autovalores y autovectores. Dada una matriz cuadrada $A \in \mathbb{R}^{n \times n}$, un vector $v$ es un *autovector* de $A$ si y sólo si existe un escalar $\lambda \in \mathbb{R}$ tal que:

$$
(Eq. 1) \quad A \cdot v = \lambda \cdot v

$$
Con la restricción explícita de que $v \neq \mathbf{0}$.

### Paso Inductivo (Demostración por el Absurdo)

Supongamos, como hipótesis de reducción al absurdo, que permitimos que el vector $v$ sea el vector nulo, es decir $v = \mathbf{0} = (0, 0, \dots, 0)^T$.

Sustituimos el vector nulo en la ecuación de definición original ($Eq. 1$):

$$
A \cdot \mathbf{0} = \lambda \cdot \mathbf{0}

$$
Por las propiedades del producto matricial, toda matriz multiplicada por el vector nulo da como resultado el vector nulo:

$$
(Eq. 2) \quad \mathbf{0} = \lambda \cdot \mathbf{0}

$$
A la derecha de la igualdad ($Eq. 2$), se tiene el multiplicar un escalar arbitrario $\lambda$ por el vector cero. Por propiedades de los espacios vectoriales, esto resulta en el vector cero independientemente del valor del escalar.

Esto genera una contradicción directa con el objetivo de hallar autovalores definidos:

Si proponemos un autovalor arbitrario cualquiera, por ejemplo $\lambda = 999.000$:

$$
\mathbf{0} = 999.000 \cdot \mathbf{0} \quad \implies \quad \mathbf{0} = \mathbf{0}

$$
La igualdad matemática es **siempre verdadera** para cualquier valor real de $\lambda$.

### Conclusión

Si se permitiera definir $v = \mathbf{0}$ como autovector, la definición perdería sentido debido a que **cualquier número real (todo $\lambda \in \mathbb{R}$) se consideraría formalmente un autovalor válido** de la matriz $A$, puesto que $\mathbf{0} = \lambda \cdot \mathbf{0}$ siempre se cumple.

El propósito de calcular un espectro es identificar aquellas direcciones específicas (y únicas) del espacio euclidiano en las cuales el operador $A$ actúa puramente como un factor de escala. El vector cero representa el origen de coordenadas, no determina una dirección, y por tanto, carece de interpretación geométrica bajo la transformación $A$.

Por lo tanto:

> **El Autovector $v$ debe ser no nulo ($v \neq \mathbf{0}$) para que la ecuación de autovalor defina soluciones útiles. Un Autovalor $\lambda$ en cambio puede ser igual a $0$, de presentarse la condición ($A \cdot v = 0 \cdot v \implies A \cdot v = \mathbf{0}$), significando que el autovector se aloja en el *Espacio Nulo* (Kernel) de la matriz $A$.**

Q.E.D.

---

## Verificación Empírica Computacional

La noción matemática puede probarse corroborando de modo algorítmico, donde cualquier $\lambda$ genérico inyectado al igualarse en evaluación con el vector nulo devuelve la condición lógica de `True`:

```python
import numpy as np

def verificar_vector_nulo(n: int = 3, num_trials: int = 1000) -> bool:
    """
    Verifica iterativamente que la ecuación A * v = lambda * v 
    es patológicamente trivial y matemáticamente inútil para cualquier v = 0,
    ya que se cumple para absolutamente CUALQUIER escalar lambda.
    """
    todas_validas = True
    
    for _ in range(num_trials):
        # 1. Creamos una matriz aleatoria A
        A = np.random.randn(n, n)
        
        # 2. Obligamos a que nuestro "candidato a autovector" sea el vector nulo
        v_nulo = np.zeros(n)
        
        # 3. Generamos un escalar lambda TOTALMENTE aleatorio (que ni siquiera es autovalor real de A)
        lambda_falso = np.random.randn()
        
        # 4. Calculamos ambos lados de la ecuación de autovectores (A*v = lambda*v)
        left_side = A @ v_nulo 
        right_side = lambda_falso * v_nulo 
        
        # 5. La trampa: Ambos lados SIEMPRE van a dar el vector cero
        es_igual = np.allclose(left_side, right_side)
        
        if not es_igual:
            todas_validas = False
            
    return todas_validas

if __name__ == "__main__":
    n = 3
    print(f"--- Verificando la Trivialidad del Vector Nulo (R^{n}) ---")
    
    trivialidad_confirmada = verificar_vector_nulo(n=n, num_trials=5000)
    
    if trivialidad_confirmada:
        print("\n✅ SIMULACIÓN EXITOSA: La ecuación A*0 = λ*0 se cumple para CUALQUIER matriz y CUALQUIER escalar λ existente.")
        print("   -> Conclusión: El vector nulo absorbe el producto.")
        print("   -> Consecuencia: No aporta NINGUNA información sobre la transformación de A ni sirve como base direccional.")
    else:
        print("\n❌ FALLO EN LA SIMULACIÓN.")

```
---

## Fuentes y Material Bibliográfico de Apoyo

Para expandir los fundamentos al respecto de la exclusión por definición del vector nulo, se lista el material a continuación:

- **[Khan Academy: Introducción a Vectores Propios y Valores Propios](https://es.khanacademy.org/math/linear-algebra/alternate-bases/eigen-everything/v/linear-algebra-introduction-to-eigenvalues-and-eigenvectors)**: (Video). En el minuto 8:00 detalla analíticamente por qué $v = \mathbf{0}$ es la solución trivial para todos los múltiplos escalares, desestimándose su aplicabilidad geométrica.
- **Libro: Álgebra Lineal y sus Aplicaciones (Gilbert Strang)**. *Capítulo 6: Valores Propios y Vectores Propios*. Strang especifica dogmáticamente que la búsqueda formulaica orientada a $(Ax = \lambda x)$ busca vectores no nulos dentro de cuyas líneas invariantes $Ax$ se comporta de modo paralela a $x$.
