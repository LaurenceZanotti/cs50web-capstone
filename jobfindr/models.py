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
        return f'pros/{self.user.id}/{filename}'

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


    # Fields
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path)
    fullname = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    about = models.TextField(max_length=1024, null=True, blank=True)
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield
    contact_info = models.ForeignKey(
        'Contact', 
        related_name="user_profile"
    )
    experience = models.ForeignKey(
        'Experience', 
        on_delete=models.SET_NULL, 
        related_name="user_profile"
    )
    education = models.ForeignKey(
        'Education', 
        on_delete=models.SET_NULL, 
        related_name="user_profile"
    )
    # Certificates have a list of items with 
    # title and description key/value pairs
    certificates = models.JSONField()
    skills = models.ManyToManyField(
        'Skill', 
        on_delete=models.SET_NULL,
        related_name="user_profile"
    )
    is_public = models.BooleanField(default=False)



class Event(models.Models):
    """Abstract class for Experience and Education"""
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        abstract = True

class Experience(Event):
    role = models.CharField(max_length=128)

class Education(Event):
    course = models.CharField(max_length=128)

class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    custom_field = models.JSONField()