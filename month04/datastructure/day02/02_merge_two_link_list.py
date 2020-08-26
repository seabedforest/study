"""
输入两个单调递增的链表，输出合并后的新单调递增的链表
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def merge_two_link_list(self, head1, head2):
        # 1.确定新链表的头节点
        cur1 = head1
        cur2 = head2
        if cur1.value <= cur2.value:
            merge_head = cur1
            cur1 = cur1.next
        else:
            merge_head = cur2
            cur2 = cur2.next
        # 2.合并
        cur3 = merge_head
        while cur1 and cur2:
            if cur1.value <= cur2.value:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
            cur3 = cur3.next
        # 循环结束后，一定有一个链表为空，要把剩余的节点合并进来
        if cur1:
            cur3.next = cur1
        else:
            cur3.next = cur2

        return merge_head


if __name__ == '__main__':
    s = Solution()
    head1 = Node(100)
    head1.next = Node(200)
    head1.next.next = Node(300)
    head1.next.next.next = Node(400)

    head2 = Node(1)
    head2.next = Node(200)
    head2.next.next = Node(600)
    head2.next.next.next = Node(800)

    new_head = s.merge_two_link_list(head1, head2)

    while new_head:
        print(new_head.value, end=' ')
        new_head = new_head.next
