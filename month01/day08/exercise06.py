"""
根据下列代码,定义函数,获取计算这是这一年的第几天.
year = int(input("请输入年份："))
month = int(input("请输入月份：")) # 5
day = int(input("请输入天："))
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_day = sum(days[:month - 1])
total_day += day
print(f"{year}年{month}月{day}日为这一年的第{total_day}天")
"""

def calculate_days(year, month, day):
    day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    days = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_day = sum(days[:month - 1])
    total_day += day
    return total_day

total_day = calculate_days(2020, 5, 11)
print(f"这一年的第{total_day}天")
