from django.shortcuts import render
from .models import GoodsCategory,GoodsInfo
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    # 1查询商品的分类
    categories = GoodsCategory.objects.all()
    # 2从每个分类中获取四个商品(每一类最后四个商品 最新的)
    for cag in categories:
        # order_by排序  根据id反向排序 [:4]获取结果的前四个
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]
    # 3获取购物车里所有的商品 cookie  商品id:数量
    # 购物车商品的列表
    cart_goods_list = []
    # 4购物车的商品的总数量
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 商品id都是数字，不是数字的跳过循环
        if not goods_id.isdigit():
            continue
        # 获取当前遍历到的商品的对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 把商品存放到列表里
        cart_goods_list.append(cart_goods)
        #  累加所有商品的数量
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods/index.html', locals())
    # return render(request,'index.html',{'categories':categories,
    #                                     'cart_goods_list':cart_goods_list,
    #                                     'cart_goods_count':cart_goods_count})


def detail(request):
    """商品详情页面"""
    # 1商品的分类
    categories = GoodsCategory.objects.all()
    # 2 购物车数据
    # 所有的购物车商品
    cart_goods_list = []
    # 购物车商品的总数量
    cart_goods_count = 0
    # 去cookie取数据   goods_id:count
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    # 3 当前要显示的商品的数据
    # 获取传过来的商品的id
    goods_id = request.GET.get('id', 1)
    goods_data = GoodsInfo.objects.get(id=goods_id)

    return render(request, 'goods/detail.html', locals())


def goods(request):
    """商品分类页面"""
    # 获取传过来的分类id
    cag_id = request.GET.get('cag', 1)
    page_id = request.GET.get('page', 1)
    current_cag = GoodsCategory.objects.get(id=cag_id)
    # 当前分类下的所有商品
    goods_data = GoodsInfo.objects.filter(goods_cag=current_cag)
    # 分页器含有所有的分页信息 Paginator
    paginator = Paginator(goods_data, 12)
    # page_data是page对象  里面有当前页面的数据
    page_data = paginator.page(page_id)

    # 所有分类
    categories = GoodsCategory.objects.all()
    # 购物车所有商品
    cart_goods_list = []
    # 购物车总数量
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods_html', {'current_cag': current_cag,
                                          'page_data': page_data,
                                          'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count,
                                          'paginator': paginator,
                                          'cag_id': cag_id})

