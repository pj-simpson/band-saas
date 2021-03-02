from django.test import TestCase
from ..models import Product

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