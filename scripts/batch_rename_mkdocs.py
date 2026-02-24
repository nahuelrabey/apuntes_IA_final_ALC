import os
import glob
import re
import argparse

def batch_rename_and_update_references(
    project_root: str, 
    target_folder: str, 
    regex_prefix: str = r'^0\d[a-z]*_'
) -> None:
    """
    Herramienta utilitaria para generadores de sitios estáticos (específicamente MkDocs).
    
    Esta función cumple dos propósitos fundamentales cuando se refactoriza la estructura de carpetas o nombres de archivo:
    1. Renombra masivamente archivos dentro de `target_folder`, removiendo un prefijo específico dictado por `regex_prefix`.
       Por defecto está configurado para remover numeraciones del estilo "01_", "02_", "03bis_", etc.
    2. Escanea recurrentemente todo el proyecto buscando archivos `.md` y `mkdocs.yml` para actualizar los enlaces
       internos (links rotos) que apuntaban a los nombres viejos, reemplazándolos con los nuevos nombres limpios.
       También repara las sentencias de inclusión de código de MkDocs (ej: --8<-- "archivo.py").

    Args:
        project_root (str): Ruta absoluta a la raíz del proyecto (donde reside mkdocs.yml).
        target_folder (str): Ruta absoluta a la carpeta cuyos archivos queremos purgar de prefijos.
        regex_prefix (str): Expresión regular que identifica el patrón a remover al principio de los nombres.
    """
    
    print(f"Iniciando escaneo en la raíz: {project_root}")
    print(f"Carpeta objetivo para renombrar: {target_folder}")
    
    # 1. Recolectar todos los archivos susceptibles de contener enlaces internos (Markdown, Py y Config)
    # Buscamos en todo el proyecto recursivamente.
    files_to_scan = glob.glob(os.path.join(project_root, '**', '*.md'), recursive=True) 
    files_to_scan += glob.glob(os.path.join(project_root, '**', '*.py'), recursive=True)
    
    mkdocs_config = os.path.join(project_root, 'mkdocs.yml')
    if os.path.exists(mkdocs_config):
        files_to_scan.append(mkdocs_config)

    # El nombre de la subcarpeta que usamos para buscar las URLs rotas (ej: "demostraciones/")
    folder_basename = os.path.basename(target_folder)
    
    # Expresión regular para encontrar las rutas en el formato: "carpeta/01_archivo.md" y transformarlo a "carpeta/archivo.md"
    # r'(carpeta/)0\d[a-z]*_'
    link_regex = re.compile(rf'({folder_basename}/){regex_prefix}')
    
    # mkdocs.yml tiene una sintaxis especial para el menú lateral (ej: "- 01. Título: carpeta/ruta.md")
    # Buscamos limpiar la numeración visual "01. " en el título del navbar también.
    mkdocs_title_regex = re.compile(rf'(\s*-\s*){regex_prefix.replace("^", "")}\.\s*([^:]+):\s*{folder_basename}/')

    # 2. Paso de Actualización de Enlaces e Inclusiones (Update References)
    for file_path in files_to_scan:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
                
            new_content = original_content
            
            # Si estamos operando sobre el árbol de navegación (mkdocs.yml)
            if file_path.endswith('mkdocs.yml'):
                # Limpia la parte visual del título de MkDocs. Ej: "- 01. Titulo:" -> "- Titulo:"
                new_content = mkdocs_title_regex.sub(rf'\1\2: {folder_basename}/', new_content)
            
            # Limpieza universal de las URLs internas en cualquier texto plano
            new_content = link_regex.sub(rf'\1', new_content)
            
            # Si hubo cambios de enlaces detectados, sobreescribimos el archivo
            if new_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'[REFERENCIAS] Actualizadas correctamente en: {os.path.relpath(file_path, project_root)}')
                
        except Exception as e:
            print(f"[ERROR] No se pudo procesar el archivo {file_path}: {e}")

    # 3. Paso de Renombrado Real en el Sistema de Archivos (File Renaming)
    if os.path.exists(target_folder):
        renombrado_count = 0
        for filename in os.listdir(target_folder):
            # Verificamos si el archivo arranca con el patrón numérico (ej: "01_") a reemplazar
            if re.match(regex_prefix, filename):
                new_filename = re.sub(regex_prefix, '', filename)
                old_filepath = os.path.join(target_folder, filename)
                new_filepath = os.path.join(target_folder, new_filename)
                
                os.rename(old_filepath, new_filepath)
                print(f'[RENOMBRADO] {filename} -> {new_filename}')
                renombrado_count += 1
                
        print(f"\nOperación finalizada. {renombrado_count} archivos renombrados físicamente.")
    else:
        print(f"\n[AVISO] La carpeta objetivo {target_folder} no existe, salto el paso de renombrado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatización de limpieza de numeraciones en MkDocs")
    parser.add_argument('--root', type=str, required=True, help='Ruta absoluta del proyecto (donde está mkdocs.yml)')
    parser.add_argument('--target', type=str, required=True, help='Ruta absoluta a la subcarpeta de los archivos a renombrar')
    parser.add_argument('--regex', type=str, default=r'^0\d[a-z]*_', help='La RegEx que matchea el prefijo a borrar')
    
    args = parser.parse_args()
    batch_rename_and_update_references(args.root, args.target, args.regex)
