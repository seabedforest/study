from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('名字', max_length=11)
    desc = models.CharField('描述', max_length=200)
