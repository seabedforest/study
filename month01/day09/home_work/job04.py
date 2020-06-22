"""
# (1). 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
# (2). 定义函数,打印商品单价小于2万的商品信息
# (3). 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
# (4). 定义函数,计算订单总价格：累加 (商品单价 * 数量)
# (5). 查找数量最多的订单(使用自定义算法,不使用内置函数)
# (6). 根据购买数量对订单列表降序排列
@author hailin
@date 2020-05-12
"""
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


# 定义打印商品格式的函数
def print_commodity_format(serial_number, dict_target):
    print(f"商品编号:{serial_number},商品名称:{dict_target[serial_number]['name']},商品单价:{dict_target[serial_number]['price']}.")


# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_information(dict_target):
    """
    打印所有商品信息
    :param dict_target: 商品列表
    :return:
    """
    for serial_number in dict_target:  # 获取商品列表的商品编号
        print_commodity_format(serial_number, dict_target)


print_commodity_information(dict_commodity_infos)


# 2. 定义函数,打印商品单价小于2万的商品信息
def print_price_lt_2w(dict_target):
    """
    打印商品单价小于2万的商品信息
    :param dict_target: 商品列表
    :return:
    """
    for serial_number in dict_target:
        if dict_target[serial_number]['price'] < 20000:
            print_commodity_format(serial_number, dict_target)


print_price_lt_2w(dict_commodity_infos)


# 3. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.

def print_orders_commodity_infos(list_target, dict_target):
    """
    打印所有订单中的商品信息
    :param list_target: 订单列表
    :param dict_target: 商品列表
    :return:
    """
    for order in list_target:
        for serial_number in dict_target:
            if order["cid"] == serial_number:
                print(
                    f"商品名称:{dict_target[serial_number]['name']},商品单价:{dict_target[serial_number]['price']},数量:{order['count']}.")
                break


print_orders_commodity_infos(list_orders, dict_commodity_infos)


# 4. 计算订单总价格：累加 (商品单价 * 数量)
def calculate_order_totle_price(list_target, dict_target):
    """
    计算订单总价格：累加 (商品单价 * 数量)
    :param list_target: 订单列表
    :param dict_target: 商品列表
    :return: 订单总价格
    """
    totle_price = 0
    for order in list_target:
        for serial_number in dict_target:
            if order["cid"] == serial_number:
                totle_price += dict_target[serial_number]['price'] * order['count']
                break

    return totle_price


print(f"订单总价格:{calculate_order_totle_price(list_orders, dict_commodity_infos)}")

# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count(list_target):
    """
    查找数量最多的订单
    :param list_target: 订单列表
    :return:
    """
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if max_value["count"] < list_target[i]["count"]:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_target[i]
    return max_value


print(order_max_by_count(list_orders))


# 6. 根据购买数量对订单列表降序排列
def get_order_sort_desc(list_target):
    """
    根据购买数量对订单列表降序排列
    :param list_target: 订单列表
    :return:
    """
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i]["count"] < list_target[j]["count"]:
                list_target[i], list_target[j] = list_target[j], list_target[i]


get_order_sort_desc(list_orders)
print(list_orders)
