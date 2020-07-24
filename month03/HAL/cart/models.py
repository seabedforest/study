from django.db import models


# Create your models here.
# 订单详情表
class OrderInfo(models.Model):
    status = (
        (1, '待付款'),
        (2, '待发货'),
        (3, '待收款'),
        (4, '已完成'),
    )
    order_id = models.CharField('订单编号', max_length=100)
    order_area = models.CharField('所在地区', max_length=100)
    order_addr = models.CharField('收货地址', max_length=100)
    order_recv = models.CharField('收货人', max_length=50)
    order_tele = models.CharField('联系电话', max_length=11)
    order_fee = models.IntegerField('运费', default=10)
    order_extra = models.CharField('订单备注', max_length=200)
    order_status = models.IntegerField('订单状态', default=1, choices=status)


# 订单跟商品关系表
class OrderGoods(models.Model):
    goods_info = models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE, verbose_name='所属商品')
    goods_num = models.IntegerField(verbose_name='商品数量')
    goods_order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name='商品所属订单')
