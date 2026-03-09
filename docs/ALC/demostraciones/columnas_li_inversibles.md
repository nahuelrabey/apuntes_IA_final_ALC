# Demostración: Independencia Lineal e Invertibilidad

## Interpretación del Enunciado

¿Una matriz cuadrada $A$, bajo la condición de que posea todas sus columnas conformando un conjunto de **vectores linealmente independientes**, gozará *siempre* de la propiedad de ser **inversible**?

La respuesta es afirmativa. Representa un teorema central de las transformaciones lineales, donde la presencia de ejes linealmente independientes garantiza un mapeo biyectivo en el espacio.

---

## Solución Analítica

Desarrollaremos la demostración del **Teorema de la Matriz Inversible (IMT)** conectando la dependencia lineal escalar con la suryectividad a través de una deducción formal.

Dada una matriz cuadrada $A \in \mathbb{R}^{n \times n}$, compuesta por $n$ vectores columna $\{a_1, a_2, \dots, a_n\}$:

$$
A = \begin{bmatrix} | & | & & | \\ a_1 & a_2 & \dots & a_n \\ | & | & & | \end{bmatrix}

$$
### Fase 1: Análisis del Espacio Nulo (Kernel)

Como dicta la consigna originaria, los precursores o vectores columna $\{a_1, \dots, a_n\}$ son un conjunto de elementos **Linealmente Independientes**.

Por definición de independencia lineal, la única forma mediante la cual una combinación escalar de los vectores iguala al vector nulo ($\mathbf{0}$) es a través de la solución trivial donde los escalares son cero.

$$
x_1 a_1 + x_2 a_2 + \dots + x_n a_n = \mathbf{0} \quad \implies \quad x_1 = x_2 = \dots = x_n = 0

$$
Dado que multiplicar una matriz $A$ por un vector $\mathbf{x}$ corresponde a armar una combinación lineal usando las columnas de $A$, la ecuación del sistema homogéneo ($A \mathbf{x} = \mathbf{0}$) queda:

$$
(Eq. 1) \quad A \cdot \mathbf{x} = \mathbf{0}

$$
Basado en la independencia de las columnas descrita anteriormente, la única solución es que $\mathbf{x} = (0, 0, \dots, 0)^T = \mathbf{0}$.

En consecuencia, el **Núcleo de la transformación** ($\text{Nul}(A)$) se encuentra contenido únicamente por el propio origen:

$$
\text{Nul}(A) = \{\mathbf{0}\}

$$
Que el núcleo solo contenga al cero implica que el mapeo es estrictamente inyectivo.

### Fase 2: Aplicación del Teorema del Rango

Con base en el **Teorema del Rango-Nulidad**, para cualquier matriz de $n$ columnas su relación inter-espacial dimensional obedece a la fórmula:

$$
\dim(\text{Col}(A)) + \dim(\text{Nul}(A)) = n

$$
Al reemplazar la constante dictaminada $\dim(\text{Nul}(A)) = 0$, obtenemos por despeje directo:

$$
\dim(\text{Col}(A)) + 0 = n

$$
$$
\text{Rango}(A) = n

$$
En consecuencia, el subespacio columna ($\text{Col}(A)$) es idéntico al codominio en su totalidad, siendo **la transformación matricial sobreyectiva**.

### Conclusión

Repasando los resultados de los vectores columnas de $A$:

1. Al estar formados por vectores linealmente independientes, su núcleo resultó exclusivamente el vector nulo $\mathbf{0}$, garantizando la **Inyectividad**.
2. A través del Teorema del Rango, se obtuvo un rango $n$ de cobertura completa, validando la **Sobreyectividad**.

Al asegurar de forma simultánea que el mapa o transformación sea inyectivo y sobreyectivo, obtenemos una función estrictamente **Biyectiva**.

Al ser de naturaleza biyectiva, existe la operación matemática inversa de la transformación lineal. Esto dictamina que **$A$ es una matriz inversible** ($\exists A^{-1}$ y $\det(A) \neq 0$).

∎

---

