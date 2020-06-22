class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)


pos01 = Vector2(3, 4)
pos02 = Vector2(8, 9)

pos03 = pos01 - pos02
print(pos03.x)
print(pos03.y)
pos04 = pos01 + pos02
print(pos04.x)
print(pos04.y)
