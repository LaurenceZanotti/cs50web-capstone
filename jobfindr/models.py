from django.forms.models import model_to_dict
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # This class is used for JobSeeker and TalentHunter users
    pass

class JobSeeker(User):
    # jobs_subscribed = None
    pass

class TalentHunter(User):
    # organizations = None
    pass

class Profile(models.Model):
    # Utility methods
    def user_directory_path(self, filename):
        # Code based on Django Docs snippet
        # https://docs.djangoproject.com/en/4.1/ref/
        # models/fields/#django.db.models.FileField.upload_to
        return f'pros/{self.user.id}/{filename}'

    # Fields
    owner = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="profile"
    )
    profile_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    fullname = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    about = models.TextField(max_length=1024, null=True, blank=True)
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield
    contact_info = models.ForeignKey(
        'Contact', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="user_profile",
    )
    # experience = See Experience model
    # education = See Education model
    # Certificates have a list of items with 
    # title and description key/value pairs
    certificates = models.JSONField(null=True, blank=True)
    skills = models.ManyToManyField(
        'Skill', 
        related_name="user_profile",
        blank=True
    )
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Overidden save method to fill fullname field
        
        Save the current instance. Override this in a subclass if you want to
        control the saving process.

        The 'force_insert' and 'force_update' parameters can be used to insist
        that the "save" must be an SQL insert or update (or equivalent for
        non-SQL backends), respectively. Normally, they should not be set.
        """
        # Fill fullname field if it is None
        # https://stackoverflow.com/questions/44421024
        # /django-model-field-with-default-value-from-another-model
        if self.fullname is None:
            self.fullname =  f'{self.owner.first_name} {self.owner.last_name}' \
                if self.owner.first_name and self.owner.last_name else \
                self.owner.username
        super(Profile, self).save(*args, **kwargs)

    def get_profile_as_dict(self):
        """
        Return profile as a dictionary
        
        Implementation based on:
        https://stackoverflow.com/questions/21925671/convert-django-model-object-to-dict-with-all-of-the-fields-intact
        """
        profile = model_to_dict(self)
        # Add fields not included with model_to_dict()
        profile['profile_picture'] = self.profile_picture if self.profile_picture else None
        profile['experience'] = list([model_to_dict(exp, exclude=['profile']) for exp in self.experience.all()])
        profile['education'] = list([model_to_dict(edu, exclude=['profile']) for edu in self.education.all()])
        profile['skills'] = list(skill.name for skill in profile['skills'])
        return profile

    def is_owner(self, user):
        """
        Returns if the a user is the profile's owner
        
        Parameter user should most likely be the request.user

        But this function can be used with any User object

        """
        if user.is_anonymous:
            return None
        return user.id == self.owner.id


class Event(models.Model):
    """Abstract class for Experience and Education"""
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True

class Experience(Event):
    profile = models.ForeignKey(
        Profile, 
        null=True,
        on_delete=models.CASCADE,
        related_name="experience"
    )
    role = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, default='', blank=True, null=True)

class Education(Event):
    profile = models.ForeignKey(
        Profile, 
        null=True,
        on_delete=models.CASCADE,
        related_name="education"
    )
    teaching_facility = models.CharField(max_length=128)

class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    custom_field = models.JSONField()