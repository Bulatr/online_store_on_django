from django.db import models
from catalog.models import Product


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

# Create your models here.
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length = 2,
                            choices = POSITIONS,
                            default = cashier),
    labor_contract = models.IntegerField()

    def __str__(self):
        return self.full_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order ID: {self.order_id}"



class ProductOrder(models.Model):
    product_order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"Product: {self.product.name}, Order: {self.in_order.order_id}"