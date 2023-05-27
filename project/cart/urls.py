from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    # Добавьте дополнительные URL-шаблоны, если необходимо
]