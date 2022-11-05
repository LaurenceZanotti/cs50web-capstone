from django.forms import ModelForm
from jobfindr.models import Profile, Experience, Education, Contact, Skill

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'profile_picture',
            'fullname',
            'title',
            'about',
            'contact_info',
            'certificates',
            'skills',
            'is_public',
        ]

class ExperienceForm(ModelForm):

    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'start_date',
            'end_date',
            'location',
            'role',
            'description',
        ]

class EducationForm(ModelForm):

    class Meta:
        model = Education
        fields = [
            'id',
            'title',
            'start_date',
            'end_date',
            'location',
            'teaching_facility',
        ]

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = [
            'id',
            'email',
            'phone',
            'custom_field',
        ]

class SkillForm(ModelForm):

    class Meta:
        model = Skill
        fields = ['name']