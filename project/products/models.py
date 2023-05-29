
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
    Класс Product определяет модель продукта в Django. У него есть следующие атрибуты:

    id - объект AutoField, который используется в качестве первичного ключа модели.

    name - обязательное поле CharField с максимальной длиной 255 символов, предназначено для хранения названия продукта. 
    Это поле уникально, так что ни один объект Product не может иметь одно и то же название.

    price - обязательное поле FloatField, которое хранит цену продукта.

    created_data - поле DateTimeField, которое хранит дату и время создания продукта. 
    Это поле автоматически устанавливается в текущее время при создании нового объекта Product.

    updated_data - поле DateTimeField, которое хранит дату и время последнего обновления продукта. 
    Это поле автоматически обновляется до текущего времени при изменении объекта Product.

    content - опциональное поле TextField, которое может использоваться для хранения 
    дополнительной информации о продукте.

    category - обязательный внешний ключ на модель Category, созданный с использованием поля ForeignKey. 
    Аргумент on_delete установлен на CASCADE, что означает, что при удалении связанного объекта Category 
    будут удалены все объекты Product, которые на него ссылаются.
    
    Класс также имеет метод __str__() для представления объекта Product в виде строки. 
    Этот метод возвращает строку, содержащую название продукта и его категорию, заключенные в скобки.
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    created_data = models.DateTimeField(auto_now_add=True)
    updatet_data = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # напиши метод дающий строку представления
    def __str__(self):
        return f"{self.name} ({self.category})"