from decimal import Decimal

from django.conf import settings
from .models import Product

class Cart(object):

    def __init__(self,request):

        self.session = request.session
        cart = self.session.get('shopping_cart')
        if not cart:
            cart = self.session['shopping_cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def remove(self,product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()