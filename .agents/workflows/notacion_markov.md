---
description: Notación estandarizada estricta para vectores de estado temporal en Cadenas de Markov.
---

# Notación de Cadenas de Markov

Al redactar documentos teóricos, demostraciones o resoluciones prácticas que involucren Cadenas de Markov o sistemas dinámicos iterativos, es de carácter **obligatorio** utilizar la convención de supraíndices entre paréntesis para denotar la evolución temporal de los vectores de estado. 

Esto previene ambigüedades matemáticas con la indexación habitual de componentes individuales dentro de un vector.

## Reglas de Notación

1. **Vector de Estado Inicial**: Se debe utilizar el supraíndice $(0)$.
   - ❌ Incorrecto: $v_0$, $x_0$
   - ✅ Correcto: $v^{(0)}$, $x^{(0)}$
2. **Vector de Estado en el paso $k$**: Se debe utilizar el supraíndice $(k)$.
   - ❌ Incorrecto: $v_k$, $x_k$
   - ✅ Correcto: $v^{(k)}$, $x^{(k)}$
3. **Vector de Estado Límite / Estacionario**: Se debe utilizar el supraíndice $(\infty)$.
   - ❌ Incorrecto: $v_\infty$, $x_\infty$, $b_\infty$
   - ✅ Correcto: $v^{(\infty)}$, $x^{(\infty)}$, $b^{(\infty)}$

*Nota: Excepciones a esta regla aplican únicamente cuando se referencian autovectores pertenecientes a una matriz o base (por ejemplo, los autovectores $v_1, v_2, \dots, v_n$ permanecen con subíndices).*
