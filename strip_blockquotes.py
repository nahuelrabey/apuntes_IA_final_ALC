import os
import re
from pathlib import Path

docs_dir = Path("docs")
count = 0

def fix_blockquotes(content):
    lines = content.split('\n')
    in_code_block = False
    new_lines = []
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        if not in_code_block:
            # Strip blockquote character if it exists at the start of the line
            line = re.sub(r'^[ \t]*>[ \t]?', '', line)
            
        new_lines.append(line)
        
    return '\n'.join(new_lines)

for md_file in docs_dir.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
        
    updated = fix_blockquotes(content)
    
    if updated != content:
        md_file.write_text(updated, encoding="utf-8")
        count += 1

print(f"Stripped markdown blockquotes from {count} files")
