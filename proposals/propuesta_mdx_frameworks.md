# Propuesta: Migración a MDX con Componentes y Gráficos

**Fecha:** 2026-03-05  
**Estado:** Borrador  
**Contexto:** Extensión de la propuesta de restructuración del repositorio

---

## Motivación

El formato Markdown actual tiene dos limitaciones concretas:

1. **Bloques delimitados por indentación** — Las admonitions de MkDocs (`!!! note`, `??? warning`) dependen de la indentación de 4 espacios para determinar el fin del bloque. Esto es frágil y propenso a errores silenciosos.
2. **Sin gráficos dinámicos** — Los scripts de verificación (`verificacion.py`) generan datos pero no tienen forma de renderizarlos en el documento final.

La solución es mover a un sistema donde el contenido es **MDX**: Markdown enriquecido con componentes con etiquetas de apertura/cierre explícitas.

---

## Requisito 1: Bloques con Etiquetas Explícitas

En MDX, los bloques son componentes JSX con etiquetas. El inicio y fin son inequívocos:

```mdx
<Nota>
El proyector ortogonal satisface $P^2 = P$ y $P^T = P$.
Esto es independiente de la indentación del texto.
</Nota>

<Advertencia>
Esta propiedad **no** se cumple para proyectores oblicuos.
</Advertencia>

<Ejercicio titulo="Demostración de idempotencia">
Sea $P$ el proyector sobre $\text{Im}(A)$...

$$
P^2 x = P(Px) = Px
$$
</Ejercicio>
```

Beneficios concretos para este proyecto:
- **Fin de bloque explícito**: `</Nota>` cierra el bloque sin ambigüedad, sin importar la indentación del contenido.
- **Props tipadas**: `titulo="..."` permite metadatos semánticos en cada bloque.
- **Compatibilidad con LaTeX**: el contenido entre etiquetas sigue siendo Markdown estándar, los delimitadores `$...$` y `$$...$$` funcionan igual.

---

## Requisito 2: Gráficos desde Scripts

El modelo de trabajo propuesto es:

```
verificacion.py  →  genera dataset (JSON/CSV)  →  componente JSX lo renderiza
```

**Ejemplo de flujo:**

```python
# verificacion.py — existente, se agrega exportación de datos
import numpy as np, json

valores = np.linalg.eigvalsh(A)
with open("eigenvalues.json", "w") as f:
    json.dump({"valores": valores.tolist()}, f)
```

```mdx
{/* En el .mdx del ejercicio */}
import eigenvalues from "./eigenvalues.json"
import { GraficoLinea } from "@/components/Graficos"

<GraficoLinea
  datos={eigenvalues.valores}
  titulo="Valores propios de A"
  ejex="Índice"
  ejey="λ"
/>
```

Esto no requiere ningún cambio en la lógica de los scripts existentes; solo agregar una exportación de datos.

---

## Comparativa de Frameworks

| Criterio | **AstroJS** | **Docusaurus** | **Nextra** | **VitePress** |
|---|---|---|---|---|
| **Soporte MDX** | ✅ Oficial via `@astrojs/mdx` | ✅ Nativo (MDX v3) | ✅ Nativo (MDX v3) | ⚠️ Solo Vue, sin MDX |
| **Framework JS** | Agnóstico (React, Svelte, Vue...) | React | React (Next.js) | Vue |
| **Matemáticas (KaTeX/MathJax)** | Plugin manual | Plugin oficial | Plugin oficial | Plugin oficial |
| **Orientado a docs** | ⚠️ General (requiere tema) | ✅ Diseñado para docs | ✅ Diseñado para docs | ✅ Diseñado para docs |
| **Sidebar/Nav automático** | ⚠️ Manual o via integración | ✅ Automático | ✅ Automático | ✅ Automático |
| **Velocidad de build** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Curva de aprendizaje** | Media | Baja | Baja-Media | Baja |
| **Migración desde MkDocs** | Media | Media | Media | Media |

### AstroJS

**Arquitectura Islands**: el JS solo se envía para los componentes interactivos (como un gráfico). El resto del sitio es HTML estático puro. Ideal para un sitio mayoritariamente de texto matemático con gráficos ocasionales.

