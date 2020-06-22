"""
根据下列代码,定义函数,计算梯形面积.
"""


def calculate_trapezoidal_area(top_base, bottom_base, height):
    """
    计算梯形面积
    :param top_base: 上底
    :param bottom_base: 下底
    :param height: 高
    :return: 梯形面积
    """
    return (top_base + bottom_base) * height / 2


print("梯形面积是：" + str(calculate_trapezoidal_area(5, 8, 4.5)))

"""
day04/home_work/exercise01
根据下列代码定义函数计算电梯状态.
num = int(input("请输入电梯承载人数:"))
weight = float(input("请输入电梯承载重量:"))
if num <= 10 and weight <= 1000:
print("电梯正常运行")
else:
print("电梯超载")
"""


def gain_running_status(number_people, weight):
    """
    计算电梯状态.
    :param number_people: 电梯承载人数
    :param weight: 电梯承载重量
    :return: 电梯状态
    """
    status = "电梯正常运行" if number_people <= 10 and weight <= 1000 else "电梯超载"
    return status

print(gain_running_status(10, 900))
