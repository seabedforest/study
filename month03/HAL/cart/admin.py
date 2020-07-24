from django.contrib import admin
from .models import OrderGoods, OrderInfo


# Register your models here.
class OrderGoodsManager(admin.ModelAdmin):
    list_display = ['id', 'goods_info', 'goods_num', 'goods_order']


admin.site.register(OrderGoods, OrderGoodsManager)
