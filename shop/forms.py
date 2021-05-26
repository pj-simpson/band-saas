from django import forms

from shop.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class ItemQuantityForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)

    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]
