---
description: Guía para la creación y estructuración de apuntes de clase.
---

# Estructura de Notas de Clase

Los apuntes de clase capturan la explicación dinámica del docente y los ejemplos prácticos discutidos en el aula.

## 1. Ubicación y Nomenclatura
Las notas de clase residen bajo la carpeta `clases/` de la materia respectiva.
Formato del archivo: `docs/{MATERIA}/clases/Clase_NN_tema.md`.
Ejemplo: `docs/ALC/clases/Clase_01_introduccion_svd.md`.

## 2. Estructura del Documento
- **Título (H1)**: `Clase NN: Tema de la Clase`.
- **Bloque de Metadatos**: Fecha de la clase y docente (opcional).
- **Contenidos Principales**: Desarrollo de los temas vistos.
- **Ejemplos de Pizarra**: Usar bloques de código o diagramas Mermaid para replicar ejemplos prácticos.

## 3. Relación con la Teoría
Es fundamental que las notas de clase vinculen a:
- `demostraciones/`: Para el rigor matemático de lo visto en clase.
- `guias/`: Si se resolvió algún ejercicio específico de la guía en clase.

## 4. Tips y Observaciones del Docente
Utilizar admoniciones para resaltar advertencias o consejos dados en clase:
```markdown
> [!TIP]
> El profesor hizo hincapié en que este teorema suele evaluarse en los finales.
```
o
```markdown
<Info titulo="Comentario Lateral">
    Se discutió brevemente la relación con la materia del cuatrimestre pasado...
</Info>
```
