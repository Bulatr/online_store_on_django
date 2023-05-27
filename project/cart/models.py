from django.db import models
from django.contrib.auth.models import User


# Это приложение будет обрабатывать операции, связанные с корзиной покупок.
# Оно может содержать модели для корзины, элементов корзины и оформления заказа,
# а также предоставлять функции для добавления товаров в корзину,
# обновления количества товаров, удаления товаров и оформления заказа.


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Класс для связи продукта и заказа (один продукт и один заказ) связь один к одному
# при добавлении в корзину товара создается эта модель.
class CartItem(models.Model):
    from products.models import Product

    # id модели заказа
    id = models.AutoField(primary_key=True)
    # Связь с корзиной
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # id модели продукта
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # количество продукта
    quantity = models.PositiveIntegerField(default=1)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # сумма заказа
    def total_price(self):
        return self.quantity * self.price

    # получение количества
    def get_quantity(self):
        return self.quantity

    # сеттер для записи количества в базу
    def set_quantity(self, value):
        self.quantity = int(value) if value >= 0 else 0
        self.save()


