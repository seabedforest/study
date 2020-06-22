"""
    for + range
        依次获取一个范围内的数据
    练习:exercise03 
"""
# 写法1:
# range(开始,结束,间隔)
# 包含开始,不包含结束
for item in range(2, 6, 1):
    print(item)  # 2~5

# 写法2:
# range(开始,结束)
# 间隔默认1
for item in range(2, 6):
    print(item)  # 2~5

# 写法3:
# range(结束)
# 开始默认0
for item in range(6):
    print(item)  # 0~5
