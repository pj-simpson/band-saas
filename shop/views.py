from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from shop.cart import Cart
from shop.forms import ItemQuantityForm
from .models import Product

def shop_home_view(request):
    products = Product.objects.all()
    return render(request, "shop/shop_home.html",{'products':products,'nav':'shop'})

def product_detail_view(request,slug):
    product = Product.objects.get(slug=slug)
    item_quantity_form = ItemQuantityForm()

    return render(request,'shop/product_detail.html', {'nav':'shop', 'product':product, 'item_quantity_form':item_quantity_form})

def basket_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = ItemQuantityForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request,'shop/basket_detail.html',{'nav':'shop','shopping_cart':cart})

@require_POST
def add_item_to_cart_view(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = ItemQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('basket_detail')

@require_POST
def remove_item_from_cart_view(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket_detail')