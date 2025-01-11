from rest_framework import serializers
from .models import TypeOfProducts, Product

class TypeOfProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfProducts
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'