"""
使用封装数据的思想
1. 创建商品类(商品编号,商品名称,商品单价)/订单类,
2. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
3. 定义函数,打印商品单价小于2万的商品信息
"""


# 1. 创建商品类(商品编号,商品名称,商品单价)/订单类,
class Commoditys:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


class Orders:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count


list_commodity_infos = [
    Commoditys(1001, "屠龙刀", 10000),
    Commoditys(1002, "倚天剑", 10000),
    Commoditys(1003, "金箍棒", 52100),
    Commoditys(1004, "口罩", 20),
    Commoditys(1005, "酒精", 30)
]

list_orders = [
    Orders(1001, 1),
    Orders(1002, 2),
    Orders(1003, 3)
]


# 2. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_single_commodity(commodity):
    print(f"商品编号:{commodity.cid},商品名称:{commodity.name},商品单价:{commodity.price}")


def show_commodity_infos(dict_target):
    for index in range(len(dict_target)):
        print_single_commodity(dict_target[index])


show_commodity_infos(list_commodity_infos)


# 3. 定义函数,打印商品单价小于2万的商品信息
def show_commodity_price_le_2w(dict_target):
    for index in range(len(dict_target)):
        if dict_target[index].price < 20000:
            print_single_commodity(dict_target[index])


show_commodity_price_le_2w(list_commodity_infos)


# 4. 定义函数,打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
def show_order_commodity_infos(list_targrt, dict_target):
    for order in list_targrt:
        for commdity in dict_target:
            if order.cid == commdity.cid:
                print(f"商品名称{commdity.name},商品单价:{commdity.price},数量{order.count}.")
                break


show_order_commodity_infos(list_orders, list_commodity_infos)


# 5. 查找数量最多的订单(使用自定义算法,不使用内置函数)
def order_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value.count < list_orders[i].count:
            # 使用更大的那个订单 替换 假设的订单
            max_value = list_orders[i]
    return max_value


result = order_max_by_count()
print(result.__dict__)


# 6. 根据购买数量对订单列表降序排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r].count < list_orders[c].count:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]


# ----------------------测试入口-----------------------------

descending_order_by_count()

for item in list_orders:
    print(item.__dict__)
