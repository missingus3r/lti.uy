import asyncio
from pyppeteer import launch
import pandas as pd
import sys
import os
from time import sleep
import json

ruta_actual = os.path.abspath("C:\\Users\\Br1\\desktop>")
os.system('cls')

# Creds
user = sys.argv[1]
passwd = sys.argv[2]

async def main():
    # HEADLESS MODE
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto("https://autenticacion.utec.edu.uy/")
    print("Entrando a portal academico...", flush=True)
    sys.stdout.flush()

    await page.type('#username', user)
    print("usuario ingresado", flush=True)
    sys.stdout.flush()

    await page.type('#password', passwd)
    print("password ingresada", flush=True)
    sys.stdout.flush()
    await page.keyboard.press('Enter')

    print("Redireccionando...", flush=True)
    sys.stdout.flush()
    await page.waitForNavigation()

    await page.goto("https://portaluxxi.utec.edu.uy/ServiciosApp/faces/inicioServicios")
    sleep(1)
    print("Entrando en Información Académica -> Progreso académico", flush=True)
    sys.stdout.flush()
    await page.waitForXPath("//span[contains(text(),'Informaci')]")
    info_academica = await page.Jx("//span[contains(text(),'Informaci')]")
    await info_academica[0].click()
    sleep(1)
    print("Obteniendo escolaridad...", flush=True)
    sys.stdout.flush()
    await page.waitForXPath("//a[contains(text(),'Progreso')]")
    link = await page.Jx("//a[contains(text(),'Progreso')]")
    await link[0].click()
    sleep(3)
    await page.waitForXPath("//table[@role='presentation']")
    sys.stdout.flush()
    rows = await page.Jx("//tr[@role='row']")
    data = [] # BUSCAR COMO AJUSTAR el jsonValue de las rows debajo para que cada elemento este separado y no todo junto para luego armar el df

    for i in range(len(rows)):
        property_handle = await rows[i].getProperty('textContent')
        inner_text = await property_handle.jsonValue()
        #json_obj = json.loads(inner_text)
        #claves = list(json_obj.keys())
        #sub_data = json_obj[claves[0]]
        print(inner_text, flush=True)
        sys.stdout.flush()

    await browser.close()

    print("Limpiando datos y armando dataframe...", flush=True)
    sys.stdout.flush()
    # Quito los saltos de linea de la columna de Notas
    cell = cell.replace('\n', ' ').strip()

    await browser.close()
    # try:
    #     # Crea una lista con los datos
    #     datos_interesantes = cell.split(' ')[2:]
    #     encabezados = ['Materia', 'Créditos', 'Tipo', 'Año y Semestre', 'Nota/Superacion/Revalida']

    #     # Crea un dataframe de Pandas con los datos y los encabezados
    #     df = pd.DataFrame([datos_interesantes[i:i+5] for i in range(0, len(datos_interesantes), 5)], columns=encabezados)

    #     # Configuración para mostrar todas las columnas y filas del DataFrame
    #     pd.set_option('display.max_columns', None)
    #     pd.set_option('display.max_rows', None)
    #     #Imprime el dataframe
    #     print(df, flush=True)
    #     sys.stdout.flush()
    #     print("Dataframe armado con éxito", flush=True)
    #     sys.stdout.flush()
    # except:
    #     print("Error en el formateo de datos. Revisar headers.", flush=True)
    #     sys.stdout.flush()

asyncio.get_event_loop().run_until_complete(main())
