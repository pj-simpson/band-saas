from django.forms import TypedChoiceField
from django.test import TestCase
from ..forms import ItemQuantityForm

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
