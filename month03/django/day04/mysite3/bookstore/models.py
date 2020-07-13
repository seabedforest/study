from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50)
    price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)
    desc = models.CharField("描述", max_length=50, default="null")

    class Meta:
        db_table='book'
