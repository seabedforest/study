"""
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""
price = float(input("商品单价："))
number = float(input("购买数量："))
cost = float(input("支付金额："))
pay_back = cost - price * number
print("应找回：" + str(pay_back))
