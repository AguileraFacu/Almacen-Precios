from django.db import models
import uuid

# Create your models here.
class TypeOfProducts(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True),
    type_product = models.ForeignKey(TypeOfProducts, on_delete=models.CASCADE, related_name='type_product')
    
    def __str__(self):
        return self.name