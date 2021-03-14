from django.shortcuts import render

from shop.cart import Cart
from .models import Product

def shop_home_view(request):
    products = Product.objects.all()
    return render(request, "shop/shop_home.html",{'products':products,'nav':'shop'})

def product_detail_view(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'shop/product_detail.html', {'nav':'shop', 'product':product})

def basket_detail_view(request):
    cart = Cart(request)
    return render(request,'shop/basket_detail.html',{'nav':'shop','shopping_cart':cart})