## Verificación Empírica Computacional

La correspondencia teórica entre la independencia lineal de vectores columna originarios y la invertibilidad se somete a validación mediante el siguiente simulador en Python.

```python
import numpy as np

def verificar_invertibilidad_y_rango(n: int = 4, num_trials: int = 1000) -> bool:
    """
    Verifica estocásticamente el Teorema de la Matriz Inversible:
    Una matriz cuadrada tiene columnas Linealmente Independientes (Rango Completo)
    SÍ Y SOLO SÍ su determinante es no nulo (Es Inversible).
    """
    todas_validas = True
    
    for _ in range(num_trials):
        # --- CASO 1: Matriz Inversible (Columnas L.I.) ---
        # Generamos una matriz aleatoria. La probabilidad de que sus columnas sean
        # linealmente dependientes por puro azar con floats es virtualmente cero.
        A_li = np.random.randn(n, n)
        
        # Calculamos el Rango (cantidad de columnas L.I.)
        rango_li = np.linalg.matrix_rank(A_li)
        
        # Calculamos el determinante
        det_li = np.linalg.det(A_li)
        
        # Verificamos la teoría: Si el rango es N (Full Rank), el determinante no debe ser 0.
        if rango_li != n or np.isclose(det_li, 0.0):
            todas_validas = False
            
            
        # --- CASO 2: Matriz Singular (Columnas L.D.) ---
        A_ld = np.random.randn(n, n)
        # Forzamos intencionalmente que la última columna sea una copia exacta de la primera
        # Esto destruye la independencia lineal del conjunto.
        A_ld[:, -1] = A_ld[:, 0]
        
        rango_ld = np.linalg.matrix_rank(A_ld)
        det_ld = np.linalg.det(A_ld)
        
        # Verificamos la teoría: Al sabotear la independencia (Rango < N), el det SE HACE 0.
        if rango_ld == n or not np.isclose(det_ld, 0.0):
            todas_validas = False
            
    return todas_validas

if __name__ == "__main__":
    n = 4
    print(f"--- Verificando el Teorema de la Matriz Inversible (R^{n}) ---")
    
    simulacion_exitosa = verificar_invertibilidad_y_rango(n=n, num_trials=5000)
    
    if simulacion_exitosa:
        print("\n✅ SIMULACIÓN EXITOSA en 5000 ciclos:")
        print("   -> Toda matriz con Rango Completo (Columnas L.I.) devolvió un Determinante != 0 (Es Inversible).")
        print("   -> Toda matriz saboteada con una columna L.D. devolvió un Determinante == 0 (Es Singular).")
        print("\n   Conclusión: La Invertibilidad y la Independencia Lineal de las columnas son lógicamente equivalentes para todo hiperplano R^n.")
    else:
        print("\n❌ FALLO EN LA SIMULACIÓN.")

```
---

## Bibliografía y Recursos Educativos

Para consolidar referencias adicionales correspondientes a este teorema ver:

### 📖 Libros de Texto y Artículos

- **Libro: Álgebra Lineal y sus Aplicaciones (David C. Lay)**. *Capítulo 2.3: Caracterizaciones de matrices invertibles*. Fundamenta el **Teorema de la Matriz Inversible** evaluando afirmaciones análogas atadas entre sí, en particular cómo la independencia lineal está ligada a la nulidad estricta y a la preexistencia de la matriz inversa de su operador.

### 🌐 Sitios Web Universitarios

- **[Interactive Linear Algebra (Georgia Tech)](https://textbooks.math.gatech.edu/ila/invertible-matrix-thm.html)**: En *3.6 - The Invertible Matrix Theorem*, se prueba que un núcleo nulo ($0$) exige un rango pleno que dota de condiciones la invertibilidad propia.

### 🇺🇸 Videos en Inglés

- **[The Invertible Matrix Theorem (Dr. Trefor Bazett)](https://www.youtube.com/watch?v=kYJj06Gz0Cg)**: Comenta las relaciones geométricas entre las diversas propiedades análogas listadas por el teorema IMT.
