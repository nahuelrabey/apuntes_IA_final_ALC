---
description: Reglas estrictas para citar libros y artículos web, de aplicación exclusiva en las demostraciones.
---

# Citación de Referencias Externas

Al agregar una sección de "Referencias Externas" o al citar material, el agente DEBE acatar indefectiblemente las siguientes directrices y su **área de aplicación estricta**:

## 0. Restricción de Ámbito (Sólo Demostraciones)
**Queda terminantemente prohibido incluir referencias bibliográficas o enlaces externos dentro de los archivos teóricos de los exámenes (los archivos `teoria.md` vinculados a un examen puntual).** Las referencias externas y bibliografía de profundización y demostración análoga pertenecen y deben ubicarse **exclusivamente** dentro de los archivos generales que conforman la capeta `docs/demostraciones/`.

## 1. Relación Directa del Material
Deben buscarse activamente libros, textos académicos y artículos (páginas web) en donde se demuestre **exactamente lo mismo** (o algo sustancialmente similar) al concepto que se está desarrollando o probando en el archivo de demostración.

## 2. Enlaces Precisos Obligatorios
La mera mención de un autor o el título de una obra es inaceptable. Toda referencia debe estar acompañada de un **enlace preciso** al recurso citado:
- **Para Libros:** Debe incluirse un enlace válido para que el usuario pueda localizar la bibliografía (por ejemplo, un link con ISBN para comprar el libro, o su enlace a Google Books). Además, es imperativo especificar la ubicación intramuros de la información: **Capítulo y Sección/Página exacta**.
- **Para Artículos y Páginas Web:** Debe proveerse la URL o URI hipervinculada directamente a la página exacta (por ejemplo, el ancla a la sección específica de Wikipedia, o el DOI/link directo del paper de donde se extrae la afirmación).

## 3. Formato Sugerido

Implementa las referencias utilizando listas desordenadas en formato Markdown, adhiriendo a esta estructura de citación:

*   **Libro**: [*Título de la Obra Completa*](URL_COMPRA_O_FUENTE_CONFIABLE) (Autor, Año). **Capítulo X, Sección Y**. Breve explicación de qué concepto particular se demuestra en esa sección análoga.
*   **Web**: [Título o Sección del Artículo](URL_EXACTA_CON_ANCLA_SI_APLICA) - *Nombre del Sitio/Journal*. Breve justificación de por qué el enlace es útil para el lector en este contexto.
