from django.test import TestCase
from django.forms.models import model_to_dict
from jobfindr.models import *
from jobfindr.forms import *


class ProfileFormTests(TestCase):
    """Checks whether a ProfileForm is working"""
    fixtures = ['test_initial_data_v2.json']

    def test_simple_profile_edit(self):
        """Check simple profile edit (no related models editing)"""
        # Get profile
        mary = Profile.objects.get(fullname="mary")
        
        # Prepare form input
        # data = model_to_dict(mary)
        data = mary.get_profile_as_dict()
        data['title'] = "Fullstack Engineer"
        data['about'] = "I craft web application with Django and NextJS"
        data['certificates'] = {
            "Year One Web Dev": "Basics to advanced in one year course about web development",
            "CTFBR": "Brazilian Capture The Flag 2nd place winner"
        }
        data['is_public'] = True


        # Get bound form
        profile_form = ProfileForm(data, instance=mary)

        # Check if it is valid
        is_valid = profile_form.is_valid()
        self.assertTrue(is_valid)
        