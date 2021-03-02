from django.urls import path

from .views import shop_home_view

urlpatterns = [
    path("", shop_home_view, name="shop_home"),
]