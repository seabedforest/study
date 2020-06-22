"""
根据年龄，输出对应的人生阶段。
    年龄       ⼈⽣阶段
    0-6 岁      童年
    7-17 岁     少年
    18-40 岁    ⻘年
    41-65 岁    中年
    65 岁之后    ⽼年
步骤:
    终端中获取年龄
    显示人生阶段
@author hailin
@date 2020-05-03
"""
age = int(input("请输入你的年龄:"))
if age > 65:
    print("老年")
elif age >= 41:
    print("中年")
elif age >= 18:
    print("青年")
elif age >= 7:
    print("少年")
elif age >=0:
    print("童年")
else:
    print("输入的年龄是错误的")