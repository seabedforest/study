"""
练习1 ： 对大文件进行拆分
将一个文件拆分成两部分，按照字节数进行平均拆分
要求使用两个子进程，分别做上半部分和下半部分的拆分，同时进程

温馨提示 ：　os.path.getsize() 获取文件大小
"""
from multiprocessing import Process
import os

filename = input("File:")
size = os.path.getsize(filename) # 获取文件大小
file = filename.split('/')[-1] # 提取出真正的文件名称

# 复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top-'+file,'wb')
    n = size // 2
    # fw.write(fr.read(n))
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bot-'+file,'wb')
    fr.seek(size//2,0) # 将文件偏移量移动到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()

jobs = []
# 循环创建进程
for i in [top,bot]:
    p = Process(target=i)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()




