"""
Descripción:
Escanea el código para migrar los bloques desplegables de MkDocs (`??? info`) al nuevo componente React `<Info>`.
"""

import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0

def process_info_blocks(content):
    # Regex to match `??? info "titulo"` followed by indented lines
    # The title might not have quotes: `??? info "¿Por qué...?"`
    
    # We can match `??? info "(.*?)"\n` then all lines that start with 4 spaces or more, or empty lines.
    pattern = re.compile(r'^\?\?\?\s+info\s+"([^"]+)"\n((?:(?: {4}.*(?:\n|$))|(?:\s*\n))*)(?=(?:^[^\s]|\Z))', re.MULTILINE)
    
    def replacer(match):
        title = match.group(1)
        body = match.group(2)
        
        # Remove the 4-space indentation from the body
        clean_body_lines = []
        for line in body.split('\n'):
            if line.startswith('    '):
                clean_body_lines.append(line[4:])
            else:
                clean_body_lines.append(line)
                
        clean_body = '\n'.join(clean_body_lines).strip()
        
        return f'<Info titulo="{title}">\n\n{clean_body}\n\n</Info>\n\n'
        
    updated = pattern.sub(replacer, content)
    return updated

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    updated = process_info_blocks(content)
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1

print(f"Refactored ??? info blocks in {count} files")
