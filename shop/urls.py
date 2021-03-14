from django.urls import path

from .views import shop_home_view, product_detail_view,basket_detail_view,add_item_to_cart_view,remove_item_from_cart_view

urlpatterns = [
    path("", shop_home_view, name="shop_home"),
    path("basket/",basket_detail_view,name='basket_detail'),
    path('basket/add/<int:product_id>/', add_item_to_cart_view, name='basket_add'),
    path('basket/remove/<int:product_id>/', remove_item_from_cart_view, name='basket_remove'),
    path("<slug:slug>/",product_detail_view,name='product_detail'),

]