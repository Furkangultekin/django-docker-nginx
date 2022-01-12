from django.db import models
from django.contrib.auth.models import AbstractUser

#USER Model
class User(AbstractUser):
    name = models.CharField(max_length=255) #user name
    email = models.CharField(max_length=255,unique=True) #user email
    password = models.CharField(max_length=255)#user password
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
