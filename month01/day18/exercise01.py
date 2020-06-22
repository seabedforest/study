"""
练习: 参照demo02,以函数式编程思想,改写下列代码.
"""


class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]


# 练习1:定义函数,在商品列表中,获取编号大于1004的所有商品信息.
def commodity_cid_over_1004(commodity):
    return commodity.cid > 1004


# 练习2:定义函数,在商品列表中,获取价格小于10000的所有商品信息.
def get_commodity_price_less_10000(commodity):
    return commodity.price < 10000


def find_commodity_infos(list_target, func):
    for commodity in list_target:
        if func(commodity):
            yield commodity


for item in find_commodity_infos(list_commodity_infos, commodity_cid_over_1004):
    print(item.__dict__)