```astro
---
// Un componente de gráfico que solo hidrata en el cliente
import GraficoLinea from "../components/GraficoLinea.jsx"
---
<GraficoLinea client:load datos={eigenvalues} />
```

**Pros:** Máxima flexibilidad, mejor rendimiento, no obliga a React.  
**Contras:** Hay que construir la estructura del sitio desde cero (sidebar, búsqueda, nav).

---

### Docusaurus

Desarrollado por Meta, especializado en documentación técnica. Incluye búsqueda, sidebar automático, versioning y i18n out of the box. Usa React y soporta MDX nativo.

```mdx
import Plotly from "../components/PlotlyChart"

<Plotly data={require("./eigenvalues.json")} />
```

**Pros:** Lista para usarse, ecosistema maduro, plugins de matemáticas ya existen.  
**Contras:** Opinionated (Infima CSS), personalización requiere swizzling de componentes React.

---

### Nextra

Construido sobre **Next.js**. Tiene dos temas oficiales: `docs` y `blog`. MDX nativo, file-based routing, soporte completo de React.

```mdx
import dynamic from "next/dynamic"
const Grafico = dynamic(() => import("../components/Grafico"), { ssr: false })

<Grafico datos={eigenvalues} />
```

**Pros:** Todo el ecosistema de Next.js disponible, fácil deployment en Vercel.  
**Contras:** Dependencia de Next.js puede ser excesiva para un sitio estático de apuntes.

---

### VitePress

Construido sobre **Vue + Vite**. No soporta MDX genérico; usa Vue SFCs dentro del Markdown. No recomendado si se quiere React o agnósticismo de framework.

**Pros:** El más rápido en build, muy simple.  
**Contras:** Sin soporte MDX real, lock-in de Vue.

---

## Recomendación

> [!IMPORTANT]
> Para este proyecto (documentación matemática académica, gráficos ocasionales, sin necesidad de interactividad compleja), la recomendación es **Docusaurus**.

**Justificación:**

- **Sidebar y navegación automáticos** — crítico dado que la estructura del repositorio ya es profunda (materia/tipo/examen/ejercicio).
- **Plugin `@docusaurus/plugin-content-docs`** maneja la jerarquía de carpetas directamente.
- **Plugin de matemáticas** (`remark-math` + `rehype-katex`) ya es un patrón documentado.
- **MDX nativo**: los bloques `<Nota>`, `<Advertencia>`, `<Ejercicio>` son componentes React simples de escribir.
- La migración desde MkDocs es mecánicamente directa: los archivos `.md` existentes son compatibles; solo las admonitions necesitan conversión de sintaxis.

