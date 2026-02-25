---
description: Guía estricta para la creación y estructuración de directorios de exámenes finales nuevos.
---

# Estructura Obligatoria de Exámenes Finales

Cuando el usuario solicite crear, inicializar o resolver un nuevo Examen Final, el agente DEBE respetar estrictamente la siguiente topología de archivos y carpetas dentro de la carpeta `docs/`.

## 1. Nomenclatura del Directorio Principal
Cada examen debe aislarse en un directorio propio bajo `docs/` con el formato:
`Examen_YYYY_MM_DD`
Ejemplo: `docs/Examen_2026_02_18`

## 2. Índice del Examen (El Enunciado)
En la raíz de la carpeta del examen, DEBE existir **siempre** un archivo llamado `enunciado.md`. 
- Este archivo actuará como presentación e índice del final.
- Contendrá el texto general, las imágenes globales o simplemente el título del examen si aún no hay contenido asimilado.
- En el archivo `mkdocs.yml`, este archivo `enunciado.md` debe ser obligatoriamente el primer ítem anidado bajo la entrada del examen, y debe llevar la etiqueta "Enunciado".

## 3. Carpetas Individuales por Ejercicio
No se debe redactar la teoría ni el código de todo el examen en un solo archivo. Por cada ejercicio o problema dictado en el examen, se debe crear **una subcarpeta dedicada**.
- Formato de Nomenclatura Promedio: `[NUMERO]_[TEMA_CORTO]`
- Ejemplo: `01_metodo_sor/`, `02_condicionamiento/`, `03_cadenas_markov/`.

Dentro de la subcarpeta de cada ejercicio, coexistirán sus artefactos correspondientes (siguiendo la metodología de `resolucion_matematica.md`):
- `teoria.md`: La resolución matemática formalizada y explicada.
- `verificacion.py`: Código en Python/NumPy (si aplica) para confirmar los resultados teóricos.

## 4. Ejemplo del Árbol de Directorios Esperado

```text
docs/
├── Examen_2026_02_18/
│   ├── enunciado.md                  <-- Archivo ÍNDICE obligatorio
│   ├── 01_metodo_sor/                <-- Carpeta Ejercicio 1
│   │   ├── teoria.md
│   │   └── verificacion.py
│   ├── 02_condicionamiento/          <-- Carpeta Ejercicio 2
│   │   └── teoria.md
│   └── 03_cadenas_markov/            <-- Carpeta Ejercicio 3
│       ├── teoria.md
│       └── verificacion.py
```

## 5. Actualización de MkDocs
Todo agente debe recordar indexar el nuevo material dentro del arreglo `nav` en el archivo `mkdocs.yml`. La agrupación jerárquica es:
```yaml
nav:
  - Finales:
      - Examen DD de mmm de YYYY:
          - Enunciado: Examen_YYYY_MM_DD/enunciado.md
          - 01. Tema del Ejercicio 1: Examen_YYYY_MM_DD/01_tema/teoria.md
          - 02. Tema del Ejercicio 2: Examen_YYYY_MM_DD/02_tema/teoria.md
```
