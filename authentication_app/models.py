from django.db import models

# Create your models here.

# from django.db import models
# from django.contrib.auth.models import User


class CustomUser(models.Model):
    username = models.CharField(null= False, blank=False, unique=False, max_length = 30)
    first_name = models.CharField(null= True, blank= True, unique= False, max_length = 20)
    last_name = models.CharField(null= False, blank= False, unique= False, max_length = 20)
    email = models.CharField(null= False, blank = False, unique= True, max_length=30)
    password = models.CharField(null = False, blank = False, unique=True, max_length= 100)


# User.objects.create_user(username)