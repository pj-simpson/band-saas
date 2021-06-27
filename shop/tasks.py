from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def successful_order_send_email(order_id):

    order = Order.objects.get(id=order_id)
    subject = f"Order: {order.id}"
    message = (
        f"Dear {order.first_name} {order.last_name},\n\n"
        f"You have successfully placed an order."
        f"Your items will be posted out soon."
    )
    mail_sent = send_mail(subject, message, "test@example.com", [order.email])
    return mail_sent
