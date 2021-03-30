from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from .base import FunctionalTest

class TestCreatingAnOrder(FunctionalTest):

    fixtures = ['fixtures/products.json']

    def test_can_add_items_to_shopping_basket_and_create_order(self):

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

        self.table_checker('basket_table',('Product 1','£ 10.99','£ 21.98'),True)

        # there is a quantity dropdown which is selected at the correct quantity
        self.check_quantity_already_picked('2')

        # the user can see that there is a link to check out and clicks on it

        checkout_link = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_id('checkout-link'))
        checkout_link.click()

        # a checkout page is displayed and a form is clear to see
        self.confirm_element_after_navigation('h1', 'Checkout')
        checkout_link = WebDriverWait(self.browser, timeout=4).until(lambda d: d.find_element_by_id('order-form'))

        # the user fills in the form with their details and hits submit
        first_name = self.browser.find_element_by_id("id_first_name")
        last_name = self.browser.find_element_by_id("id_last_name")
        email = self.browser.find_element_by_id("id_email")
        address = self.browser.find_element_by_id("id_address")
        postal_code = self.browser.find_element_by_id("id_postal_code")
        city = self.browser.find_element_by_id("id_city")

        first_name.send_keys('Peter')
        last_name.send_keys('Simpson')
        email.send_keys('peter@example.com')
        address.send_keys('7 a house, road road')
        postal_code.send_keys('E5 6YY')
        city.send_keys('London')

        # the form is submitted correctly and a page displaying their order number UUID shows

        self.fail('extend this functional test')
