from django.db import models
from datetime import datetime



# Класс сотрудники
class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    manager = 'MG'
    cashier = 'CA'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (manager, 'Менеджер'),
        (cashier, 'Кассир')
    ]

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    # должность
    position = models.CharField(max_length = 255, choices = POSITIONS, default = manager)
    # номер контракта (договора)
    labor_contract = models.IntegerField()


    def get_last_name(self):
        return self.full_name.split()[0]


# Класс заказы
# В одном заказе может быть несколько продуктов
class Order(models.Model):

    id = models.AutoField(primary_key=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    # сумма заказа
    cost = models.FloatField(default = 0.0)
    # не помню что это
    pickup = models.BooleanField(default = False)
    # заказ выполнен или нет
    complete = models.BooleanField(default = False)
    # сотрудник отвечающий за заказ
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)


    def finish_order(self):
        self.update_data = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.create_data:
            duration = self.update_data - self.create_data
        else:
            duration = datetime.now() - self.create_data

        minutes = int(duration.total_seconds() // 60)
        return minutes





# Класс для связи продукта и заказа (один продукт и один заказ) связь один к одному
# при добавлении в корзину товара создается эта модель.
class CartItem(models.Model):
    from catalog.models import Product

    # id модели заказа
    id = models.AutoField(primary_key=True)
    # id модели продукта
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # количество продукта
    _amount = models.IntegerField(default = 1)

    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)

    summ = models.FloatField(default=0.0)

    # получение количества
    @property
    def amount(self):
        return self._amount

    # сеттер для записи количества в базу
    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

    # сумма заказа
    def product_sum(self):
        product_price = self.product.price
        return product_price * self._amount