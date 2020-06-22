"""
# 1)打印所有城市（一行一个）
# 2)打印北京所有美食（一行一个）
# 3)打印四川所有景区（一行一个）
# 4)打印所有城市的所有景区（一行一个）
# 5)为北京添加景区："天坛"
# 6)删除四川美食：兔头
"""
dict_travel_info = {
"北京": {
    "景区": ["长城", "故宫"],
    "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
},
"四川": {
    "景区": ["九寨沟", "峨眉山"],
    "美食": ["火锅", "兔头"]
}
}
# 1)打印所有城市（一行一个）
for city in dict_travel_info.keys():
    print(city)
# 2)打印北京所有美食（一行一个）
for cate in dict_travel_info["北京"]["美食"]:
    print(cate)
# 3)打印四川所有景区（一行一个）
for scenic in dict_travel_info["四川"]["景区"]:
    print(scenic)
# 4)打印所有城市的所有景区（一行一个）
for city in dict_travel_info.keys():
    for scenic in dict_travel_info[city]["景区"]:
        print(scenic)
# 5)为北京添加景区："天坛"
dict_travel_info["北京"]["景区"].append("天坛")
# 6)删除四川美食：兔头
dict_travel_info["四川"]["美食"].remove("兔头")
print(dict_travel_info)