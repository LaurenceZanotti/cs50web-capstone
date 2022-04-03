from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os

# Create your tests here.
class IndexTests(TestCase):
    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

class SeleniumIndexTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = ChromeOptions()
        if os.environ.get('IS_CICD_TESTING'):
            chrome_options.add_argument('--headless')
        cls.selenium = webdriver.Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_index(self):
        self.selenium.get(f'{self.live_server_url}/')
        self.assertEqual(self.selenium.title, 'Jobfindr')