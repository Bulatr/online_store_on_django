from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    class Meta:
        managed = False
        db_table = 'products' #Связываю с таблицей в бд



class ProductCategory(models.Model):
    pass
