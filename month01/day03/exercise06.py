"""
    在收银台练习基础上，增加新功能。
	如果钱不够提示"金额不足"
	否则提示"应找回：xx元"
"""
prece = float(input("商品单价："))
number = int(input("购买的数量："))
payment_amount = float(input("支付金额："))
find_money = payment_amount - prece * number
if payment_amount > prece * number:
    print("应找回" + str(find_money) + "元")
else:
    print("余额不足")
