"""
文件读取示例
"""

f = open("1.txt",'r')

# 读取文件内容
data = f.read() # 不加参数表示读取所有文件中的内容
print("读取到的内容:",data)

# 对于大文件，通常避免一次读取过大的数据，循环读取
# while True:
#     data = f.read() # 当读取到文件结尾继续读会得到空字符串
#     if not data:
#         # data 为空字符串则退出循环
#         break
#     print(data)
f.seek(0,0)
# 每次读取一行内容
line = f.readline()
print("一行内容:",line)
line = f.readline()
print("一行内容:",line)

# 读取文件形成一个列表
# list_ = f.readlines()
# print(list_)

# 对文件对象迭代取值,每次取一行内容
# for line in f:
#     print(line)


f.close()