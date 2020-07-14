from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name='作者姓名', max_length=11)


class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=11)
    authors = models.ManyToManyField(Author)
