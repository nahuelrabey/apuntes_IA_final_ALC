# Ejercicio 4: Factorización LU

> **Ejercicio 4.** Dada una matriz $A$ de $\mathbb{R}^{n \times n}$,
>
> **(a)** Detalle el procedimiento para encontrar la factorización $A = LU$ sin pivoteo, indicando
> cuándo falla. ¿El fallo del algoritmo implica la inexistencia de la factorización $LU$?
>
> **(b)** Describa condiciones conocidas para que la factorización $LU$ de $A$ exista y/o sea única.

---

## Interpretación del Enunciado

<!-- El ejercicio pide distinguir entre: (1) el fallo del algoritmo de eliminación gaussiana
     sin pivoteo, y (2) la inexistencia de la factorización LU. Son conceptos distintos. -->

---

## Solución del Ejercicio

### Inciso A — Procedimiento y Fallo

> **(a)** Detalle el procedimiento para encontrar $A = LU$ sin pivoteo. ¿Cuándo falla?
> ¿El fallo implica inexistencia de LU?

<!-- 1. Describir la eliminación gaussiana: en el paso k se requiere que a_{kk}^{(k)} ≠ 0
        (pivote no nulo). Si es cero, el algoritmo FALLA (división por cero).

     2. Pero esto NO implica que LU no exista: puede existir LU aunque el algoritmo sin
        pivoteo falle. Dar un contraejemplo (ej. matriz con a_{11}=0 pero LU existe). -->

### Inciso B — Condiciones de Existencia y Unicidad

> **(b)** Describa condiciones conocidas para que la factorización $LU$ exista y/o sea única.

<!-- Condiciones suficientes de existencia:

     - Todas las submatrices principales de A son no singulares (menores principales ≠ 0).
     - A es estrictamente diagonal dominante.
     - A es definida positiva (simétrica).

     Unicidad: si L se normaliza con diagonal 1 (forma de Doolittle), la factorización LU
     es única cuando existe. -->

---

Ver implementación en [`verificacion.py`](verificacion.py).

--8<-- "Examen_2026_02_25/04_factorizacion_lu/verificacion.py"
