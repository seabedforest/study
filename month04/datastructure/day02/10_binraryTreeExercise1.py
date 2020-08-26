"""
从上到下打印二叉树 同一层结点从左至右输出，每一层输出一行
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree_layer(self, root):
        cur_queue = [root]
        next_queue = []
        while cur_queue:
            cur = cur_queue.pop(0)
            print(cur.value, end=' ')
            # 添加左右孩子到下一层队列
            if cur.left:
                next_queue.append(cur.left)
            if cur.right:
                next_queue.append(cur.right)

            # 如果cur_queue为空时,说明当前层打印完成,下一层添加完毕
            if not cur_queue:
                cur_queue, next_queue = next_queue, cur_queue
                print()


if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p6 = Node(6)
    p7 = Node(7)
    p8 = Node(8)
    p9 = Node(9)
    p10 = Node(10)
    p1.left = p2
    p1.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    p4.left = p8
    p4.right = p9
    p5.left = p10
    s.print_tree_layer(p1)
