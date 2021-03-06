"""
输入一个链表，按链表值从尾到头依次排列
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_array_list(self, head):
        array_list = []
        cur = head
        while cur:
            array_list.append(cur.value)
            cur = cur.next
        # 反转链表
        array_list.reverse()
        return array_list


if __name__ == '__main__':
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    s = Solution()
    print(s.get_array_list(head))
