"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
《两两交换链表中的节点》

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

说明:
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from utils.list_utils import *

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:  # 只有一个节点或者为空
            return head

        result = node_pair_prev = ListNode  # 补充一个节点
        node_pair_prev.next = head
        while True:
            node1 = node_pair_prev.next
            if node1 is None:
                return result.next
            node2 = node1.next
            if node2 is None:
                return result.next
            node_pair_last = node2.next

            # 进行交换
            node_pair_prev.next = node2
            node2.next = node1
            node1.next = node_pair_last

            # 更新
            node_pair_prev = node1

sol = Solution()
head = create_link_list([1,2,3,4])
print(sol.swapPairs(head))
head = create_link_list([1,2])
print(sol.swapPairs(head))
head = create_link_list([1,2,3,4,5])
print(sol.swapPairs(head))
head = create_link_list([1])
print(sol.swapPairs(head))