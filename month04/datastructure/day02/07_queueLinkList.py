"""
链表队列
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListQueue:
    def __init__(self):
        """初始化一个空队列"""
        self.head = None

    def is_empty(self):
        """判断是否为空队列"""
        return self.head == None

    def enqueue(self, item):
        """队尾入队:相当于在链表尾部添加一个节点"""
        node = Node(item)
        # 空队列情况
        if self.is_empty():
            self.head = node
            return
        # 非空队列情况
        cur = self.head
        while cur.next:
            cur = cur.next
        # 循环结束后,cur一定指向尾节点
        cur.next = node
        node.next = None

    def dequeue(self):
        """队头出队:删除链表头节点"""
        if self.is_empty():
            raise Exception('dequeue from empty queue')

        item = self.head.value
        self.head = self.head.next
        return item


if __name__ == '__main__':
    lq = LinkListQueue()
    lq.enqueue(100)
    lq.enqueue(200)
    lq.enqueue(300)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())