"""
定义数值累乘的函数
32,43,54,5,6,78,8
"""


def get_multiplicative_value(*args):
    sum_totole = 1
    for i in args:
        sum_totole *= i
    return sum_totole


print(get_multiplicative_value(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(get_multiplicative_value("12"))
