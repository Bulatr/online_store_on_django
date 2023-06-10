from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView
from .models import Product, Category
from .forms import SortForm, PriceForm
from .filters import ProductFilter


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class ProductList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'product_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.

    context_object_name = 'products'

    # пагинация
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort_form = SortForm(self.request.GET)
        price_form = PriceForm(self.request.GET)
        context['sort_form'] = sort_form
        context['price_form'] = price_form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        price_range = self.request.GET.get('price_range')  # Получаем выбранный диапазон цен из GET-параметра
        if price_range:
            min_price, max_price = price_range.split('-')
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'name':
            queryset = queryset.order_by('name')
        if sort_by == 'price':
            queryset = queryset.order_by('price')
        elif sort_by == 'price-desc':
            queryset = queryset.order_by('-price')
        return queryset

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


