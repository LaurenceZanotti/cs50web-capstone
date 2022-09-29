from django.test import TestCase
from jobfindr.models import *

# Create your tests here.
class ProfileModelsTests(TestCase):
    fixtures = ['test_initial_data.json']
    
    def test_save_profile_model(self):
        """Test create a profile and save"""
        # Create profile
        user = JobSeeker.objects.get(pk=3)
        profile = Profile(owner=user)
        profile.save()
        # Test queries
        self.assertTrue(Profile.objects.get(pk=1))
        self.assertTrue(user.profile)