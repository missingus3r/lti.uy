import asyncio
from pyppeteer import launch
from time import sleep

async def run_script(user, passwd):
    async def main():
        try:
            browser = await launch(handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
        except Exception as error:
            print("An exception occurred : ",error )
            
        page = await browser.newPage()
        await page.goto("https://ev1.utec.edu.uy/moodle/login/index.php")
        await page.type('#username', user)
        await page.type('#password', passwd)
        await page.keyboard.press('Enter')
        await page.waitForNavigation()
        sleep(1)

        alerts = await page.querySelector("#loggedin-user")
        await browser.close()
        return "OK"

    try:
        result = await main()
        return result
    except:
        return "ERROR"