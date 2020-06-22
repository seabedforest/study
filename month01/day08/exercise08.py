"""
根据下列代码定义函数根据字母判断颜色.
dict_color_info = {"R": "红色" "G": "绿色" "B": "蓝色" "A": "透明度"}
color = input("请输入颜色(RGBA):")
# print(dict_color_info[color]) # 如果字典不存在当前key会报错.

if color in dict_color_info:
print(dict_color_info[color])
else:
print("您输入的颜色不存在")
"""


def get_color(key):
    """..."""
    dict_color_info = {"R": "红色", "G": "绿色", "B": "蓝色", "A": "透明度"}
    return dict_color_info[color] if key in dict_color_info else None

color = input("请输入颜色(RGBA):")
print(get_color(color))
