"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
@author hailai
@date 2020-05-28
"""


def calculate_rabbit_total(month):
    if month <= 2:
        return 1
    return calculate_rabbit_total(month - 1) + calculate_rabbit_total(month - 2)


print(calculate_rabbit_total(5))
