from django.shortcuts import render
from .models import Product

def shop_home_view(request):
    products = Product.objects.all()
    return render(request, "shop/shop_home.html",{'products':products,'nav':'shop'})

def product_detail_view(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'shop/product_detail.html', {'nav':'shop', 'product':product})