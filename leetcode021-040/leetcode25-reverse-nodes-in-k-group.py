"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
《 k个一组翻转链表》

给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from utils.list_utils import *


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        类似于翻转成对的链表节点，核心点在于标记出前后两个节点
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        result = ListNode(0)
        result.next = head
        node_prev = result  # nodes前一个

        while node_prev is not None:
            nodes = []  # 被交换的节点
            node_tmp = node_prev
            for i in range(k):
                node_tmp = node_tmp.next
                if node_tmp is None:  # 存在空跳出
                    break
                nodes.append(node_tmp)
            if len(nodes) < k:
                break
            node_post = nodes[-1].next  # nodes后一个

            # 进行交换
            for i in range(k-1,0,-1):
                nodes[i].next = nodes[i-1]
            nodes[0].next = node_post
            node_prev.next = nodes[-1]

            node_prev = nodes[0]

        return result.next


sol = Solution()
head = create_link_list([1,2,3,4])
print(sol.reverseKGroup(head, 2))
head = create_link_list([1,2])
print(sol.reverseKGroup(head, 3))
head = create_link_list([1,2])
print(sol.reverseKGroup(head, 2))
head = create_link_list([1,2,3,4,5])
print(sol.reverseKGroup(head, 3))
head = create_link_list([1])
print(sol.reverseKGroup(head, 1))