from .base import FunctionalTest
from unittest import skip

@skip('test when initially setting the project up')
class TestDjangoAndSeleniumWorking(FunctionalTest):

    def test_can_launch_development_server_of_django_app(self):

        self.browser.get(self.live_server_url)
        assert 'Django' in self.browser.title
