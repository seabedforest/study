"""
list_city = ["黑龙江", "香港", "台湾"]
list_cofirmed = [138, 104, 95]
list_total = [944, 1040, 440]

1. 在list_city列表中,删除香港,删除第一个元素
2. 在list_cofirmed列表中,删除前两个元素
3. 在list_total列表中,删除中间元素
"""
list_city = ["黑龙江", "香港", "台湾"]
list_cofirmed = [138, 104, 95]
list_total = [944, 1040, 440]
list_city.remove("香港")
print(list_city)
del list_city[0]
print(list_city)
del list_cofirmed[:2]
print(list_cofirmed)
del list_total[len(list_total) // 2]
print(list_total)
