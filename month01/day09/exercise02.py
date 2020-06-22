"""
# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
# 2. 定义函数,打印商品单价小于2万的商品信息
# 3. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
"""
# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


# 定义打印商品格式的函数
def print_commodity_format(commodity):
    print(f"商品编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}.")


# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_information():
    """..."""
    for commodity in list_commodity_infos:
        print_commodity_format(commodity)


print_commodity_information()


# 2. 定义函数,打印商品单价小于2万的商品信息
def print_price_lt_2w():
    """..."""
    for commodity in list_commodity_infos:
        if commodity["price"] < 20000:
            print_commodity_format(commodity)


print_price_lt_2w()


# 3. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.

def print_orders_commodity_infos():
    """..."""
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order["cid"] == commodity["cid"]:
                print(f"商品名称:{commodity['name']},商品单价:{commodity['price']},数量:{order['count']}.")
                break


print_orders_commodity_infos()


# 4. 计算订单总价格：累加 (商品单价 * 数量)
def calculate_order_totle_price():
    """..."""
    totle_price = 0
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order["cid"] == commodity["cid"]:
                totle_price += commodity['price'] * order['count']
                break

    return totle_price


print(f"订单总价格:{calculate_order_totle_price()}")


# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value["count"] < list_orders[i]["count"]:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_orders[i]
    return max_value


print(order_max_by_count())


# 6. 根据购买数量对订单列表降序排列
def get_order_sort():
    for i in range(len(list_orders) - 1):
        for j in range(i + 1, len(list_orders)):
            if list_orders[i]["count"] < list_orders[j]["count"]:
                list_orders[i], list_orders[j] = list_orders[j], list_orders[i]


get_order_sort()
print(list_orders)
