"""
    格式化字符串
        格式%(变量)
"""
# 字符串拼接:  格式 + 变量 + 格式 + 变量
# 缺点:代码可读性差
# number_jin = 3
# number_liang = 6
# print("结果为：" + str(number_jin) + "斤" + str(number_liang) + "两")

# usd = 10
# rmb = 70.812
# print(str(usd) + "美元 = " + str(rmb) + " 人民币")

usd = 10
rmb = 70.892
print("%.2f 美元 = %.1f 人民币" % (usd, rmb))

number_jin = 3
number_liang = 6
print("结果为：%d斤%d两" % (number_jin, number_liang))


