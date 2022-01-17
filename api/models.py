# Create your models here.
from django.db import models
from authentication_app.models import CustomUser

class Blogs(models.Model):
    tag = models.CharField(
        max_length=15,
        null=True
    )
    article = models.TextField(max_length=None, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(
        max_length=80,
        null=False
    )
    summary = models.CharField(
        max_length=200,
    )
    imageUrl = models.URLField()
