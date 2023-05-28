
# Это приложение будет отвечать за управление пользователями.
# В нем можно создать модели для профилей пользователей, авторизации, аутентификации и регистрации.
# Также здесь можно реализовать функции для управления учетными записями пользователей, профилями, аутентификации и авторизации.

from django.db import models

# Класс сотрудники
class Staff(models.Model):
    '''
    Класс сотрудников
    '''
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
        # преобразуем в строку
        full_name = str(self.full_name)
        return full_name.split()[0]

    def __str__(self):
            return f'{self.full_name.title()}: {self.position}'
