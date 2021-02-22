from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.live_server_url = 'http://localhost:8000'

    def tearDown(self) -> None:
        self.browser.quit()
        super().tearDown()



