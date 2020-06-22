"""
对大文件进行拆分，一分为二，按照字节数进行平均拆分
"""
from multiprocessing import Process
import os

f = open("dict.txt", "rb")
f_size = os.path.getsize("dict.txt")
fw1 = open("dict-1.txt", 'wb')
fw2 = open("dict-2.txt", 'wb')
def fun01():

    data1 = f.read(f_size // 2)
    fw1.write(data1)
    fw1.close()


def fun02():

    f.seek(f_size // 2, 0)
    data2 = f.read(f_size // 2)
    fw2.write(data2)
    fw2.close()


f_list1 = [fun01, fun02]
p_list = []
for i in f_list1:
    p = Process(target=i)
    p_list.append(p)
    p.start()

for i in p_list:
    i.join()

f.close()
