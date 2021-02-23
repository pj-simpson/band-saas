from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Release(models.Model):
    title = models.CharField(blank=False,max_length=200)
    info = models.TextField()
    release_date = models.DateField(blank=False)