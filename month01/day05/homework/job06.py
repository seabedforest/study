"""
8.  判断一个字符串是否是回文
    例如：上海自来水来自海上
         山西运煤车煤运西山
    思路:字符串正序 等于 反序
@author hailin
@date 2020-05-07
"""


# 定义回文函数
def plalindrome(str):
    if str[:] == str[::-1]:
        print("该字符串是回文")


#  字符串数据
str01 = "上海自来水来自海上"
str02 = "山西运煤车煤运西山"

# 显示结果
plalindrome(str01)
plalindrome(str02)
