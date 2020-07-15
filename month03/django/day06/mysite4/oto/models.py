from django.db import models


# Create your models here.
class Author(models.Model):
    aname = models.CharField(verbose_name="作者姓名", max_length=11)


class Wife(models.Model):
    wname = models.CharField(verbose_name="妻子姓名", max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
