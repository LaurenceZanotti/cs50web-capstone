from django.test import TestCase, Client

DOMAIN = 'host.docker.internal'
CONTAINER_URL = f'http://{DOMAIN}:3000'

# Create your tests here.
class IndexTests(TestCase):
    def test_index(self):
        c = Client()
        response = c.get("/api/")
        self.assertEqual(response.status_code, 200)

class AuthTests(TestCase):
    target_url_register = "/api/register"
    target_url_login = "/api/login"
    target_url_user = "/api/user"

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
        response = c.post(self.target_url_register, {
            'username': 'dine',
            'email': 'dine@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })

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
        response = c.post(self.target_url_register, {
            'username': 'emilly',
            'email': 'emilly@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'talenthunter'
        })

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
        response = c.post(self.target_url_register, {
            'username': 'johndoe',
            'email': 'johndoe@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Repeat request and form information
        response = c.post(self.target_url_register, {
            'username': 'johndoe',
            'email': 'johndoe@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })
        
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
        response = c.post(self.target_url_register, {
            'username': 'johndoe',
            'email': 'johndoe@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'talenthunter'
        })

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Repeat request and form information
        response = c.post(self.target_url_register, {
            'username': 'johndoe',
            'email': 'johndoe@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'talenthunter'
        })
        
        # Test if JSON response is correct
        self.check_json_response(
            response=response,
            json_message={
                'msg': 'User already exists'
            },
            status_code=409
        )

    def test_login_jobseeker(self):
        """Test user login"""
        c = Client()

        # Sign up user
        response = c.post(self.target_url_register, {
            'username': 'dine',
            'email': 'dine@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })

        # Attempt to log in user
        response = c.post(self.target_url_login, {
            'username': 'dine',
            'password': 'secret'
        })

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
        response = c.post(self.target_url_register, {
            'username': 'emilly',
            'email': 'emilly@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'talenthunter'
        })

        # Attempt to log in user
        response = c.post(self.target_url_login, {
            'username': 'emilly',
            'password': 'secret'
        })

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
        response = c.post(self.target_url_login, {
            'username': 'emilly',
            'password': 'secret'
        })

        # Test response
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Invalid username and/or password.'
            },
            status_code=401
        )

        # Sign a user
        response = c.post(self.target_url_register, {
            'username': 'dine',
            'email': 'dine@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })

        # Attempt to log in user with wrong credentials
        response = c.post(self.target_url_login, {
            'username': 'dine',
            'password': 'secret1'
        })

        # Test response
        self.check_json_response(
            response=response, 
            json_message={
                'msg': 'Invalid username and/or password.'
            },
            status_code=401
        )

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
        response = c.post(self.target_url_register, {
            'username': 'dine',
            'email': 'dine@test.com',
            'password': 'secret',
            'cpassword': 'secret',
            'usertype': 'jobseeker'
        })

        # Sign user in
        response = c.post(self.target_url_login, {
            'username': 'dine',
            'password': 'secret'
        })

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