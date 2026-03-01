import os
import re
from pathlib import Path


def fix_math_blocks(content):
    """
    Corrige el formato de bloques matemáticos ($$...$$) en contenido Markdown.

    Reglas aplicadas (según estructuracion_markdown.md):
    - Los delimitadores $$ deben estar solos en su propia línea.
    - Debe haber una línea vacía antes del $$ de apertura y después del $$ de cierre.
    - Si el bloque está dentro de un blockquote (> ), el separador vacío es ">" solo.
    """
    # 1. Proteger bloques de código para no tocarlos
    code_blocks = []

    def code_replacer(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

    content = re.sub(r'```.*?```', code_replacer, content, flags=re.DOTALL)
    content = re.sub(r'`[^`]*`', code_replacer, content)

    # 2. Procesamiento línea por línea
    lines = content.split('\n')
    result = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detectar el prefijo de blockquote (ej: "> " o "")
        bq_match = re.match(r'^((?:>\s*)*>)(\s*)(.*)', line)
        if bq_match:
            bq_prefix = bq_match.group(1)  # ">" o "> >" etc
            rest = bq_match.group(3)
        else:
            bq_prefix = ""
            rest = line

        # ¿Esta línea contiene $$?
        if '$$' not in rest:
            result.append(line)
            i += 1
            continue

        # Separar la línea por $$
        segments = rest.split('$$')

        # Si hay exactamente 1 $$ (2 segmentos): apertura o cierre suelto
        # Si hay exactamente 2 $$ (3 segmentos): bloque inline completo en una línea
        # Reconstruimos las partes expandidas
        expanded = []
        for j, seg in enumerate(segments):
            text = seg.strip()
            if text:
                if bq_prefix:
                    expanded.append(f"{bq_prefix} {text}")
                else:
                    expanded.append(text)
            # Agregar $$ después de cada segmento excepto el último
            if j < len(segments) - 1:
                if bq_prefix:
                    expanded.append(f"{bq_prefix} $$")
                else:
                    expanded.append("$$")

        # Ahora insertamos separadores vacíos donde haga falta
        for item in expanded:
            stripped_item = item.lstrip('> \t')

            if stripped_item == '$$':
                # Determinar si es apertura o cierre
                # Contamos cuántos $$ ya hay en result
                count_dd = sum(1 for r in result if r.lstrip('> \t') == '$$')
                is_opening = (count_dd % 2 == 0)

                if is_opening:
                    # Necesitamos una línea vacía antes
                    if result and result[-1].lstrip('> \t') != '':
                        # Insertar línea vacía (respetando blockquote)
                        if bq_prefix:
                            result.append(bq_prefix)
                        else:
                            result.append('')
                result.append(item)

                if not is_opening:
                    # Es cierre: necesitamos una línea vacía después
                    # La añadimos ahora; si la siguiente línea es texto, quedará bien
                    if bq_prefix:
                        result.append(bq_prefix)
                    else:
                        result.append('')
            else:
                result.append(item)

        i += 1

    content = '\n'.join(result)

    # 3. Limpiar líneas vacías consecutivas excesivas (máximo 1 línea vacía = 2 \n)
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Limpiar blockquotes vacíos consecutivos (> \n> -> uno solo)
    content = re.sub(r'(>\n)(>\n)+', r'\1', content)

    # 4. Restaurar bloques de código
    for i, block in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{i}__", block)

    # 5. Limpiar trailing whitespace por línea
    content = '\n'.join(line.rstrip() for line in content.split('\n'))

    return content.strip() + '\n'


def fix_list_blocks(content):
    """
    Corrige el formato de bloques de lista en contenido Markdown.

    Regla aplicada (según estructuracion_markdown.md):
    - El primer ítem de un bloque de lista (- o 1.) debe estar precedido
      por al menos una línea vacía. Si está dentro de un blockquote (>),
      el separador vacío es ">" solo.
    """
    lines = content.split('\n')
    result = []
    in_list = False

    for i, line in enumerate(lines):
        is_list_item = bool(re.match(r'^>*\s*(?:-|\d+\.)\s+', line))

        if is_list_item and not in_list:
            in_list = True
            if i > 0:
                prev_line = lines[i - 1]
                is_blank = (prev_line.strip(' >\t\r') == '')
                if not is_blank:
                    # Detectar prefijo blockquote de la línea actual
                    bq_match = re.match(r'^((?:>\s*)*>)', line)
                    if bq_match:
                        result.append(bq_match.group(1))
                    else:
                        result.append('')
        elif not is_list_item:
            if line.strip(' >\t\r') == '':
                in_list = False
            elif not re.match(r'^>*\s+', line) and in_list:
                in_list = False

        result.append(line)

    return '\n'.join(result)


def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Error leyendo {filepath}: {e}")
        return False

    new_content = fix_math_blocks(original_content)
    new_content = fix_list_blocks(new_content)

    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    docs_dir = Path('docs')
    if not docs_dir.exists():
        print(f"No se encontró el directorio de docs en {docs_dir.absolute()}")
        return

    modificados = 0
    for md_file in docs_dir.rglob('*.md'):
        if process_file(md_file):
            modificados += 1
            print(f"-> Corregido: {md_file}")

    print(f"\nProceso completado. Se normalizaron {modificados} archivos.")


if __name__ == '__main__':
    main()
