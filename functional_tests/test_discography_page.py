from selenium.webdriver.support.ui import WebDriverWait

from discogs.models import Release

from .base import FunctionalTest


class TestDiscographyPage(FunctionalTest):

    fixtures = ["fixtures/releases.json"]

    def test_can_navigate_to_the_discogs_page_and_see_list_of_releases(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        self.confirm_homepage()

        # The user find the discography nav link and clicks

        self.browser.find_element_by_link_text("Discog").click()

        # A page is loaded up which looks to be a discography, because the active nav link is now, Discog

        self.confirm_nav_context("Discog")

        # The user can clearly see that there is a table with content
        self.table_checker("discog_table", ("Release 1",), True)

        # The user sees a link to 'more info' regarding a release and clicks on it

        self.browser.find_element_by_link_text("More info...").click()

        # The specific page for the release is loaded up and the user can see the relevant info
        self.confirm_element_after_navigation("h1", "Release 1")

        # The user navigates back to the discogs page and clicks on the second release item from the table

        self.browser.find_element_by_link_text("Discog").click()

        el = WebDriverWait(self.browser, timeout=4).until(
            lambda d: d.find_element_by_id("discog_table")
        )
        self.browser.find_element_by_xpath(
            '//*[@id="discog_table"]/tbody/tr[2]/td[4]/a'
        ).click()

        self.confirm_element_after_navigation("h1", "Release 2")

        # are we still in the correct navbar context for discogs?
        discogs_link_class = self.browser.find_element_by_css_selector(
            "li.nav-item.active a"
        )
        self.assertEqual(discogs_link_class.text, "Discog")

        # satisfied that they can browse releases the user then correctly navigates back to the home page.

        self.browser.find_element_by_link_text("Home").click()

        self.confirm_nav_context("Home")
