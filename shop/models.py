from django.db import models

class Product(models.Model):
    name = models.CharField(blank=False,max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
