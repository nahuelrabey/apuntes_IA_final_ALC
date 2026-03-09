import fs from 'fs';
import { compile } from '@mdx-js/mdx';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

async function testFile(filePath) {
    try {
        const mdxContent = fs.readFileSync(filePath, 'utf8');
        await compile(mdxContent, {
            remarkPlugins: [remarkMath],
            rehypePlugins: [rehypeKatex]
        });
        console.log(`${filePath}: SUCCESS`);
    } catch (err) {
        console.error(`ERROR in ${filePath}:`);
        console.error(err.message);
        if (err.position) {
            console.error(`At line ${err.position.start.line}, column ${err.position.start.column}`);
        } else {
            console.error(err);
        }
    }
}

testFile('docs/ALC/demostraciones/numero_condicion_svd.md');
testFile('docs/ALC/demostraciones/cambio_base.md');
testFile('docs/ALC/finales/Examen_2026_02_25/04_factorizacion_lu/teoria.md');
