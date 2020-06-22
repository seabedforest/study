"""
    条件表达式
        有选择性的为变量赋值
    练习:exercise11
"""
sex = input("请输入性别:")
# if sex == "男":
#     value = 1
# else:
#     value = 0
value = 1 if sex == "男" else 0
print(value)
