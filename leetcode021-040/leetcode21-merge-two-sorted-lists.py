"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/
《合并两个有序链表》

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from utils.list_utils import *


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:  # 把l1强制为小的
            l3 = l1
            l1 = l2
            l2 = l3

        p1_post = l1
        p1_cur = l1.next
        p2_cur = l2
        while True:
            if p1_cur is None or p2_cur is None:
                if p1_cur is None:
                    p1_post.next = p2_cur
                break

            if p1_cur.val < p2_cur.val: # 第二列更大，p1指针往后移动
                p1_cur = p1_cur.next
                p1_post = p1_post.next
            else:
                p1_post.next = p2_cur
                p2_cur = p2_cur.next
                p1_post.next.next = p1_cur
                p1_post = p1_post.next

        return l1

sol = Solution()

link_list1 = create_link_list([1,2,4])
link_list2 = create_link_list([1,3,4])
merged = sol.mergeTwoLists(link_list1, link_list2)
print_link_list(merged)


link_list1 = create_link_list([1,2,4])
link_list2 = create_link_list([5])
merged = sol.mergeTwoLists(link_list1, link_list2)
print_link_list(merged)

link_list1 = create_link_list([1,2,4])
link_list2 = create_link_list([5,6,7,8,9,10])
merged = sol.mergeTwoLists(link_list1, link_list2)
print_link_list(merged)


link_list1 = create_link_list([1,2,4, 7,8, 9])
link_list2 = create_link_list([5])
merged = sol.mergeTwoLists(link_list1, link_list2)
print_link_list(merged)


link_list1 = create_link_list([1])
link_list2 = create_link_list([5])
merged = sol.mergeTwoLists(link_list1, link_list2)
print_link_list(merged)