"""
对一组数完成选择排序
@author hailai
@date 2020-05-28
"""


def conduct_select_sort(list_target):
    for fillslot in range(len(list_target) - 1, 0, -1):
        positionofmax = 0
        for location in range(1, fillslot + 1):
            if list_target[location] > list_target[positionofmax]:
                positionofmax = location
        temp = list_target[fillslot]
        list_target[fillslot] = list_target[positionofmax]
        list_target[positionofmax] = temp


list01 = [5, 8, 1, 2, 5, 6, 9, 0, 19, 23, 34, 21]
conduct_select_sort(list01)
print(list01)
