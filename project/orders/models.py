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
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length = 2,
                            choices = POSITIONS,
                            default = cashier),
    labor_contract = models.IntegerField()

#    class Meta:
#        managed = False
#        db_table = 'STAFF' #Связываю с таблицей в бд

    def get_last_name(self):
        return self.full_name.split()[0]


# Класс заказы
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through = 'ProductOrder')
#    class Meta:
#        managed = False
#        db_table = 'ORDERS' #Связываю с таблицей в бд

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default = 1)
#    class Meta:
#        managed = False
#        db_table = 'PRODUCTS_ORDERS' #Связываю с таблицей в бд

    def product_sum(self):
        product_price = self.Product.price
        return product_price * self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()