**Alternativa si se prefiere evitar React:** **AstroJS** con el tema [Starlight](https://starlight.astro.build/), que provee sidebar automático, búsqueda y soporte matemático, manteniendo la arquitectura Islands de performance.

---

## Componentes a Definir

Si se avanza con cualquiera de los dos, los componentes mínimos serían:

| Componente | Equivalente actual (MkDocs) | Props sugeridas |
|---|---|---|
| `<Nota>` | `!!! note` | `titulo?` |
| `<Advertencia>` | `!!! warning` | `titulo?` |
| `<Ejercicio>` | Sección H3 | `numero`, `titulo` |
| `<Demostracion>` | Sección H3 | `titulo` |
| `<GraficoLinea>` | *(no existe)* | `datos`, `titulo`, `ejex`, `ejey` |
| `<GraficoMatriz>` | *(no existe)* | `matriz`, `titulo` |

---

## Implicaciones para los Workflows Actuales

- **`estructuracion_markdown.md`**: necesitaría una versión paralela para MDX que defina cuándo usar `<Nota>` vs `<Advertencia>` y cómo incrustar scripts.
- **`resolucion_matematica.md`**: sin cambios. El contenido matemático en LaTeX es idéntico.
- **`estructura_evaluaciones.md`**: sin cambios estructurales; los paths siguen siendo los mismos.
- Los scripts `verificacion.py` existentes no necesitan cambios; solo se agrega un bloque de exportación de datos al final.

---

## Convivencia Python (uv) + JavaScript en el mismo repositorio

### El modelo propuesto

El repositorio ya tiene un intérprete Python gestionado con `uv` (`pyproject.toml` + `uv.lock` en la raíz). La pregunta es si el intérprete JS del framework de documentación debe vivir también en esa raíz (`package.json` + `node_modules/`) o separado.

La estructura resultante sería:

```text
/                          ← raíz del repo
├── pyproject.toml         ← Python (uv)
├── uv.lock
├── .python-version
├── package.json           ← JS (npm/pnpm)
├── node_modules/
├── docs/
│   └── ALC/
│       └── finales/
│           └── Examen_2025_07_21/
│               └── 01_svd/
│                   ├── teoria.mdx
│                   ├── verificacion.py      ← genera datasets
│                   └── eigenvalues.json     ← output del script
└── src/                   ← componentes MDX (Docusaurus/Astro)
    └── components/
```

### ¿Es un antipatrón?

**No es un antipatrón**, es un patrón conocido como **polyrepo híbrido** o simplemente **monorepo multi-lenguaje**. Es común en proyectos que mezclan un backend Python con un frontend JS. Ejemplos reales: repositorios de Jupyter Book, Quarto, y la mayoría de proyectos Django + React.

Lo que sí importa es que los dos sistemas de dependencias estén **claramente delimitados** y no interfieran entre sí. `uv` y `npm`/`pnpm` son completamente independientes a nivel de archivos: no comparten lockfiles ni resolutores.

### Dónde convive el código Python: scripts locales al ejercicio

Los scripts de generación de datos pertenecen al ejercicio específico que documentan. No tiene sentido factorizarlos como librería central. La convención propuesta:

```text
docs/ALC/finales/Examen_2025_07_21/01_svd/
├── teoria.mdx
├── generar_datos.py       ← genera eigenvalues.json, singular_values.json, etc.
└── eigenvalues.json       ← commiteado o generado en build
```

El script se ejecuta manualmente (o en CI) con:

```bash
uv run docs/ALC/finales/Examen_2025_07_21/01_svd/generar_datos.py
```

`uv run` resuelve las dependencias del `pyproject.toml` raíz sin activar virtualenv manualmente. No se necesita un `pyproject.toml` local por ejercicio.

> [!NOTE]
> Los archivos `.json` generados pueden commitearse al repositorio (son pequeños y deterministas), o regenerarse en cada build de CI antes del paso de Docusaurus/Astro. La segunda opción es más limpia a largo plazo.

### ¿Dependencias Python locales por ejercicio?

En este proyecto, los scripts de verificación usan librerías estándar del proyecto (`numpy`, `scipy`). Las dependencias no varían por ejercicio: todas son comunes y viven en el `pyproject.toml` raíz.

Si en algún momento un ejercicio necesitara una dependencia excepcional, `uv` soporta **inline script dependencies** (PEP 723), que no requieren un `pyproject.toml` separado:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["scipy", "numpy"]
# ///

import numpy as np
...
```

Ejecutado con `uv run generar_datos.py`, `uv` instala las dependencias declaradas en el header del propio archivo. Ideal para scripts de un solo propósito.

### Decisión: raíz compartida

`pyproject.toml` y `package.json` conviven en `/`. Los dos gestores de dependencias (`uv` y `npm`/`pnpm`) son completamente independientes a nivel de archivos y no interfieren entre sí.

### Estructura de archivos de gestión resultante

```text
/
├── pyproject.toml         ← dependencias Python (numpy, etc.)
├── uv.lock                ← lockfile Python
├── .python-version        ← versión Python fijada por uv
├── package.json           ← dependencias JS (Docusaurus o Astro)
├── package-lock.json      ← lockfile JS (o pnpm-lock.yaml)
├── .gitignore             ← excluye node_modules/, .venv/, *.json generados
└── docs/                  ← contenido (mismo esquema que propuesta de restructuración)
```

El `.gitignore` es el único archivo que necesita coordinación explícita entre los dos sistemas:

```gitignore
# Python
.venv/
__pycache__/
*.pyc

# JS
node_modules/
.docusaurus/
build/

# Datos generados (opcional: committear o ignorar)
**/eigenvalues.json
**/singular_values.json
```
