---
description: Guía estricta para la creación y estructuración de guías de ejercicios.
---

# Estructura Obligatoria de Guías Prácticas

Cuando el usuario solicite crear o resolver ejercicios pertenecientes a una guía práctica, el agente DEBE respetar la siguiente topología de archivos y carpetas.

## 1. Ubicación y Nomenclatura
Las guías residen bajo la carpeta `guias/` de la materia respectiva. 
El directorio para una guía entera lleva el formato estructurado: `Guia_XX_tema`.
Ejemplo: `docs/ALC/guias/Guia_01_iterativos/`

## 2. Índice de la Guía (`index.md`)
Cada guía debe contener indefectiblemente un archivo `index.md` en su raíz.
A diferencia de los exámenes, **las guías NO tienen un `enunciado.md` único**. El `index.md` sirve como portada, introduciendo los temas de la guía y proporcionando el índice de enlaces hacia cada ejercicio resuelto.

## 3. Carpetas por Ejercicio
Cada inciso numérico o problema de la guía debe estar aislado en un subdirectorio propio, usando una nomenclatura estándar y progresiva:
Ejemplo: `ejercicio_01/`, `ejercicio_02/`, `ejercicio_03a/`.

## 4. Archivos Internos de Cada Ejercicio
Dentro del directorio del ejercicio, se seguirá el formato unificado:
- **`teoria.md`**: Contendrá el enunciado de ese ejercicio en particular como título/cita inicial, seguido inmediatamente de la demostración matemática formalizada y explicada. (Importante: a diferencia del pasado, usamos `teoria.md` y no `resolucion.md` para mantener consistencia estricta con los exámenes).
- **`verificacion.py`**: El script sancionador/validador en Python, de corresponder.

## 5. Ejemplo del Árbol de Directorios Esperado

```text
docs/
├── {MATERIA}/
│   ├── guias/
│   │   ├── Guia_01_iterativos/
│   │   │   ├── index.md                      <-- Portada de la guía
│   │   │   ├── ejercicio_01/                 <-- Carpeta para el Ejercicio 1
│   │   │   │   ├── teoria.md                 <-- Enunciado breve + Resolución
│   │   │   │   └── verificacion.py
│   │   │   ├── ejercicio_02/
│   │   │   │   ├── teoria.md
```

## 6. Actualización en MkDocs
La guía debe registrarse en `mkdocs.yml` bajo la rama correspondiente a la materia y sección Guías:
```yaml
nav:
  - {MATERIA}:
      - Guías:
          - Guía 01 - Iterativos:
              - Introducción: {MATERIA}/guias/Guia_01_iterativos/index.md
              - Ejercicio 1: {MATERIA}/guias/Guia_01_iterativos/ejercicio_01/teoria.md
              - Ejercicio 2: {MATERIA}/guias/Guia_01_iterativos/ejercicio_02/teoria.md
```
