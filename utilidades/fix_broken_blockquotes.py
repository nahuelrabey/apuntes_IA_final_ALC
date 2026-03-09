"""
Descripción:
Restaura blockquotes matemáticos que habían sido rotos por conversiones previas (ej. `> $$`).
"""

import os
from pathlib import Path

docs_dir = Path("docs")
count = 0

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    updated = content.replace(">\n\n$$", "> $$")
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1

print(f"Restored broken blockquote math blocks in {count} files")
