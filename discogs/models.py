from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class CustomUser(AbstractUser):
    pass

class Release(models.Model):
    title = models.CharField(blank=False,max_length=200)
    info = models.TextField()
    release_date = models.DateField(blank=False)
    slug = models.SlugField(null=True,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('release_page',kwargs={'slug':self.slug})