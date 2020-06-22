"""
在终端中录入一个内容,循环打印每个文字的编码值。
@author hailin
@date 2020-05-06
"""
name = input("你的姓名:")
for word in name:
    word_value = ord(word)
    print(word_value)