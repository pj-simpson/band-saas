from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from .base import FunctionalTest

class TestShoppingCart(FunctionalTest):

    fixtures = ['fixtures/products.json']

    def test_can_navigate_to_a_product_and_place_in_shopping_basket(self):

        selenium_browser = self.browser.get(self.live_server_url)

        # The user can see that they are on the home page because the nav link with 'Home' is active
        self.confirm_homepage()

        # The user find the shop nav link and clicks
        self.navigate_to_shop()

        # The user can clearly see that there are products

        product_container = self.browser.find_element_by_id('product-card-container')
        cards = product_container.find_elements_by_tag_name('h5')
        self.assertIn('Product 1', [card.text for card in cards])

        # The user sees a link to 'more info' regarding a release and clicks on it

        self.browser.find_element_by_link_text('More info').click()

        # The specific page for the product is loaded up and the user can see the relevant info

        product_header = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_tag_name("h1"))
        self.assertEqual(product_header.text,"Product 1")

        # The user sees a quanity drop down button to add a product to their shopping cart, so selects 2 items

        self.select_quantity_dropdown_add_to_basket('2','id_quantity')

        # The user is redirected to a page which gives a summary of their shopping cart
        self.confirm_element_after_navigation('h1','Your Shopping Basket')

        # a table is displayed featuring a list of the product of which we have two items of, the produt base and total price

        self.table_checker('basket_table',('Product 1','2','£ 10.99','£ 21.98'),True)

        # The user decides that now actually they dont want this product, so removes it from their basket

        self.browser.find_element_by_xpath('//*[@id="basket_table"]/tbody/tr[1]/td[5]/form/input[1]').click()

        # they await the page reload and see and empty table
        self.confirm_element_after_navigation('h1','Your Shopping Basket')
        self.table_checker('basket_table',('Product 1','2','£ 10.99','£ 21.98'),False)

        # The user navigates back to products.

        self.navigate_to_shop()

        # The user can clearly see that there are products

        self.browser.find_element_by_xpath('//*[@id="product-card-container"]/div[1]/div[2]/small/a').click()

        # they put 2 of product 1 in their basket

        self.confirm_element_after_navigation('h1','Product 1')
        self.select_quantity_dropdown_add_to_basket('2','id_quantity')


        # they again navigate back to products

        self.navigate_to_shop()

        # the put one of product 2 in their basket
        self.browser.find_element_by_xpath('//*[@id="product-card-container"]/div[2]/div[2]/small/a').click()
        self.confirm_element_after_navigation('h1','Product 2')
        self.select_quantity_dropdown_add_to_basket('1', 'id_quantity')

        # they are able to see the total price of the basket accurately reflected on the page.

        basket_table_footer = WebDriverWait(self.browser, timeout=4).until(
            lambda d: d.find_element_by_id('basket-table-footer'))
        rows = basket_table_footer.find_elements_by_tag_name('td')
        self.assertIn('£ 27.93', [row.text for row in rows])

        self.fail('extend this functional test!')


