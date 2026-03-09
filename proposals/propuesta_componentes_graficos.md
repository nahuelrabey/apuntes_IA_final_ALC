# Propuesta de Arquitectura: Componentes Gráficos Interactivos

En la presente propuesta delineamos el diseño y las tecnologías sugeridas para implementar los componentes interactivos `<GraficoLinea>` y `<GraficoMatriz>` en el entorno MDX de Docusaurus.

## 1. Diferencias Conceptuales

### `<GraficoLinea>` (Representación Vectorial y Geométrica)
Este componente está destinado a graficar elementos en un espacio cartesiano (2D o 3D). Su enfoque central es la geometría del Álgebra Lineal.

- **Casos de Uso:**
  * Dibujar vectores libres o acotados (v, u).
  * Graficar la recta de ajuste por Mínimos Cuadrados junto con el scatter-plot de los puntos (x, y).
  * Visualizar proyecciones ortogonales (el vector original, el subespacio proyectante y el vector residual).
  * Mostrar autovectores en el espacio y cómo la transformación los escala sin rotarlos.
- **Formato Visual:** Ejes X/Y/Z, grilla de fondo, puntos, líneas, vectores direccionales (flechas).

### `<GraficoMatriz>` (Representación Estructural y de Estado)
Este componente abandona el eje cartesiano para enfocarse en la estructura tabular y los valores numéricos directos de una matriz o un sistema de estado.

- **Casos de Uso:**
  * Representar un grafo de Markov y las probabilidades de transición.
  * Visualizar patrones de esparcidad (dónde hay ceros y dónde no) en matrices de gran tamaño.
  * Mostrar mapas de calor (heatmaps) para ilustrar los tamaños relativos de valores singulares ($SVD$).
  * Explicar el proceso de factorización LU celda por celda numéricamente o mediante colores.
- **Formato Visual:** Retículas cuadrículas, mapas de calor (escalas de color según el valor númerico), grafos de nodos (opcional).

---

## 2. Tecnologías Recomendadas

Para lograr una integración nativa en React dentro de Docusaurus asegurando alta performance y tipado dinámico, sugerimos las siguientes librerías:

### Para `<GraficoLinea>`:
* **`recharts` o `victory`:** Excelentes para gráficos estadísticos 2D estándar (como los Mínimos Cuadrados). Son componentes 100% React.
* **`plotly.js` (React-Plotly.js):** Por excelencia, la mejor herramienta para Álgebra Lineal en web por su soporte nativo para **vectores en 3D**. Permite dibujar planos, proyecciones en el espacio y superficies paramétricas de forma sencilla.
* **`mafs`:** Una librería más reciente construida especialmente para matemáticas interactivas, similar a Desmos o GeoGebra, pero en código React. Es ideal para planos 2D, rectas paramétricas y vectores arrastrables.

### Para `<GraficoMatriz>`:
* **Tailwind CSS / CSS Grid (Vanilla React):** Muchos gráficos matemáticos estructurales (como matrices de 3x3 hasta 10x10) no requieren una librería pesada de gráficos. Se pueden construir iterando una lista de arrays bidimensionales y pintando celdas paramétricamente en React con CSS Grid.
* **`react-vis` o `recharts` (Heatmaps):** Si las matrices son enormes (ejemplo, matrices de Markov de 50x50), se puede utilizar un mapa de calor para mostrar densidades numéricas.
* **`react-flow`:** Ideal por si la matriz de Markov se la desea ilustrar como un grafo y no estrictamente como una tabla rectangular.

---

## 3. Arquitectura del Componente MDX

El objetivo es que en tu archivo Markdown, invoques estos componentes de forma hiper-limpia, delegando la complejidad numérica a los props:

```mdx
### Ejemplo de Mínimos Cuadrados

<GraficoLinea 
    tipo="minimos-cuadrados"
    puntos={[[1, 2], [2, 3], [3, 5], [4, 4], [5, 6]]}
    ecuacionRecta={{ m: 0.9, b: 1.1 }}
    etiquetas={true}
/>
```

```mdx
### Ejemplo de Distribución de Matriz SVD

<GraficoMatriz 
    tipo="heatmap"
    matriz={[ [1, 0, 0], [0, 0.5, 0], [0, 0, 0.1] ]}
    maxValor={1.0}
    esquemaColor="viridis"
/>
```

## 4. Plan de Implementación Futuro

1. **Instalación Base:** Seleccionar e instalar la librería ganadora (ej. `npm install react-plotly.js plotly.js mafs`).
2. **Desarrollo del Wrapper:** Crear un archivo `src/components/Graficos/GraficoLinea.jsx` que tome un set predefinido de "tipos de gráfico" (vectores, scatter, planos) e inicialice la librería.
3. **Puliendo el CSS:** Vincular los colores de las líneas corporativos o heredados de las variables globales CSS de Infima (los verdes, azules de Docusaurus) para que en _Modo Oscuro_ las matemáticas se sigan viendo elegantes.
4. **Registro en MDX:** Finalmente inyectarlo de forma idéntica a `<Enunciado>`, exponiendo el parser JSX en el `MDXProvider` principal.
