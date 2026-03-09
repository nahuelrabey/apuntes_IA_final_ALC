import React from 'react';
// Import the original mapper
import MDXComponents from '@theme-original/MDXComponents';
import { Nota, Advertencia, Info } from '@site/src/components/Admonitions';
import { Ejercicio, Demostracion, Enunciado } from '@site/src/components/Estructuras';

export default {
    ...MDXComponents,
    Nota,
    Advertencia,
    Info,
    Ejercicio,
    Demostracion,
    Enunciado,
};
