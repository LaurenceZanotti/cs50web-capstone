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