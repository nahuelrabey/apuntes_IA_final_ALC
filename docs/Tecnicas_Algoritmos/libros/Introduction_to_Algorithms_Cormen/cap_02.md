---
title: "Capítulo 2: Getting Started"
sidebar_label: "Capítulo 2"
---

# Capítulo 2: Getting Started

Esto corresponde a la materia anterior, pero introduce la idea de "dividir y conquistar".

## Insertion Sort

```python
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
```

Notemos que para este algoritmo podemos definir un _invariante_:

Antes de cada iteración del bucle `for`, el subarreglo `A[0..j-1]` está ordenado (1). 

<Info titulo="Invariante">
Un invariante es algo que vale antes:
1. antes de entrar al bucle
2. luego de cada iteración
3. al salir del bucle
</Info>

¿Porqué vale?

Antes de entrar: j = 1, por lo tanto `A[0..0]` tiene un sólo elemento, y por lo tanto está ordenado.

Luego de cada iteración: Va moviendo `A[j]` hacia la izquierda hasta encontrar un elemento mayor a él (en su defecto, va a estar en la posición 0 del arreglo). Cuando lo encuentra, inserta `A[j]` justo detrás de él. Esto lo hace con cada elemento en `A[1..j]. Luego de esto, el subarreglo `A[0..j]` está ordenado.

Al salir: j = n, por lo tanto `A[0..n-1]` está ordenado.


(Hacer los ejercicios de la página 43)


### Analisis del algoritmo

(Evaluar si hace falta completar esto)


## Mege Sort


```python
def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    # Creo deos arreglos de "n1" y "n2" elementos
    L = [0]*(n1+1)
    R = [0]*(n2+1)

    #L toma los valores de A[p..q]
    for i in range(n1): #ciclo (a)
        L[i] = A[p+i]
    #R toma los valores de A[q+1..r] 
    for j in range(n2): #ciclo (b)
        R[j] = A[q+j+1]

    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i] #instrucción (c)
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
```

### Observación
Antes de arrancar quiero que veamos esto. Si yo tengo un arreglo de números, este algoritmo lo va a partir en arreglos de un sólo elemento. Los va a ordenar en un o de dos elementos (con tiras ya ordenadas). Luego los va a ordenar en arreglos de 4 elementos (con tiras de 2 ordenadas), y así sucesivamente hasta tener el arreglo ordenado.

### Estudiamos merge
Importante, usar "merge" asume que los arreglos $A[p..q]$ y $A[q+1..r]$ están ordenados.

Veamos porqué $n_1 = q-p+1$ 

Supongamos que tenemos un arreglo `A = [a,b,c,d,e]`. Si quiero agarrar una parte, por ejemplo A[1,3] = [b,c,d], notemos que tengo 3 elementos. Pero, $d(1,3)=|3-1|=2$, es decir, la distancia de 1 a 3, es de 2. Por lo tanto, para tener un arreglo que vaya desde el índice p hasta el índice q, necesitamos $q-p+1$ elementos.

Veamos porqué $n_2 = r-q$

Quiero un arreglo que vaya desde q+1 hasta r. Por lo tanto, siguiendo la lógica anterior, tendría $n_2 = r - (q+1) + 1 = r-q$ elementos.

Notemos que L = A[p..q] y R = A[q+1..r].

Por lo tanto, el ciclo (a) construye L empezando por `A[p + 0]` y el ciclo (b) construye R empezando por `A[q + 1 + 0]`.

Cuando termina el ciclo (a), $i = n_1-1$. Cuando termina el ciclo (b), $j = n_2-1$. 

Por lo tanto 
$$L[n_1-1] = A[p + n_1 - 1] = A[p + q - p + 1 - 1] = A[q].$$

Además
$$R[n_2-1] = A[q + n_2 - 1 + 1] = A[q + r - q - 1 + 1] = A[r].$$

Una última cuestión, $L.length = n_1+1$ y $R.length = n_2+1$. Esto es así, porque el último elemento de cada arreglo es un "comodín" ($\infty$).

Propuesta de invariante:

El arreglo $A[p..k-1]$ conteine siempre los $k-p$ más pequeños de los arreglos $L$ y $R$ ordenados. Además, $L[i]$ y $R[j]$ son los elementos más pequeños de $L$ y $R$ que no han sido copiados a $A$.

Chequiemos esto

**Inicialización:**

k = p, por lo tanto $A[p..p-1]$ tiene 0 elementos, y por lo tanto está ordenado. Además, $L[0]$ y $R[0]$ son los elementos más pequeños de $L$ y $R$ que no han sido copiados a $A$.

**Mantenimiento:**

Supongamos que $L[i]<=R[j]$. Por lo tanto $L[i]$ es el elemento más chico de $L$ que no fue copiado. 

Vamos a usar $k_c$ cómo el valor de $k$ durante el ciclo.

Cómo $A[p...k_c-1]$ contiene los $k_c-p$ elementos más pequeños, luego de (c) $A[p..k_c]$ contiene los $k_c-p+1$ elementos más pequeños.

Luego, al terminar el ciclo, $k = k_c+1$, y vemos que se cumple que $A[p..k]$ contiene los $k-p$ elementos más pequeños

Además, el valor de $i$ ahor apunta al siguiente elemento, que cómo $L$ está ordenado, debe ser el mínimo que aún no ha sido compiado en $A$.

Supongamos que `R[j] <= L[i]` 

Es idéntico al anterior, pero usando R.

**Finalización**

Tenemos $k = r+1$. Por el invariante, sabemos que $A[p...k-1]$ tiene $k-p$ elementos más pequeños de $L$ y $R$ ordenados.

Por lo tanto, $A[p...r]$ debe tener los $r-p+1$ elementos más pequeños de $L$ y $R$ ordenados.

Particularmente, los útliomos elementos de $L$ y $R$, que son un comodí, no serán copiados pues no cumplen ninguno la condición de mayor-igual/menor-estricto entre sí.

### Analisis de merge-sort

(nada, falta incluirlo, veré si es parte de los ejercicios de las guías)

### Costo de computabilidad.

Quiero remarcar lo siguiente. Cómo el algoritmo va partiendo en partes "más chiquitas", particularmente, a cada arreglo lo va partiendo a la mitad, en algún momento esto va a chocar con un arreglo con un sólo elemento.

```
[1,2,3,...,n]
[1,...,n/2] [n/2+1,...,n]
[1,...,n/4] [n/4+1,...,n/2] [n/2+1,...,3n/4] [3n/4+1,...,n]
...
[1] [2] [3] [4] ... [n]
```

Bueno, supongamos que $n$ es par. Entonces ¿cuantas veces puedo partir el arreglo?

$$
\frac{n}{2^i} = 1 
$$

$$
2^i = n
$$

$$
i = lg_2(n)
$$

Además, podemos saber que "merge" nos cuesta $\Theta(n)$ tiempo. Por lo tanto, el costo total de "merge-sort" es:

$$
\Theta(n lg n)
$$

En el libro hacen re complicada esta explicación, pero básicamente es esto.
