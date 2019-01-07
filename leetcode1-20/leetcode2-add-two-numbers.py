# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/add-two-numbers/description/
《两数相加--链表》

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    逐位相加，考虑进位
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = []
    node1 = l1
    node2 = l2
    step = 0  # 记录进位
    while not (node1 is None and node2 is None and step == 0):
        m = n = 0
        if node1 is not None:
            m = node1.val
            node1 = node1.next
        if node2 is not None:
            n = node2.val
            node2 = node2.next
        sum = m + n + step  # 累加进位
        sum2 = sum % 10  # 取余
        result.append(sum2)

        if sum != sum2:
            step = 1  # 记录进位
        else:
            step = 0
    return result


def addTwoNumbers2(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    def reverse_list(l):
        """
        :param l:
        :return:
        """
        cur = l
        next = cur.next
        l.next = None
        while next is not None:
            next_next = next.next
            next.next = cur
            cur = next
            next = next_next
        return cur

    l1_reverse = reverse_list(l1)
    l2_reverse = reverse_list(l2)

    result = []
    node1 = l1_reverse
    node2 = l2_reverse
    while node1 is not None and node2 is not None:
        m = n = 0
        if node1 is not None:
            m = node1.val
        if node2 is not None:
            n = node2.val
        node1 = node1.next
        node2 = node2.next
        result.append(m + n)

    return result


ll1 = ListNode(2)
ll1.next = ListNode(4)
ll1.next.next = ListNode(3)

ll2 = ListNode(5)
ll2.next = ListNode(6)
ll2.next.next = ListNode(4)
result = addTwoNumbers(ll1, ll2)
print(result)
