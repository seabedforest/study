"""
之字形打印二叉树
奇数层： 从左到右
偶数层： 从右到左
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree_node(self, root):
        cur_stack = [root]
        next_stack = []
        level = 1
        while cur_stack:
            cur = cur_stack.pop()
            print(cur.value, end=' ')

            # 分支： 奇数层先左后右，偶数层先右后左
            if level % 2 == 1:
                if cur.left:
                    next_stack.append(cur.left)
                if cur.right:
                    next_stack.append(cur.right)
            else:
                if cur.right:
                    next_stack.append(cur.right)
                if cur.left:
                    next_stack.append(cur.left)
            if not cur_stack:
                cur_stack, next_stack = next_stack, cur_stack
                print()
                level += 1


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

    s.print_tree_node(p1)