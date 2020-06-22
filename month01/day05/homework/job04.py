"""
6. 计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
   字符串列表：words =["qtx","看一看","想啊想","练练"]
@author hailin
@date 2020-05-07
"""
# 字符串列表
words = ["qtx", "看一看", "想啊想", "练练"]
list_word = []
# 遍历、逻辑比较
for word in words:
    if len(word) > 2:
        if word[0] == word[-1]:
            list_word.append(word)
# 显示结果
# print(f"第⼀个和最后⼀个字符相同的字符串个数为{len(list_word)},分别为{list_word}")
print("第⼀个和最后⼀个字符相同的字符串个数为%d,分别为%s" % (len(list_word), list_word))
