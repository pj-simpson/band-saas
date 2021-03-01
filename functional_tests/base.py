from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver import DesiredCapabilities


class FunctionalTest(StaticLiveServerTestCase):
    host= 'django'

    def setUp(self) -> None:
        self.browser = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self) -> None:
        self.browser.quit()
        super().tearDown()



