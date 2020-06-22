"""
练习 ： 编写一个程序，列出指定目录（input输入）下所有大小超过 1024字节的普通文件文件名
"""
import os

dir_path=input("目录路径:")
dir_list = os.listdir(dir_path)
for item in dir_list:
    if os.path.isfile(dir_path+'\\'+item):
        if os.path.getsize(dir_path+'\\'+item) > 1024:
            print(item)