from project_month01.iterable_tools import IterableHelper


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

# 在商品列表中,获取编号大于1004的所有商品信息.
commdity = IterableHelper.find_all(list_commodity_infos, lambda com: com.cid > 1004)
for item in commdity:
    print(item.__dict__)

# 在商品列表中, 查找编号是1002的商品对象
commdity = IterableHelper.find_single(list_commodity_infos, lambda com: com.cid == 1002)
print(commdity.__dict__)

# 在商品列表中,统计商品名称为口罩有多少
count = IterableHelper.get_count(list_commodity_infos, lambda com: com.name == "口罩")
print(count)
# 在商品列表中, 查找所有商品名称
commdity = IterableHelper.select(list_commodity_infos, lambda com: com.name)
for item in commdity:
    print(item)
# 在商品列表中，查找所有商品名称和单价
commdity = IterableHelper.select(list_commodity_infos, lambda com: (com.name, com.price))
for item in commdity:
    print(item)

# 在商品列表中, 查找最便宜的商品
commdity = IterableHelper.get_min(list_commodity_infos, lambda com: com.price)
print(commdity.__dict__)

# 在商品列表中, 根据单价对商品列表升序排列
commdity = IterableHelper.order_by(list_commodity_infos, lambda com: com.price)
for item in commdity:
    print(item.__dict__)
# 在商品列表中, 根据商品名称字符长度升序排列
commdity = IterableHelper.order_by(list_commodity_infos, lambda com: len(com.name))
for item in commdity:
    print(item.__dict__)