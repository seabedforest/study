"""
两个栈实现一个队列，完成队列的push和pop操作
"""


class Solution:
    def __init__(self):
        """初始化两个空栈"""
        self.stack_a = []
        self.stack_b = []

    def push(self, item):
        """入队操作: 相当于在stack_a中append一个元素"""
        self.stack_a.append(item)

    def pop(self):
        """出队操作: 在stack_b中pop一个元素"""
        if self.stack_b:
            return self.stack_b.pop()

        # 当stack_b为空时,把stack_a中的元素出栈到stack_b中
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()


if __name__ == '__main__':
    s = Solution()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.pop())
    print(s.pop())
    print(s.pop())
