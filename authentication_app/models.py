from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import UserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    username = models.CharField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(50), MinLengthValidator(5)],
        unique=True,
        max_length=50
    )
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(null=False, blank=False, unique=True, max_length=150)
    full_name = models.CharField(
        null=True,
        blank=True,
        validators=[MaxLengthValidator(100), MinLengthValidator(2)],
        max_length=50
    )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'full_name', 'password']