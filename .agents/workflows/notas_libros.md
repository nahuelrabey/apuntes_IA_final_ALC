---
description: Guía para la creación y estructuración de notas de libros y bibliografía.
---

# Estructura de Notas de Libros

Cuando el usuario solicite resumir un libro o tomar notas de una lectura específica, el agente DEBE seguir esta estructura para mantener la coherencia del repositorio.

## 1. Ubicación y Nomenclatura
Las notas de libros residen bajo la carpeta `libros/` de la materia respectiva.
Formato del directorio: `docs/{MATERIA}/libros/{Titulo_Libro_Autor}/`.
Ejemplo: `docs/ALC/libros/Linear_Algebra_Lay/`.

## 2. Archivo Principal (`index.md`)
Cada libro debe tener un `index.md` que sirva como portada.
**Contenido obligatorio:**
- **Ficha Bibliográfica**: Debe seguir estrictamente el formato de `.agents/workflows/citas_referencias.md`.
- **Objetivo de la Lectura**: Breve explicación de por qué este libro es relevante para la materia.
- **Relación con Demostraciones**: Una lista de enlaces a archivos en `docs/{MATERIA}/demostraciones/` que utilicen este libro como fuente.

## 3. Notas por Capítulos
Si el libro es extenso, se deben crear archivos separados para cada capítulo o tema significativo:
`cap_01_introduccion.md`, `cap_02_espacios_vectoriales.md`, etc.

## 4. Formato de las Notas
- **Encabezados**: Mantener una jerarquía clara (H1 para el título del capítulo, H2 para secciones).
- **Blockquotes para Citas**: Toda cita textual del libro debe estar en un bloque de cita (`> ...`).
- **Observaciones**: Usar el formato de componente `<Info titulo="Título"> ... </Info>` para profundizaciones, tal como se especifica en `AGENTS.md`.

## 5. Ejemplo de Estructura de Archivo de Capítulo

```markdown
# Capítulo 4: Cadenas de Markov

> "Un proceso de Markov es un modelo estocástico que describe una secuencia de eventos posibles..." (Lay, p. 250)

## Interpretación del Concepto
Explicación simplificada del texto...

$$
v^{(k+1)} = P v^{(k)}
$$

<Info titulo="Relación con la Práctica">
    Este concepto es la base del Ejercicio 1 del Examen de Julio 2025.
</Info>
```
