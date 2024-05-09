import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from utils.browser import Driver  # Importe a fábrica de navegador


class RecipeHomePageFunctionalTest(StaticLiveServerTestCase):
    def sleep(self, seconds=2):
        time.sleep(seconds)

    def test_the_test(self):
        # Crie uma instância de navegador usando sua fábrica de navegador
        browser = Driver().browser
        browser.get(self.live_server_url)
        self.sleep(6)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhuma receita encontrada aqui', body.text)
        browser.quit()
