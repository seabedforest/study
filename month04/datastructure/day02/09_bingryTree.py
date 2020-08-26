"""
二叉树
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        """初始化一颗空树,树根为None的树为空树"""
        self.root = None

    def add(self, item):
        """在二叉树中添加一个节点"""
        node = Node(item)
        # 情况1： 空树情况
        if not self.root:
            self.root = node
            return
            # 情况2: 非空树情况
        node_list = [self.root]
        while True:
            cur = node_list.pop(0)
            # 判断左孩子
            if cur.left:
                node_list.append(cur.left)
            else:
                cur.left = node
                return

                # 判断右孩子
            if cur.right:
                node_list.append(cur.right)
            else:
                cur.right = node
                return

    def breadth_travel(self):
        """广度遍历： 层次遍历，利用队列思想"""
        # 情况1: 空树情况
        if not self.root:
            return

        # 2.非空树情况
        node_list = [self.root]
        while node_list:
            cur = node_list.pop(0)
            print(cur.value, end=' ')
            # 添加左右孩子
            if cur.left:
                node_list.append(cur.left)
            if cur.right:
                node_list.append(cur.right)

if __name__ == '__main__':
    bt = BinaryTree()
    bt.add("A")
    bt.add("B")
    bt.add("C")
    bt.add("D")
    bt.add("E")
    bt.add("F")
    bt.add("G")
    bt.add("H")
    bt.add("I")
    bt.add("J")
    bt.add("K")
    bt.add("L")
    bt.add("M")
    #终端1 广度遍历
    bt.breadth_travel()