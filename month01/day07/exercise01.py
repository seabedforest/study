"""
练习1：将两个列表，合并为一个字典
姓名列表["张无忌","赵敏","周芷若"]
房间列表[101,102,103]
练习2：颠倒练习1字典键值
"""
list_name = ["张无忌","赵敏","周芷若"]
list_room = [101,102,103]
dict_name_room01 = {list_name[i]:list_room[i] for i in range(len(list_name))}
print(dict_name_room01)

dict_name_room02 = {value:key for key,value in dict_name_room01.items()}
print(dict_name_room02)