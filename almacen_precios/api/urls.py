from django.urls import path
from .views import ProductList, ProductDetail, TypeOfProductsList, TypeOfProductsDetail, CreateProduct


urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products-create/', CreateProduct.as_view(), name='create-product'),
    path('products/<str:pk>/', ProductDetail.as_view(), name='product-id'),
    path('typeproducts/', TypeOfProductsList.as_view(), name='type-products'),
    path('type-products/<str:pk>/', TypeOfProductsDetail.as_view(), name='type-product-id'),
]
