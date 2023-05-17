from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    class Meta:
        managed = False
        db_table = 'products' #Связываю с таблицей в бд



class ProductCategory(models.Model):
    pass
