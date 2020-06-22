"""
小泽老师很不幸,买了一箱有虫子(1只)的苹果
    虫子吃完一个苹果再吃另外一个苹果
    在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
    请打印没有被虫子吃过的苹果数量（整数,最小也是0）
@author hailin
@date 2020-05-03
"""
# 获取数据
apples = int(input("苹果数量:"))
eat_apple_speed = float(input("虫子吃苹果的速度（小时/个）:"))
time = float(input("经过多长时间(小时)"))
# 公式计算
rest_apples = int(apples - time / eat_apple_speed)

# 显示结果
if rest_apples < 0:
    print("剩余的苹果为零个")
else:
    print("剩余的苹果为", int(rest_apples), "个")