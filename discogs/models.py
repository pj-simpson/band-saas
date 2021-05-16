from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class CustomUser(AbstractUser):
    pass

class Release(models.Model):
    title = models.CharField(blank=False,max_length=200)
    info = RichTextUploadingField()
    release_date = models.DateField(blank=False)
    slug = models.SlugField(null=True,unique=True)
    image = models.ImageField(upload_to="discography_images/", blank=True)
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('release_page',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title