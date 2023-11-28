import os

# Ruta del directorio que contiene los archivos JavaScript y minificados
directorio_js = 'login/static/js/'

# Recorrer todos los archivos en el directorio
#Excluidos los del template
for archivo in os.listdir(directorio_js):
    if archivo.endswith('.min.js') and archivo not in ["sb-admin-2.min.js", "sb-admin-2.js"]:
        ruta_completa = os.path.join(directorio_js, archivo)
        os.remove(ruta_completa)

print("Archivos .min.js eliminados con éxito en el mismo directorio, excluyendo sb-admin-2.min.js y sb-admin-2.js.")
