"""
    两个变量交换
        左手 = "武大郎"
        右手 = "潘金莲"
        步骤：
        桌子 = 左手
        左手 = 右手
        右手 = 桌子
        结果
        print(左手)  # "潘金莲"
        print(右手)  # "武大郎"
"""

bridegroom_name = "武大郎"
bride_name = "潘金莲"

# 思想
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp

# Python 语法
bridegroom_name, bride_name = bride_name, bridegroom_name
print("交换后的新郎：" + bridegroom_name)  #
print("交换后的新娘：" + bride_name)  #
