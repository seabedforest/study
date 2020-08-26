"""
顺序存储的方式实现栈
思路：
    1、栈 ：LIFO 后进先出
    2、设计
       列表尾部作为栈顶（入栈、出栈操作）
       列表头部作为栈底（不进行任何操作）
"""


class Stack:
    def __init__(self):
        """初始化一个空栈"""
        self.elems = []

    def is_empty(self):
        """判断栈是否为空栈"""
        return self.elems == []

    def push(self, item):
        """入栈: 相当于在链表尾部添加1个元素"""
        self.elems.append(item)

    def destack(self):
        """出栈: 相当于在列表尾部弹出1个元素"""
        if self.is_empty():
            raise Exception('destack from empty stack')
        return self.elems.pop()


if __name__ == '__main__':
    s = Stack()
    # 栈(栈底->栈顶): 100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 终端1: 300 200 100 异常
    print(s.destack())
    print(s.destack())
    print(s.destack())
    print(s.destack())
