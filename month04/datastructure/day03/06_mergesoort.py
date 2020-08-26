"""
python实现归并排序
"""


def merge_sort(li):
    # 递归出口
    if len(li) == 1:
        return li
    # 1.先拆分
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    # 递归思想，left和right两个小列表继续按同样方式拆分
    left_li = merge_sort(left)
    right_li = merge_sort(right)
    # 2.合并
    return megre(left_li, right_li)


def megre(left_li, right_li):
    """合并的函数"""
    result = []
    while left_li and right_li:
        if left_li[0] >= right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))
    if left_li:
        result.extend(left_li)
    else:
        result.extend(right_li)
    return result


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(li))
