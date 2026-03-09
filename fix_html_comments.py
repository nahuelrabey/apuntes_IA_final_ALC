import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0

# We use re.DOTALL to match multiline comments
comment_pattern = re.compile(r'<!--(.*?)-->', re.DOTALL)

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    updated = comment_pattern.sub(r'{/*\1*/}', content)
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1
        
print(f"Converted HTML comments to JSX comments in {count} files")
