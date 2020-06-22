"""
电梯设置规定：
        如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
    步骤:
        终端中获取人数/总重量
        显示 电梯正常运行
            电梯超载
@author hailin
@date 2020-05-03
"""
#获取数据
num_people = int(input("输入承载⼈数(位):"))
weight = int(input("输入承载⼈的总重量(千克):"))
#判断条件
if num_people <= 10 and weight <= 1000:
    print("电梯正常运行")
else:
    print("电梯超载")