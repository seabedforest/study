"""
从一个文本中查找单词： 编写一个而程序，input输入一个单词
获取这个单词的解释，打印出来。

提示 ： dict.txt
      每行一个单词
      单词与解释之间有空格
      单词有序排列 (后面的大于前面的)
"""
word = input("单词:")

f = open("/home/tarena/PycharmProjects/python_study/month02/day03/dict.txt")
#查单词
for line in f:
    w = line.split(" ")
    if w[0] > word:
        print("没有该单词")
        break
    elif word == w[0]:
        print(line)
        break
else:
    print("没有该单词")

f.close()