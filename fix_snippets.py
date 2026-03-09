import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0
comment_pattern = re.compile(r'^<!--\s+--8<--\s+"([^"]+)"\s+-->')

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    lines = content.split('\n')
    new_lines = []
    changed = False
    
    for line in lines:
        match = comment_pattern.match(line.strip())
        if match:
            target_path = match.group(1).replace('\\', '/')
            # Fix path
            if target_path.startswith("docs/demostraciones"):
                target_path = target_path.replace("docs/demostraciones", "docs/ALC/demostraciones")
            elif target_path.startswith("demostraciones/"):
                target_path = target_path.replace("demostraciones/", "docs/ALC/demostraciones/")
            elif target_path.startswith("docs/Examen_"):
                target_path = target_path.replace("docs/Examen_", "docs/ALC/finales/Examen_")
            elif target_path.startswith("../demostraciones"):
                target_path = "docs/ALC/demostraciones/" + target_path.split("/")[-1]
            elif "factorizacion_lu" in target_path:
                target_path = "docs/ALC/finales/Examen_2026_02_25/04_factorizacion_lu/verificacion.py"
            
            full_path = Path(target_path).resolve()
            
            if not full_path.exists():
                print(f"Warning still missing: {full_path} in {md_file}")
                new_lines.append(line)
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
        
print(f"Inlined previously missed snippets in {count} files")
