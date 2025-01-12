from .serializer import ViewProductSerializer, TypeOfProductSerializer, CreateProductSerializer
from .models import Product, TypeOfProducts
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            "GET": 'products/'
        },
        {
            "POST": 'products-create/'
        },
        {
            "GET": 'product/id/'
        },
        {
            "GET": 'typeproducts/'
        },
        {
            "GET": 'typeproduct/id/'
        },
        {
            "POST": 'typeproduct-create/'
        },
    ]
    return Response(routes)
class ProductList(generics.ListAPIView):
    serializer_class = ViewProductSerializer
    queryset = Product.objects.all()

class CreateProduct(generics.CreateAPIView):
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()

class TypeOfProductsList(generics.ListAPIView):
    serializer_class = TypeOfProductSerializer
    queryset = TypeOfProducts.objects.all()

class CreateTypeOfProductsList(generics.CreateAPIView):
    serializer_class = TypeOfProductSerializer
    queryset = TypeOfProducts.objects.all()

class TypeOfProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TypeOfProductSerializer
    queryset = TypeOfProducts.objects.all()