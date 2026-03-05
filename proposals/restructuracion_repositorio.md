# Propuesta: Restructuración del Repositorio

**Fecha:** 2026-03-05  
**Estado:** Aprobada — pendiente de implementación

---

## Contexto

El repositorio actualmente organiza exámenes finales y demostraciones de una sola materia (ALC/IA). Su escala futura requiere:

1. **Nuevos tipos de evaluación**: parciales y ejercicios de guías.
2. **Nuevas materias**: otras asignaturas de matemática.

---

## Estructura Propuesta para `docs/`

La reorganización introduce dos niveles nuevos: **materia** y **tipo de evaluación**.

```text
docs/
├── index.md                          ← Portada general del sitio
│
├── ALC/                              ← Materia: Álgebra Lineal y Computacional
│   ├── index.md                      ← Portada de la materia
│   ├── demostraciones/               ← Demostraciones propias de ALC
│   │   └── (archivos actuales)
│   ├── finales/                      ← Exámenes finales
│   │   ├── Examen_2025_07_21/
│   │   ├── Examen_2025_08_07/
│   │   └── ...
│   ├── parciales/                    ← [NUEVO] Exámenes parciales
│   │   └── Parcial_YYYY_MM_DD/
│   │       ├── enunciado.md
│   │       └── 01_tema/
│   │           └── teoria.md
│   └── guias/                        ← [NUEVO] Guías de ejercicios
│       └── Guia_01_nombre/
│           ├── index.md
│           └── ejercicio_01/
│               └── resolucion.md
│
├── ejercicios_sueltos/           ← [NUEVO] Desafíos de clase individuales
│       └── nombre_del_ejercicio/         ← Nombre descriptivo, sin numeración
│           ├── teoria.md
│           └── verificacion.py
│
│
├── Analisis_Avanzado/                ← [NUEVA MATERIA]
│   ├── index.md
│   ├── demostraciones/
│   ├── finales/
│   ├── parciales/
│   ├── guias/
│   └── ejercicios_sueltos/
│
└── (otras materias siguiendo el mismo esquema)
```

### Decisiones de diseño

- **`demostraciones/` es por materia**, no global. Las demostraciones son específicas al lenguaje y notación de cada asignatura.
- **La carpeta raíz `docs/` no contiene exámenes directamente**, solo materias. Esto permite escalar sin colisiones de nombres.
- **Tipos de evaluación uniformes dentro de cada materia**: `finales/`, `parciales/`, `guias/`, `ejercicios_sueltos/`.
- **`ejercicios_sueltos/`**: cada carpeta tiene un nombre descriptivo (sin numeración) y la misma estructura interna que un ejercicio de examen (`teoria.md` + `verificacion.py`). No existe un `enunciado.md` ni un índice agrupadador.

---

## Cambios en `mkdocs.yml`

La navegación pasaría de plana a jerárquica:

```yaml
nav:
  - Inicio: index.md
  - ALC:
      - Inicio: ALC/index.md
      - Finales:
          - Examen 07 ago 2025: ALC/finales/Examen_2025_08_07/enunciado.md
          - ...
      - Parciales:
          - Parcial 1 - 2026: ALC/parciales/Parcial_2026_04_10/enunciado.md
      - Guías:
          - Guía 01 - Métodos iterativos: ALC/guias/Guia_01_iterativos/index.md
      - Ejercicios Sueltos:
          - Nombre del ejercicio: ALC/ejercicios_sueltos/nombre_del_ejercicio/teoria.md
      - Demostraciones:
          - (listado actual)
  - Análisis Avanzado:
      - Inicio: Analisis_Avanzado/index.md
      - ...
```

---

## Cambios en `.agents/workflows/`

| Workflow actual | Cambio propuesto |
|---|---|
| `estructura_examenes.md` | **Generalizar** para soporte multi-materia. Renombrar a `estructura_evaluaciones.md`. Ver detalle abajo. |
| `notacion_markov.md` | Sin cambios. La notación de Markov es universal y puede aplicar en cualquier materia. |
| `citas_referencias.md` | Sin cambios. Es universal. |
| `estructuracion_markdown.md` | Sin cambios. Es universal. |
| `minimal_figurative_language.md` | Sin cambios. Es universal. |
| `resolucion_matematica.md` | Sin cambios. Es universal. |
| `actualizar_meta_analysis.md` | Sin cambios. Es universal. |

### Detalle: `estructura_evaluaciones.md` y el parámetro de materia

El workflow actual tiene los paths **fijos** para una sola materia:

```text
docs/Examen_YYYY_MM_DD/01_tema/
```

Con la nueva estructura, el path correcto depende de la materia en la que se está trabajando:

```text
docs/ALC/finales/Examen_YYYY_MM_DD/01_tema/
docs/Analisis/finales/Examen_YYYY_MM_DD/01_tema/
```

Sin una instrucción explícita en el workflow, el agente no tiene información suficiente para determinar la ubicación correcta y podría crear carpetas en `docs/` raíz por defecto.

El cambio consiste en agregar una instrucción al inicio del workflow:

> *Antes de crear la carpeta del examen, identificar la materia correspondiente (por ejemplo: `ALC`, `Analisis`) y usarla como prefijo del path. El directorio destino es `docs/{MATERIA}/finales/Examen_YYYY_MM_DD/`.*

### Nuevo workflow sugerido: `estructura_guias.md`


Las guías tienen una estructura diferente a los exámenes (no hay un enunciado único, los ejercicios son independientes). Convendría un workflow específico que defina:

- Nomenclatura de carpetas dentro de `guias/`
- Formato del `index.md` de cada guía
- Si los ejercicios van con `resolucion.md` o con `teoria.md`

---

## Plan de Migración (si se aprueba)

La migración de los archivos existentes se haría en un solo paso:

1. Crear `docs/ALC/` con subdirectorios `finales/`, `demostraciones/`, `parciales/`, `guias/`.
2. Mover `docs/Examen_*` → `docs/ALC/finales/Examen_*`.
3. Mover `docs/demostraciones/` → `docs/ALC/demostraciones/`.
4. Actualizar todas las referencias internas (links entre demostraciones y teorías).
5. Actualizar `mkdocs.yml`.
6. Actualizar el workflow `estructura_examenes.md`.

> [!WARNING]
> Todos los hipervínculos internos entre `teoria.md` y `demostraciones/` usan rutas relativas. La migración romperá estos links y requerirá una búsqueda y reemplazo sistemática.

---

## Puntos Resueltos

- **Primera materia adicional**: `Analisis_Avanzado`. El esquema de carpetas se valida contra esta materia antes de generalizarse a otras.
- **Estructura de guías**: las guías tienen un `index.md` central que presenta y lista los ejercicios de forma ordenada. Cada ejercicio es una subcarpeta con su propio `teoria.md` / `verificacion.py`. La progresión es intencional (no es un banco de problemas sueltos).
- **Parciales**: misma estructura que los finales — subcarpeta por ejercicio con `enunciado.md` + `teoria.md` + `verificacion.py` opcional.
- **Ejercicios sueltos**: carpeta con nombre descriptivo libre (sin numeración), conteniendo `teoria.md` y `verificacion.py`. Sin `enunciado.md` ni índice.

