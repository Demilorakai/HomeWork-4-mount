from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    prise = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=False)


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)


class Pricing(models.Model):
    name = models.CharField(max_length=255)
    full_support = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=False)
    duration = models.IntegerField(default=0)
    storage = models.IntegerField(default=0)
    prise = models.IntegerField(default=0)
