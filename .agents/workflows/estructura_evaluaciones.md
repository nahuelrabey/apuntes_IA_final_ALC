---
description: Guía estricta para la creación y estructuración de directorios de exámenes finales y parciales nuevos.
---

# Estructura Obligatoria de Evaluaciones

Cuando el usuario solicite crear, inicializar o resolver un nuevo Examen Final o Parcial, el agente DEBE respetar estrictamente la siguiente topología de archivos y carpetas dentro de la carpeta `docs/{MATERIA}/`.

> **IMPORTANTE**: Antes de crear la carpeta del examen, identificar la materia correspondiente (por ejemplo: `ALC`, `Analisis_Avanzado`) y usarla como prefijo del path. El directorio destino es `docs/{MATERIA}/finales/Examen_YYYY_MM_DD/` o `docs/{MATERIA}/parciales/Parcial_YYYY_MM_DD/`.

## 1. Nomenclatura del Directorio Principal
Cada evaluación debe aislarse en un directorio propio bajo la materia y tipo que corresponda con el formato:
`docs/{MATERIA}/{TIPO_EVALUACION}/{Nombre_Evaluacion}/`
Ejemplos: 
- `docs/ALC/finales/Examen_2026_02_18`
- `docs/ALC/parciales/Parcial_2026_04_10`

## 2. Índice de la Evaluación (El Enunciado)
En la raíz de la carpeta de la evaluación, DEBE existir **siempre** un archivo llamado `enunciado.md`. 
- Este archivo actuará como presentación e índice.
- Contendrá el texto general inicial o las imágenes globales.
- **Contenido Teórico Obligatorio**: Además del enunciado bruto, este archivo debe listar de forma explícita los **temas generales**, así como los **teoremas y proposiciones teóricas** clave que resultaron necesarios para resolver los ejercicios propuestos. **Atención vital: Cada teorema o proposición enumerada aquí debe contar con su correspondiente archivo de demostración en `docs/{MATERIA}/demostraciones/`, y su mención en el enunciado debe actuar como un hipervínculo directo hacia dicha demostración.**
- En el archivo `mkdocs.yml`, este `enunciado.md` debe ser obligatoriamente el primer ítem anidado bajo la entrada de la evaluación, y debe llevar la etiqueta "Enunciado".

## 3. Carpetas Individuales por Ejercicio
No se debe redactar la teoría ni el código de toda la evaluación en un solo archivo. Por cada ejercicio, se debe crear **una subcarpeta dedicada**.
- Formato de Nomenclatura Promedio: `[NUMERO]_[TEMA_CORTO]`
- Ejemplo: `01_metodo_sor/`, `02_condicionamiento/`.

Dentro de la subcarpeta de cada ejercicio, coexistirán sus artefactos (siguiendo la metodología de `resolucion_matematica.md`):
- `teoria.md`: La resolución matemática formalizada y explicada.
- `verificacion.py`: Código en Python/NumPy (si aplica) para confirmar los resultados teóricos.

## 4. Ejemplo del Árbol de Directorios Esperado

```text
docs/
├── ALC/
│   ├── finales/
│   │   ├── Examen_2026_02_18/
│   │   │   ├── enunciado.md                  <-- Archivo ÍNDICE obligatorio
│   │   │   ├── 01_metodo_sor/                <-- Carpeta Ejercicio 1
│   │   │   │   ├── teoria.md
│   │   │   │   └── verificacion.py
│   │   │   ├── 02_condicionamiento/          <-- Carpeta Ejercicio 2
│   │   │   │   └── teoria.md
```

## 5. Actualización de MkDocs
Todo agente debe recordar indexar el nuevo material dentro del arreglo `nav` en el archivo `mkdocs.yml`. La agrupación jerárquica es:
```yaml
nav:
  - {MATERIA}:
      - Finales:
          - Examen DD de mmm de YYYY:
              - Enunciado: {MATERIA}/finales/Examen_YYYY_MM_DD/enunciado.md
              - 01. Tema del Ejercicio 1: {MATERIA}/finales/Examen_YYYY_MM_DD/01_tema/teoria.md
```
