from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack


class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="mario", email="mario@gmail.com", password="pass")
        self.snack = Snack.objects.create(
            name = 'breadstick', description = 'Cheesy thick breadstick', purchaser = self.user)
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack.name), 'breadstick')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'breadstick')

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'Cheesy thick breadstick')

    def test_snack_purchaser(self):
        self.assertEqual(f'{self.snack.purchaser}', 'mario')

    def test_user_email(self):
        self.assertEqual(str(self.user.email), 'mario@gmail.com')

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_error_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertIsNot(response.status_code, 400)

    def test_base_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
