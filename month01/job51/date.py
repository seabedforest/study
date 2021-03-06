"""
从屏幕输入一个日期，判断该日期是这一年的第几天
@author hailin
@date  2020-05-03
"""
# p ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# r ={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日份:"))

# 判断年份是平年还是闰年(平年：rn=0,闰年：rn=1)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    rn = 1
else:
    rn = 0
# 以月份为键，以这个月的天数为值
date = {1: 31, 2: 28 + rn, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# 逻辑运算，计算总共有多少天
days = 0
if month < 1 or month > 12 or day < 1 or day > 31:
    print("输入的是错误的月份(1~12)或日份(1~31)")
else:
    for i in range(1, month):
        days += date[i]
    else:
        days += day
    # 显示结果
    print("今天是今年第", days, "天")
