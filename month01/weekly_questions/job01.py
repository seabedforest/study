dict_region_information = {
    "北京": {
        "景区": ["长城", "故宫"], "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"], "美食": ["火锅", "兔头"]
    }
}


print(dict_region_information["北京"]["美食"][2])
dict_region_information["四川"]["美食"][1] = "双流兔头"
print(dict_region_information)

dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]

list_commodity_infos = list(dict_commodity_infos.items())
for i in range(len(list_commodity_infos) -1):
    for j in range(i+1,len(list_commodity_infos)):
        if list_commodity_infos[i][1]['price'] > list_commodity_infos[j][1]['price']:
            list_commodity_infos[i],list_commodity_infos[j]=list_commodity_infos[j],list_commodity_infos[i]

print(list_commodity_infos)