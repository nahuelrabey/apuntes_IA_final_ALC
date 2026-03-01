# Finales - Álgebra Lineal Computacional

Este repositorio contiene la resolución argumentativa (analítica y computacional) de los exámenes finales de la materia **Álgebra Lineal Computacional**, construida en conjunto con agentes de Inteligencia Artificial ("Antigravity"). 

El proyecto no solo alberga resoluciones estáticas, sino que funciona como una **Base de Conocimiento viva** y verificable computacionalmente gracias a su diseño emparejado entre Markdown de deducción matemática y scripts validadores de Python con librerías como `NumPy` y `SymPy`.

---

## 🚀 Cómo Usar Este Repositorio

Toda la documentación está orquestada con [MkDocs](https://www.mkdocs.org) (junto al tema Material for MkDocs y soporte para MathJax/Mermaid). Para compilar el sitio y visualizar la red de teoremas y demostraciones de forma interactiva en tu navegador local, sigue estos pasos:

### 1. Prerrequisitos
Asegúrate de tener instalado Python en tu máquina. Luego, instala las dependencias necesarias de `mkdocs` ejecutando en tu terminal:

```bash
pip install mkdocs-material pymdown-extensions
```

*(Nota técnica: para ejecutar los validadores `.py` en las carpetas anidadas necesitarás tener instalados `numpy` y `sympy`)*.

### 2. Levantar el Servidor Local
Abre una terminal interactiva apuntando al directorio raíz de este proyecto (donde se encuentra el archivo `mkdocs.yml`) y ejecuta:

```bash
mkdocs serve
```

### 3. Visualización
El comando anterior levantará un servidor virtualizado, en caliente y recargable en vivo. Se asignará una dirección web local (usualmente `http://127.0.0.1:8000/`); abre esa URL en cualquier navegador de internet para navegar por el sitio de forma gráfica.

---

## 📁 Estructura del Directiorio

La topología de este proyecto es deliberada y se rige por un marco de trabajo de separación de intereses (teoría transaccional frente a teoría matricial):

```text
Finales_ALC_IA/
├── mkdocs.yml              # Índice jerárquico y configuración del engine de MkDocs.
├── .agents/workflows/      # Reglas inquebrantables del motor de IA para generar contenido 
│                           # (Estructuración de Markdown, rigor de resolución, política de citas).
└── docs/                   # Contenedor raíz de todo el knowledge.
    ├── index.md            # Página de Inicio de la documentación web.
    ├── lecciones_aprendidas.md
    │
    ├── demostraciones/     # 📚 NÚCLEO TEÓRICO: Toda proposición universal y teorema
    │   ├── teorema_XX.md   # Explicación deductiva del teorema.
    │   └── teorema_XX.py   # Validación estocástica con floats del entorno real de ese teorema.
    │
    └── Examen_YYYY_MM_DD/  # Carpetas aisladas por fecha de final oficial.
        ├── enunciado.md    # Índice del examen (Conceptos teóricos, incisos, mapeo del día).
        ├── 01_ejercicio_1/ # Subcarpetas individuales para NO colapsar la resolución.
        │   ├── teoria.md       # Desarrollo del ejercicio. DEBE hipervincularse a 'demostraciones/' si usa teoremas.
        │   └── verificacion.py # Código NumPy parajustificar los pasos algorítmicos.
        └── ...
```

---

## 🤖 Normas para el Agente (Workflows)
Puedes encontrar la estricta guía a la que se sujeta el agente colaborador de IA en la carpeta `.agents/workflows`. Ésta domina el formato exacto de redacción matemática deductiva (`estructuracion_markdown.md`), los estándares tolerantes a floats empíricos de Python (`resolucion_matematica.md`), jerarquías de estructura de exámenes y políticas irrestricibles de citación con enlaces directos limitados a demostraciones (`citas_referencias.md`).
