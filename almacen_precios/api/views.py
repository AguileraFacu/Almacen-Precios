from .serializer import ProductSerializer, TypeOfProductSerializer
from .models import Product, TypeOfProducts
from rest_framework import generics
# Create your views here.


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class TypeOfProductsList(generics.ListCreateAPIView):
    serializer_class = TypeOfProductSerializer
    queryset = TypeOfProducts.objects.all()

class TypeOfProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TypeOfProductSerializer
    queryset = TypeOfProducts.objects.all()