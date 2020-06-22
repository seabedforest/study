"""
confirmed = int(input("请输入确诊人数："))
cure = int(input("请输入治愈人数："))
cure_rate = cure / confirmed * 100
print("治愈比例为" + str(cure_rate) + "%")
"""

def gain_cure_rate(confirmed, cure):
    """
    获取治愈比列
    :param confirmed: 确诊人数
    :param cure: 治愈人数
    :return: 治愈比列
    """
    cure_rate = cure / confirmed * 100
    return cure_rate

print(gain_cure_rate(100, 90))

"""
total_weight = int(input("请输入多少两："))
number_jin = total_weight // 16
number_liang = total_weight % 16
print("结果为：" + str(number_jin) + "斤" + str(number_liang) + "两")
"""
def liang_to_jin(total_weight):
    """
    一斤十六两，把两转换成斤
    :param total_weight: 总共多少两
    :return:
    """
    number_jin = total_weight // 16
    number_liang = total_weight % 16
    return number_jin,number_liang

jin,liang=liang_to_jin(100)
print("结果为：" + str(jin) + "斤" + str(liang) + "两")
