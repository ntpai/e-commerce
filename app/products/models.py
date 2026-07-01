from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_STATUS = [
        ("Active", "active"),
        ("Inactive","inactive"),
    ]

    product_name = models.CharField(max_length=256)
    category = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(max_length=10, choices=PRODUCT_STATUS)
 