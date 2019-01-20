"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/
《合并K个排序链表》

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from utils.list_utils import *

class Solution:
    def mergeKLists0(self, lists):
        """
        非常普通的做法：每次比较各链表的首位，找到最小的，然后取出能节点连入结果中，更新链表首位
        时间复杂度o(m*n)  m链表个数，n最长的链表长度
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i = 0
        while i < len(lists):  # 去除为空的链表
            if lists[i] is None:
                lists.pop(i)
                i -= 1
            i += 1

        result = ListNode(-1)
        cur_node = result
        while len(lists) > 0:
            if len(lists) == 1:
                cur_node.next = lists[0]
                break
            # 找到最小的那个节点
            min_node = lists[0]
            min_idx = 0
            for i in range(len(lists)):
                l = lists[i]
                if l.val < min_node.val:
                    min_node = l
                    min_idx = i

            cur_node.next = min_node
            cur_node = min_node
            if min_node.next is None:
                lists.pop(min_idx)
            else:
                lists[min_idx] = min_node.next
            cur_node.next = None

        return result.next

    def mergeKLists(self, lists):
        """
        先对lists排序，每次移入第0个节点到结果链表中，他的后续做后二分插入lists，
        时间复杂度为o(log(m)*n)  m链表个数，n最长的链表长度
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i = 0
        while i < len(lists):  # 去除为空的链表
            if lists[i] is None:
                lists.pop(i)
                i -= 1
            i+=1

        lists.sort(key = lambda node: node.val)# 排序

        result = ListNode(-1)
        cur_node = result
        while len(lists) > 0:
            # 只有一个链表，直接链过去
            if len(lists) == 1:
                cur_node.next = lists[0]
                break

            min_node = lists[0]
            min_idx = 0
            cur_node.next = min_node
            cur_node = min_node
            insert_node = min_node.next
            cur_node.next = None

            lists.pop(min_idx)
            if insert_node is not None:
                insert_val = insert_node.val
                # 二分查找到需要加入的位置
                n = len(lists)
                first = 0
                last = n - 1
                while first <= last:
                    mid = (last + first) // 2
                    if lists[mid].val > insert_val:
                        last = mid - 1
                    elif lists[mid].val < insert_val:
                        first = mid + 1
                    else:
                        first = mid
                        break
                idx= first
                lists.insert(idx, insert_node)

        return result.next


sol = Solution()

# ll1 = create_link_list([1,4,5])
# ll2 = create_link_list([1,3,4])
# ll3= create_link_list([2,6])
# print(sol.mergeKLists([ll1,ll2,ll3]))
#
# ll1 = create_link_list([1,4,5])
# print(sol.mergeKLists([ll1]))

# [[-8,-7,-6,-3,-2,-2,0,3],[-10,-6,-4,-4,-4,-2,-1,4],[-10,-9,-8,-8,-6],[-10,0,4]]
ll1 = create_link_list([-8,-7,-6,-3,-2,-2,0,3])
ll2 = create_link_list([-10,-6,-4,-4,-4,-2,-1,4])
ll3= create_link_list([-10,-9,-8,-8,-6])
ll4= create_link_list([-10,0,4])
print(sol.mergeKLists([ll1,ll2,ll3, ll4]))


