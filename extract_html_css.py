import os
from bs4 import BeautifulSoup
from datetime import datetime

# Directorios de entrada y salida
input_dir = 'login/templates/login'
output_dir = 'login/static/css'

# Asegurémonos de que la carpeta de salida exista
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Itera a través de los archivos HTML en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith('.html'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.css')

        with open(input_path, 'r', encoding='utf-8') as file:
            html = file.read()

        # Parsea el HTML con Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Encuentra todos los elementos <style> en el HTML
        styles = soup.find_all('style')

        # Crea un archivo CSS en el directorio de salida
        with open(output_path, 'w', encoding='utf-8') as css_file:
            # Itera a través de los estilos y escribe su contenido en el archivo CSS
            for style in styles:
                css_content = style.get_text()
                
                # Agrega una línea comentada con la fecha de creación al principio del archivo CSS
                creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                css_file.write(f'/* Creado el {creation_date} */\n')
                css_file.write(css_content)

        print(f"Estilos CSS extraídos de {filename} y guardados en {os.path.basename(output_path)}")
