# 根据命题写出代码：是闰年
# 条件1:年份能够被４整除但是不能被100整除
# 条件2:年份能够被400整除

year = int(input("输入年份"))
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
