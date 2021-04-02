from decimal import Decimal

from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from ..cart import Cart
from ..models import Product

class CartTest(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/')

        # adding session
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()

    def test_cart_initialization(self):
        cart = Cart(self.request)
        self.assertEqual(self.request.session[settings.CART_SESSION_ID],{})

    def test_adding_items_to_cart(self):
        product1 = Product.objects.create(name='Product 1',price=5.95)

        cart = Cart(self.request)
        cart.add(product1,1)
        self.assertEqual(self.request.session[settings.CART_SESSION_ID]['1'],{'quantity':1,'price':'5.95'})

    def test_removing_items_from_cart(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=3.99)

        cart = Cart(self.request)
        cart.add(product1, 1)
        cart.add(product2, 1)

        cart.remove(product1)
        for item in cart:
            self.assertEqual(item, {'quantity': 1, 'price': Decimal('3.99'), 'product': product2, 'total_price': Decimal('3.99')})


    def test_cart_iteration(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=3.99)

        cart = Cart(self.request)
        cart.add(product1, 1)
        cart.add(product2, 2)

        expected = [{'quantity': 1, 'price': Decimal('5.95'), 'product': product1, 'total_price': Decimal('5.95')},{'quantity': 2, 'price': Decimal('3.99'), 'product': product2, 'total_price': Decimal('7.98')}]

        for item in cart:
            self.assertIn(item, expected)


    def test_cart_total_price_method(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=15.78)
        cart = Cart(self.request)
        cart.add(product1, 2)
        cart.add(product2, 1)

        self.assertEqual(cart.total_price(), Decimal('27.68'))



# TO DO - Find a way to test the cart clear method using a mock?
    # def test_clear(self):
    #
    #     product1 = Product.objects.create(name='Product 1', price=5.95)
    #     product2 = Product.objects.create(name='Product 2', price=15.78)
    #     cart = Cart(self.request)
    #     cart.add(product1, 2)
    #     cart.add(product2, 1)
    #
    #     cart.clear()
    #     self.assertEqual(cart.__dict__ ,{})


