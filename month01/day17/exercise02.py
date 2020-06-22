class MyRangeIterator:  # 迭代器
    def __init__(self, data_end):
        self.data_end = data_end
        self.index = -1

    def __next__(self):
        # 数据如果到了最大值,则停止迭代.
        if self.index > self.data_end - 2:
            raise StopIteration()
        self.index += 1
        return self.index


class MyRange:  # 可迭代对象
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)


for i in MyRange(5):
    print(i)
