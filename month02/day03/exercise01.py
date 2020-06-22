"""
从一个文本中查找单词： 编写一个而程序，input输入一个单词
获取这个单词的解释，打印出来。
"""
word = input("输入要查询的单词:")
f = open("dict.txt", 'r')

for line in f:
    w = line.split(' ')
    if w[0] > word:
        print("没有该单词")
        break
    elif word == w[0]:
        print(line)
        break
else:
    print("没有该单词")
f.close()