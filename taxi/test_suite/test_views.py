from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="12345")

    def test_login_view(self):
        response = self.client.post(reverse("login"), data={"username": "alex",
                                                            "password": "12345"
                                                            })
        self.assertEqual(response.status_code, 302)
