from django.urls import path
from .views import ProductList, ProductDetail, create_product, update_product

app_name = 'products'


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('create/', create_product, name='product_create'),
    path('<int:product_id>/update/', update_product, name='product_update')

]