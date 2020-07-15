from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(verbose_name='出版社名称', max_length=11)


class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
