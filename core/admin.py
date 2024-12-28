from django.contrib import admin
from .models import Product, Banner

# Registering the models to the Django admin site
admin.site.register(Product)
admin.site.register(Banner)
