class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 对象相同的判定语句
    def __eq__(self, other):
        # return id(self) == id(other) 在父类中默认按地址比较
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x


pos01 = Vector2(1, 2)
pos02 = Vector2(1, 3)
# 本质: pos01.__eq__(pos02)
print(pos01 == pos02)  # True 内容相同
print(pos01 is pos02)  # False 地址相同 两个变量存储的对象不同

list01 = [
    Vector2(4, 4),
    Vector2(2, 2),
    Vector2(1, 1),
    Vector2(5, 5),
    Vector2(3, 3),
]

# 练习:
# TypeError: '<' not supported between instances of 'Vector2' and 'Vector2'
list01.sort()  # 从小到大排序
for item in list01:
    print(item.__dict__)
