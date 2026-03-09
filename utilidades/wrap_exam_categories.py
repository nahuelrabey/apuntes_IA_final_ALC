"""
Descripción:
Genera de forma procedural los archivos `_category_.json` para aplanar la visualización de los exámenes en la barra lateral.
"""

import os
import json
from pathlib import Path

docs_dir = Path("docs/ALC/finales")
count = 0

def format_title(folder_name):
    # folder_name e.g. "01_svd" -> "Ejercicio 01: SVD"
    # "02_semejanza_matrices" -> "Ejercicio 02: Semejanza Matrices"
    parts = folder_name.split('_', 1)
    if len(parts) == 2 and parts[0].isdigit():
        num = parts[0]
        # uppercase specific math acronyms 
        rest = parts[1].replace('_', ' ').title()
        rest = rest.replace('Svd', 'SVD').replace('Lu', 'LU').replace('Sor', 'SOR')
        return f"Ejercicio {num}: {rest}"
    return folder_name.replace('_', ' ').title()

# We need to iterate over all exam folders (e.g., Examen_2025_02_24)
for exam_folder in docs_dir.iterdir():
    if not exam_folder.is_dir() or not exam_folder.name.startswith("Examen_"):
        continue
        
    # Inside each exam, we have folders like 01_svd
    for exercise_folder in exam_folder.iterdir():
        if not exercise_folder.is_dir() or not exercise_folder.name[0].isdigit():
            continue
            
        # Create _category_.json to flatten the sidebar and link to theory.md
        cat_file = exercise_folder / "_category_.json"
        
        # Link to the document 'teoria'. In Docusaurus, a category can link to a document
        # by providing id. The id is relative or absolute?
        # A doc link: id = "ALC/finales/Examen_2025_02_24/01_semejanza_matrices/teoria"
        
        # Docusaurus doc ID is the path from `docs/` without extension
        doc_path = exercise_folder / "teoria.md"
        if not doc_path.exists():
            continue
            
        # calculate doc_id
        # docs_dir is relative to CWD. The doc ID starts from the root of docs/
        # Very important: Docusaurus strips number prefixes from folders!
        # example folder: "01_semejanza_matrices" -> doc id uses "semejanza_matrices"
        rel_path_parts = doc_path.relative_to("docs").parts
        cleaned_parts = []
        for p in rel_path_parts:
            # strip the regex ^[0-9]+_
            import re
            p_clean = re.sub(r'^[0-9]+_', '', p)
            cleaned_parts.append(p_clean)
            
        doc_id = "/".join(cleaned_parts)
        # remove .md
        doc_id = doc_id[:-3]
        
        title = format_title(exercise_folder.name)
        
        cat_data = {
            "label": title,
            "link": {
                "type": "doc",
                "id": doc_id
            }
        }
        
        with open(cat_file, "w", encoding="utf-8") as f:
            json.dump(cat_data, f, indent=4, ensure_ascii=False)
            
        count += 1

print(f"Created {count} category files to flatten the exam exercises.")
