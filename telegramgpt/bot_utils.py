import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://liaobots.com/en'


async def generate_token() -> str:

    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    print("Starting driver...")
    driver = await asyncio.to_thread(webdriver.Chrome, service = service, options = options, keep_alive = False)
    driver.get(url)

    print("Waiting for token to generate...")
    await asyncio.sleep(5)

    data = await asyncio.to_thread(driver.execute_script, "return window.localStorage.getItem('authCode')")
    driver.close()
    return data