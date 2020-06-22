"""
9.  在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
    考点:如何记录不重复的地区
@author hailin
@date 2020-05-07
"""
# 获取疫情地区名称、创建城市列表
list_city = []
while True:
    district = input("输入疫情地区名称:")
    if district == "":
        break
    if district not in list_city:
        list_city.append(district)

# 倒序打印所有省份名称(一行一个)
for num in range(len(list_city) - 1, -1, -1):
    print(list_city[num])
