import profile
from django.test import TestCase
from django.forms.models import model_to_dict
from django.urls import is_valid_path
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

    def test_complete_profile_edit(self):
        """
        Check complete new profile edit 
        (a profile with all fields altered, and more than 1 related object)
        """
        # Get profile
        mary = Profile.objects.get(fullname="mary")
        new_mary = mary.get_profile_as_dict()
        new_mary['title'] = "Fullstack Engineer"
        new_mary['about'] = "I craft web application with Django and NextJS"
        new_mary['certificates'] = {
            "Year One Web Dev": "Basics to advanced in one year course about web development",
            "CTFBR": "Brazilian Capture The Flag 2nd place winner"
        }
        new_mary['is_public'] = True

        # Validate profile_form
        profile_form = ProfileForm(new_mary, instance=mary)
        self.assertTrue(profile_form.is_valid())

        if profile_form.is_valid():
            # Update or create related objects

            ######################
            # Experience objects #
            ######################
            # This item should be created
            experience1 = {
                "title": "Senior Developer",
                "role": "ABC Company",
                "description": "Lead a web dev team to launch a new version of a product for 1m users",
                "start_date": "2020-01-01",
                "location": "Park St. Ave 1395, New York, NY, USA"
            }
            # This item should be created
            experience2 = {
                "title": "Software Developer",
                "role": "DEF Company",
                "description": "Lead a web dev team to launch a new version of a product for 1m users",
                "start_date": "2019-01-01",
                "location": "Park St. Ave 1395, New York, NY, USA"
            }
            # This item should update the experience2 above
            experience_updated = {
                "id": 2,
                "title": "Junior Software Developer",
                "role": "DEF Company",
                "description": "Learning internship",
                "start_date": "2014-01-01",
                "location": "Park St. Ave 1395, New York, NY, USA"
            }
            ###########################################
            # Experience validation, update or create #
            ###########################################
            for exp in [experience1, experience2, experience_updated]:
                exp_form = ExperienceForm(exp)
                self.assertTrue(exp_form.is_valid())
                if exp_form.is_valid():
                    # https://stackoverflow.com/questions/2297820/django-forms-with-get-or-create
                    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#update-or-create
                    new, created = Experience.objects.update_or_create(
                        id=exp.get('id'), 
                        defaults={
                            'title': exp_form.cleaned_data['title'],
                            'role': exp_form.cleaned_data['role'],
                            'description': exp_form.cleaned_data['description'],
                            'start_date': exp_form.cleaned_data['start_date'],
                            'end_date': exp_form.cleaned_data['end_date'],
                            'location': exp_form.cleaned_data['location'],
                        }
                    )
                    mary.experience.add(new) if created else None
                
            #####################
            # Education objects #
            #####################
            # This item should be created
            education1 = {
                "title": "Computer Science",
                "teaching_facility": "Harvard University",
                "description": "COMPSCI bachelors course on Harvard",
                "start_date": "2015-01-01",
                "location": "Park St. Ave 1395, New York, NY, USA"
            }
            # This item should be created
            education2 = {
                "title": "Mathematics and Engineering",
                "teaching_facility": "MIT",
                "description": "Mathematics to become a master and to apply on our daily lives!",
                "start_date": "2015-01-01",
                "end_date": "2016-01-01",
            }
            # This should update education1
            education_update = {
                "id": 1,
                "title": "Computer Science",
                "teaching_facility": "Harvard University",
                "description": "COMPSCI bachelors course on Harvard with updated text",
                "start_date": "2013-01-01",
                "end_date": "2017-01-01",
                "location": "Park St. Ave 1395, New York, NY, USA"
            }
            ##########################################
            # Education validation, update or create #
            ##########################################
            for edu in [education1, education2, education_update]:
                edu_form = EducationForm(edu)
                if edu_form.is_valid():
                    new, created = Education.objects.update_or_create(
                        id=edu.get('id'), 
                        defaults={
                            'title': edu_form.cleaned_data['title'],
                            'teaching_facility': edu_form.cleaned_data['teaching_facility'],
                            'start_date': edu_form.cleaned_data['start_date'],
                            'end_date': edu_form.cleaned_data['end_date'],
                            'location': edu_form.cleaned_data['location'],
                        }
                    )
                    mary.education.add(new) if created else None

            ##################
            # Skills objects #
            ##################
            skills_input = ["HTML", "CSS", "JavaScript", "React", "Selenium", "CI/CD", "git", "HTML"]
            #######################################
            # Skills validation, update or create #
            #######################################
            for skill in skills_input:
                skill_form = SkillForm({"name": skill})
                if skill_form.is_valid():
                    new, created = Skill.objects.update_or_create(
                        name=skill_form.cleaned_data.get("name"),
                        defaults={"name": skill_form.cleaned_data.get("name")}
                    )
                    mary.skills.add(new) if created else None

            ###################
            # Contact objects #
            ###################
            # This should create contact
            contact = {
                "email": "mary@test.com",
                "phone": "+553245315103",
            }
            # This should update contact
            contact_update = {
                "id": 1,
                "email": "mary@test.com",
                "phone": "+553245315103",
                "custom_field": {
                    "instagram": "marymarymaryacc",
                    "github": "marymarygithubb"
                }
            }
            ########################################
            # Contact validation, update or create #
            ########################################
            # Obs: In practice, there won't be lists of contacts as input
            # This is just to simulate a create and update
            for ct in [contact, contact_update]:
                ct_form = ContactForm(ct)
                if ct_form.is_valid():
                    new, created = Contact.objects.update_or_create(
                        id=ct.get("id"),
                        defaults={
                            'email': ct_form.cleaned_data.get("email"),
                            'phone': ct_form.cleaned_data.get("phone"),
                            'custom_field': ct_form.cleaned_data.get("custom_field") or {},
                        }
                    )
                    mary.contact_info = new
                    mary.save()