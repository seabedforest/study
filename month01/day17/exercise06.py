"""
# 练习:打印字典中所有键值对的同时,打印索引.
"""
weeks_dict = {0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"}
for i, (key, value) in enumerate(weeks_dict.items()):
    print(f"编号是{i},键是{key},值是{value}")