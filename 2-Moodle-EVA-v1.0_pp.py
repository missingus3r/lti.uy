import asyncio
from pyppeteer import launch
import sys

# Creds
user = sys.argv[1]
passwd = sys.argv[2]

async def main():
    # Launch the browser
    browser = await launch(headless=True)

    # Open a new page
    page = await browser.newPage()
    await page.goto("https://ev1.utec.edu.uy/moodle/login/index.php")
    print("Entrando a Moodle...", flush=True)
    sys.stdout.flush()  # Limpiar el buffer de salida

    # Input username and password and login
    await page.type('#username', user)
    print("usuario ingresado", flush=True)
    sys.stdout.flush()
    await page.type('#password', passwd)
    await page.keyboard.press('Enter')
    await page.waitForNavigation()

    # Check alerts
    alerts = await page.querySelector("#loggedin-user")
    alerts2 = await alerts.querySelectorAll(".popover-region.collapsed.popover-region-notifications")
    if len(alerts2) == 0:
        alerts3 = await alerts2[0].querySelector(".count-container")
        count_text = await page.evaluate('(element) => element.textContent', alerts3)
        print(count_text, flush=True)
        sys.stdout.flush()
    else :
        print("No hay mensajes.", flush=True)
        sys.stdout.flush()
    
    # Go to profile
    await page.goto("https://ev1.utec.edu.uy/moodle/user/profile.php?id=2847")
    await page.waitForSelector('a[title="Ver más"]')
    await page.click('a[title="Ver más"]')

    # Get matriculas
    await page.waitForSelector('.contentnode')
    matriculas = await page.querySelectorAll('.contentnode li')
    cell_content = [await page.evaluate('(element) => element.textContent', matricula) for matricula in matriculas]
    
    for i in range(len(cell_content)):
        print(cell_content[i], flush=True)
        sys.stdout.flush()
    await browser.close()
    print("EndOfScript", flush=True)
    sys.stdout.flush()

asyncio.get_event_loop().run_until_complete(main())


# user = "Bruno.Silveira"
# passwd = "ibp7zve6.-"