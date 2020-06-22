"""
定义函数,根据年/月/日三个参数,获取星期.
星期一
星期二
...
星期日
"""
import time


def get_weeks():
    year = int(input("输入年份"))
    mother = int(input("输入月份"))
    day = int(input("输入日份"))
    weeks_dict = {0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"}
    # weeks_tuple = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    date_tuple = time.strptime(f"{year}/{mother}/{day}", "%Y/%m/%d")
    # return weeks_tuple[date_tuple[-3]]
    return weeks_dict[date_tuple[-3]]


print(get_weeks())
