import random
from django.utils import timezone as tz
from django.db import models


def random_sign():
    signs = ['hahaha', 'heiheihei']
    return random.choice(signs)


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    email = models.EmailField()
    password = models.CharField(max_length=32, verbose_name='密码')
    sign = models.CharField(max_length=50, verbose_name='个人签名', default=random_sign)
    info = models.CharField(max_length=150, verbose_name='个人简介', default='')
    avatar = models.ImageField(upload_to='avator', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    login_time = models.DateTimeField(default=tz.now)

    class Meta:
        db_table = 'user_user_profile'
