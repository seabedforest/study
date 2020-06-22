"""
(选做)定义函数,从列表中删除多个元素(有坑)
​    -- 定义函数,将列表中奇数设置为1
​    -- 定义函数,将列表中奇数删除
​    测试数据:[3,4,5,6,7,8,9]
@author hailin
@date 2020-05-15
"""


# 定义函数,将列表中奇数设置为1
def change_odd_to_one(list_target):
    """
    将列表中奇数设置为1
    :param list_target: 列表
    :return:
    """
    for index in range(len(list_target)):
        if list_target[index] % 2:
            list_target[index] = 1


list01 = [3, 4, 5, 6, 7, 8, 9]
change_odd_to_one(list01)
print(list01)


# 定义函数,将列表中奇数删除

def remove_odd(list_target):
    """
    将列表中奇数删除
    :param list_target: 列表
    :return:
    """
    for index in range(len(list_target) - 1, -1, -1):
        if list_target[index] % 2:
            del list_target[index]


list02 = [3, 4, 5, 6, 7, 8, 9]
remove_odd(list02)
print(list02)
