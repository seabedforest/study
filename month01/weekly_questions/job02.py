# 商品列表
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]


# 1. （5分）打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def show_commodity_infos(dict_target):
    """
    打印所有商品信息
    :param dict_target: 商品列表
    :return:
    """
    for serial_number in dict_target:
        print(
            f"商品编号{serial_number},商品名称{dict_target[serial_number]['name']},"
            f"商品单价{dict_target[serial_number]['price']}.")


# 测试
show_commodity_infos(dict_commodity_infos)


# 2. （5分）打印所有订单信息,格式：订单编号xx,数量:xx.
def show_order_infos(list_targrt):
    """
    打印所有订单信息
    :param list_targrt: 订单列表
    :return:
    """
    for order_info in list_targrt:
        print(f"订单编号{order_info['cid']},数量:{order_info['count']}.")


# 测试
show_order_infos(list_orders)


# 3. （15分）打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
def show_order_commodity_infos(list_targrt, dict_target):
    """
    打印所有订单中的商品信息
    :param list_targrt:订单列表
    :param dict_target:商品列表
    :return:
    """
    for order_info in list_targrt:
        print(
            f"商品名称{dict_target[order_info['cid']]['name']},商品单价:{dict_target[order_info['cid']]['price']},"
            f"数量{order_info['count']}.")


# 测试
show_order_commodity_infos(list_orders, dict_commodity_infos)


# 4. （20分）计算订单总价格：累加商品单价 * 数量
def calculate_totle_price_order(list_targrt, dict_target):
    """
    计算订单总价格
    :param list_targrt: 订单列表
    :param dict_target: 商品列表
    :return: 订单总价格
    """
    totle_price = 0
    for order_info in list_targrt:
        totle_price += dict_target[order_info['cid']]['price'] * order_info['count']
    return totle_price


# 测试
print("订单总价格:%.2f" % calculate_totle_price_order(list_orders, dict_commodity_infos))


# 5.（20分）查找数量最少的订单(使用自定义算法,不使用内置函数)
def find_smallest_order(list_targrt):
    """
    查找数量最少的订单
    :param list_targrt: 订单列表
    :return: 数量最少的订单
    """
    min_value = list_targrt[0]
    for index in range(1, len(list_targrt)):
        if min_value["count"] > list_targrt[index]["count"]:
            min_value = list_targrt[index]
    return min_value


# 测试
print(find_smallest_order(list_orders))


# 6. （25分）根据单价,升序排列商品信息(使用自定义算法,不使用内置函数)
def sort_asc_commdity_infos(dict_target):
    """
    根据单价,升序排列商品信息
    :param dict_target: 商品列表
    :return:
    """
    list_commodity_infos = list(dict_target.items())
    for i in range(len(list_commodity_infos) - 1):
        for j in range(i + 1, len(list_commodity_infos)):
            if list_commodity_infos[i][1]['price'] > list_commodity_infos[j][1]['price']:
                list_commodity_infos[i], list_commodity_infos[j] = list_commodity_infos[j], list_commodity_infos[i]
    return list_commodity_infos


# 测试
print(sort_asc_commdity_infos(dict_commodity_infos))
