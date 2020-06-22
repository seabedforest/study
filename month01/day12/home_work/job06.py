"""
6.
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
        Commodity(1005, "酒精", 30)
        Commodity(1006, "屠龙刀", 10000),
        Commodity(1007, "口罩", 50),
    ]
    -- 定义函数,删除列表中价格大于1w的商品
    -- (选做) 定义函数,删除列表中商品名称相同的商品(不使用其他容器,自定义算法)
@author hailin
@date 2020-05-17
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
    Commodity(1007, "口罩", 50)
]


# 定义函数,删除列表中价格大于1w的商品
def delete_price_gt_1w(list_target):
    """
    删除列表中价格大于1w的商品
    :param list_target: 商品列表
    :return:
    """
    for element in list_target:
        if element.price > 10000:
            list_target.remove(element)


# 测试
delete_price_gt_1w(list_commodity_infos)
for commodity in list_commodity_infos:
    print(commodity.__dict__)

print()
# 定义函数,删除列表中商品名称相同的商品(不使用其他容器,自定义算法)

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50)
]


def delete_duplicate_commodity(list_target):
    """
    删除列表中商品名称相同的商品
    :param list_target: 商品列表
    :return:
    """
    count = 0
    for element01 in list_target:
        count += 1
        for element02 in list_target[count:]:
            if element01.name == element02.name:
                list_target.remove(element02)




# 测试
delete_duplicate_commodity(list_commodity_infos)

for commodity in list_commodity_infos:
    print(commodity.__dict__)
