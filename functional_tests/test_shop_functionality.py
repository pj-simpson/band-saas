from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait

class TestDiscographyPage(FunctionalTest):

    fixtures = ['fixtures/products.json']

    def test_can_navigate_to_the_shop_page_and_see_list_of_products(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(home_link_class.text,'Home')

        # The user find the discography nav link and clicks

        self.browser.find_element_by_link_text('Shop').click()

        # A page is loaded up which looks to be a shop, because the active nav link is now, Shop

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_css_selector('li.nav-item.active a'))
        assert el.text == "Shop"

        # The user can clearly see that there are products

        product_container = self.browser.find_element_by_id('product-card-container')
        cards = product_container.find_elements_by_tag_name('h5')
        self.assertIn('Product 1',[card.text for card in cards])

        # The user sees a link to 'more info' regarding a release and clicks on it

        self.browser.find_element_by_link_text('More info').click()


        # The specific page for the product is loaded up and the user can see the relevant info

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Product 1"

        # The user navigates back to the shop page and clicks on the second product item from the table

        self.browser.find_element_by_link_text('Shop').click()

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_id('product-card-container'))
        self.browser.find_element_by_xpath('//*[@id="product-card-container"]/div[2]/div[2]/small/a').click()

        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Product 2"
        #
        # # are we still in the correct navbar context for discogs?
        # discogs_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        # self.assertEqual(discogs_link_class.text, 'Discog')
        #
        # # satisfied that they can browse releases the user then correctly navigates back to the home page.
        #
        # self.browser.find_element_by_link_text('Home').click()
        #
        # home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        # self.assertEqual(home_link_class.text, 'Home')