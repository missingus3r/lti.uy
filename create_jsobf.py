import os
import subprocess

# Ruta del directorio que contiene los archivos JavaScript a procesar
directorio_js = 'login/static/js/'

# Recorrer todos los archivos JavaScript en el directorio
for root, dirs, files in os.walk(directorio_js):
    for archivo in files:
        if archivo.endswith('.js'):
            ruta_completa = os.path.join(root, archivo)
            archivo_minificado = os.path.splitext(ruta_completa)[0] + '.min.js'

            # Configuración para Javascript-obfuscator
            configuracion_obfuscator = f"""
            const JavaScriptObfuscator = require('javascript-obfuscator');
            const fs = require('fs');

            const code = fs.readFileSync("{ruta_completa}", 'utf-8');

            const obfuscationResult = JavaScriptObfuscator.obfuscate(code, {{
                compact: true,
                controlFlowFlattening: true,
                controlFlowFlatteningThreshold: 1,
                selfDefending: true
            }});

            const archivoMinificado = "{archivo_minificado}";
            fs.writeFileSync(archivoMinificado, obfuscationResult.getObfuscatedCode(), 'utf-8');
            """

            # Escribir la configuración en un archivo temporal
            with open('config_obfuscator.js', 'w') as archivo_config:
                archivo_config.write(configuracion_obfuscator)

            # Ejecutar el ofuscador en el archivo JavaScript
            comando_obfuscador = 'node config_obfuscator.js'
            subprocess.run(comando_obfuscador, shell=True)

            # Eliminar el archivo temporal de configuración
            os.remove('config_obfuscator.js')

print("Archivos JavaScript minimizados y ofuscados con éxito en la misma carpeta de origen utilizando Javascript-obfuscator.")
