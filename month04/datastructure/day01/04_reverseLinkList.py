"""
输入一个链表，反转链表后，输出新链表的表头
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverse_link(self, head):
        # 创建两个游标
        pre = None
        cur = head
        while cur:
            # 记录当前操作节点的下一个节点
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        # 循环结束后,pre代表的节点就是反转后链表的头节点
        return pre


if __name__ == '__main__':
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)

    s = Solution()
    new_head = s.reverse_link(head)
    cur=new_head
    while cur:
        print(cur.value,end=' ')
        cur=cur.next