"""
day04/home_work/exercise02
根据下列代码定义函数获取人生阶段
age = int(input("请输入年龄："))
if age <= 6:
print("童年")
elif age <= 17:
print("少年")
elif age <= 40:
print("青年")
elif age <= 65:
print("中年")
else:
print("老年")
"""


def acquire_life_stage(age):
    if age <= 6:
        return "童年"
    if age <= 17:
        return "少年"
    if age <= 40:
        return "青年"
    if age <= 65:
        return "中年"
    return "老年"


print(acquire_life_stage(18))