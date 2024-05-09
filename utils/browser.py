from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@dataclass()
class Driver:

    options = Options()

    # options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(browser, 10)


driver = Driver().browser
wait = Driver().wait

url = 'https://www.google.com.br/'
driver.get(url)

wait
