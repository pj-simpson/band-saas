from decimal import Decimal

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
        self.assertEqual(self.request.session['shopping_cart'],{})

    def test_adding_items_to_cart(self):
        product1 = Product.objects.create(name='Product 1',price=5.95)

        cart = Cart(self.request)
        cart.add(product1,1)
        self.assertEqual(self.request.session['shopping_cart']['1'],{'quantity':1,'price':'5.95'})
#
#     def test_adding_more_items_to_cart_of_already_present_product(self):
#         pass


#
#     def test_adding_items_to_cart_overriding_current_quantity(self):
#         pass
    # TO DO Add handler for the override boolean in the cart's add method. IF we are overriding, we overwrite the
    #     product quantity. If not, we increment it
#
    def test_removing_items_from_cart(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=3.99)

        cart = Cart(self.request)
        cart.add(product1, 1)
        cart.add(product2, 1)

        cart.remove(product1)
        for item in cart:
            self.assertEqual(item, {'quantity': 1, 'price': Decimal('3.99'), 'product': product2, 'total_price': Decimal('3.99')})
    #
    # def test_removing_non_existent_items_from_cart(self):
    #     pass

    def test_cart_iteration(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=3.99)

        cart = Cart(self.request)
        cart.add(product1, 1)
        cart.add(product2, 2)

        expected = [{'quantity': 1, 'price': Decimal('5.95'), 'product': product1, 'total_price': Decimal('5.95')},{'quantity': 2, 'price': Decimal('3.99'), 'product': product2, 'total_price': Decimal('7.98')}]

        for item in cart:
            self.assertIn(item, expected)


#
#     def test_cart_len_method(self):
#         pass
#
    def test_cart_total_price_method(self):

        product1 = Product.objects.create(name='Product 1', price=5.95)
        product2 = Product.objects.create(name='Product 2', price=15.78)
        cart = Cart(self.request)
        cart.add(product1, 2)
        cart.add(product2, 1)

        self.assertEqual(cart.total_price(), Decimal('27.68'))
#
#     def test_clearing_cart(self):
#         pass


