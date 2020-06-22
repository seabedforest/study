"""
实现希尔排序
@author hailai
@date 2020-06-21
"""


def shellSort(target_list):
    sublistcount = len(target_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(target_list, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", target_list)
        sublistcount = sublistcount // 2


def gapInsertionSort(target_list, start, gap):
    for i in range(start + gap, len(target_list), gap):
        currentvalue = target_list[i]
        position = i
        while position >= gap and target_list[position - gap] > currentvalue:
            target_list[position] = target_list[position - gap]
            position = position - gap
        target_list[position] = currentvalue


list_01 = [7, 8, 13, 12, 15, 26, 39, 10, 19, 23, 30, 21]
shellSort(list_01)
print(list_01)
