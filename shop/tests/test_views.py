from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from shop.views import basket_detail_view, add_item_to_cart_view, remove_item_from_cart_view
from ..models import Product
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
    #
    # def test_add_item_to_cart_adds_redirects_correctly(self):
    #     product1 = Product.objects.create(name="product 1", price=10.50)
    #     response = self.client.post('/shop/basket/add/1')
    #     self.assertRedirects(response,'/shop/basket/',status_code=301,target_status_code=301)

    # def test_remove_item_from_cart_adds_redirects_correctly(self):
    #     product1 = Product.objects.create(name="product 1", price=10.50)
    #     response = self.client.post('/shop/basket/remove/1')
    #     self.assertRedirects(response,'/shop/basket/',status_code=301,target_status_code=301)





