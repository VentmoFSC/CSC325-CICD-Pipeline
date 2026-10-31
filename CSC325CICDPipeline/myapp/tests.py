from django.test import SimpleTestCase
from django.urls import reverse


class ViewTests(SimpleTestCase):
    def test_home_page_returns_expected_content(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
        self.assertContains(response, "home page")

    def test_about_page_returns_expected_content(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Page")
        self.assertContains(response, "This is the about page")

