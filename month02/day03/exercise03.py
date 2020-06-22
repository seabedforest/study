"""
使用input输入一个系统中的普通文件路径，将这个文件拷贝到
练习代码所在目录    不确定复制文件的格式 （linux系统）
"""


def copy_file(file_url):
    file_name = file_url.split('/')[-1]
    fr = open(file_url, 'rb')
    fw = open(file_name, 'wb')
    while True:
        data = fr.read(1024 * 1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


if __name__ == '__main__':
    file_url = input("文件路径:")
    copy_file(file_url)
