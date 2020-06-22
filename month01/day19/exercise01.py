"""
使用内置高阶函数实现：
1. ([11],[222],[333])
获取元组中长度最大的列表
2. 在老婆列表列表，获取所有名称与身高
3. 在老婆列表中，获取所有体重大于50的老婆
4. 对老婆列表，根据身高进行降序排列
5. 获取所有身高大于1.6的老婆名称和身高.
"""


class Wife:
    def __init__(self, name="", height=0, weight=0, face_score=0, money=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.face_score = face_score
        self.money = money


list_wifes = [
    Wife("双儿", 171, 100, 96, 6000),
    Wife("小郡主", 162, 90, 86, 20000),
    Wife("建宁", 168, 95, 95, 30000),
    Wife("方怡", 173, 108, 96, 5000),
    Wife("凤姐", 150, 180, 30, 10000),
    Wife("沐剑屏", 61, 100, 90, 6000),
    Wife("阿珂", 181, 88, 100, 6000)
]

# 1.获取元组中长度最大的列表
tup01 = ([11], [222], [333])
result = max(tup01, key=lambda item: len(item))
print(result)

# 2.在老婆列表列表，获取所有名称与身高
for item in map(lambda item: (item.name, item.height), list_wifes):
    print(item)

# 3. 在老婆列表中，获取所有体重大于50的老婆
for item in filter(lambda item: item.weight > 50, list_wifes):
    print(item.__dict__)
