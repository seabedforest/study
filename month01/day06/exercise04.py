"""
根据年月日,计算是这一年的第几天.
公式：前几个月天数 + 当月天数
例如：2020年5月10日
计算：31 29 31 30 + 10
"""

year = int(input("请输入一个年份："))
month = int(input("请输入一个月份："))
day = int(input("请输入一个天数："))
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# 一年12个月的所有天数,存入容器
days = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_day = sum(days[:month - 1]) + day
print(total_day)
