from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.product_id

class ProductCategory(models.Model):
    pass
