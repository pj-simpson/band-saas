from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse, parse_qs

class TestDiscographyPage(FunctionalTest):

    fixtures = ['fixtures/newsitems.json']

    def test_can_navigate_to_the_news_page_and_user_pagination(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        self.confirm_homepage()

        # The user find the news nav link and clicks

        self.browser.find_element_by_link_text('News').click()

        # A page is loaded up which looks to be a news feed, because the active nav link is now, News

        self.confirm_nav_context('News')

        # The User can see 5 news cards displayed on the page.

        news_cards = self.browser.find_elements_by_id('news-item-card')
        assert len(news_cards) == 5

        # The user scrolls to the bottom and can see that there is pagination links

        pagination_links = self.browser.find_element_by_id('news-pagination-list')

        # The user clicks on the 'Next' link

        self.browser.find_element_by_link_text('Next').click()

        # They are still on the news page

        self.confirm_nav_context('News')

        # However the url now has 'page=2' appended on the end
        url = self.browser.current_url
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        assert query['page'][0] == '2'

        # This page of news items only has one new item on it (6 news items in total and we paginate 5 to a page)
        second_page_news_cards = self.browser.find_elements_by_id('news-item-card')
        assert len(second_page_news_cards) == 1

        # The user can see a 'previous' button to navigate back to the first page

        self.browser.find_element_by_link_text('Previous').click()

        self.confirm_nav_context('News')

        # They are on the page from before the url now has 'page=1' appended on the end
        url = self.browser.current_url
        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        assert query['page'][0] == '1'

        # Its the same 5 news cards from before
        news_cards = self.browser.find_elements_by_id('news-item-card')
        assert len(news_cards) == 5


