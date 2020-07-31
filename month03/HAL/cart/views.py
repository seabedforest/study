from django.shortcuts import render, redirect
from cart.models import OrderGoods, OrderInfo
from goods.models import GoodsCategory, GoodsInfo
import time


# Create your views here.
def add_cart(request):
    """添加到购物车  cookie goods_id:count"""
    # 1获取传过来的商品
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获取上一个页面的地址  redirect 重定向访问一个其它的视图
        prev_url = request.META['HTP_REFERER']
        response = redirect(prev_url)
        # 获取之前的商品在购物车的数量
        goods_count = request.COOKIES.get(goods_id)
        # 2.把商品id存到cookie里 如果之前购物车里有商品  那么就在之前的数量+1
        # 如果之前没有 那么就添加1个
        if goods_count:
            goods_count = int(goods_count) + 1
        else:
            goods_count = 1
        # 把商品id和数量保存到cookie
        response.set_cookie(goods_id, goods_count)
    return response


def show_cart(request):
    """显示购物车商品"""
    # 1.获取购物车商品列表
    cart_goods_list = []
    # 2购物车商品的总数量
    cart_goods_count = 0
    # 3购物车的总价格
    cart_goods_money = 0

    # 从cookie获取数据  遍历cookie goods_id:count
    for goods_id, goods_num in request.COOKIES.items():
        # 判断id不是数字 来确定是不是商品数据
        if not goods_id.isdigit():
            continue
        # 根据id获取商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品数量 存到对应的对象里
        cart_goods.goods_num = goods_num
        # 当前商品的价格小计
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        # 把商品添加到列表
        cart_goods_list.append = (cart_goods)
        # 累加所有商品的数量
        cart_goods_count = cart_goods_count + int(goods_num)
        # 购物车所有商品总价格
        cart_goods_money = cart_goods_money + int(goods_num) * cart_goods.goods_price
    return render(request, 'cart.html', {'cart_goods_list': cart_goods_list,
                                         'cart_goods_count': cart_goods_count,
                                         'cart_goods_money': cart_goods_money})


def remove_cart(request):
    # 删除商品
    # 获取要删除的商品的id
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获取上一个页面的url地址
        prev_url = request.META['HTTP_REFERER']
        # 获取到要返回的response对象 redirect是重定向 当我们删除后 要重新加载显示购物车的页面
        response = redirect(prev_url)
        # 先去cookie里 获取当前商品
        goods_count = request.COOKIES.get(goods_id, '')
        # 通过是否获取到 来判断商品是否存在
        if goods_count:
            response.delete_cookie(goods_id)
    return response


def place_order(request):
    """提交订单页面"""
    # 购物车的所有商品
    cart_goods_list = []
    # 购物车所有商品的数量
    cart_goods_count = 0
    # 购物车总的价格
    cart_goods_money = 0
    # 从cookie里获取数据  商品的id:商品的数量
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 根据id获取商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品的数量存到商品对象里
        cart_goods.goods_num = goods_num
        cart_goods.total_money = cart_goods.goods_price * int(goods_num)
        # 把商品对象存到列表里
        cart_goods_list.append(cart_goods)
        # 计算总的数量
        cart_goods_count += int(goods_num)
        # 累加总的价格
        cart_goods_money += cart_goods.goods_price * int(goods_num)

    return render(request, 'place_order.html', locals())


def submit_order(request):
    # 提交订单功能
    # 获取生成订单需要的数据
    # 收货地址
    addr = request.POST.get('addr', '')
    # 收货人
    recv = request.POST.get('recv', '')
    # 联系电话
    tele = request.POST.get('tele', '')
    # 备注
    extra = request.POST.get('extra')

    # 实例化订单对象
    order_info = OrderInfo()
    # 给订单赋值
    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extra = extra
    # 生成订单编号 用日期
    order_info.order_id = str(time.time() * 1000) + str(time.clock() * 1000000)
    # 数据保存到数据库
    order_info.save()

    # 提交成功的页面
    response = redirect('cart/submit_success/?id=%s' % order_info.order_id)
    # 遍历购物车的数据，生产OrderGoods的对象
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 获取商品的对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 生成订单商品的对象
        order_goods = OrderGoods()
        # 把对应商品添加到订单对象里
        order_goods.goods_info = cart_goods
        # 商品数量
        order_goods.goods_num = goods_num
        # 属于的订单
        order_goods.goods_order = order_info
        # 保存到数据库
        order_goods.save()
        # 把数据从购物车删除 删除cookie
        response.delete_cookie(goods_id)
    return response


def submit_success(request):
    """订单提交成功"""
    # 获取传过来的订单号
    order_id = request.GET.get('id')
    # 获取订单对象
    orderinfo = OrderInfo.objects.get(order_id=order_id)
    order_goods_list = OrderGoods.objects.filter(goodss_order=orderinfo)

    # 总价
    total_money = 0
    # 总数量
    total_num = 0
    for goods in order_goods_list():
        # 商品价格小计
        goods.total_money = goods.goods_info.goods_price * goods.goods_num
        # 计算总价
        total_money += goods.total_money
        # 累加总的数量
        total_num += goods.goods_num

    return render(request, '', {'orderinfo': orderinfo,
                                'order_goods_list': order_goods_list,
                                'total_money': total_money,
                                'total_num': total_num})
