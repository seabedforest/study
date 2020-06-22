"""
使用input输入一个系统中的普通文件路径，将这个文件拷贝到
练习代码所在目录    （windows系统）
"""
file_url = input("普通文件路径：")
file_name = file_url.split('\\')[-1]
fr = open(file_url)
fw = open(file_name, 'w+')
for line in fr:
    fw.write(line)
fr.close()
fw.close()
