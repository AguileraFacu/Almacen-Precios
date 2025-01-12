from rest_framework import serializers
from .models import TypeOfProducts, Product

class TypeOfProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfProducts
        fields = '__all__'

class ViewProductSerializer(serializers.ModelSerializer):
    type_product = serializers.CharField(source='type_product.name')
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'type_product')
        
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
