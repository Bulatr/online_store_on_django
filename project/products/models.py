
# Это приложение будет отвечать за управление товарами в магазине.
# В нем можно определить модели для товаров, атрибутов товаров, категорий,
# а также предоставить функционал для создания, редактирования и удаления товаров.

from django.db import models

class Category(models.Model):
    '''
    Категории товаров
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    created_data = models.DateTimeField(auto_now_add=True)
    updatet_data = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    def get_ancestors(self):
        """
        Метод для получения всех предков данной категории.
        """
        ancestors = []
        category = self
        while category.parent:
            category = category.parent
            ancestors.append(category)
        return ancestors

    def get_descendants(self):
        """
        Метод для получения всех потомков данной категории.
        """
        descendants = []
        self._get_descendants_recursive(descendants)
        return descendants

    def _get_descendants_recursive(self, descendants):
        """
        Вспомогательный рекурсивный метод для получения всех потомков.
        """
        children = self.children.all()
        descendants.extend(children)
        for child in children:
            child._get_descendants_recursive(descendants)

class Product(models.Model):
    '''
    Класс продукта
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    created_data = models.DateTimeField(auto_now_add=True)
    updatet_data = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

