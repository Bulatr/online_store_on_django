'''
В этом приложении можно управлять заказами и их обработкой.
Здесь могут быть определены модели для заказов, статусов заказов, доставки и оплаты,
а также функции для создания заказа, отслеживания его статуса и обработки платежей.
'''
from django.db import models
from datetime import datetime
from cart.models import Cart

# Класс заказы
# В одном заказе может быть несколько продуктов
class Order(models.Model):
    from users.models import Staff

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
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

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
