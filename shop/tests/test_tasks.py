from unittest.mock import patch

from django.test import TestCase, TransactionTestCase, override_settings
from django.urls import reverse

from ..models import Order, OrderItem, Product
from ..tasks import successful_order_send_email


class OrderSuccessfulSendEmailTest(TransactionTestCase):
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch("shop.tasks.send_mail")
    def test_send_email_after_successful_payment(self, mock_send_mail):

        product1 = Product.objects.create(name="Product 1", price=5.50)
        order1 = Order.objects.create(
            first_name="Peter",
            last_name="Simpson",
            email="peter@example.com",
            address="123 blah blah way",
            postal_code="e1 4rt",
            city="London",
        )
        order_item1 = OrderItem.objects.create(
            order=order1, product=product1, price=product1.price, quantity=2
        )
        successful_order_send_email(order1.id)
        mock_send_mail.assert_called_with(
            f"Order: {order1.id}",
            f"Dear {order1.first_name} {order1.last_name},\n\n"
            f"You have successfully placed an order."
            f"Your items will be posted out soon.",
            "test@example.com",
            [order1.email],
        )
