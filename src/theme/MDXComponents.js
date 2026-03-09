import React from 'react';
// Import the original mapper
import MDXComponents from '@theme-original/MDXComponents';
import { Nota, Advertencia } from '@site/src/components/Admonitions';
import { Ejercicio, Demostracion } from '@site/src/components/Estructuras';

export default {
    // Re-use the default mapping
    ...MDXComponents,
    // Map the custom tags to our components
    Nota,
    Advertencia,
    Ejercicio,
    Demostracion,
};
