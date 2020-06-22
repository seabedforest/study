"""
    在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
@author hailin
@date 2020-05-08
"""
dict_color = {"R": "红色", "G": "绿色", "B": "蓝色", "A": "透明度"}
color_sequence = input("输入颜色序列(RGBA):")
if color_sequence not in dict_color:
    print("该颜色不存在")
else:
    print(dict_color[color_sequence])
