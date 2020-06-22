"""
    匀变速直线运动的速度与位移公式：
    位移 = 初速度 * 时间 + 加速度 * 时间平方的一半
    已知(在终端中录入)：位移、时间、初速度
    计算：加速度

    2 * (位移 - 初速度 * 时间)  /  时间**2 = 加速度
"""

distence = float(input("距离为:"))
initial_velocity = float(input("速度为"))
time = float(input("时间为"))
accelerated_speed = 2 * (distence - initial_velocity * time) / time ** 2
print("加速度为" + str(accelerated_speed))
