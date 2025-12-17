from django.test import TestCase
from taxi.models import Driver, Car, Manufacturer


class SearchTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.manufacturer1 = Manufacturer.objects.create(name="BMW Germany")
        cls.manufacturer2 = Manufacturer.objects.create(name="Audi Germany")

        cls.car1 = Car.objects.create(model="X5",
                                      manufacturer=cls.manufacturer1)
        cls.car2 = Car.objects.create(model="A6",
                                      manufacturer=cls.manufacturer2)

        cls.driver1 = Driver.objects.create(username="ivan",
                                            license_number="TES12345")
        cls.driver2 = Driver.objects.create(username="petro",
                                            license_number="TES12346")

    def test_driver_search_by_username(self):
        results = Driver.objects.filter(username__icontains="ivan")
        self.assertIn(self.driver1, results)
        self.assertNotIn(self.driver2, results)

    def test_car_search_by_model(self):
        results = Car.objects.filter(model__icontains="X5")
        self.assertIn(self.car1, results)
        self.assertNotIn(self.car2, results)

    def test_manufacturer_search_by_name(self):
        results = Manufacturer.objects.filter(name__icontains="BMW")
        self.assertIn(self.manufacturer1, results)
        self.assertNotIn(self.manufacturer2, results)
