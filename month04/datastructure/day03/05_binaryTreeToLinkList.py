"""
二叉搜索树转为排序的双向链表
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.mid_result = []

    def binarytree_to_link_list(self, root):
        array_list = self.mid_travel(root)
        if len(array_list) == 0:
            return
        elif len(array_list) == 1:
            return root
        # 1.搞定头节点和尾节点
        array_list[0].left = None
        array_list[0].right = array_list[1]
        array_list[-1].right = None
        array_list[-1].left = array_list[-2]
        # 2.搞定中间节点
        for index in range(1, len(array_list) - 1):
            array_list[index].left = array_list[index - 1]
            array_list[index].right = array_list[index + 1]
        # 返回双向链表的头节点
        return array_list[0]

    def mid_travel(self, root):
        if not root:
            return
        self.mid_travel(root.left)
        self.mid_result.append(root)
        self.mid_travel(root.right)

        return self.mid_result


if __name__ == '__main__':
    s = Solution()
    n12 = Node(12)
    n5 = Node(5)
    n2 = Node(2)
    n9 = Node(9)
    n15 = Node(15)
    n16 = Node(16)
    n17 = Node(17)
    n18 = Node(18)
    n19 = Node(19)
    # 创建二叉搜索树
    n12.left = n5
    n12.right = n18
    n5.left = n2
    n5.right = n9
    n18.left = n15
    n18.right = n19
    n15.right = n17
    n17.left = n16
    # 测试方法
    head = s.binarytree_to_link_list(n12)
    cur = head
    while cur:
        print(cur.value, end=" ")
        cur = cur.right
