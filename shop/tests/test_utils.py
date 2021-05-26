import braintree
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from shop.models import Order

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def fake_payment_process_view(request, fail_flag):
    order = "place holder for fake order"
    fail_flag = fail_flag

    if fail_flag == "pass":
        nonce = "fake-valid-nonce"
    elif fail_flag == "fail":
        nonce = "fake-luhn-invalid-nonce"

    if request.method == "POST":
        result = gateway.transaction.sale(
            {
                "amount": "10.00",
                "payment_method_nonce": "fake-valid-nonce",
                "options": {"submit_for_settlement": True},
            }
        )
        if result.is_success:
            # real view does order stuff here!
            return redirect("payment_done")
        else:
            return redirect("payment_error")
    else:
        client_token = gateway.client_token.generate()

        return render(
            request,
            "shop/payment_process.html",
            {"order": order, "client_token": client_token, "nav": "shop"},
        )
