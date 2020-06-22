"""
4. 使用列表存储1970年到2050年之间所有闰年
@author hailin
@date 2020-05-08
"""
list_year = [year for year in range(1970, 2051) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]

# 显示结果
print(list_year)
