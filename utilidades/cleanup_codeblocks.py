"""
Descripción:
Limpia y corrige bloques de código mal formados en Markdown.
"""

import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    # Pattern to match ```python\n```python\n and replace with ```python\n
    # and match ```\n```\n and replace with ```\n
    
    updated = content
    # Some files might have ```python\n```python
    updated = re.sub(r'```([a-z]*)\s*\n```([a-z]+)\s*\n', r'```\2\n', updated)
    updated = re.sub(r'```\s*\n```\s*\n', r'```\n', updated)
    
    # Also handle the trailing ```\n``` issue which might not have \n between them if end of file
    updated = re.sub(r'```\s*\n\s*```(\s|$)', r'```\1', updated)
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1
        
print(f"Cleaned up nested codeblocks in {count} files")
