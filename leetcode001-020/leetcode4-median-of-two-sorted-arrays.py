# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
《寻找两个有序数组的中位数》

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""

"""
一种错误的方法：
对于两个“等长”数组的中位数，这是一个很好解决的问题：
1. 各取各自数组的中位数，那么最终的中位数肯定在较小中位数所在数组的右段，较大的左段
2. 改动两个数组进入递归
3. 当各自都只剩两个元素时，求这四个数的中位数即最终的结果

那么问题就变成了如何把非等长数组变成等长：
》可以简单证明对于中位数结果，如果在任一数组头尾成对增加最大最小元素，中位数结果不变
故可以通过这个手段来改动数组成为至多相差一个元素的数组，但是这样的最终结果还是会有问题
"""


class Solution(object):
    def find_median(self, nums):
        len_nums = len(nums)
        if len_nums % 2 == 0:
            # 偶数返回中间两值的均值，同时index为右边
            return (nums[len_nums >> 1] + nums[(len_nums >> 1) - 1]) / 2., len_nums >> 1
        else:
            return nums[((len_nums + 1) >> 1) - 1], ((len_nums + 1) >> 1) - 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        中位数，又称中点数，中值。 数组长度N奇数时为nums[(n+1)/2-1]，偶数时为(nums[n/2-1]+nums[n/2])/2。
        很容易得到一个law：
        》》从有序序列的首尾区域（不包含中值）内随机剥离等数目的数值，最终的中位数不变
        1. 从nums1和nums2中分别算的中位数m1,m2
        2. 用两个中位数进行比较，取中间的两段——即较大中位数所在数组的左段，较小中位数所在数组的右段。
            左右两段形成时，需要从原本数组中剥离等数量的数值。
            这时候由law可推导得：两个子数组的中位数，等于原先数组的中位数
        3. 从新的两端数组中寻找中位数，形成递归


        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        # 递归终止，找到了中位数
        if len_nums1 == 0:  # 其中一个数组为空
            median, _ = self.find_median(nums2)
            return median
        if len_nums2 == 0:
            median, _ = self.find_median(nums1)
            return median
        if len_nums1 <= 2 or len_nums2 <= 2:  # 其中一个数组长度不足
            nums = []
            nums.extend(nums1)
            nums.extend(nums2)
            nums.sort()
            median, _ = self.find_median(nums)
            return median

        median1, med_idx1 = self.find_median(nums1)
        median2, med_idx2 = self.find_median(nums2)
        if median1 == median2:  # 两数组的中位数相等，直接返回
            return median1
        else:  # 不等进入递归
            if median1 > median2:  # 取nums1的左侧，nums2的右侧
                if len_nums2 % 2 == 0:  # 偏移偶数数组nums2的指针，从而子数组能够包含中间两位
                    med_idx2 -= 1
                strip_len = min(len(nums1) - med_idx1 - 1,
                                med_idx2)  # 这里需要等额剥离相同长度。依据原理：从有序序列的首尾区域（不包含中值）内随机剥离等量的数值，最终的中位数不变
                new_num1 = nums1[0:len(nums1) - strip_len]
                new_num2 = nums2[-(len(nums2) - strip_len):]
            else:
                if len_nums1 % 2 == 0:
                    med_idx1 -= 1
                strip_len = min(len(nums2) - med_idx2 - 1, med_idx1)
                new_num2 = nums2[0:len(nums2) - strip_len]
                new_num1 = nums1[-(len(nums1) - strip_len):]
            return self.findMedianSortedArrays(new_num1, new_num2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        先进行归并排序，然后直接取中位数
        :param nums1:
        :param nums2:
        :return:
        """
        nums = []
        i = j = 0
        while i < len(nums1):
            n1 = nums1[i]
            while j < len(nums2):
                n2 = nums2[j]
                if n2 < n1:
                    nums.append(n2)
                    j += 1
                else:
                    break
            nums.append(n1)
            i += 1
        if j < len(nums2):
            nums.extend(nums2[j:])

        len_nums = len(nums)
        if len_nums % 2 == 1:
            return nums[(len_nums - 1) // 2]
        else:
            return float(nums[len_nums // 2 - 1] + nums[len_nums // 2]) / 2


sol = Solution()

assert (sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)  # 3
assert (sol.findMedianSortedArrays([1, 2], [3, 4, 5]) == 3)  # 3
assert (sol.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6]) == 4.5)  # 4.5
assert (sol.findMedianSortedArrays([1, 3, 3, 3, 5], [2, 4, 6]) == 3)  # 3
assert (sol.findMedianSortedArrays([1, 3, 5, 8, 9, 10, 12, 13], [2]) == 8)  # 8
assert (sol.findMedianSortedArrays([1, 3, 5, 8, 9, 10, 12, 13], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2)
assert (sol.findMedianSortedArrays([], [1, 2, 3, 4]) == 2.5)
assert (sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)  # 2.5
assert (sol.findMedianSortedArrays([1, 1, 1, 1], [3, 3, 3, 3]) == 2)  # 2
assert (sol.findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3]) == 2)  # 2
assert (sol.findMedianSortedArrays([4, 5, 6, 8], [1, 2, 3, 7, 9, 10]) == 5.5)  # 2
