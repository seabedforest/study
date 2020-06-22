"""
    在终端中录入一个整数，
    如果是奇数为变量state赋值"奇数",
    否则赋值"偶数"。
    尽量使用:真值表达式,条件表达式
"""
number = int(input("请输入数字："))
state = "偶数" if number % 2 == 0 else "奇数"
print(state)
