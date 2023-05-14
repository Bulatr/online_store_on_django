from django.apps import AppConfig

'''
Приложение для управления товарами и категориями в магазине. 
Оно может содержать модели для товаров, изображений, характеристик, 
а также представления для отображения списка товаров, 
страницы отдельного товара и фильтрации товаров по различным критериям.
'''

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
