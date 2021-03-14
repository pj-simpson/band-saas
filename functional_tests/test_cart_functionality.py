from selenium.webdriver.support.select import Select

from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait

class TestDiscographyPage(FunctionalTest):

    fixtures = ['fixtures/products.json']

    def test_can_navigate_to_a_product_and_place_in_shopping_basket(self):

        self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(home_link_class.text,'Home')

        # The user find the shop nav link and clicks

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

        # The user sees a quanity drop down button to add a product to their shopping cart, so selects 2 items

        select = Select(self.browser.find_element_by_id('id_quantity'))
        select.select_by_value('2')

        # Then clicks on 'Add to Basket'
        self.browser.find_element_by_xpath('/html/body/div/form/input[1]').click()


        # The user is redirected to a page which gives a summary of their shopping cart
        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Your Shopping Basket"

        # a table is displayed featuring a list of the product of which we have two items of, the produt base and total price

        basket_table = self.browser.find_element_by_id('basket_table')
        rows = basket_table.find_elements_by_tag_name('td')
        self.assertIn('Product 1', [row.text for row in rows])
        self.assertIn('2', [row.text for row in rows])
        self.assertIn('£ 10.99', [row.text for row in rows])
        self.assertIn('£ 21.98', [row.text for row in rows])

        # The user decides that now actually they dont want this product, so removes it from their basket

        self.browser.find_element_by_xpath('//*[@id="basket_table"]/tbody/tr[1]/td[5]/form/input[1]').click()

        # they await the page reload and see and empty table
        el = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        assert el.text == "Your Shopping Basket"
        empty_basket_table = self.browser.find_element_by_id('basket_table')
        rows = empty_basket_table.find_elements_by_tag_name('td')
        self.assertNotIn('Product 1', [row.text for row in rows])
        self.assertNotIn('2', [row.text for row in rows])
        self.assertNotIn('£ 10.99', [row.text for row in rows])
        self.assertNotIn('£ 21.98', [row.text for row in rows])

        self.fail('extend this functional test')
