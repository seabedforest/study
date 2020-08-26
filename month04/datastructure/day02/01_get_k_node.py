"""
单链表 输出倒数第k个节点
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_k_node(self, head, k):
        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next
        if k > len(li):
            raise Exception('index out of range')
        return li[-k]


if __name__ == '__main__':
    s = Solution()
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.get_k_node(head, 2).value)
