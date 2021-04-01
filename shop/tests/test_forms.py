from django.forms import TypedChoiceField,CharField
from django.test import TestCase
from ..forms import ItemQuantityForm, OrderForm

class ItemQuantityFormTest(TestCase):

    def test_form_renders_correct_markup(self):
        form = ItemQuantityForm()
        self.assertIn('for="id_quantity"',form.as_p())

    def test_form_has_correct_fields(self):
        form = ItemQuantityForm()
        self.assertIsInstance(form.fields['quantity'],TypedChoiceField)

    def test_form_is_valid(self):
        form = ItemQuantityForm(data={'quantity':1})
        self.assertTrue(form.is_valid())

    def test_form_has_hidden_field(self):
        form = ItemQuantityForm()
        self.assertEqual(1,len(form.hidden_fields()))

class OrderFormTest(TestCase):

    def test_form_renders_correct_markup(self):
        form = OrderForm()
        self.assertIn('for="id_first_name"',form.as_p())
        self.assertIn('for="id_last_name"', form.as_p())
        self.assertIn('for="id_email"', form.as_p())
        self.assertIn('for="id_address"', form.as_p())
        self.assertIn('for="id_postal_code"', form.as_p())
        self.assertIn('for="id_city"', form.as_p())

    def test_form_has_correct_fields(self):
        form = OrderForm()
        self.assertIsInstance(form.fields['first_name'],CharField)
        self.assertIsInstance(form.fields['last_name'], CharField)
        self.assertIsInstance(form.fields['email'], CharField)
        self.assertIsInstance(form.fields['address'], CharField)
        self.assertIsInstance(form.fields['postal_code'], CharField)
        self.assertIsInstance(form.fields['city'], CharField)
