from django.urls import path
from .views import ProductList, ProductDetail, TypeOfProductsList, TypeOfProductsDetail, CreateProduct, CreateTypeOfProductsList, get_routes


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('', get_routes, name='routes'),
    path('products-create/', CreateProduct.as_view(), name='create-product'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-id'),
    path('typeproducts/', TypeOfProductsList.as_view(), name='type-products'),
    path('typeproduct-create/', CreateTypeOfProductsList.as_view(), name='type-products'),
    path('typeproduct/<int:pk>/', TypeOfProductsDetail.as_view(), name='type-product-id'),
]
