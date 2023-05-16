from django.db import models
from catalog.models import Product
from datetime import datetime


director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

# Класс сотрудники
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255, default='', null=True)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]


# Класс заказы
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE, null=True)
    products = models.ManyToManyField(Product, through = 'ProductOrder')


    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.time_out:
            duration = self.time_out - self.time_in
        else:
            duration = datetime.now(timezone.utc) - self.time_in

        minutes = int(duration.total_seconds() // 60)
        return minutes



class ProductOrder(models.Model):
    product_order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    _amount = models.IntegerField(default = 1)


    def product_sum(self):
        product_price = Product.price
        return product_price * self._amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

