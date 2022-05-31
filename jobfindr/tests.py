from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import os

CONTAINER_URL = 'http://capstone-front-1:3000'

# Create your tests here.
class IndexTests(TestCase):
    def test_index(self):
        c = Client()
        response = c.get("/api/")
        self.assertEqual(response.status_code, 200)

class SeleniumIndexTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = ChromeOptions()
        if os.environ.get('IS_CICD_TESTING'):
            chrome_options.add_argument('--headless')
        cls.selenium = webdriver.Remote(
            command_executor='http://capstone-selenium-1:4444', 
            options=chrome_options
        )
        # cls.selenium = webdriver.Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_hello(self):
        self.selenium.get(f'{CONTAINER_URL}/')
        main = self.selenium.find_element(By.TAG_NAME, "main")
        self.assertEqual('Hello world! as JSON', main.text)
  
        # self.assertEqual(self.selenium.title, 'Jobfindr')