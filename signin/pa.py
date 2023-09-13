import asyncio
from pyppeteer import launch
import sys
from time import sleep
import json

async def main():
    user = 'mariano.collazo'
    passwd = 'poiuyt123Q.'
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.goto("https://autenticacion.utec.edu.uy/")
    print("1-Entrando a portal academico...", flush=True)
    sys.stdout.flush()

    await page.type('#username', user)
    print("1-usuario ingresado", flush=True)
    sys.stdout.flush()

    await page.type('#password', passwd)
    print("1-password ingresada", flush=True)
    sys.stdout.flush()
    await page.keyboard.press('Enter')

    print("1-Redireccionando...", flush=True)
    sys.stdout.flush()
    await page.waitForNavigation()
    await page.goto("https://portaluxxi.utec.edu.uy/ServiciosApp/faces/inicioServicios")
    sleep(1)
    
    print("1-Entrando en Información Académica -> Progreso académico", flush=True)
    sys.stdout.flush()
    await page.waitForXPath("//span[contains(text(),'Informaci')]")
    info_academica = await page.Jx("//span[contains(text(),'Informaci')]")
    await info_academica[0].click()
    sleep(1)
        
    print("1-Obteniendo escolaridad...", flush=True)
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
        data.append(inner_text)
        #print("1-"+inner_text, flush=True)
        
        sys.stdout.flush()
    
    print(data, flush=True)

    await browser.close()
    #print('DESPUES DE CLOSE BROWASE')
    #return data
    # print("1-Limpiando datos y armando dataframe...", flush=True)
    # sys.stdout.flush()
    # # Quito los saltos de linea de la columna de Notas
    # cell = cell.replace('\n', ' ').strip()

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
    #     print("1-Dataframe armado con éxito", flush=True)
    #     sys.stdout.flush()
    # except:
    #     print("1-Error en el formateo de datos. Revisar headers.", flush=True)
    #     sys.stdout.flush()
#print('DESKKKKPUES DE CLOSE BROWASE')

asyncio.get_event_loop().run_until_complete(main())
