from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    host= 'django'

    def setUp(self) -> None:
        self.browser = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self) -> None:
        self.browser.quit()
        super().tearDown()

    def confirm_homepage(self):
        home_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(home_link_class.text, 'Home')

    def navigate_to_shop(self):
        self.browser.find_element_by_link_text('Shop').click()

        shop_navigation = WebDriverWait(self.browser, timeout=4).until(
            lambda d: d.find_element_by_css_selector('li.nav-item.active a'))
        self.assertEqual(shop_navigation.text,'Shop')

    def select_quantity_dropdown_add_to_basket(self,quantity,id):
        select = Select(self.browser.find_element_by_id(f'{id}'))
        select.select_by_value(f'{quantity}')
        self.browser.find_element_by_xpath('/html/body/div/form/input[1]').click()

    def confirm_element_after_navigation(self,tag,text):
        header = WebDriverWait(self.browser, timeout=10).until(lambda d: d.find_element_by_tag_name(f"{tag}"))
        self.assertEqual(header.text,text)

    def confirm_nav_context(self,nav_text):
        active_link_class = self.browser.find_element_by_css_selector('li.nav-item.active a')
        self.assertEqual(active_link_class.text, nav_text)


    def table_checker(self,table_id,value_array,in_or_not):

        """ table_id = string the id of the table
            value_array = a list of strings we want to check if they are in the table
            in_or_not = a bool to denote whether or not we are checking if these values are in or absent from the table
        """

        table = self.browser.find_element_by_id(f'{table_id}')
        rows = table.find_elements_by_tag_name('td')
        if in_or_not:
            for item in value_array:
                self.assertIn(item,[row.text for row in rows])
        else:
            for item in value_array:
                self.assertNotIn(item,[row.text for row in rows])

    def check_quantity_already_picked(self,value):
        quantity_selection =self.browser.find_element_by_xpath(f'//*[@id="id_quantity"]/option[{value}]')
        self.assertEqual(quantity_selection.text,value)


