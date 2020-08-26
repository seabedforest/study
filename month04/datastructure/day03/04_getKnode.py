"""
给定一颗二叉搜索树，返回第k小的结果
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.mid_result = []

    def get_k_node(self, root, k):
        array_list = self.mid_travel(root)
        if len(array_list) < k:
            raise Exception('paranormal')
        return array_list[k - 1]

    def mid_travel(self, root):
        if not root:
            return

        self.mid_travel(root.left)
        self.mid_result.append(root.value)
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
    print(s.get_k_node(n12, 3))
