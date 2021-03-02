from django.test import TestCase
from ..models import Product

class ShopHomeTest(TestCase):

    def test_shop_home_uses_correct_template(self):
        response = self.client.get('/shop/')
        self.assertTemplateUsed(response,'shop/shop_home.html')

    def test_shop_home_has_correct_nav_menu_context(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.context['nav'], 'shop')

    def test_discogs_fetches_release_objects(self):
        product1 = Product.objects.create(name="product 1",price=10.50,)
        response = self.client.get('/shop/')
        self.assertEqual(response.context['products'][0], product1)