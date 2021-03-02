from _decimal import InvalidOperation

from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Product


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
