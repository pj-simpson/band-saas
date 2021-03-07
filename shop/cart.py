from django.conf import settings

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