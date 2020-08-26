"""
链式存储实现栈模型
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListStack:
    def __init__(self):
        """初始化一个空栈"""
        self.head = Node

    def is_empty(self):
        """判断是否为空栈"""
        return self.head == None

    def push(self, item):
        """入栈：相当于在链表头部添加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        """出栈：相当于删除链表头节点"""
        if not self.head:
            raise Exception('pop from empty stack')
        item = self.head.value
        self.head = self.head.next

        return item

if __name__ == '__main__':
    s= LinkListStack()
    s.push(100)
    s.push(200)
    s.push(300)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())