from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
from discogs.models import Release

class TestDiscographyPage(FunctionalTest):
    fixtures = ['fixtures/releases.json']

    def test_can_navigate_to_the_discogs_page_and_see_list_of_releases(self):

        self.browser.get(self.live_server_url)

        # The user find the discography nav link and clicks

        self.browser.find_element_by_link_text('Discog').click()

        # A page is loaded up which looks to be a discography

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Discography"



        print(Release.objects.latest('release_date'))

        # The user can clearly see that there is a table with content

        discog_table = self.browser.find_element_by_id('discog_table')
        rows = discog_table.find_elements_by_tag_name('td')
        self.assertIn('Blah',[row.text for row in rows])