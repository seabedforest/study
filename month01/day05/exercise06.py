"""
list_city = ["黑龙江", "香港", "台湾"]
list_cofirmed = [138, 104, 95]
list_total = [944, 1040, 440]

1. 从头到尾打印list_city中所有元素
2. 从尾到头打印list_cofirmed中所有元素
3. 从第二个元素开始到尾打印list_total元素
要求:一个元素独占一行
"""
list_city = ["黑龙江", "香港", "台湾"]
list_cofirmed = [138, 104, 95]
list_total = [944, 1040, 440]
for i in list_city:
    print(i)

for i in range(len(list_cofirmed) - 1, -1, -1):
    print(list_cofirmed[i])

for i in range(1, len(list_total)):
    print(list_total[i])
