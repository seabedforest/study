"""
输入两个链表，查找第一个公共节点
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_first_pubilc_node(self, head1, head2):
        # 1.2个列表,分别存储两个链表中的所有节点
        li1 = []
        li2 = []
        cur1 = head1
        while cur1:
            li1.append(cur1)
            cur1 = cur1.next
        cur2 = head2
        while cur2:
            li2.append(cur2)
            cur2 = cur2.next
        # 2.从尾到头依次判断
        node = None
        while li1 and li2:
            if li1[-1] is li2[-1]:
                node = li1.pop()
                li2.pop()
            else:
                break
        return node


if __name__ == '__main__':
    s = Solution()
    n100 = Node(100)
    n200 = Node(200)
    n300 = Node(300)
    n400 = Node(400)
    n666 = Node(666)
    head1 = n100
    head1.next = n200
    n200.next = n300
    n300.next = n400

    head2 = n666
    head2.next = n300
    n300.next = n400

    print(s.get_first_pubilc_node(head1, head2).value)
