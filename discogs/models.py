from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from solo.models import SingletonModel


class HomePage(SingletonModel):
    page_info = RichTextUploadingField()

class CustomUser(AbstractUser):
    pass

class Project(models.Model):
    name = models.CharField(blank=False, max_length=200)
    table_header_color = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Format(models.Model):
    name = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.name


class Release(models.Model):
    title = models.CharField(blank=False, max_length=200)
    info = RichTextUploadingField()
    release_date = models.DateField(blank=False)
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to="discography_images/", blank=True)
    link = models.URLField(blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    format = models.ForeignKey(Format,on_delete=models.CASCADE,null=True)
    label = models.CharField(blank=True, default='#FFFFFF',max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("release_page", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


