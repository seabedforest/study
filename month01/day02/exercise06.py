"""
    在终端中录入一个疫情确诊人数再录入一个治愈人数
    打印治愈比例
    格式：治愈比例为xx%
"""

confirmed = int(input("请输入确诊人数："))
cure = int(input("请输入治愈人数："))
cure_rate = cure / confirmed * 100
print("治愈比例为" + str(cure_rate) + "%")
