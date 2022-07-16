from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    prise = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=255)
    prise = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
