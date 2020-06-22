"""
写出for元组的原理
写出for字典的原理(不使用for,获取字典键值对)
"""
tup01 = (1, 2, 3, 4, 5, 6)
dict01 = {0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"}


iterator01=tup01.__iter__()
iterator02=dict01.items().__iter__()
while True:
    try:
        item = iterator01.__next__()
        print(item)
    except StopIteration:
        break


while True:
    try:
        item01 = iterator02.__next__()
        print(item01)
    except StopIteration:
        break