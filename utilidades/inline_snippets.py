"""
Descripción:
Reemplaza las referencias a snippets externos inyectando el código directamente en los archivos MDX.
"""

import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0
snippet_pattern = re.compile(r'^--8<--\s+"([^"]+)"')

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    lines = content.split('\n')
    new_lines = []
    changed = False
    
    for line in lines:
        match = snippet_pattern.match(line.strip())
        if match:
            # We found a snippet include
            target_path = match.group(1)
            # The path in mkdocs snippets is relative to the docs directory or the file itself?
            # Usually it's relative to docs/ if it starts with "docs/" or the repo root.
            # Example: "docs/demostraciones/verificacion_cambio_base.py"
            # Since the script runs in the repo root
            full_path = Path(target_path)
            if not full_path.exists():
                print(f"Warning: Snippet {full_path} not found for {md_file}")
                new_lines.append(f"<!-- {line} -->")
                changed = True
                continue
                
            snippet_content = full_path.read_text(encoding="utf-8")
            ext = full_path.suffix.lstrip('.')
            if ext == 'py':
                ext = 'python'
            
            new_lines.append(f"```{ext}")
            new_lines.append(snippet_content)
            new_lines.append("```")
            changed = True
        else:
            new_lines.append(line)
            
    if changed:
        md_file.write_text('\n'.join(new_lines), encoding="utf-8")
        count += 1
        
print(f"Inlined snippets in {count} files")
