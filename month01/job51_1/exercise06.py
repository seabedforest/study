"""
如果是vip客户,消费小于等于500,享受85折
            消费大于500,享受8折
如果不是vip客户,消费大于等于800,享受9折
              消费小于800,原价
在终端中输入账户类型,消费金额,计算折扣.
循环计算折扣,直到账户输入空字符串结束
"""
# 无限循环，空字符串结束循环
while True:
    account_type = input("请输入你的账号类型")
    if account_type == "":
        break
    sum_consumption = float(input("请输入你消费金额:"))
    if account_type == "vip":
        if sum_consumption > 500:
            print("享受8折")
        else:
            print("享受85折")
    else:
        if sum_consumption >= 800:
            print("享受9折")
        else:
            print("原价")