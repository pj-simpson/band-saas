from django.shortcuts import render
from .models import Product

def shop_home_view(request):
    products = Product.objects.all()
    return render(request, "shop/shop_home.html",{'products':products,'nav':'shop'})