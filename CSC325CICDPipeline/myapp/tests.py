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

        
class APIStatusTests(SimpleTestCase):

    def test_api_status_returns_200(self):
        response = self.client.get(reverse("api_status"))
        self.assertEqual(response.status_code, 200)

    def test_api_status_returns_expected_json(self):
        response = self.client.get(reverse("api_status"))

        self.assertEqual(response.json(), {
            "status": "success",
            "message": "CSC325 CI/CD Pipeline API is running"
        })