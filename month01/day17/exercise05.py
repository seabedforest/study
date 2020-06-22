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
commodity01 = (commodity for commodity in list_commodity_infos if commodity.cid > 1004)
for item in commodity01:
    print(item.__dict__)

# 练习2:定义函数,在商品列表中,获取价格小于10000的所有商品信息.
commodity02 = (commodity for commodity in list_commodity_infos if commodity.price > 10000)
for item in commodity02:
    print(item.__dict__)

# 练习3:定义函数,在商品列表中,获取编号是1006的商品信息.
commodity03 = [commodity for commodity in list_commodity_infos if commodity.cid > 1006]
print(commodity03[0].__dict__)