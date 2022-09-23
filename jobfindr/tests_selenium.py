from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os

DOMAIN = 'host.docker.internal'
CONTAINER_URL = f'http://{DOMAIN}:5000'

# Create your tests here.
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
        cls.selenium.implicitly_wait(3)

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

class SeleniumAuthTests(LiveServerTestCase):
    """Test suite for form existence, components and links"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = ChromeOptions()
        if os.environ.get('IS_CICD_TESTING'):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920,1080') # This line fixes a bug from 5bd797e
            # https://stackoverflow.com/questions/47776774/element-is-not-clickable-at-point-in-headless-mode-but-when-we-remove-headless
        cls.selenium = webdriver.Remote(
            command_executor='http://host.docker.internal:4444', 
            options=chrome_options
        )
        # cls.selenium = webdriver.Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_page_title(self):
        """Make sure login page title is correct"""
        self.selenium.get(f'{CONTAINER_URL}/login')
        self.assertEqual(self.selenium.title, "Log in | Jobfindr")

    def test_login_form_existence(self):
        """Make sure login form exists with correct placeholders"""
        self.selenium.get(f'{CONTAINER_URL}/login')

        # Test form existence
        form = self.selenium.find_element(By.CSS_SELECTOR, 'form[method="post"]')
        self.assertTrue(form)

        # Test form elements
        username_input = form.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        self.assertTrue(username_input)
        self.assertEqual(username_input.get_attribute("placeholder"), "Username")

        password_input = form.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        self.assertTrue(password_input)
        self.assertEqual(password_input.get_attribute("placeholder"), "Password")

        login_button = form.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        self.assertTrue(login_button)
        self.assertEqual(login_button.get_attribute("value"), "Log in")

    def test_login_page_create_account_link(self):
        """Make sure create account link is working"""
        self.selenium.get(f'{CONTAINER_URL}/login')
        
        self.assertEqual(self.selenium.title, "Log in | Jobfindr")

        # Find and click "Create one" link to be redirected to the register page
        create_account_button = self.selenium.find_element(By.CSS_SELECTOR, 'a[href="/register"]')
        create_account_button.click()

        # Make sure the title changed
        self.assertNotEqual(self.selenium.title, "Log in | Jobfindr")
        self.assertEqual(self.selenium.title, "Register | Jobfindr")

    def test_register_page_title(self):
        """Make sure register page title is correct"""
        self.selenium.get(f'{CONTAINER_URL}/register')
        self.assertEqual(self.selenium.title, "Register | Jobfindr")

    def test_register_page_form_existence(self):
        """Make sure login form exists with correct placeholders"""
        self.selenium.get(f'{CONTAINER_URL}/register')

        # Test form existence
        form = self.selenium.find_element(By.CSS_SELECTOR, 'form[method="post"]')
        self.assertTrue(form)

        # Test form elements
        username_input = form.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        self.assertTrue(username_input)
        self.assertEqual(username_input.get_attribute("placeholder"), "Username")

        email_input = form.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        self.assertTrue(email_input)
        self.assertEqual(email_input.get_attribute("placeholder"), "Email")

        password_input = form.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        self.assertTrue(password_input)
        self.assertEqual(password_input.get_attribute("placeholder"), "Password")

        cpassword_input = form.find_element(By.CSS_SELECTOR, 'input[name="cpassword"]')
        self.assertTrue(cpassword_input)
        self.assertEqual(cpassword_input.get_attribute("placeholder"), "Confirm your password")

        login_button = form.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        self.assertTrue(login_button)
        self.assertEqual(login_button.get_attribute("value"), "Register")
    
    def test_register_page_already_have_account_link(self):
        """Make sure already have an account link is working"""
        self.selenium.get(f'{CONTAINER_URL}/register')
        
        self.assertEqual(self.selenium.title, "Register | Jobfindr")

        # Close modal
        modal = self.selenium.find_element(
            By.CSS_SELECTOR, 
            "div#headlessui-portal-root"
        )
        modal_buttons = modal.find_elements(By.TAG_NAME, 'button')
        modal_buttons[1].click()

        # Find and click "Create one" link to be redirected to the register page
        already_have_account_link = self.selenium.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        already_have_account_link.click()

        # Make sure the title changed
        self.assertNotEqual(self.selenium.title, "Register | Jobfindr")
        self.assertEqual(self.selenium.title, "Log in | Jobfindr")

    def test_register_page_modal_jobseeker_button(self):
        """Make sure modal job seeker modal button is working"""
        self.selenium.get(f'{CONTAINER_URL}/register')
        self.assertEqual(self.selenium.title, "Register | Jobfindr")
        
        # Find modal and button
        modal = self.selenium.find_element(
            By.CSS_SELECTOR, 
            "div#headlessui-portal-root"
        )
        modal_buttons = modal.find_elements(By.TAG_NAME, 'button')
        modal_buttons[1].click()

        # Make sure the selected options is reflected within the form
        hidden_input = self.selenium.find_element(By.CSS_SELECTOR, 'input#usertype')
        self.assertEqual("jobseeker", hidden_input.get_attribute("value"))
        label_container = self.selenium.find_element(By.CSS_SELECTOR, "div#usertype_label")
        label = label_container.find_element(By.TAG_NAME, 'span')
        self.assertEqual("jobs", label.text)

    def test_register_page_modal_talenthunter_button(self):
        """Make sure modal talent hunter modal button is working"""
        self.selenium.get(f'{CONTAINER_URL}/register')
        self.assertEqual(self.selenium.title, "Register | Jobfindr")
        
        # Find modal and button
        modal = self.selenium.find_element(
            By.CSS_SELECTOR, 
            "div#headlessui-portal-root"
        )
        modal_buttons = modal.find_elements(By.TAG_NAME, 'button')
        modal_buttons[2].click()

        # Make sure the selected options is reflected within the form
        hidden_input = self.selenium.find_element(By.CSS_SELECTOR, 'input#usertype')
        self.assertEqual("talenthunter", hidden_input.get_attribute("value"))
        label_container = self.selenium.find_element(By.CSS_SELECTOR, "div#usertype_label")
        label = label_container.find_element(By.TAG_NAME, 'span')
        self.assertEqual("talents", label.text)

class SeleniumLoginTests(LiveServerTestCase):
    """Tests for peforming account login"""
    fixtures = ['initial_data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = ChromeOptions()
        if os.environ.get('IS_CICD_TESTING'):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--window-size=1920,1080') # This line fixes a bug from 5bd797e
            # https://stackoverflow.com/questions/47776774/element-is-not-clickable-at-point-in-headless-mode-but-when-we-remove-headless
        cls.selenium = webdriver.Remote(
            command_executor='http://host.docker.internal:4444', 
            options=chrome_options
        )
        # cls.selenium = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def get_auth_form_elements(self):
        """
        Returns auth form elements as a dictionary

        Driver should have accessed an URL for this function to work
        """
        form_elements = {}

        form = self.selenium.find_element(By.CSS_SELECTOR, 'form[method="post"]')
        form_inputs = form.find_elements(By.CSS_SELECTOR, 'input')
        
        # Transform list of inputs into dictionary
        for input in form_inputs:
            form_elements[input.get_attribute('name') or input.get_attribute('type')] = input

        return form_elements

    def test_login_jobseeker(self):
        """Test a JobSeeker user login"""
        self.selenium.get(f'{CONTAINER_URL}/login')
        self.assertEqual(self.selenium.title, "Log in | Jobfindr")

        # Locate components
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        login_button = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

        # Fill form fields
        username_input.send_keys('dine')
        password_input.send_keys('test12345')

        # Send form / attempt login
        login_button.click()

        # Code snippet from: 
        # https://selenium-python.readthedocs.io/waits.html#explicit-waits
        # Wait (fluently) for the page redirect
        try:
            element = WebDriverWait(
                self.selenium, 
                10, 
                poll_frequency=1, 
                ignored_exceptions=[NoSuchElementException]
            ).until(
                EC.presence_of_element_located((By.ID, "profile-container"))
            )
            element.click()
        except NoSuchElementException as e:
            print(e)

        profile_container = self.selenium.find_element(By.ID, "profile-container")
        self.assertTrue(profile_container)
        
        # Check if profile page is correct
        self.assertEqual("Profile | Jobfindr", self.selenium.title)
        self.assertEqual(
            'Profile', 
            profile_container.find_element(By.TAG_NAME, 'h1').text
        )
        self.assertEqual(
            r'{"user":{"id":3,"username":"dine"}}', 
            profile_container.find_element(By.TAG_NAME, 'div').text
        )

    def test_login_talenthunter(self):
        """Test a TalentHunter user login"""
        self.selenium.get(f'{CONTAINER_URL}/login')
        self.assertEqual(self.selenium.title, "Log in | Jobfindr")

        # Locate components
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        login_button = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

        # Fill form fields
        username_input.send_keys('emilly')
        password_input.send_keys('test12345')

        # Send form / attempt login
        login_button.click()

        # Wait (fluently) for the page redirect
        try:
            element = WebDriverWait(
                self.selenium, 
                10, 
                poll_frequency=1, 
                ignored_exceptions=[NoSuchElementException]
            ).until(
                EC.presence_of_element_located((By.ID, "profile-container"))
            )
            element.click()
        except NoSuchElementException as e:
            print(e)

        profile_container = self.selenium.find_element(By.ID, "profile-container")
        self.assertTrue(profile_container)
        
        # Check if profile page is correct
        self.assertEqual("Profile | Jobfindr", self.selenium.title)
        self.assertEqual(
            'Profile', 
            profile_container.find_element(By.TAG_NAME, 'h1').text
        )
        self.assertEqual(
            r'{"user":{"id":7,"username":"emilly"}}', 
            profile_container.find_element(By.TAG_NAME, 'div').text
        )

    def test_register_jobseeker(self):
        """Test register JobSeeker action"""
        self.selenium.get(f'{CONTAINER_URL}/register')

        # Choose "Job opportunities" modal button
        modal = self.selenium.find_element(
            By.CSS_SELECTOR, 
            "div#headlessui-portal-root"
        )
        modal_buttons = modal.find_elements(By.TAG_NAME, 'button')
        modal_buttons[1].click()

        # Fill form
        form_elements = self.get_auth_form_elements()
        form_elements['username'].send_keys('johndoe')
        form_elements['email'].send_keys('johndoe@test.com')
        form_elements['password'].send_keys('test12345')
        form_elements['cpassword'].send_keys('test12345')
        form_elements['submit'].click()
        
        # Wait (fluently) for the page redirect
        try:
            element = WebDriverWait(
                self.selenium, 
                10, 
                poll_frequency=1, 
                ignored_exceptions=[NoSuchElementException]
            ).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[value="Log in"]'))
            )
            element.click()
        except NoSuchElementException as e:
            print(e)

        login_button = self.selenium.find_element(By.CSS_SELECTOR, '[value="Log in"]')
        self.assertTrue(login_button)