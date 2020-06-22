"""
3. 参照下列代码,定义函数,打印矩形
    side_length = int(input("输入边长:"))  # 5
    for item in range(1, side_length + 1):
        # 第一行 或者 最后一行
        if item == 1 or item == side_length:
            print("*" * side_length)
        else:  # 中间行
            #  " " * (side_length - 2)  空格重复多次
            print("*%s*" % (" " * (side_length - 2)))
            # print(f"*{' ' * (side_length - 2)}*")
@author hailin
@date 2020-05-11
"""


def print_rectangular(side_length):
    """
    打印矩形
    :param side_length: 边长
    :return:
    """
    for item in range(1, side_length + 1):
        if item == 1 or item == side_length:
            print("*" * side_length)
        else:
            print("*%s*" % (" " * (side_length - 2)))


print_rectangular(6)
