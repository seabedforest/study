"""
python实现快速排序
"""


def quick_sort(li, first, last):
    # 递归出口
    if first > last:
        return

    # part():给一个基准值找到正确的位置，返回正确位置的下标索引
    split_position = part(li, first, last)

    quick_sort(li, first, split_position - 1)
    quick_sort(li, split_position + 1, last)


def part(li, first, last):
    """给基准值找到正确位置，返回值为正确位置的下标索引"""
    mid = li[first]
    lcur = first + 1
    rcur = last
    # 比较: 循环
    # 左游标右移遇到大的停
    while True:
        while lcur <= rcur and li[lcur] <= mid:
            lcur += 1
        # 右游标左移遇到小的停
        while lcur <= rcur and li[rcur] >= mid:
            rcur -= 1

        # 要么左右游标互换位置，要么基准值和右游标互换位置
        if lcur > rcur:
            li[first], li[rcur] = li[rcur], li[first]
            break
        else:
            li[lcur], li[rcur] = li[rcur], li[lcur]
    # 最终返回值是右游标
    return rcur


if __name__ == '__main__':
    li = [6, 5, 3, 1,21, 8, 7, 2, 4]
    quick_sort(li, 0, len(li) - 1)
    print(li)
