import os
import glob
import re

def main():
    docs_dir = 'docs'
    md_files = glob.glob(os.path.join(docs_dir, '**', '*.md'), recursive=True)
    out = []
    out.append("--- INICIANDO VALIDACION ---")
    for fpath in md_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        violations = []
        
        # 1. Enunciado al principio para teoria.md
        if 'teoria.md' in fpath:
            content_start = "".join(lines[:15])
            if '> ' not in content_start and 'Ejercicio' not in content_start:
                violations.append("Falta el enunciado (blockquote '> ') al principio del archivo")

        # 2. Espacios alrededor de $$ y listas desordenadas
        in_list = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Check $$
            if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 2:
                # Math block in a single line
                pass
            elif stripped == '$$':
                # Block start or end
                pass

            # Check unordered lists "- "
            if line.startswith('- ') or line.startswith('> - '):
                # Ensure previous line is empty (blank) or also a list item?
                # The rule says: blank line before starting list, AND blank line between items.
                # So if this is a list item, the PREVIOUS line MUST be empty.
                if i > 0:
                    prev_line = lines[i-1].strip()
                    if prev_line != '' and prev_line != '>' and not prev_line.startswith('<!--'):
                        violations.append(f"Linea {i+1}: Falta salto de línea antes del ítem de lista ('{stripped[:20]}...')")
                        
            # Check $$ blocks (simple heuristic: if a line is just $$, ensure prev and next are empty if outside blockquote)
            if stripped == '$$':
                if i > 0:
                    prev_line = lines[i-1].strip()
                    if prev_line != '' and prev_line != '>':
                        violations.append(f"Linea {i+1}: Falta salto de línea antes de bloque $$")
                if i < len(lines) - 1:
                    next_line = lines[i+1].strip()
                    if next_line != '' and next_line != '>':
                        violations.append(f"Linea {i+1}: Falta salto de línea después de bloque $$")
                        
        if violations:
            out.append(f"\\n[!] VIOLACIONES EN: {fpath}")
            for v in violations:
                out.append(f"  - {v}")
                
    with open('reporte_formato.log', 'w', encoding='utf-8') as f:
        f.write('\\n'.join(out))
        print("Reporte generado en reporte_formato.log")

if __name__ == '__main__':
    main()
