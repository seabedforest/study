"""
在终端中循环录入内容,如果录入空字符串则停止.
打印所有录入的内容(字符串)
"""
list_city=[]
while True:
    outbreak = input("请输入疫情地区:")
    if outbreak == "":
        break
    list_city.append(outbreak)

result = "-".join(list_city)
print(result)