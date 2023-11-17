from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(default="",max_length=100)
    profile = models.CharField(default="",max_length=5000)
    email = models.CharField(default="",max_length=100)
    password = models.CharField(default="",max_length=100)
