"""
正则表达式功能扩展
"""

import re

# 目标字符串
s = """Hello 
北京
"""

# 只能匹配英文字符
l = re.findall(r"\w+", s, flags=re.A | re.I)  # 同时使用多个扩展
print(l)
print("................................")
# 让.可以匹配换行
l = re.findall(r".+", s, flags=re.S)
print(l)
print("................................")
# 匹配时忽略字母大小写
l = re.findall(r"[a-z]+", s, flags=re.I)
print(l)
print("................................")
# 让 ^ 匹配每一行的开始位置  $ 匹配每一行的结尾位置
l = re.findall(r"^\w+", s, flags=re.M)
print(l)
