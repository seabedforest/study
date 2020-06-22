"""
    在终端中,重复执行下列代码,输入q退出.
    number = int(input("请输入数字："))
    state = "偶数" if number % 2 == 0 else "奇数"
    print(state)
"""
while True:
    number = int(input("请输入数字："))
    state = "偶数" if number % 2 == 0 else "奇数"
    print(state)
    if input("如果退出请输入q：")=="q":
        break # 退出