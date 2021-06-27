from django.urls import path

from .tests.test_utils import fake_payment_process_view
from .views import (
    add_item_to_cart_view,
    basket_detail_view,
    order_form_view,
    payment_done_view,
    payment_error_view,
    payment_process_view,
    product_detail_view,
    remove_item_from_cart_view,
    shop_home_view,
)

urlpatterns = [
    path("", shop_home_view, name="shop_home"),
    path("basket/", basket_detail_view, name="basket_detail"),
    path("orderform/", order_form_view, name="order_form"),
    path("payment-process/", payment_process_view, name="payment_process"),
    path(
        "test-payment-process/<str:fail_flag>",
        fake_payment_process_view,
        name="test_payment_process",
    ),
    path("payment-done/", payment_done_view, name="payment_done"),
    path("payment-error/", payment_error_view, name="payment_error"),
    path("basket/add/<int:product_id>/", add_item_to_cart_view, name="basket_add"),
    path(
        "basket/remove/<int:product_id>/",
        remove_item_from_cart_view,
        name="basket_remove",
    ),
    path("<slug:slug>/", product_detail_view, name="product_detail"),
]
