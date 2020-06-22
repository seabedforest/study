"""
对一组数完成插入排序
@author hailai
@date 2020-05-28
"""


def conduct_insert_sort(list_target):
    for index in range(1, len(list_target)):
        currentvalue = list_target[index]
        position = index
        while position > 0 and list_target[position - 1] > currentvalue:
            list_target[position] = list_target[position - 1]
            position -= 1
        list_target[position] = currentvalue


list01 = [5, 8, 1, 2, 5, 6, 9, 0, 19, 23, 34, 21]
conduct_insert_sort(list01)
print(list01)
