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
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = None
    # profile_picture = models.ImageField(upload_to="")
    # ImageField needs Pillow library
    fullname = models.CharField(max_length=254)
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