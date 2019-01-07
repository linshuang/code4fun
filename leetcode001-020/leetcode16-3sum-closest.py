"""
https://leetcode-cn.com/problems/3sum-closest/
《最接近的三数之和》

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        思路基本类似15题，也是1排序2固定3头尾指针移动
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closet = nums[0]+nums[1]+nums[2]
        diff = abs(closet-target)
        for i in range(len(nums)):
            num1 = nums[i]
            m = i + 1
            n = len(nums) - 1
            while m < n:
                num2 = nums[m]
                num3 = nums[n]
                sum = num1 + num2 + num3
                if sum < target:
                    m += 1
                elif sum > target:
                    n -= 1
                else:
                    return target
                diff_tmp = abs(sum-target)
                if diff_tmp < diff:
                    closet = sum
                    diff = diff_tmp
        return closet


sol = Solution()
# assert (sol.threeSumClosest([-1, 2, 1, -4], 1) == 2)
# assert (sol.threeSumClosest([-1, 2, 1, -4], 2) == 2)
# assert (sol.threeSumClosest([-1, -2, -3], 1) == -6)
assert (sol.threeSumClosest([-3, -2, -1, 3], 1) == 0)
assert (sol.threeSumClosest([-3, -2, -1, 3, 4], 1) == 1)
