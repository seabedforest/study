"""
顺序队列 - 实现

"""


class ListQueue:
    def __init__(self):
        """初始化一个空队列"""
        self.queue = []

    def is_empty(self):
        """判断是否为空队列"""
        return self.queue == []

    def enqueue(self, item):
        """入队: 相当于在列表的尾部添加一个元素"""
        self.queue.append(item)

    def dequeue(self):
        """出队: 相当于删除列表第一个元素"""
        if self.is_empty():
            raise Exception('dequeue from empty queue')
        return self.queue.pop(0)


if __name__ == '__main__':
    lq = ListQueue()
    lq.enqueue(100)
    lq.enqueue(200)
    lq.enqueue(300)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
