from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField('书名', max_length=50, unique=True)
    pub = models.CharField('出版社', max_length=100)
    price = models.DecimalField('定价', max_digits=6, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=6, decimal_places=2)
    is_active = models.BooleanField('是否活跃',default=True)
    class Meta:
        db_table = 'book'

    def __str__(self):
        return 'title %s pub %s price %s market_price %s' % (self.title, self.pub, self.price, self.market_price)


class Author(models.Model):
    name = models.CharField('姓名', max_length=11)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)

    class Meta:
        db_table = 'author'
