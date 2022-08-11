from django.contrib import admin
from .models import Product, Categories, Pricing

# Register your models here.

admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Pricing)