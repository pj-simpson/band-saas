import braintree
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from shop.cart import Cart
from shop.forms import ItemQuantityForm, OrderForm
from .models import Product, OrderItem, Order

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)



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

def order_form_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            return redirect('payment_process')
    else:
        form = OrderForm()
        return render(request,'shop/order_form.html',{'nav':'shop', 'form':form})


# PAYMENT VIEWS

def payment_process_view(request):

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    client_token = gateway.client_token.generate()

    return render(request,
                  'shop/payment_process.html',
                  {'order': order,
                   'client_token': client_token,
                   'nav':'shop'})




def payment_done_view(request):
    return render(request, 'shop/payment_done.html')

def payment_error_view(request):
    return render(request, 'shop/payment_error.html')


