"""
需求:
在商品列表中,查找编号是1002的商品对象
在商品列表中,查找名称是金箍棒的商品对象
.....
查找满足条件的单个对象

步骤:
1. 实现完整功能
2. 使用函数式编程思想(分,隔,做),拆分完整功能.
编写不变的/变化的/连接的代码
3. 将不变的定义到IterableHelper类中
4. 在当前模块中调用IterableHelper类中代码
"""
from commdity.iterable_tools import IterableHelper


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

# 在商品列表中,查找编号是1002的商品对象
for item in IterableHelper.find_infos(list_commodity_infos, lambda commdity: commdity.cid == 1002):
    print(item.__dict__)

# 在商品列表中,查找名称是金箍棒的商品对象
for item in IterableHelper.find_infos(list_commodity_infos, lambda commdity: commdity.name == "金箍棒"):
    print(item.__dict__)

# 在商品列表中,统计商品单价大于10000个数
number = IterableHelper.get_count(list_commodity_infos, lambda commdity: commdity.price > 10000)
print(number)

# 在商品列表中,查找最便宜的商品
commodity = IterableHelper.get_min(list_commodity_infos, lambda commdity: commdity.price)
print(commodity.__dict__)
# 在商品列表中,查找商品编号最小的商品
commodity = IterableHelper.get_min(list_commodity_infos, lambda commdity: commdity.cid)
print(commodity.__dict__)

# 在商品列表中,根据单价对商品列表升序排列
IterableHelper.sort_asc(list_commodity_infos, lambda commdity: commdity.price)
for commodity in list_commodity_infos:
    print(commodity.__dict__)
# 在商品列表中,根据商品名称字符长度升序排列
IterableHelper.sort_asc(list_commodity_infos, lambda commdity: len(commdity.name))
for commodity in list_commodity_infos:
    print(commodity.__dict__)