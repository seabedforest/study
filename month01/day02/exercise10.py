"""

"""
number = int(input("请输出一个四位数："))
# unit01 = number % 10  # 1234 % 10 --> 4
# unit02 = number % 100 // 10  # 1234 % 100 --> 34 // 10 -> 3
# unit03 = number // 100 % 10  # 1234 // 100 --> 12 % -> 2
# unit04 = number // 1000  # 1234 // 1000 --> 1
# result = unit01 + unit02 + unit03 + unit04

result = number % 10  # 个位
result += number % 100 // 10  # 累加十位
result += number // 100 % 10  # 累加百位
result += number // 1000  # 累加千位
print(result)
