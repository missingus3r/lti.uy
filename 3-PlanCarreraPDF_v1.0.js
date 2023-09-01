const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  try {
    await page.goto('https://utec.edu.uy/es/educacion/carrera/licenciatura-en-tecnologias-de-la-informacion/');

    // Tab plan de estudios
    const buttonIdPlan = 'plan-tab'; 
    await page.click(`#${buttonIdPlan}`);

    // Esperar y hacer clic en el botón "Ver Plan"
    await page.waitForSelector('#plan > div > p.m-0 > a'); 
    await page.click('#plan > div > p.m-0 > a');

    // Esperar a que se cargue el nuevo contenido
    await page.waitForSelector('selector-del-nuevo-contenido'); // Cambia por el selector que corresponda

    const currentUrl = page.url();
    console.log(`URL actual: ${currentUrl}`);
  } catch (error) {
    console.error("Error:", error);
  } finally {
    await browser.close();
  }
})();
