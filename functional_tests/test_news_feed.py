from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait

class TestDiscographyPage(FunctionalTest):

    fixtures = ['fixtures/newsitems.json']

    def test_can_navigate_to_the_news_page_and_see_news_feed(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        self.confirm_homepage()

        # The user find the news nav link and clicks

        self.browser.find_element_by_link_text('News').click()

        # A page is loaded up which looks to be a news feed, because the active nav link is now, News

        self.confirm_nav_context('News')

        # The user can clearly see that there are news items displayed in a 'feed'

        news_container = self.browser.find_element_by_id('news-item-container')
        cards = news_container.find_elements_by_tag_name('h4')
        self.assertIn('Headline 1', [card.text for card in cards])


        # The user sees a link to 'more info' regarding a release and clicks on it

        self.browser.find_element_by_xpath('//*[@id="news-item-card"]/div[2]/a').click()

        # The specific page for the particular news item is loaded up and the user can see the relevant info
        self.confirm_element_after_navigation('h1','Headline 1')

        # The user navigates back to the news page and clicks on the second news item from the feed

        self.browser.find_element_by_link_text('News').click()

        self.confirm_nav_context('News')
        self.browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/a').click()

        self.confirm_element_after_navigation('h1','Headline 2')

        # are we still in the correct navbar context for discogs?
        news_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(news_link_class.text, 'News')

        # satisfied that they can browse releases the user then correctly navigates back to the home page.

        self.browser.find_element_by_link_text('Home').click()

        self.confirm_nav_context('Home')

