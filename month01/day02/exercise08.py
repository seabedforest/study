"""
    古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""
total_weight = int(input("请输入多少两："))
number_jin = total_weight // 16
number_liang = total_weight % 16
print("结果为：" + str(number_jin) + "斤" + str(number_liang) + "两")
