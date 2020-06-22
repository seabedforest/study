"""
在终端中循环录入年龄,如果录入空,则退出循环.
   最后打印平均年龄(总年龄除以人数)
@author hailin
@date 2020-05-06
"""
count = 0
age_sum = 0
while True:
    age = input("请输入你的年龄:")
    if age == "":
        average = age_sum // count
        print("平均年龄为%d" % average)
        break
    count += 1
    age_sum += int(age)
