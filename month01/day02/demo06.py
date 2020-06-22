"""
    数据类型转换
        数据类型:str /  int  /  float
        结果 = 数据类型(待转数据)
    练习:exercise05
"""
print("1" + "2")  # "12" 字符拼接
print(1 + 2)  # 3 数学计算
# print("1" + 2) # 报错TypeError

# str --> int
number01 = int("18")
# int --> str
message = str(18)
# str --> float
number02 = float("1.234")
# float --> int
number03 = int(1.934)  # 1.? -向下取整数-> 1
print(number03)

# 案例:计算明年年龄
# age = int(input("请输入年龄:"))
# print("明年你" + str(age + 1) + "岁啦")

# 案例:找零
# price = float(input("请输入价格:"))
# print(10 - price)

# 注意
# 字符串必须符合代转类型的格式
# number = int("程小华")  # 报错
# number = int("1.234")  # 报错  int(1.234) 可以
