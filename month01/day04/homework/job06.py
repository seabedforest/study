"""
6. 模拟登录
    如果账号的密码错误3次，提示锁定账户，效果如下：
        请输入账号：qtx
        请输入密码：1234
        登录失败
        你还剩余 2 次机会
        请输入账号：Qtx
        请输入密码：1234
        登录失败
        你还剩余 1 次机会
        请输入账号：Qtx
        请输入密码：123456
        登录成功
@author hailin
@date 2020-05-06
"""
# 账户、密码、计算器
id = "hailin"
password = "123456"
count = 3
# 循环登录账户过程
while count > 0:
    get_id = input("请输入你的账号:")
    get_password = input("请输入你的密码:")
    if get_id == id and get_password == password:
        print("登录成功")
        break
    else:
        count -= 1
        if count == 0:
            print("你的账号被锁定")
            break
        print("登录失败，你还剩余%d次机会" % count)
