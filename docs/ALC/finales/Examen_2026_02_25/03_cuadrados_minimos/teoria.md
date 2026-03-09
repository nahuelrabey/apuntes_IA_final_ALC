# Ejercicio 3: Cuadrados Mínimos — Ranking de Solitario

> **Ejercicio 3.** Para ver quién es el mejor en el solitario, un grupo de $m$ amigos organiza $n$
> partidas del juego. Anotan el resultado en la forma $(A|b)$, con $A$ una matriz de $n \times m$,
> que tiene un 1 en la posición $i,j$ si el amigo $j$ jugó en la partida $i$ (y 0 si no); y $b$ un
> vector de longitud $n$ que tiene un 1 en la posición $i$ si la partida fue victoriosa y 0 si no.
> Para establecer un ranking buscan un vector de puntajes $x$ tal que $Ax = b$.
>
> **(a)** ¿Qué condición se debe cumplir para que el puntaje $x$ esté definido unívocamente para
> todos los amigos?
>
> **(b)** Muestre que el puntaje $x_j$ del amigo $j$ es igual a la fracción de victorias que obtuvo.
>
> **(c)** Para el caso en el que tres amigos juegan $N$ partidas, y todos ganan la mitad de ellas,
> calcule el error promedio por partida $\frac{1}{3N}\|Ax - b\|_2$. ¿Aumenta o disminuye con el
> número de partidas?

---

## Interpretación del Enunciado

{/* El sistema Ax = b es típicamente sobredeterminado (n >> m). Se busca la solución
     de cuadrados mínimos x* = argmin ||Ax - b||_2. */}

---

## Solución del Ejercicio

### Inciso A — Condición de Unicidad

> **(a)** ¿Qué condición se debe cumplir para que el puntaje $x$ esté definido unívocamente?

{/* La solución de cuadrados mínimos es única ⟺ A tiene rango columna completo (rango = m),
     es decir, las columnas de A son linealmente independientes. */}

### Inciso B — Puntaje = Fracción de Victorias

> **(b)** Muestre que el puntaje $x_j$ del amigo $j$ es igual a la fracción de victorias.

{/* Escribir las ecuaciones normales A^T A x = A^T b. Analizar la estructura de A^T A
     (diagonal con número de partidas jugadas por cada amigo) y A^T b (victorias por amigo). */}

### Inciso C — Error Promedio con 3 Amigos y N Partidas

> **(c)** Para tres amigos con $N$ partidas y todos ganando la mitad, calcule
> $\frac{1}{3N}\|Ax - b\|_2$. ¿Aumenta o disminuye con $N$?

{/* Con x_j = 1/2 para todo j, calcular Ax - b explícitamente en términos de N
     y evaluar la norma. */}

---

Ver implementación en [`verificacion.py`](verificacion.py).

{/* --8<-- "Examen_2026_02_25/03_cuadrados_minimos/verificacion.py" */}
