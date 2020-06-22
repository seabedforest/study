"""
6.  参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
@author hailin
@date 2020-05-11
"""


def Calculate_social_security_contributions(salary_before_tax):
    """
    计算社保缴纳费用
    :param salary_before_tax: 税前工资
    :return:  返回缴纳社保费用
    """
    return salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3


# 调试
print("个人需要缴纳社保费用：" + str(Calculate_social_security_contributions(10000)))
