from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(blank=False,max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})
