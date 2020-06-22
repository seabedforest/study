"""
给你一个 n*m 的二维数组，每行元素保证递增，每列元素保证递增，试问如何找到某个数字，或者判断这个数字不存在。
@author hailin
@date 2020-06-04
"""
two_dimensional_array = [
    [1, 2, 3, 4],
    [2, 4, 5, 7],
    [8, 9, 10, 14],
    [12, 20, 32, 45]
]


def find_num(target, array):
    """
    n*m 的二维数组,每行元素保证递增，每列元素保证递增，找出其中一个数字
    :param target:目标数字
    :param array:n*m 的二维数组
    :return:True or False
    """
    row = 0
    maxrow = len(array) - 1
    col = len(array[0]) - 1
    while col >= 0 and row <= maxrow:
        if target == array[row][col]:
            return True
        elif target > array[row][col]:
            row += 1
        else:
            col -= 1
    return False


print(find_num(8, two_dimensional_array))
