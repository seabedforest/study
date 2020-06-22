"""
给你一个长度为n的数组，其中只有一个数字出现了1次，其他均出现2次，问如何快速的找到这个数字。
@author hailin
@date 2020-06-04
"""


def find_num_appears_once(target):
    """
    一个长度为n的数组，其中只有一个数字出现了1次，其他均出现2次,找出出现一次的数字
    :param target: 长度为n的数组
    :return: 出现一次的数字
    """
    num_dict = {}
    for num in target:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    for key in num_dict:
        if num_dict[key] == 1:
            return key


tup01 = (1, 2, 3, 4, 5, 4, 3, 2, 6, 5, 1)
print(find_num_appears_once(tup01))