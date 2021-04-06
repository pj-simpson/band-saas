from decimal import Decimal
from unittest import mock
from unittest.mock import patch

from django.forms import model_to_dict
from django.test import TestCase

from shop.forms import ItemQuantityForm
from shop.views import basket_detail_view
from ..models import Product, Order
from ..cart import Cart


class ShopHomeTest(TestCase):

    def test_shop_home_uses_correct_template(self):
        response = self.client.get('/shop/')
        self.assertTemplateUsed(response,'shop/shop_home.html')

    def test_shop_home_has_correct_nav_menu_context(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.context['nav'], 'shop')

    def test_shop_home_fetches_product_objects(self):
        product1 = Product.objects.create(name="product 1",price=10.50)
        response = self.client.get('/shop/')
        self.assertEqual(response.context['products'][0], product1)

    def test_product_detail_uses_correct_template(self):
        product1 = Product.objects.create(name="product 1", price=10.50)
        response = self.client.get('/shop/product-1/')
        self.assertTemplateUsed(response,'shop/product_detail.html')

    def test_product_detail_has_correct_nav_menu_context(self):
        product1 = Product.objects.create(name="product 1", price=10.50)
        response = self.client.get('/shop/product-1/')
        self.assertEqual(response.context['nav'], 'shop')

    def test_product_detail_fetches_release_objects(self):
        product1 = Product.objects.create(name="product 1",price=10.50)
        product2 = Product.objects.create(name="product 2", price=5.50)
        response = self.client.get('/shop/product-1/')
        self.assertEqual(response.context['product'], product1)
        self.assertNotEqual(response.context['product'], product2)


class BasketDetailTest(TestCase):

    def test_basket_detail_uses_correct_template(self):
        response = self.client.get('/shop/basket/')
        self.assertTemplateUsed(response,'shop/basket_detail.html')

    def test_basket_detail_has_correct_nav_menu_context(self):
        response = self.client.get('/shop/basket/')
        self.assertEqual(response.context['nav'], 'shop')

    def test_basket_detail_returns_cart_object(self):
        response = self.client.get('/shop/basket/')
        self.assertIsInstance(response.context['shopping_cart'],Cart)

    def test_basket_detail_returns_cart_object(self):
        response = self.client.get('/shop/basket/')
        self.assertIsInstance(response.context['shopping_cart'], Cart)

    def test_add_item_to_cart_adds_redirects_correctly(self):
        product1 = Product.objects.create(name="product 1", price=10.50)
        response = self.client.post('/shop/basket/add/1/',data={'quantity':1})
        self.assertRedirects(response,'/shop/basket/')

    def test_remove_item_from_cart_adds_redirects_correctly(self):
        product1 = Product.objects.create(name="product 1", price=10.50)
        response = self.client.post('/shop/basket/add/1/', data={'quantity': 1})
        response_2 = self.client.post('/shop/basket/remove/1/')
        self.assertRedirects(response,'/shop/basket/')


class OrderFormTest(TestCase):

    def test_order_form_uses_correct_template(self):
        response = self.client.get('/shop/orderform/')
        self.assertTemplateUsed(response,'shop/order_form.html')

    def test_order_form_has_correct_nav_menu_context(self):
        response = self.client.get('/shop/orderform/')
        self.assertEqual(response.context['nav'], 'shop')

    def test_post_order_form_redirects_correctly(self):
        response = self.client.post('/shop/orderform/')
        self.assertRedirects(response,'/shop/payment-process/')

    def test_payment_process_uses_correct_template(self):
        response = self.client.get('/shop/payment-process/')
        self.assertTemplateUsed(response,'shop/payment_process.html')

    def test_order_form_post_success(self):
        response = self.client.post('/shop/orderform/',
                                    data = {'first_name':'Peter',
                                           'last_name': 'Simpson',
                                           'email':'peter@example.com',
                                           'address':'123 blah blah way',
                                           'postal_code':'e1 4rt',
                                           'city':'London'
                                           })
        self.assertEqual(response.status_code,302)

    def test_order_form_post_creates_new_order(self):

        data = {'first_name':'Peter',
                                           'last_name': 'Simpson',
                                           'email':'peter@example.com',
                                           'address':'123 blah blah way',
                                           'postal_code':'e1 4rt',
                                           'city':'London'
                                           }
        response = self.client.post('/shop/orderform/',
                                    data = data)

        order1 = model_to_dict(Order.objects.all()[0])
        self.assertEqual(order1['first_name'],data['first_name'])
        self.assertEqual(order1['last_name'], data['last_name'])
        self.assertEqual(order1['email'], data['email'])
        self.assertEqual(order1['address'], data['address'])
        self.assertEqual(order1['postal_code'], data['postal_code'])
        self.assertEqual(order1['city'], data['city'])

    # TO DO - Create a test which ensures the associated order items are correctly created?
    # TO DO - Create a test which ensures that the order passes the order to the session

@mock.patch('shop.views.get_object_or_404')
@mock.patch('shop.views.gateway')
class PaymentTests(TestCase):

    def test_payment_done_returns_correct_template(self, mock_get_object_or_404,mock_gateway):
        response = self.client.get('/shop/payment-done/')
        self.assertTemplateUsed(response,'shop/payment_done.html')

    def test_payment_error_returns_correct_template(self, mock_get_object_or_404,mock_gateway):
        response = self.client.get('/shop/payment-error/')
        self.assertTemplateUsed(response, 'shop/payment_error.html')

    def test_payment_view_generates_client_token(self, mock_get_object_or_404,mock_gateway):

        order1 = Order.objects.create(first_name='Peter',
                                      last_name='Simpson',
                                      email='peter@example.com',
                                      address='123 blah blah way',
                                      postal_code='e1 4rt',
                                      city='London')

        mock_get_object_or_404.return_value = order1
        mock_gateway.client_token.generate.return_value = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI'

        response = self.client.get('/shop/payment-process/')
        self.assertTrue(mock_gateway.called_once())

    # @patch('shop.views.Order')
    # def test_payment_view_success(self, mock_get_object_or_404,mock_gateway,mock_order):
    #
    #     order1 = Order.objects.create(first_name='Peter',
    #                                   last_name='Simpson',
    #                                   email='peter@example.com',
    #                                   address='123 blah blah way',
    #                                   postal_code='e1 4rt',
    #                                   city='London')
    #
    #     mock_get_object_or_404.return_value = order1
    #     mock_order.get_total_cost.return_value = 5.00
    #     mock_gateway.transaction.sale.return_value = True
    #
    #     response = self.client.post('/shop/payment-process/')
    #     self.assertRedirects(response,'/shop/payment-done/')

    # def test_payment_view_cancellation(self):
    #     # TO DO USE MOCKS HERE
    #     pass