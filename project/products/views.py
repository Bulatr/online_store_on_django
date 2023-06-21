from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView
from .models import Product, Category
from .forms import SortForm, PriceForm
from .filters import ProductFilter
from .forms import ProductForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy


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
        # Получение текущего номера страницы
        page_number = self.request.GET.get('page')

        # Установка текущего номера страницы в параметры формы
        sort_form = SortForm(self.request.GET, initial={'page': page_number})
        price_form = PriceForm(self.request.GET, initial={'page': page_number})
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

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

# Обработка данных формы
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product_id = product.id
            # Дополнительные действия после сохранения формы
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # после сохранения перенапрвляется на страницу товара
            return redirect('product_detail', product_id=product_id)
            # Дополнительные действия после сохранения формы
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': form})

