"""
定义张三的成绩，显示所获奖励，成绩100，爸爸买辆车，大于90小于100，妈妈买iPhone，大于60小于90，妈妈买参考书，小于60，什么都不买
@author hailin
@date 2020-05-03
"""
result = float(input("请输入张三的成绩:"))
if result == 100:
    print("爸爸买辆车")
elif result >= 90:
    print("妈妈买iPhone")
elif result >= 60:
    print("妈妈买参考书")
else:
    print("什么都不买")
