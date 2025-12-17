from django.test import TestCase
from taxi.models import Manufacturer, Car, Driver


class ManufacturerModelTest(TestCase):
    def test_str_returns_name(self):
        manufacturer = Manufacturer.objects.create(name="BMW Germany")
        self.assertEqual(str(manufacturer).strip(), "BMW Germany")


class CarModelTest(TestCase):
    def test_str_returns_model(self):
        manufacturer = Manufacturer.objects.create(name="BMW Germany")
        car = Car.objects.create(model="X5", manufacturer=manufacturer)
        self.assertEqual(str(car), "X5")


class DriverModelTest(TestCase):
    def test_str_returns_username(self):
        driver = Driver.objects.create(username="ivan",
                                       license_number="TES12345")
        self.assertEqual(str(driver).split()[0], "ivan")
