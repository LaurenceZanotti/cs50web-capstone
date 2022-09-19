import re
from urllib import request
from django.test import TestCase, Client

# Create your tests here.
class IndexTests(TestCase):
    """Welcome page test suite"""
    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

class AuthTests(TestCase):
    """Authentication API test suite"""
    target_url_register = "/api/register"
    target_url_login = "/api/login"
    target_url_user = "/api/user"
    target_url_logout = "/api/logout"

    # Utility functions
    def check_json_response(self, response, status_code, json_message):
        """Check if JSON response is correct"""
        # Test JSON response status and headers
        self.assertEqual(response.headers.get('Content-Type'), 'application/json')
        self.assertEqual(response.status_code, status_code)
        # Test if API returns the appropriate message
        self.assertJSONEqual(
            str(response.content, encoding='utf8'), json_message
        )

    # Tests
    def test_register_jobseeker(self):
        """Tests the sign up of a Job Seeker user"""
        c = Client()
        response = c.post(
            self.target_url_register, 
            {
                'username': 'dine',
                'email': 'dine@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            }, 
            content_type='application/json'
        )

        # Test if JSON response is correct
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User created!'
            },
            status_code=201
        )

    def test_register_talenthunter(self):
        """Tests the sign up of a Talent Hunter user"""
        c = Client()
        response = c.post(
            self.target_url_register, 
            {
                'username': 'emilly',
                'email': 'emilly@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'talenthunter'
            }, 
            content_type='application/json'
        )

        # Test if JSON response is correct
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User created!'
            },
            status_code=201
        )

    def test_register_jobseeker_already_exists(self):
        """Tests if the API returns user already exists response"""
        c = Client()
        response = c.post(
            self.target_url_register, 
            {
                'username': 'johndoe',
                'email': 'johndoe@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            }, 
            content_type='application/json'
        )

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Repeat request and form information
        response = c.post(
            self.target_url_register, 
            {
                'username': 'johndoe',
                'email': 'johndoe@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            },
            content_type='application/json'
        )
        
        # Test if JSON response is correct
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User already exists'
            },
            status_code=409
        )

    def test_register_talenthunter_already_exists(self):
        """Tests if the API returns user already exists response"""
        c = Client()
        response = c.post(
            self.target_url_register, 
            {
                'username': 'johndoe',
                'email': 'johndoe@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'talenthunter'
            },
            content_type='application/json'
        )

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Repeat request and form information
        response = c.post(
            self.target_url_register, 
            {
                'username': 'johndoe',
                'email': 'johndoe@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'talenthunter'
            },
            content_type='application/json'
        )
        
        # Test if JSON response is correct
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User already exists'
            },
            status_code=409
        )

    def test_register_empty_field(self):
        """Test if any empty field is correctly handled"""
        c = Client()

        # Prepare empty form test cases
        form_input_test_cases = [
            # All fields are blank case
            {
                'username': '',
                'email': '',
                'password': '',
                'cpassword': '',
                'usertype': ''
            },
            # One of the fields cases
            {
                'username': 'testuser',
                'email': '',
                'password': '',
                'cpassword': '',
                'usertype': ''
            },
            {
                'username': '',
                'email': 'test@test.com',
                'password': '',
                'cpassword': '',
                'usertype': ''
            },
            {
                'username': '',
                'email': '',
                'password': 'secrettest',
                'cpassword': '',
                'usertype': ''
            },
            {
                'username': '',
                'email': '',
                'password': '',
                'cpassword': 'secrettest',
                'usertype': ''
            },
            {
                'username': '',
                'email': '',
                'password': '',
                'cpassword': '',
                'usertype': 'talenthunter'
            },
            {
                'username': '',
                'email': '',
                'password': '',
                'cpassword': '',
                'usertype': 'jobseeker'
            },
        ]

        # For each scenario, test form submission response
        for input in form_input_test_cases:
            response = c.post(
                self.target_url_register, 
                input,
                content_type='application/json'
            )

            # Check if all fields are empty response
            self.check_json_response(
                response=response,
                json_message={
                    'msg': 'There must be no empty fields'
                },
                status_code=400
            )


    def test_register_passwords_doesnt_match(self):
        """Test register passwords doesn't match response"""
        c = Client()

        # Request
        response = c.post(
            self.target_url_register, 
            {
                'username': 'testuser',
                'email': 'test@test.com',
                'password': 'secret',
                'cpassword': 'secretwrong',
                'usertype': 'jobseeker'
            },
            content_type='application/json'
        )

        # Check if response reflects wrong password confirmation
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'Password and confirmation password doesn\'t match'
            },
            status_code=400
        )

    def test_register_usertype_not_specified(self):
        """Test if usertype is not specified response"""
        c = Client()

        # First case scenario with all form fields except usertype
        response = c.post(
            self.target_url_register, 
            {
                'username': 'testuser',
                'email': 'test@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': ''
            },
            content_type='application/json'
        )
        
        # First response check
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'There must be no empty fields'
            },
            status_code=400
        )

        # Second case scenario with all form fields and wrong usertype
        response = c.post(
            self.target_url_register, 
            {
                'username': 'testuser',
                'email': 'test@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'another'
            },
            content_type='application/json'
        )
        
        # Second response check
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User must tell if they are looking for jobs or talents'
            },
            status_code=400
        )

    def test_login_jobseeker(self):
        """Test user login"""
        c = Client()

        # Sign up user
        response = c.post(
            self.target_url_register, 
            {
                'username': 'dine',
                'email': 'dine@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            },
            content_type='application/json'
        )

        # Attempt to log in user
        response = c.post(
            self.target_url_login, 
            {
                'username': 'dine',
                'password': 'secret'
            }, 
            content_type='application/json'
        )

        # Test if response is correct
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Logged in successfully!'
            },
            status_code=200
        )

    def test_login_talenthunter(self):
        """Test user login"""
        c = Client()

        # Sign up user
        response = c.post(
            self.target_url_register, 
            {
                'username': 'emilly',
                'email': 'emilly@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'talenthunter'
            },
            content_type='application/json'
        )

        # Attempt to log in user
        response = c.post(
            self.target_url_login,
            {
                'username': 'emilly',
                'password': 'secret'
            },
            content_type='application/json'
        )

        # Test if response is correct
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Logged in successfully!'
            },
            status_code=200
        )

    def test_login_invalid(self):
        """Test invalid login"""
        c = Client()

        # Attempt to log in user that doesn't exists
        response = c.post(
            self.target_url_login, 
            {
                'username': 'emilly',
                'password': 'secret'
            },
            content_type='application/json'
        )

        # Test response
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Invalid username and/or password.'
            },
            status_code=401
        )

        # Sign a user
        response = c.post(
            self.target_url_register, 
            {
                'username': 'dine',
                'email': 'dine@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            },
            content_type='application/json'
        )

        # Attempt to log in user with wrong credentials
        response = c.post(
            self.target_url_login, 
            {
                'username': 'dine',
                'password': 'secret1'
            },
            content_type='application/json'
        )

        # Test response
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Invalid username and/or password.'
            },
            status_code=401
        )

    def test_login_empty_form(self):
        """Test login form empty response"""
        c = Client()

        # Prepare test scenarios
        input_scenarios = [
            { 'username': '', 'password': '' },
            { 'username': 'dine', 'password': '' },
            { 'username': '', 'password': 'secret1' },
        ]

        # Test each form input scenario
        for input in input_scenarios:
            # Get response
            response = c.post(
                self.target_url_login, 
                input,
                content_type='application/json'
            )

            # Test if all inputs are empty response
            self.check_json_response(
                response=response,
                json_message={
                    'msg': 'You must provide your username and password'
                },
                status_code=400
            )

    def test_login_wrong_http_method(self):
        """Test redirect response when wrong HTTP method is used"""
        c = Client()

        response = c.get(self.target_url_login)
        self.assertEqual(302, response.status_code)

        response = c.delete(self.target_url_login)
        self.assertEqual(302, response.status_code)

        response = c.put(self.target_url_login)
        self.assertEqual(302, response.status_code)

        response = c.patch(self.target_url_login)
        self.assertEqual(302, response.status_code)

    def test_retrieve_anonymous_user_info(self):
        """Test if anonymous user information is being retrieved"""
        c = Client()

        response = c.get(self.target_url_user)

        # Log user in
        self.check_json_response(
            response=response,
            json_message={
                'user': None,
                'error': 'Not authenticated'
            },
            status_code=403
        )

    def test_retrieve_user_info(self):
        """Test if signed in user information is being retrieved"""
        c = Client()

        # Sign up a user
        response = c.post(
            self.target_url_register, 
            {
                'username': 'dine',
                'email': 'dine@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            }, 
            content_type='application/json'
        )

        # Sign user in
        response = c.post(
            self.target_url_login, 
            {
                'username': 'dine',
                'password': 'secret'
            },
            content_type='application/json'
        )

        # Retrieve logged in user information
        response = c.get(self.target_url_user)
        id = response.json()['user']['id']
        self.check_json_response(
            response=response,
            json_message={
                    'user': {
                    'id': id,
                    'username': 'dine'
                }
            },
            status_code=200
        )

    def test_logout(self):
        """Test if logout is working"""
        c = Client()

         # Sign up a user
        response = c.post(
            self.target_url_register, 
            {
                'username': 'dine',
                'email': 'dine@test.com',
                'password': 'secret',
                'cpassword': 'secret',
                'usertype': 'jobseeker'
            },
            content_type='application/json'
        )
        self.assertEqual(201, response.status_code)

        # Sign user in
        response = c.post(
            self.target_url_login, 
            {
                'username': 'dine',
                'password': 'secret'
            },
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)

        response = c.get(self.target_url_logout)
        self.assertEqual(200, response.status_code)
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'Logged out'
            },
            status_code=200
        )

    def test_logout_wrong_http_method(self):
        """Test logout redirect response when wrong HTTP method is used"""
        c = Client()

        response = c.get(self.target_url_logout)
        self.assertEqual(302, response.status_code)

        response = c.delete(self.target_url_logout)
        self.assertEqual(302, response.status_code)

        response = c.put(self.target_url_logout)
        self.assertEqual(302, response.status_code)

        response = c.patch(self.target_url_logout)
        self.assertEqual(302, response.status_code)

    def test_logout_login_required_redirect(self):
        """Test logout redirect when user is not authenticated"""
        c = Client()

        response = c.get(self.target_url_logout)

        self.assertEqual(302, response.status_code)