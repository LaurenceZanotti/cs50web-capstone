from django.test import TestCase, Client, LiveServerTestCase

# Create your tests here.
class IndexTests(TestCase):
    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)