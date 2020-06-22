"""
    汇率转换器
"""

# 获取美元
usd = float(input("请输入美元:"))
# 美元 转换为 人民币
rmb = usd * 7.0812
# 显示结果
print(str(usd) + "美元=" + str(rmb) + "人民币")
