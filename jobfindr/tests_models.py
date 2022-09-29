from django.test import TestCase
from jobfindr.models import *

# Create your tests here.
class ProfileModelsTests(TestCase):
    fixtures = ['test_initial_data.json']
    
    def setUp(self):
        # Fullname user and profile creation
        # When the user creates a profile, the save method will 
        # use first and last name to create a fullname field
        # or username
        fullname_user = JobSeeker.objects.create_user(
            username="johndoe",
            first_name="John",
            last_name="Doe",
            email="johndoe@johndoe.com", 
            password="test12345"
        )
        johndoe_profile = Profile.objects.create(owner=fullname_user)
        
        # Only username user and profile creation
        only_nickname_user = TalentHunter.objects.create_user(
            username="janedoe",
            email="janedoe@janedoe.com",
            password="test12345"
        )
        janedoe_profile = Profile.objects.create(owner=only_nickname_user)

    def test_save_profile_model(self):
        """Test create a profile and save"""
        # Create profile
        user = JobSeeker.objects.get(pk=3)
        profile = Profile(owner=user)
        profile.save()
        # Test queries
        self.assertTrue(Profile.objects.get(pk=7))
        self.assertTrue(user.profile)

    def test_profile_fullname_with_username(self):
        """Test if profile fullname is using username 
        when there is no first and last name fields"""
        profile = Profile.objects.get(fullname="John Doe")
        self.assertTrue(profile)
        self.assertEqual("John Doe", profile.fullname)

    def test_profile_fullname_with_fullname(self):
        """Test if profile fullname is using username 
        when there is first and last name fields"""
        profile = Profile.objects.get(fullname="janedoe")
        self.assertTrue(profile)
        self.assertEqual("janedoe", profile.fullname)