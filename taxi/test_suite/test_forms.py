from django.test import TestCase
from taxi.forms import DriverForm


class DriverFormTest(TestCase):
    def test_valid_form(self):
        data = {"username": "ivan", "license_number": "TES12345"}
        form = DriverForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        data = {"username": "ivan"}
        form = DriverForm(data=data)
        self.assertFalse(form.is_valid())
