from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
from discogs.models import Release

class TestDiscographyPage(FunctionalTest):

    fixtures = ['fixtures/releases.json']

    def test_can_navigate_to_the_discogs_page_and_see_list_of_releases(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(home_link_class.text,'Home')

        # The user find the discography nav link and clicks

        self.browser.find_element_by_link_text('Discog').click()

        # A page is loaded up which looks to be a discography, because the active nav link is now, Discog

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_css_selector('li.nav-item.active a'))
        assert el.text == "Discog"

        # The user can clearly see that there is a table with content

        discog_table = self.browser.find_element_by_id('discog_table')
        rows = discog_table.find_elements_by_tag_name('td')
        self.assertIn('Release 1',[row.text for row in rows])

        # The user sees a link to 'more info' regarding a release and clicks on it

        self.browser.find_element_by_link_text('More info').click()


        # The specific page for the release is loaded up and the user can see the relevant info

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Release 1"

        # The user navigates back to the discogs page and clicks on the second release item from the table

        self.browser.find_element_by_link_text('Discog').click()

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_id('discog_table'))
        self.browser.find_element_by_xpath('//*[@id="discog_table"]/tbody/tr[2]/td[4]/a').click()

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Release 2"

        # are we still in the correct navbar context for discogs?
        discogs_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(discogs_link_class.text, 'Discog')

        # satisfied that they can browse releases the user then correctly navigates back to the home page.

        self.browser.find_element_by_link_text('Home').click()

        home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(home_link_class.text, 'Home')