"""
5.  参照下列代码,定义函数,计算加速度.
    distence = float(input("距离为:"))
    initial_velocity = float(input("速度为"))
    time = float(input("时间为"))
    accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
    print("加速度为" + str(accelerated_speed))
@author hailin
@date 2020-05-11
"""


def calculated_acceleration(distence, initial_velocity, time):
    """
    计算加速度
    :param distence: 行驶距离(公里)
    :param initial_velocity: 初速度(每小时多少公里)
    :param time: 行驶时间(小时)
    :return:
    """
    accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
    return accelerated_speed


# 调用函数，打印结果
print("加速度为" + str(calculated_acceleration(100, 3, 10)))
