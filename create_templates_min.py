import os
from htmlmin import minify

# Ruta del directorio que contiene los archivos HTML a minificar
source_directory = 'login/templates/login'
# Ruta del directorio de destino para los archivos minificados
destination_directory = 'login/templates-min'

# Si el directorio de destino no existe, créalo
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Recorre todos los archivos HTML en el directorio fuente
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)

            # Lee el contenido del archivo HTML
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Minifica el contenido HTML
            minified_content = minify(html_content, remove_comments=True, remove_empty_space=True)

            # Crea la ruta para el archivo de destino
            destination_path = os.path.join(destination_directory, file)

            # Sobrescribe el archivo con el contenido minificado en el directorio de destino
            with open(destination_path, 'w', encoding='utf-8') as f:
                f.write(minified_content)

print("Archivos HTML minificados y guardados en el directorio de destino 'login/templates-min'.")
