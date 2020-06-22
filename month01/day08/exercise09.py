"""
day04/home_work/exercise03
根据下列代码,定义函数,判断折扣.
account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))
if account_type == "vip":
if money < 500:
print("享受85折扣")
else:
print("享受8折扣")
else:
if money > 800:
print("享受9折扣")
else:
print("原价购买")
"""



def get_account_type(account_type):
    return account_type == "vip"

def get_discount(account_type, consumption_money):
    if get_account_type(account_type):
        return 0.85 if consumption_money < 500 else 0.8
    return 0.9 if consumption_money > 800 else 1

account_type = input("请输入账户类型：")
consumption_money = float(input("请输入消费金额："))
print(get_discount(account_type,consumption_money))