"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
《删除链表的倒数第N个节点》

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        p2_prev = None
        tik = 0
        while True:
            if p1.next is None:
                break
            if tik >= n - 1:
                p2_prev = p2
                p2 = p2.next
            p1 = p1.next
            tik += 1
        if p2_prev is None:
            return head.next
        else:
            p2_prev.next=p2.next
            return head


def create_link_list(num_list):
    head = ListNode(num_list[0])
    cur_node = head
    for i in range(1, len(num_list)):
        next_node = ListNode(num_list[i])
        cur_node.next = next_node
        cur_node = next_node

    return head


def print_link_list(head):
    node = head
    s = ''
    while node is not None:
        s+=str(node.val)
        s+='->'
        node = node.next
    print(s)

sol = Solution()
# head = sol.removeNthFromEnd(create_link_list([1,2,3,4,5]), 2)
# print_link_list(head)
#
# head = sol.removeNthFromEnd(create_link_list([1,2,3,4,5]),1)
# print_link_list(head)

head = sol.removeNthFromEnd(create_link_list([1,2,3,4,5]),5)
print_link_list(head)

head = sol.removeNthFromEnd(create_link_list([1]),1)
print_link_list(head)