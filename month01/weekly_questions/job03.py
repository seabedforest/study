"""
对一组数完成冒泡排序
@author hailai
@date 2020-05-28
"""


def conduct_bublle_sort(list_target):
    for i in range(len(list_target) - 1):
        swap = False
        for j in range(len(list_target) - i - 1):
            if list_target[j] > list_target[j + 1]:
                list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]
                swap = True
        if not swap:
            return list_target
    return list_target


list01 = [5, 8, 1, 2, 5, 6, 9, 0, 19, 23, 34, 21]
conduct_bublle_sort(list01)
print(list01)
