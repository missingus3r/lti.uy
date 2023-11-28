import os
from bs4 import BeautifulSoup
from datetime import datetime

# Directorios de entrada y salida
input_dir = 'login/templates/login'
output_dir = 'login/static/js'

# Asegurémonos de que la carpeta de salida exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Itera a través de los archivos HTML en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith('.html'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.js')

        with open(input_path, 'r', encoding='utf-8') as file:
            html = file.read()

        # Parsea el HTML con Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Encuentra todos los elementos <script> en el HTML
        scripts = soup.find_all('script')

        # Crea un archivo JS en el directorio de salida
        with open(output_path, 'w', encoding='utf-8') as js_file:
            # Itera a través de los scripts y escribe su contenido en el archivo JS
            for script in scripts:
                js_content = script.get_text()
                
                # Agrega una línea comentada con la fecha de creación al principio del script
                creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                js_file.write(f'// Creado el {creation_date}\n')
                js_file.write(js_content)

        print(f"Scripts extraídos de {filename} y guardados en {os.path.basename(output_path)}")
