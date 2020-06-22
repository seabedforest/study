"""
在log.txt文件上完成，写一个程序
input输入一个接口名称
得到该接口描述中的 address is 的地址值
@author hailin
@date 2020-06-01
"""
import re
def gain_logfile_mac(interface_name):
    f = open("log.txt")
    data = f.read()
    obj01 = re.split('\n\n',data)
    for line in obj01:
        name =re.match(r"\b%s\b" % interface_name,line)
        if name:
            mac=re.search("\w+?\.\w+?\.\w{4}",line).group()
            f.close()
            return interface_name,mac
interface_name = input("输入接口名称:")
print(gain_logfile_mac(interface_name))