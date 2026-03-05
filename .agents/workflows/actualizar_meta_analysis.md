---
description: Recordatorio de actualizar meta_analysis al finalizar cada sesión de trabajo.
---

# Actualización de meta_analysis

Al concluir cualquier sesión de trabajo sustancial sobre el proyecto, se debe actualizar el directorio `meta_analysis/` para mantener una memoria metodológica activa.

## Cuándo aplica

Este workflow aplica cuando en la sesión se haya:

- Creado o modificado archivos de teoría, demostraciones o verificación.
- Agregado o ajustado workflows en `.agents/workflows/`.
- Identificado un patrón nuevo de estudio, error recurrente o mejora metodológica.

## Qué actualizar

### `analisis_metodologico.md`

Agregar o refinar reflexiones sobre:

- Nuevas observaciones sobre la metodología de trabajo del usuario.
- Ajustes a los tres pilares del proyecto (resolución, visualización, formateo).
- Lecciones aprendidas en la sesión.

### `historial_prompts.md`

Registrar los prompts más representativos de la sesión, especialmente aquellos que:

- Introdujeron un concepto nuevo no cubierto antes.
- Corrigieron un error metodológico.
- Generaron una nueva demostración o workflow.

## Formato de entrada en historial

```
## Sesión YYYY-MM-DD

- **Tema**: [tema principal trabajado]
- **Archivos modificados**: [lista]
- **Prompts clave**: [resumen breve de los prompts más relevantes]
- **Observaciones**: [cualquier patrón o aprendizaje notable]
```
