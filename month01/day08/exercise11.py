"""
day07/home_work/exercise03
根据下列代码,定义函数,获取一个范围内的所有闰年.
list_year = [item for item in range(1970, 2051)
if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
print(list_year)
"""


def get_leap_year_area(year_start, year_finish):
    list_year = [item for item in range(year_start, year_finish)
                 if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
    return list_year


print(get_leap_year_area(1970, 2051))
