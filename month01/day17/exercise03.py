"""
list01 = [4,43,5,546,456,56,75,678]
# 练习1: 定义函数,创建列表存储所有偶数,并且返回列表.
# 练习2: 定义函数,判断偶数,通过yield返回.
# 调试,体会程序的差异性.
"""
list01 = [4, 43, 5, 546, 456, 56, 75, 678]


# 练习1: 定义函数,创建列表存储所有偶数,并且返回列表.
def get_even(target):
    even_munber_list = []
    for item in target:
        if item % 2 == 0:
            even_munber_list.append(item)
    return even_munber_list


# 练习2: 定义函数,判断偶数,通过yield返回.
def get_even_number(target):
    for item in target:
        if item % 2 == 0:
            yield item


list02 = get_even(list01)
list03 = get_even_number(list01)
for i in list03:
    print(i)
