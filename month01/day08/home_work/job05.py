"""
7. 参照下列代码,定义函数,计算税率和速算扣除数.
        money = float(input('请输入应纳税所得额'))
        if money <= 36000:
            tax_rate = 0.03
            deduction = 0
        elif money <= 144000:
            tax_rate = 0.1
            deduction = 2520
        elif money <= 300000:
            tax_rate = 0.2
            deduction = 16920
        elif money <= 420000:
            tax_rate = 0.25
            deduction = 31920
        elif money <= 660000:
            tax_rate = 0.3
            deduction = 52920
        elif money <= 960000:
            tax_rate = 0.35
            deduction = 85920
        else:
            tax_rate = 0.45
            deduction = 181920
        # print('税率是%.0f%%速算扣除数是%d' % (tax_rate * 100, deduction))
        print(f'税率是{tax_rate * 100}%速算扣除数是{deduction}')
"""


def calculate_rates_deductions(money):
    """
    计算税率和速算扣除数
    :param money: 应纳税所得额
    :return: 返回税率和速算扣除数
    """
    if money < 36000:
        return 0.03, 0
    if money <= 144000:
        return 0.1, 2520
    if money <= 300000:
        return 0.1, 2520
    if money <= 420000:
        return 0.25, 31920
    if money <= 660000:
        return 0.3, 52920
    elif money <= 960000:
        return 0.35, 85920
    return 0.45, 181920


# 调用

tax_rate, deduction = calculate_rates_deductions(960000)
print(f'税率是{tax_rate * 100}%速算扣除数是{deduction}')
