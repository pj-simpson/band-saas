from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField



class NewsItem(models.Model):
    headline = models.CharField(blank=False,max_length=200)
    summary = models.CharField(blank=False, max_length=400)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,unique=True)
    image = models.ImageField(upload_to="news_item_images/", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_item_page',kwargs={'slug':self.slug})
