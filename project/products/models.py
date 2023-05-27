
# Это приложение будет отвечать за управление товарами в магазине.
# В нем можно определить модели для товаров, атрибутов товаров, категорий,
# а также предоставить функционал для создания, редактирования и удаления товаров.

from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updatet_data = models.DateTimeField(auto_now=True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    created_data = models.DateTimeField(auto_now_add=True)
    updatet_data = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

