from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class ItemQuantityForm(forms.Form):

    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

class OrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    address= forms.CharField()
    postal_code = forms.CharField()
    city = forms.CharField()