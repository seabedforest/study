"""
实现单链表
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    def __init__(self):
        # 初始化一个空链表：头节点为None即为空链表
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        # 判断头节点是否为空
        return self.head == None

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        """在链表头部添加一个节点"""
        # 把node节点添加到头节点
        node = Node(item)
        # 1、把新添加的节点指针指向原来头节点
        node.next = self.head
        # 2、添加的节点设置为新的头
        self.head = node

    def append(self, item):
        """在链表尾部添加一个节点"""
        node = Node(item)
        cur = self.head
        # 1.空链表情况
        if cur is Node:
            self.head = node
            return
        # 2.非空链表情况
        while cur.next:
            cur = cur.next
        # 循环结束后,cur指向尾节点
        cur.next = node
        node.next = None

    def insert(self, position, item):
        """在指定的位置添加节点,position指索引,从0开始"""
        node = Node(item)
        cur = self.head
        count = 0
        while count < position - 1:
            cur = cur.next
            count += 1
        # 循环结束后，cur移动到position的前一个节点
        p = cur.next
        cur.next = node
        node.next = p

    def remove(self, item):
        """在链表中移除一个节点"""
        # 情况1：删除链表节点
        if self.head.value == item:
            self.head = self.head.next

        cur = self.head
        pre = None
        while cur:
            if cur.value == item:
                pre.next = cur.next
                return
            # 移动两个游标
            pre = cur
            cur = cur.next

    def length(self):
        """计算链表的长度"""
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count


if __name__ == '__main__':
    s = SingleLinkList()
    s.add(300)
    s.add(200)
    s.add(100)
    s.append(400)
    print(s.is_empty())
    s.insert(2,666)
    s.travel()
    s.remove(300)
    s.travel()
    print(s.length())
