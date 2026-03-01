# Convergencia de Métodos Iterativos y Radio Espectral

> **Teorema de Convergencia.**
> Sea el sistema lineal $Ax = b$ y un método iterativo de la forma:
>
> $$
> x^{(k+1)} = B x^{(k)} + c
> $$
>
> donde $B$ es la matriz de iteración. El método converge a la solución única $x^*$ para cualquier vector inicial $x^{(0)}$ si y solo si el radio espectral de $B$ es menor a la unidad:
>
> $$
> \rho(B) < 1
> $$
>

## Interpretación del Enunciado

Se busca demostrar la condición necesaria y suficiente para que un proceso iterativo lineal sea convergente. La clave reside en analizar cómo evoluciona el error entre la solución exacta y las aproximaciones sucesivas, y cómo esta evolución depende de las propiedades espectrales (autovalores) de la matriz de iteración.

---

## Solución del Ejercicio

### 1. Relación Recurrente del Error

Definimos el error en el paso $k$ como $e^{(k)} = x^{(k)} - x^*$, donde $x^*$ es el punto fijo del sistema, es decir, la solución exacta que cumple:

$$
x^* = B x^* + c
$$

Restamos esta igualdad de la fórmula recursiva del método $x^{(k+1)} = B x^{(k)} + c$:

$$
x^{(k+1)} - x^* = (B x^{(k)} + c) - (B x^* + c)
$$

$$
e^{(k+1)} = B (x^{(k)} - x^*) = B e^{(k)}
$$

Aplicando esta relación de forma sucesiva desde el error inicial $e^{(0)}$:

$$
e^{(1)} = B e^{(0)}
$$

$$
e^{(2)} = B e^{(1)} = B(B e^{(0)}) = B^2 e^{(0)}
$$

$$
\dots
$$

$$
e^{(k)} = B^k e^{(0)}
$$

### 2. Condición de Convergencia

Para que el método converja, el error debe tender a cero cuando el número de iteraciones tiende a infinito:

$$
\lim_{k \to \infty} e^{(k)} = 0 \iff \lim_{k \to \infty} B^k e^{(0)} = 0
$$

Esta condición debe cumplirse para **cualquier** error inicial $e^{(0)}$. Por lo tanto, la condición es equivalente a que la matriz $B$ sea una matriz convergente a cero:

$$
\lim_{k \to \infty} B^k = \mathbf{0}
$$

### 3. El Rol del Radio Espectral

El radio espectral $\rho(B)$ se define como el máximo de los módulos de los autovalores de $B$:

$$
\rho(B) = \max \{ |\lambda| : \lambda \in \sigma(B) \}
$$

Un teorema fundamental del álgebra lineal (basado en la Forma Canónica de Jordan) establece que:

$$
\lim_{k \to \infty} B^k = \mathbf{0} \iff \rho(B) < 1
$$

??? info "Esbozo de la justificación (Jordan)"
    Si consideramos la descomposición de Jordan $B = P J P^{-1}$, entonces $B^k = P J^k P^{-1}$. La matriz $J^k$ tiende a cero si y solo si los bloques de Jordan tienden a cero. Un bloque de Jordan $J_\lambda$ tiende a cero si y solo si su autovalor asociado cumple $|\lambda| < 1$. Si al menos un autovalor tiene $|\lambda| \ge 1$, los elementos de las potencias de ese bloque no convergerán a cero (u oscilarán o crecerán indefinidamente).

### 4. Conclusión

La velocidad de convergencia está dictada por $\rho(B)$. Cuanto más pequeño sea el radio espectral, más rápido decaerá el error hacia cero. En el método SOR, el diseño del parámetro $\omega$ busca minimizar justamente este radio espectral para acelerar la resolución del sistema.

---

## Verificación Empírica Computacional

Se simula la evolución del error para matrices con radio espectral mayor y menor a 1, confirmando la divergencia y convergencia respectivamente.

```python
--8<-- "demostraciones/convergencia_radio_espectral.py"
```
