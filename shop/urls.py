from django.urls import path

from .views import shop_home_view, product_detail_view

urlpatterns = [
    path("", shop_home_view, name="shop_home"),
    path("<slug:slug>/",product_detail_view,name='product_detail')
]