# Propiedad del Módulo de una Potencia

Esta demostración justifica la propiedad $|a^n| = |a|^n$ para $a \in \mathbb{C}$ y $n \in \mathbb{N}$, y su aplicación en desigualdades de convergencia.

## 1. Demostración de $|a^n| = |a|^n$

Para demostrar esta igualdad, partimos de la propiedad fundamental del módulo del producto de dos números complejos $z$ y $w$:

$$ |z \cdot w| = |z| \cdot |w| $$

### Prueba por Inducción sobre $n$

**Caso base ($n=1$):**

$$ |a^1| = |a| \quad \text{y} \quad |a|^1 = |a| $$
La igualdad se cumple trivialmente.

**Hipótesis inductiva:**
Asumimos que vale para $k$: $|a^k| = |a|^k$.

**Paso inductivo:**
Probamos para $k+1$:

$$ |a^{k+1}| = |a^k \cdot a| $$
Aplicando la propiedad distributiva del módulo respecto al producto:

$$ |a^k \cdot a| = |a^k| \cdot |a| $$
Por hipótesis inductiva ($|a^k| = |a|^k$):

$$ |a^k| \cdot |a| = |a|^k \cdot |a| = |a|^{k+1} $$

Por lo tanto, $|a^n| = |a|^n$ para todo $n \in \mathbb{N}$.

---

## 2. Aplicación a la Desigualdad de Convergencia

En el contexto del método SOR, surge la implicancia:

$$ |(1-\omega)^n| < 1 \implies |1-\omega| < 1 $$

### Justificación

1. Por la propiedad demostrada anteriormente:
   $$ |(1-\omega)^n| = |1-\omega|^n $$
2. La desigualdad original se transforma en:
   $$ |1-\omega|^n < 1 $$
3. Definimos $x = |1-\omega|$. Notar que $x \ge 0$ por definición de módulo.
4. La función $f(x) = x^n$ es **estrictamente creciente** en el intervalo $[0, \infty)$ para $n \ge 1$.
5. Dado que $1^n = 1$, si $x^n < 1^n$, entonces necesariamente $x < 1$.

En conclusión:

$$ |1-\omega|^n < 1 \iff |1-\omega| < 1 $$

Esto confirma que para que el determinante de la matriz de iteración SOR tenga módulo menor a 1, el parámetro $\omega$ debe cumplir $|1-\omega| < 1$.

---

## 3. Verificación Empírica
Se puede verificar esta propiedad computacionalmente para diversos valores de $a$ (reales y complejos) y potencias $n$.

```python
--8<-- "demostraciones/potencia_modulo.py"
```
