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
    target_url = "/api/register"

    def test_register_jobseeker(self):
        """Tests the sign up of a Job Seeker user"""
        c = Client()
        response = c.post(self.target_url, {
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
        response = c.post(self.target_url, {
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