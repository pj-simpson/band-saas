from _decimal import InvalidOperation

from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Product, Order, OrderItem


class ProductModelTest(TestCase):

    def test_saving_product(self):
        product1 = Product.objects.create(name='Product 1',price=10.99)
        product2 = Product.objects.create(name='Product 2',price=10.99)
        self.assertEqual(product1,Product.objects.all()[0])

    def test_cannot_save_product_without_name(self):
        with self.assertRaises(ValidationError):
            product1 = Product.objects.create(name='',price=10.99)
            product1.full_clean()

    def test_cannot_save_product_without_price(self):
        with self.assertRaises(IntegrityError):
            product1 = Product.objects.create(name='product1')
            product1.full_clean()

    def test_cannot_save_product_with_too_many_digits(self):
        with self.assertRaises(InvalidOperation):
            product1 = Product.objects.create(name='product1',price=12345678912)
            product1.full_clean()

    def test_cannot_save_product_with_too_many_decimal_places(self):
        with self.assertRaises(ValidationError):
            product1 = Product.objects.create(name='product1',price=10.998)
            product1.full_clean()

    def test_release_slug_is_created_correctly(self):
        product1 = Product.objects.create(name='Product 1',price=10.99)
        self.assertEqual(product1.slug,'product-1')

    def test_release_slug_unique(self):
        product1 = Product.objects.create(name='Product 1',price=10.99)
        with self.assertRaises(IntegrityError):
            product1 = product1 = Product.objects.create(name='Product 1',price=10.99)
            product1.full_clean()

    def test_get_absolute_url(self):
        product1 = Product.objects.create(name='Product 1',price=10.99)
        self.assertEqual(product1.get_absolute_url(),f'/shop/{product1.slug}/')


class OrderModelTest(TestCase):

    def test_saving_order(self):
        order1 = Order.objects.create(first_name = 'Peter',
                                       last_name = 'Simpson',
                                       email ='peter@example.com',
                                       address ='123 blah blah way',
                                       postal_code ='e1 4rt',
                                       city ='London')
        order2 = Order.objects.create(first_name = 'Bob',
                                       last_name = 'Jones',
                                       email ='b@example.com',
                                       address ='456 blah blah road',
                                       postal_code ='e7 8xx',
                                       city ='Southampton')
        self.assertEqual(2,len(Order.objects.all()))

    def test_cannot_save_order_without_mandatory_fields(self):
        with self.assertRaises(ValidationError):
            order1 = Order.objects.create(first_name = '',
                                       last_name = '',
                                       email ='b@example.com',
                                       address ='456 blah blah road',
                                       postal_code ='e7 8xx',
                                       city ='Southampton')
            order1.full_clean()

    def test_ordering(self):
        order1 = Order.objects.create(first_name='Peter',
                                      last_name='Simpson',
                                      email='peter@example.com',
                                      address='123 blah blah way',
                                      postal_code='e1 4rt',
                                      city='London')
        order2 = Order.objects.create(first_name='Bob',
                                      last_name='Jones',
                                      email='b@example.com',
                                      address='456 blah blah road',
                                      postal_code='e7 8xx',
                                      city='Southampton')
        order3 = Order.objects.create(first_name='Jim',
                                      last_name='Jimothy',
                                      email='jimjimjim@example.com',
                                      address='100 blah blah road',
                                      postal_code='se16 9yu',
                                      city='Leeds')
        self.assertEqual(Order.objects.last(),order1)

    def test_total_cost_calculation(self):

        product1 = Product.objects.create(name='Product 1',price=5.50)
        product2 = Product.objects.create(name='Product 2', price=7.50)
        order1 = Order.objects.create(first_name='Peter',
                                      last_name='Simpson',
                                      email='peter@example.com',
                                      address='123 blah blah way',
                                      postal_code='e1 4rt',
                                      city='London')
        order_item1 = OrderItem.objects.create(order=order1,
                                               product=product1,
                                               price=product1.price,
                                               quantity=2)
        order_item2 = OrderItem.objects.create(order=order1,
                                               product=product2,
                                               price=product2.price,
                                               quantity=1)

        self.assertEqual(order1.get_total_cost(),18.50)

class OrderItemModelTest(TestCase):

    def test_saving_order_item(self):
        product1 = Product.objects.create(name='Product 1', price=5.50)
        product2 = Product.objects.create(name='Product 2', price=7.50)
        order1 = Order.objects.create(first_name='Peter',
                                      last_name='Simpson',
                                      email='peter@example.com',
                                      address='123 blah blah way',
                                      postal_code='e1 4rt',
                                      city='London')
        order_item1 = OrderItem.objects.create(order=order1,
                                               product=product1,
                                               price=product1.price,
                                               quantity=2)
        order_item2 = OrderItem.objects.create(order=order1,
                                               product=product2,
                                               price=product2.price,
                                               quantity=1)
        self.assertEqual(order_item1,OrderItem.objects.all()[0])

    def test_cannot_save_order_item_without_mandatory_fields(self):
        with self.assertRaises(IntegrityError):
            order_item1 = OrderItem.objects.create(
                                                   price=10.00,
                                                   quantity=2)
            order_item1.full_clean()

    def test_get_cost(self):

        product1 = Product.objects.create(name='Product 1', price=5.50)
        order1 = Order.objects.create(first_name='Peter',
                                      last_name='Simpson',
                                      email='peter@example.com',
                                      address='123 blah blah way',
                                      postal_code='e1 4rt',
                                      city='London')
        order_item1 = OrderItem.objects.create(order=order1,
                                               product=product1,
                                               price=product1.price,
                                               quantity=2)

        self.assertEqual(order_item1.get_cost(), 11.00)
