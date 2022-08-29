from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import os

DOMAIN = 'host.docker.internal'
CONTAINER_URL = f'http://{DOMAIN}:3000'

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
            command_executor='http://host.docker.internal:4444', 
            options=chrome_options
        )
        # cls.selenium = webdriver.Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_welcome_page_title(self):
        """Make sure Welcome page title is correct"""
        self.selenium.get(f'{CONTAINER_URL}/')
        # main = self.selenium.find_element(By.TAG_NAME, "main")
        # self.assertEqual('Hello world! as JSON', main.text)
        self.assertEqual(self.selenium.title, 'Jobfindr - Your future happens now')

    def test_welcome_page_section_titles(self):
        """Make sure Welcome page section titles are correct"""
        self.selenium.get(f'{CONTAINER_URL}/')
        titles_to_test = [
            "A job is waiting for you!",
            "Getting your best opportunity",
            "Are you a talent hunter? All you need is here!"
        ]
        section_titles = self.selenium.find_elements(By.CSS_SELECTOR, "h2 .section-title")

        # Test titles
        for title in section_titles:
            self.assertTrue(title.text in titles_to_test)

    def test_welcome_page_logos(self):
        """Make sure product logo is correct"""
        self.selenium.get(f'{CONTAINER_URL}/')

        # Get logos
        logos = self.selenium.find_elements(By.CSS_SELECTOR, "h1 .font-logo")
        # Test logos
        for logo in logos:
            self.assertEqual(logo.text, "Jobfindr")

    def test_welcome_page_cta(self):
        """Make sure CTA button redirects correctly"""
        self.selenium.get(f'{CONTAINER_URL}/')

        # Get CTA button and click it
        self.selenium.find_element(By.ID, "hero-section-cta-button").click()

        # Test current page title to see if page was redirected
        self.assertEqual(self.selenium.title, "Register | Jobfindr")
        self.assertNotEqual(self.selenium.title, "Jobfindr - Your future happens now")

    def test_welcome_page_navbar(self):
        """Make sure navbar items are correct"""        
        self.selenium.get(f'{CONTAINER_URL}/')
        
        navbar_options = [
            "Home",
            "Search jobs",
            "Looking for talents",
            "Contact us"
        ]

        ul = self.selenium.find_element(By.ID, "navbar-items")
        navbar_items = ul.find_elements(By.TAG_NAME, "li")

        for item in navbar_items:
            self.assertTrue(item.text in navbar_options)