from django.contrib import admin
from .models import Product, TypeOfProducts
# Register your models here.
admin.site.register(Product)
admin.site.register(TypeOfProducts)