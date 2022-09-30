from django.test import TestCase
from jobfindr.models import *
from datetime import date
from json import dumps, load

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

        # Complete profile user
        ciclano_user = JobSeeker.objects.create_user(
            username="ciclano",
            first_name="Ciclano",
            last_name="da Silva",
            email="ciclano@ciclano.com", 
            password="test12345"
        )
        # Create profile fields
        contact = Contact.objects.create(
            email="ciclano@ciclano.com", 
            phone="+5511919199192",
            custom_field={
                "instagram": "ciclano",
                "portfolio": "ciclano.dev.br",
                "github": "CiclanoGitAcc"
            }
        )
        skill_react = Skill.objects.create(name="React")
        skill_django = Skill.objects.create(name="Django")
        skill_selenium = Skill.objects.create(name="Selenium")

        # Create complete profile
        profile_title="Full stack Developer"
        profile_about="I craft full-stack web applications. Currently working on a startup using Django, React, MariaDB and Selenium for tests."
        profile_certificates={
            "CS50's Web Programming with Python and JavaScript": "Introduction to the intellectual enterprises of computer science and the art of programming.",
            "Data Analysis": "A course on data analysis",
        }        
        ciclano_profile = Profile.objects.create(
            owner=ciclano_user, 
            title=profile_title,
            about=profile_about,
            contact_info=contact,
            certificates=profile_certificates,
            is_public=True
        )

        # Add academic history and experience
        experience = Experience.objects.create(
            profile=ciclano_profile,
            title="Insurance Assistance CO",
            role="International Assistant",
            start_date=date(2017, 12, 1),
            end_date=date(2020, 2, 27),
            location="Zetaville",
        )
        education_cs50 = Education.objects.create(
            profile=ciclano_profile,
            title="CS50's Introduction to Computer Science",
            teaching_facility="edX",
            start_date=date(2020, 9, 1),
            end_date=date(2020, 12, 15),
            location="edX Platform",
        )
        education_cs50web = Education.objects.create(
            profile=ciclano_profile,
            title="CS50's Web Programming with Python and JavaScript",
            teaching_facility="edX",
            start_date=date(2021, 1, 1),
            end_date=date(2022, 12, 30),
            location="edX Platform",
        )

    def test_save_profile_model(self):
        """Test create a profile and save"""
        # Create profiles
        jobseeker = JobSeeker.objects.get(username='mary')
        jobseeker_profile = Profile(owner=jobseeker)
        jobseeker_profile.save()
        talenthunter = TalentHunter.objects.get(username='edu')
        talenthunter_profile = Profile(owner=talenthunter)
        talenthunter_profile.save()

        # Test queries
        self.assertTrue(Profile.objects.get(fullname='mary'))
        self.assertTrue(jobseeker.profile)
        self.assertTrue(Profile.objects.get(fullname='edu'))
        self.assertTrue(talenthunter.profile)

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
    
    def test_complete_profile(self):
        """Create a complete profile for a user"""
        
        # Create user
        fulano_user = JobSeeker(
            username="fulano",
            first_name="Fulano",
            last_name="da Silva",
            email="fulano@fulano.com", 
            password="test12345"
        )
        fulano_user.save()
        
        # Create profile fields
        contact = Contact(
            email="fulano@fulano.com", 
            phone="+5511919199191",
            custom_field={
                "instagram": "fulano",
                "portfolio": "fulano.dev.br",
                "github": "FulanoGitAcc"
            }
        )
        contact.save()
        skill_html = Skill(name="HTML")
        skill_css = Skill(name="CSS")
        skill_javascript = Skill(name="JavaScript")
        for skill in [skill_html, skill_css,skill_javascript]:
            skill.save()
        

        # Create profile
        profile_title="Full stack Django Developer"
        profile_about="I craft full-stack web applications. Currently working on a \
                job search/talent hunt web application using Django, React, \
                MariaDB and Selenium for tests.",
        profile_certificates={
            "CS50's Introduction to Computer Science": "Introduction to \
                the intellectual enterprises of computer science and the art \
                of programming.",
            "Computer Graphics": "A course on image and video editing and 3D",
        },
        fulano_profile = Profile(
            owner=fulano_user, 
            title=profile_title,
            about=profile_about,
            contact_info=contact,
            certificates=profile_certificates,
            is_public=True
        )
        fulano_profile.save()

        # Add skills to profile
        for skill in [skill_html, skill_css,skill_javascript]:
            fulano_profile.skills.add(skill)

        # Add academic history and experience
        experience = Experience(
            profile=fulano_profile,
            title="Insurance Assistance CO",
            role="International Assistant",
            start_date=date(2017, 12, 1),
            end_date=date(2020, 2, 27),
            location="Zetaville",
        )
        experience.save()
        education_cs50 = Education(
            profile=fulano_profile,
            title="CS50's Introduction to Computer Science",
            teaching_facility="edX",
            start_date=date(2020, 9, 1),
            end_date=date(2020, 12, 15),
            location="edX Platform",
        )
        education_cs50web = Education(
            profile=fulano_profile,
            title="CS50's Web Programming with Python and JavaScript",
            teaching_facility="edX",
            start_date=date(2021, 1, 1),
            end_date=date(2022, 12, 30),
            location="edX Platform",
        )
        for education in [education_cs50, education_cs50web]:
            education.save()

        # Check if fields exist
        self.assertTrue(fulano_profile)
        self.assertFalse(fulano_profile.profile_picture)
        for field in [
            fulano_profile.owner,
            fulano_profile.fullname,
            fulano_profile.title,
            fulano_profile.about,
            fulano_profile.contact_info,
            fulano_profile.experience.all(),
            fulano_profile.education.all(),
            fulano_profile.certificates,
            fulano_profile.skills,
            fulano_profile.is_public,

        ]:
            self.assertTrue(field)

        # Check if fields are correct
        self.assertEqual('Fulano da Silva', fulano_profile.fullname)
        self.assertEqual(profile_title, fulano_profile.title)
        self.assertEqual(profile_about, fulano_profile.about)
        self.assertEqual(profile_certificates, fulano_profile.certificates)

    def test_get_simple_profile_as_dict(self):
        """Get simple profile as a dictionary"""
        johndoe = Profile.objects.get(fullname="John Doe")
        self.assertDictEqual(
            {
                'id': 8,
                'owner': 15,
                'profile_picture': None,
                'fullname': 'John Doe',
                'title': None,
                'about': None,
                'contact_info': None,
                'education': [],
                'experience': [],
                'certificates': None, 
                'is_public': False, 
                'skills': []
            },
            johndoe.get_profile_as_dict()
        )

    def test_get_complete_profile_as_dict(self):
        """Get complete profile as a dictionary"""
        ciclano = JobSeeker.objects.get(username="ciclano")
        profile = Profile.objects.get(pk=ciclano.profile.id)
        for skill in Skill.objects.all():
            profile.skills.add(skill)
        profile.save()
        profile_as_dict = profile.get_profile_as_dict()
        # Test contents
        test_file = open('jobfindr/fixtures/test_complete_profile.json')
        test_data = load(test_file)
        self.assertJSONEqual(dumps(test_data, default=str), dumps(profile_as_dict, default=str))
        