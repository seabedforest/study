"""
练习1:
创建列表,存储前3个疫情地区名称
创建列表,存储前3个现有确诊人数
创建列表,存储前3个疫情累计人数
练习2:
为练习1的三个列表,追加第4个信息.
为练习1的三个列表,将北京信息插入到第1个位置.
"""
# 练习1
outbreak = ["黑龙江", "香港", "台湾"]
number_of_confirmed = [138, 102, 29]
number_of_cumulative = [68128, 1589, 1276]

# 练习2

outbreak.append("陕西")
number_of_confirmed.append(39)
number_of_cumulative.append(308)

outbreak.insert(0, "北京")
number_of_confirmed.insert(0, 27)
number_of_cumulative.insert(0, 593)
print(outbreak)
print(number_of_confirmed)
print(number_of_cumulative)
