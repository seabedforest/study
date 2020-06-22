"""
现在有两个文本文件（自己指定），编写一个程序，将两个文件合并为一个
@author hailin
@date 2020-05-31
"""
def merge_file_contents(file01,file02,newfile):
    """
    将两个文本文件合并为一个文本文件
    :param file01: 要被合并的文件1
    :param file02: 要被合并的文件2
    :param newfile: 合并成的新文件
    :return: None
    """
    fr01 = open(file01)
    fr02 = open(file02)
    fw = open(newfile,'w+')
    while True:
        data = fr01.read(1024*1024)
        if not data:
            break
        fw.write(data)

    while True:
        data = fr02.read(1024*1024)
        if not data:
            break
        fw.write(data)

    fr01.close()
    fr02.close()
    fw.close()


if __name__ == '__main__':
    file01 = input("输入要被合并的文件1路径:")
    file02 = input("输入要被合并的文件2路径:")
    newfile = input("输入合并后文件所存储的路径:")
    merge_file_contents(file01,file02,newfile)