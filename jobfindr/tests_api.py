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

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Test if JSON response is correct and if user was created
        # https://stackoverflow.com/questions/27472663/
        # how-to-use-djangos-assertjsonequal-to-verify-response-of-view-returning-jsonres
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'msg': 'User created!'
            }
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

        # Test if resource was created by status code
        self.assertEqual(
            201, 
            response.status_code, 
            msg="Status code not correct"
        )

        # Test if JSON response is correct and if user was created
        # https://stackoverflow.com/questions/27472663/
        # how-to-use-djangos-assertjsonequal-to-verify-response-of-view-returning-jsonres
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'msg': 'User created!'
            }
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
        
        # Test JSON response status and headers
        self.assertEqual(response.headers.get('Content-Type'), 'application/json')
        self.assertEqual(response.status_code, 409)
        # Test if API returns "User already exists" message
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'msg': 'User already exists'
            }
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
        
        # Test JSON response status and headers
        self.assertEqual(response.headers.get('Content-Type'), 'application/json')
        # Justification of the use of 409 code (not really using a standard)
        # https://stackoverflow.com/questions/3825990/
        # http-response-code-for-post-when-resource-already-exists
        self.assertEqual(response.status_code, 409)
        # Test if API returns "User already exists" message
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'msg': 'User already exists'
            }
        )

    def test_login(self):
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