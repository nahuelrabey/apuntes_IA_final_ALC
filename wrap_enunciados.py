import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0

# We are looking for something like:
# **Ejercicio X**
# 
# (content until horizontal rule `---` or end of file or a new `##` header?)
# Generally, an exam structure is:
# ## 01 Semejanza Matrices
# 
# **Ejercicio 1**
# content...
# ---

# We want to replace it with:
# <Enunciado titulo="Ejercicio X">
# content...
# </Enunciado>

def process_file(content):
    # This might be tricky because we stripped the blockquote `>` previously.
    # Looking at enunciado.md:
    # **Ejercicio 1**
    #
    # Se dice que A...
    # ...
    # --- (or ##)
    
    # Let's target the exact string pattern.
    # Match: \*\*Ejercicio\s+([^>]*?)\*\*  (non-greedy until the end, but we need to match blocks)
    # Actually, a safer approach is to do it line-by-line or with a specific split.
    
    # Split by `**Ejercicio `
    if "**Ejercicio " not in content:
        return content
        
    parts = content.split('**Ejercicio ')
    new_content = parts[0]
    
    for part in parts[1:]:
        # '1**\n\nSe dice que...'
        # Extract the title/number
        end_title_idx = part.find('**')
        if end_title_idx == -1:
            new_content += '**Ejercicio ' + part
            continue
            
        numero = part[:end_title_idx]
        rest = part[end_title_idx+2:].lstrip()
        
        # Where does the enunciado end? It ends before the next `---` or `##` or end of file
        # In files like `01_semejanza_matrices/teoria.md`, there's usually a `---` after the statement.
        # Let's find the first `\n---` or `\n## `
        
        end_idx_1 = rest.find('\n---')
        end_idx_2 = rest.find('\n## ')
        
        # If both not found, it's the EOF
        if end_idx_1 == -1 and end_idx_2 == -1:
            end_idx = len(rest)
        elif end_idx_1 == -1:
            end_idx = end_idx_2
        elif end_idx_2 == -1:
            end_idx = end_idx_1
        else:
            end_idx = min(end_idx_1, end_idx_2)
            
        enunciado_body = rest[:end_idx].strip()
        remainder = rest[end_idx:]
        
        new_content += f'<Enunciado titulo="Ejercicio {numero}">\n\n{enunciado_body}\n\n</Enunciado>\n\n' + remainder
        
    return new_content

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    updated = process_file(content)
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1

print(f"Wrapped enunciados in {count} files")
