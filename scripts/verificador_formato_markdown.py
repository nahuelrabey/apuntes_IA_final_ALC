import os
import re
from pathlib import Path

def find_line_number(content, index):
    return content.count('\n', 0, index) + 1

def check_markdown_files(directory):
    docs_path = Path(directory)
    if not docs_path.exists():
        print(f"Directorio {directory} no encontrado.")
        return

    errors_found = False

    for filepath in docs_path.rglob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_errors = []
        lines = content.split('\n')

        # 0. Enunciado al principio para teoria.md
        if filepath.name == 'teoria.md':
            content_start = "\n".join(lines[:15])
            if '> ' not in content_start and 'Ejercicio' not in content_start:
                file_errors.append(f"Regla de Estructura: Falta el enunciado (blockquote '> ') en las primeras 15 líneas.")

        # 1. Regresión de listas: Listas ordenadas (-) o numeradas (1.) deben tener un salto previo 
        
        in_list = False
        for i, line in enumerate(lines):
            # Regex que detecta un item de lista al principio, perdonando blockquotes (>) e indentación
            is_list_item = bool(re.match(r'^>*\s*(?:-|\d+\.)\s+', line))
            
            # Chequeamos la línea de apertura.
            if is_list_item and not in_list:
                in_list = True
                
                # Si no estamos en la primera línea.
                if i > 0:
                    prev_line = lines[i-1]
                    # La linea previa debería ser vacía, o solo el bloque (>)
                    is_blank = (prev_line.strip(' >\t\r') == '')
                    
                    if not is_blank:
                        file_errors.append(f"Línea {i+1}: El bloque de lista no está precedido por al menos un salto de línea en blanco.")
            
            # Fin de lista
            elif not is_list_item:
                if line.strip(' >\t\r') == '':
                    in_list = False
                elif not re.match(r'^>*\s+', line) and in_list: 
                    # Rompemos si hay texto pegado debajo
                    in_list = False

        # 2. Regresión de bloques matemáticos $$ ... $$
        # Buscamos de forma no-greedy para no agarrar de corrido 2 ecuaciones
        for match in re.finditer(r'\$\$.*?\$\$', content, flags=re.DOTALL):
            start = match.start()
            end = match.end()
            line_start = find_line_number(content, start)
            line_end = find_line_number(content, end)
            
            # Chequeamos la línea donde se abrió el $$
            start_line_text = lines[line_start - 1]
            # Si la línea tiene algo más que $$ (y blockquotes o espacios), entonces está sucio (el texto está pegado)
            if re.sub(r'[\s>\$]', '', start_line_text) != '':
                file_errors.append(f"Línea {line_start}: El bloque matemático de apertura '$$' no debe compartir línea con otro texto.")
            else:
                # Chequeamos la línea anterior para asegurar que esté "vacía"
                if line_start > 1:
                    prev_line_text = lines[line_start - 2]
                    is_blank = (prev_line_text.strip(' >\t\r') == '')
                    if not is_blank:
                        file_errors.append(f"Línea {line_start}: El bloque matemático de apertura '$$' no está precedido por al menos un salto de línea en blanco.")

            # Chequeamos la línea donde se cerró el $$
            end_line_text = lines[line_end - 1]
            if re.sub(r'[\s>\$]', '', end_line_text) != '':
                file_errors.append(f"Línea {line_end}: El bloque matemático de cierre '$$' no debe compartir línea con otro texto.")
            else:
                # Chequeamos la línea siguiente para asegurar que esté "vacía"
                if line_end < len(lines):
                    next_line_text = lines[line_end]
                    is_blank = (next_line_text.strip(' >\t\r') == '')
                    if not is_blank:
                         file_errors.append(f"Línea {line_end}: El bloque matemático de cierre '$$' no está seguido por al menos un salto de línea en blanco.")

        # Si acumulamos errores para este archivo, los revelamos a la consola
        if file_errors:
            errors_found = True
            print(f"\nArchivo: {filepath}")
            # Eliminamos duplicados locales de línea 
            unique_errors = []
            seen = set()
            for err in file_errors:
                if err not in seen:
                    unique_errors.append(err)
                    seen.add(err)
            
            # Ordenamos sintéticamente por números de línea
            unique_errors.sort(key=lambda x: int(re.search(r'Línea (\d+)', x).group(1)))
            for err in unique_errors:
                print(f"  - {err}")

    if not errors_found:
        print("✓ No se encontraron errores de formato (Listas y Bloques $$) en los archivos Markdown.")

if __name__ == '__main__':
    print(f"Ejecutando linter estricto de sintáxis Markdown en ./docs ...")
    check_markdown_files('docs')
